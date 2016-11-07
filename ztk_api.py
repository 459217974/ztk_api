# -*- coding: utf-8 -*-
__author__ = 'caoda'
# @Time: 2016/11/1 10:50
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import tornado.ioloop
import tornado.web

import json
import requests
import re
from PIL import Image as image
from socket import *
import struct
from cStringIO import StringIO
import xmltodict
import traceback

r = r'g_page_config = (.*);[\s\S]*g_srp_loadCss'
r2 = r'"tfsid":"(.*?)"'
reg = re.compile(r)
reg2 = re.compile(r2)


# http://assets1.styleai.cn/img-shopping/819ecb248b7037c81b8feb994e752f3d2ba09629.jpg
class MaLongHandler(tornado.web.RequestHandler):
    def get(self):
        imglink = self.get_argument('imglink')
        try:
            detect_res = self._detect(imglink)
        except:
            self.write({'status': -1, 'errmsg': traceback.format_exc()})
        loc = ''
        for n in detect_res['boxes'][0][0]:
            loc += str(n) + '-'
        loc = loc[:len(loc) - 1]
        cat = detect_res['boxes'][0][1][0][0]
        gender = detect_res['boxes'][0][2][0]
        try:
            res = self.search(cat, gender, loc, imglink)
        except:
            self.write({'status': -1, 'errmsg': traceback.format_exc()})
        self.write(json.dumps(self.format_res(res, imglink), ensure_ascii=False))

    def post(self):
        cat = self.get_argument('cat')
        gender = self.get_argument('gender')
        loc = self.get_argument('loc')
        imglink = self.get_argument('imglink')
        try:
            res = self.search(cat, gender, loc, imglink)
        except:
            self.write({'status': -1, 'errmsg': traceback.format_exc()})
        self.write(json.dumps(self.format_res(res, imglink), ensure_ascii=False))

    def _detect(self, imglink):
        url = 'http://webdemo.styleai.cn/service/msn/detect?fromCode=juanpi'
        args = {'top_m_bboxes': 4, 'url': imglink}
        req = requests.post(url, data=args)
        return req.json()

    def search(self, cat, gender, loc, imglink):
        url = 'http://webdemo.styleai.cn/service/search_after_detect?fromCode=juanpi'
        args = {
            'cat': cat,
            'cat2': cat,
            'gender': gender,
            'gender2': gender,
            'loc': loc,
            'url': imglink
        }
        req = requests.post(url, data=args)
        return req.json()

    def format_res(self, res, imglink):
        format_res = {'match': []}
        goods_info = {'box': {}, 'good_list': []}
        format_res.update(push_img(imglink))
        goods_info['box']['x'], goods_info['box']['y'], goods_info['box']['w'], goods_info['box']['h'] = res['loc']
        for good in res['results']:
            goods_info['good_list'].append(
                {'good_url': good['buy_url'], 'showimage': 'http://assets1.styleai.cn/img-shopping/' + good['pic_uid']})
        format_res['match'].append(goods_info)
        return {'status': 0, 'data': [format_res, res]}


class MaLong_detectHandler(tornado.web.RequestHandler):
    def get(self):
        imglink = self.get_argument('imglink')
        url = 'http://webdemo.styleai.cn/service/msn/detect?fromCode=juanpi'
        args = {'top_m_bboxes': 4, 'url': imglink}
        try:
            req = requests.post(url, data=args).json()
        except:
            self.write({'status': -1, 'errmsg': traceback.format_exc()})
        self.write(json.dumps(req, ensure_ascii=False))


class TaoBaoHandler(tornado.web.RequestHandler):
    def get(self):
        imglink = self.get_argument('imglink')
        try:
            content = requests.get('http://www.pailitao.com/image?q=' + imglink).content
        except:
            self.write({'status': -1, 'errmsg': traceback.format_exc()})
        self.write(json.dumps(self.format_res(content, imglink), ensure_ascii=False))

    def post(self):
        tfsid = self.get_argument('tfsid')
        region = self.get_argument('region')
        try:
            content = requests.get(
                'http://www.pailitao.com/search?app=imgsearch&tfsid=' + tfsid + '&region=' + region).content
        except:
            self.write({'status': -1, 'errmsg': traceback.format_exc()})
        self.write(json.dumps(self.format_res(content), ensure_ascii=False))

    def format_res(self, content, imglink=''):
        json_data = json.loads(re.findall(reg, content)[0])
        goods_list = json_data['mods']['itemlist']['data']['collections'][0]['auctions']
        region = json_data['mods']['banner']['data']['region'].split(',')
        tfsid = re.findall(reg2, content)[0]
        format_res = {'match': [], 'tfsid': tfsid}
        goods_info = {'box': {}, 'good_list': []}
        goods_info['box']['x'], goods_info['box']['y'], goods_info['box']['w'], goods_info['box']['h'] = region
        if imglink:
            format_res.update(push_img(imglink))
        for good in goods_list:
            goods_info['good_list'].append(
                {'good_url': 'http:' + good['detail_url'], 'showimage': 'http:' + good['pic_url']})
        format_res['match'].append(goods_info)
        return {'status': 0, 'data': [format_res, json_data]}


