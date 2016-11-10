# -*- coding: utf-8 -*-
__author__ = 'caoda'
# @Time: 2016/11/10 10:25
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import requests
import base64
import json


url = 'http://imgserver.yunshitu.cn/v1/dispatcher'
args = {
    "combiner_id": "6100",
    'image_url': 'http://pic.adkalava.com/img005/358/a015d02f0da5d3ee.jpg'
}
req = requests.post(url, data=args)
print req.content
sys.exit(0)

base64Pic = base64.b64encode(
    requests.get('http://pic.adkalava.com/img005/358/a015d02f0da5d3ee.jpg').content)

url = 'http://fashion.sensetime.com/fashion/search_clothes'

print json.dumps(requests.post(url, data={'base64Pic': base64Pic}).json(), ensure_ascii=False)