class KalavaHandler(tornado.web.RequestHandler):
    def get(self):
        imglink = self.get_argument('imglink')
        res = self.kalava_search(imglink)
        self.write(json.dumps(self.format_res(res, imglink), ensure_ascii=False))

    def kalava_search(self, imglink):
        url = 'http://imgserver.yunshitu.cn/v1/dispatcher'
        args = {
            "combiner_id": "6100",
            'image_url': imglink
        }
        req = requests.post(url, data=args)
        return req.json()

    def format_res(self, res, imglink):
        if res['errno'] != 0:
            self.write(json.dumps({'status': res['errno'], 'errmsg': res}))
        format_res = push_img(imglink)
        format_res['match'] = []
        for detect in res['data']['detect']:
            match = {'good_list': [], 'box': detect['box']}
            for good in detect['child']['match']:
                match['good_list'].append({'good_url': good['name'].split('_')[0], 'showimage': good['showimage']})
            format_res['match'].append(match)
        return {'status': 0, 'data': [format_res, res]}


def make_app():
    return tornado.web.Application([
        (r"/malong", MaLongHandler),
        (r"/malong/detect", MaLong_detectHandler),
        (r"/taobao", TaoBaoHandler),
        (r"/kalava", KalavaHandler),
    ])


def resizeImg(**args):
    args_key = {'ori_img': '', 'dst_img': '', 'dst_w': '', 'dst_h': '', 'save_q': 100}
    arg = {}
    for key in args_key:
        if key in args:
            arg[key] = args[key]

    im = image.open(StringIO(arg['ori_img']))
    ori_w, ori_h = im.size
    widthRatio = heightRatio = None
    ratio = 1
    if (ori_w and ori_w > arg['dst_w']) or (ori_h and ori_h > arg['dst_h']):
        if arg['dst_w'] and ori_w > arg['dst_w']:
            widthRatio = float(arg['dst_w']) / ori_w  # 正确获取小数的方式
        if arg['dst_h'] and ori_h > arg['dst_h']:
            heightRatio = float(arg['dst_h']) / ori_h

        if widthRatio and heightRatio:
            if widthRatio < heightRatio:
                ratio = widthRatio
            else:
                ratio = heightRatio

        if widthRatio and not heightRatio:
            ratio = widthRatio
        if heightRatio and not widthRatio:
            ratio = heightRatio

        newWidth = int(ori_w * ratio)
        newHeight = int(ori_h * ratio)
    else:
        newWidth = ori_w
        newHeight = ori_h

    out = StringIO()
    im.resize((newWidth, newHeight), image.ANTIALIAS).save(out, quality=arg['save_q'], format='JPEG')
    img = out.getvalue()
    out.close()

    return img


def push_img(pic_url):
    HOST = '192.168.1.91'
    PORT = 8090
    ADDR = (HOST, PORT)
    try:
        tag = None
        pic = requests.get(pic_url).content
        if len(pic) > 1048000:
            tag = True
            print 'resize img', len(pic)
            pic = resizeImg(ori_img=pic, dst_w=1000, dst_h=1000, save_q=100)
        packdata = struct.pack('<8si2h14s2hi%ds' % len(pic), 'YST1.0.0', len(pic) + 26, 1, 1, '0' * 14, 1, 0, len(pic),
                               pic)
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        tcpCliSock.send(packdata)
        head = struct.unpack('<8s', tcpCliSock.recv(8))[0]
        tcpCliSock.recv(18)
        cmd_type = struct.unpack('<h', tcpCliSock.recv(2))[0]
        status = struct.unpack('<i', tcpCliSock.recv(4))[0]

        # print 'head:', head, 'status:', status, 'cmd_type:', cmd_type
        if head == 'YST1.0.0' and status == 0:
            lenth = struct.unpack('<i', tcpCliSock.recv(4))[0]
            res = ''
            while len(res) < lenth:
                res += tcpCliSock.recv(lenth)
            res = struct.unpack('<%ds' % lenth, res)[0]
            res = xmltodict.parse(res)
            imgid, imgpath, imgsize = res['doc']['base']['imgid'], res['doc']['base']['imgpath'], res['doc']['base'][
                'imgsize']
            tcpCliSock.close()
            if tag:
                print imgpath
            return {'imgid': imgid, 'imgpath': imgpath, 'imgsize': imgsize, 'imglink': pic_url}
    except:
        traceback.print_exc()
        return 0


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
