# 找同款API说明

### 接口基础信息

* 服务器：192.168.1.123
* 端口：9876
* 示例URL：http://192.168.1.123:9876/kalava?imglink=http://pic.adkalava.com/img005/989/99a24c99c7783a5d.jpg

具体各功能地址见下方具体描述

### MaLong

* 检框接口

    URL：/malong/detect?imglink=
    
    请求方式：GET
    
    返回结果：
    
        {
          "boxes": [
            [ // 检框结果数组
              [ // 框
                0.29875,
                0.0,
                0.62375,
                0.9475
              ],
              [ // 所有服装种类的检测，打分
                [
                  "G_ONEPIECES",
                  0.847759485244751
                ],
                [
                  "G_ONEPIECES",
                  0.10610660910606384
                ],
                [
                  "G_ONEPIECES",
                  0.040946926921606064
                ],
                [
                  "G_TOPS",
                  -1
                ],
                [
                  "G_OUTERWEAR",
                  -1
                ],
                [
                  "G_BOTTOMS",
                  -1
                ],
                [
                  "G_FOOTWEAR",
                  -1
                ],
                [
                  "G_ACCESSORIES",
                  -1
                ],
                [
                  "G_BAGS",
                  -1
                ]
              ],
              [ // 服装适用性别
                "FEMALE",
                1.0
              ],
              [ // 服装分类
                "CATEGORY",
                "ABOVEKNEEDRESSES"
              ]
            ],
            [
              [
                0.0,
                0.335,
                0.2625,
                0.57875
              ],
              [
                [
                  "NONFASHION",
                  0.999991774559021
                ],
                [
                  "G_TOPS",
                  -1
                ],
                [
                  "G_OUTERWEAR",
                  -1
                ],
                [
                  "G_BOTTOMS",
                  -1
                ],
                [
                  "G_FOOTWEAR",
                  -1
                ],
                [
                  "G_ONEPIECES",
                  -1
                ],
                [
                  "G_ACCESSORIES",
                  -1
                ],
                [
                  "G_BAGS",
                  -1
                ]
              ],
              [
                "ALL",
                1.0
              ],
              [
                "CATEGORY",
                "NONFASHION"
              ]
            ],
            [
              [
                0.51375,
                0.80375,
                0.255,
                0.14875
              ],
              [
                [
                  "NONFASHION",
                  0.9999909400939941
                ],
                [
                  "G_TOPS",
                  -1
                ],
                [
                  "G_OUTERWEAR",
                  -1
                ],
                [
                  "G_BOTTOMS",
                  -1
                ],
                [
                  "G_FOOTWEAR",
                  -1
                ],
                [
                  "G_ONEPIECES",
                  -1
                ],
                [
                  "G_ACCESSORIES",
                  -1
                ],
                [
                  "G_BAGS",
                  -1
                ]
              ],
              [
                "ALL",
                1.0
              ],
              [
                "CATEGORY",
                "NONFASHION"
              ]
            ],
            [
              [
                0.77875,
                0.685,
                0.22,
                0.30875
              ],
              [
                [
                  "NONFASHION",
                  0.9999927282333374
                ],
                [
                  "G_TOPS",
                  -1
                ],
                [
                  "G_OUTERWEAR",
                  -1
                ],
                [
                  "G_BOTTOMS",
                  -1
                ],
                [
                  "G_FOOTWEAR",
                  -1
                ],
                [
                  "G_ONEPIECES",
                  -1
                ],
                [
                  "G_ACCESSORIES",
                  -1
                ],
                [
                  "G_BAGS",
                  -1
                ]
              ],
              [
                "ALL",
                1.0
              ],
              [
                "CATEGORY",
                "NONFASHION"
              ]
            ]
          ],
          "ver": 5.21,
          "time": "0.330"
        }

* 找同款接口

    URL：/malong?imglink=
    
    请求方式：GET、POST
    
    POST：
    
        args = {
                'cat': "G_ONEPIECES", //检框接口返回的服装分类
                'cat2': "G_ONEPIECES", //和上面一样的取值，意义不明
                'gender': "FEMALE", //服装适合的性别
                'gender2': "FEMALE", //和上面一样的取值，意义不明
                'loc': "0.29875-0.0-0.62375-0.9475", //框，'-'连接
                'url': imglink //图片链接
            }
            
    GET：
    
        默认返回第一个框的结果
    
    返回结果：

		{
		  "status": 0, //状态，0为正常
		  "data": [ //数组，固定只有两个元素，第一个为整理后数据，第二个为原始数据
		    {
		      "imglink": "http://pic.adkalava.com/img005/989/99a24c99c7783a5d.jpg", //原图链接
		      "imgid": "11070495057390352989",
		      "imgsize": "800*800",
		      "match": [ //为适用我们的接口返回多个匹配结果的情况，这是一个匹配结果的数组
		        {
		          "box": {
		            "y": 0.0,
		            "x": 0.29875,
		            "w": 0.62375,
		            "h": 0.9475
		          },
		          "good_list": [ // 匹配商品的列表
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/73f884d7885d011e677d4c107a0aa5c936fe7c04.jpg",
		              "good_url": "http://item.yohobuy.com/product/pro_404945_514417/SENNOSZHOUSZ16105008HengDaiChangChenYi.html?from=list-c-12_46_33"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/e23509245d7a5ded3a38fa9f02a1bd762724d95b.jpg",
		              "good_url": "http://item.m.jd.com/product/10193869987.html"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/7878f238e101bf001c11c3b8e095f10a0b5a9e45.jpg",
		              "good_url": "http://m.meilishuo.com/share/item/4078919471?ad_tag=0_0_0_0_0-1895952159-1_0-0_0-0-0_bb4f64d9e0859fcb3b33eb786ca1429f&d_r=6__0-27-9-10"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/a8cc0416528f1fc8cc8e57a00ba1dc62d0564c28.jpg",
		              "good_url": "http://a.m.taobao.com/i530222159803.htm?&sid=da5e603a821bc5ee668777c472acf305"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/80fbe1cab3a8a7b5979c0038a182dcca23f8695e.jpg",
		              "good_url": "http://m.meilishuo.com/share/item/3858234313?ad_tag=0_0_0_0_0-1748109023-1_0-0_0-0-0_f0d501a78a216cc77e92cec686451de9&d_r=6__0-7-6-15"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/bfb1c171328d0b3b5b4dfc1fd7a3888edc490630.jpg",
		              "good_url": "http://m.yougou.com/c-huaimei/sku-bh3359c6535-100446490"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/cb41bfaa5f6b5188eee64b124abaecf50cb2de5c.jpg",
		              "good_url": "http://m.meilishuo.com/share/item/3688904555?ad_tag=0_0_0_0_0-1684927915-1_0-0_0-0-0_353741f6774a2c9b45e1e17cd3117e98&d_r=6__0-1-2-7"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/dcab2aa5b3f2f37bd25f70dc66720263dc77ee53.jpg",
		              "good_url": "http://m.meilishuo.com/share/item/4011478979?ad_tag=0_0_0_0_0-1827895811-1_0-0_0-0-0_14ea0f77b359c8a5aa2fa0c70c7e93e2&d_r=6__0-22-4-19"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/b5365de9872cbe87549f7e6cefd6b5aaf80d22ed.jpg",
		              "good_url": "http://m.d2cmall.com/product/113096"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/1bc3948a616cf0ca90f34b608d0c6d500aafd6dd.jpg",
		              "good_url": "http://m.d2cmall.com/product/106996"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/543bac87e75f09374548cf2e79583ca615369dd1.jpg",
		              "good_url": "http://m.meilishuo.com/share/item/3590772991?ad_tag=0_0_0_0_0-1655271801-1_0-0_0-0-0_308abb4d5dd3446b1b586b7faeb13a4a&d_r=6__0-17-4-20"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/43d8025a119aad6ef8377b694d718a7551fd77b0.jpg",
		              "good_url": "http://item.yohobuy.com/product/pro_377309_481475/YOUPPIETiaoWenLianYiQunYAUN205013.html?from=list-c-31_32_35"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/5e8d6acd87c6ebe3d81d4f6dce53a7ae2f01a44e.jpg",
		              "good_url": "http://item.m.jd.com/product/10266225534.html"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/3c77e81c24845603d4549f35cc4915cb21be02af.jpg",
		              "good_url": "http://item.m.jd.com/product/10272051763.html"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/7bf28ed2532c5c884ed2be2122acee7b7e395476.jpg",
		              "good_url": "http://item.yohobuy.com/product/pro_413765_524943/LUNALIMITEDChaoBaoXianShouDARKSKIRTHeiLianYiQunJinKouMianLiaoLY00545.html?from=list-c-31_3_10"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/efca3dfc63499039df58a20bdec7c30bac058478.jpg",
		              "good_url": "http://m.meilishuo.com/share/item/4118302829?ad_tag=0_0_0_0_0-1921681459-1_0-0_0-0-0_ddbdcc13fe570cd4985b1dc5a21d9ce4&d_r=6__0-2-2-5"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/f6e7df790ec11046230adb9688d1a5d4f6399228.jpg",
		              "good_url": "http://m.meilishuo.com/share/item/4075090143?ad_tag=0_0_0_0_0-1893460345-1_0-0_0-0-0_cf9864527562e630e1464a78e5917912&d_r=6__0-23-7-13"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/6c390930a0c2e8711f5d736caac26e0c5a32ecbd.jpg",
		              "good_url": "http://m.meilishuo.com/share/item/4025233075?ad_tag=0_0_0_0_0-1837176137-1_0-0_0-0-0_b366d8c3cc22a08c00b7cafada5a3872&d_r=6__0-5-3-4"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/a0dfe61c8f5046bba1c988b4b6df21c00bb14330.jpg",
		              "good_url": "http://item.m.jd.com/product/10184907469.html"
		            },
		            {
		              "showimage": "http://assets1.styleai.cn/img-shopping/15d0c033c8e447e121299e255f25376458a40d7c.jpg",
		              "good_url": "http://m.meilishuo.com/share/item/4124560025?ad_tag=0_0_0_0_0-1924990187-1_0-0_0-0-0_cbd25619a9cd31e6acf537873087c786&d_r=6__0-10-7-11"
		            }
		          ]
		        }
		      ],
		      "imgpath": "img005/989/99a24c99c7783a5d.jpg"
		    },
		    { // 原始数据
		      "loc": [ //框
		        0.29875,
		        0.0,
		        0.62375,
		        0.9475
		      ],
		      "ver": 5.21,
		      "results": [ //匹配商品列表
		        {
		          "h_to_w": 1.3333333730697632,
		          "loc": [
		            0.15238095819950104,
		            0.21250000596046448,
		            0.5976190567016602,
		            0.7607142925262451
		          ],
		          "crawl_date": 1462785341.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "YOHOBUY",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 420,
		          "cat": "ONEPIECES",
		          "price": 199.0,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.6274797320365906,
		          "buy_url": "http://item.yohobuy.com/product/pro_404945_514417/SENNOSZHOUSZ16105008HengDaiChangChenYi.html?from=list-c-12_46_33",
		          "pic_uid": "73f884d7885d011e677d4c107a0aa5c936fe7c04", //showimage，前面加上'http://assets1.styleai.cn/img-shopping/'，后面加上'.jpg'，可访问图片
		          "prod_uid": "4b0345199b94d50d786b5e94d49c5004",
		          "o_h": 560
		        },
		        {
		          "h_to_w": 1.0,
		          "loc": [
		            0.23250000178813934,
		            0.14499999582767487,
		            0.5774999856948853,
		            0.6537500023841858
		          ],
		          "crawl_date": 1461619139.0,
		          "off_market": false,
		          "fl_web_url": "http://union.click.jd.com/jdc?e=&p=AyIOZRlZEgESAlQaUyUCEwddGVISChoOUysfSlpMWGVCHlBDGRlLQx5BXg1bSkAOClBMW0taGEtXVlUQBVsUAhoFXBxTHQsUGAxeB0gyZmYpEwBvRHNkI0sSaX1bdQVEWGp6cgtZK14UBRQCUhhfFDISBlQaWhUEEwddK2tzfyJGOx5THQYaN1QrWxAFEAFdGl4dBRcCXCtcJdSDt42w7MOUstDuqo2Ep8a59StrJQ%3D%3D&t=W1dCFBBFC1pXUwkEBwpZRxgHRQcLQ1FZAF8JUBwSBlUTWRwFGg9cHURMR05a",
		          "store_name": "JD",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 800,
		          "cat": "LONGDRESSES",
		          "price": 198.0,
		          "currency": "CNY",
		          "fl_app_url": "http://union.click.jd.com/jdc?e=&p=AyIBZRlZEgESAlQaUyUCEwddGVISChoOUysfSlpMWGVCHlBDGRlLQx5BXg1bSkAOClBMW0taGEtXVlUQBVsUAhoFXBxTHQsUGAxeB0gyZ1JRS1sUWlRnUAEDcX1pBhIdPWUYYgtZK14UARAAVRpSFzISBlQaWhUEEwddK2tzfyJGOx5THQYaN1QrWxAFEAFdHF8UBhYPVytZFzLEluXD8KLUhKeCoOrDk7fT67trJTI%3D&t=W1dCFBBFC1pXUwkEBwpZRxgHRQcLQ1FZAF8JUBwSBlUTWRwFGg9cHURMR05a",
		          "score": 0.6296935081481934,
		          "buy_url": "http://item.m.jd.com/product/10193869987.html",
		          "pic_uid": "e23509245d7a5ded3a38fa9f02a1bd762724d95b",
		          "prod_uid": "426c602393e2746f12e7146c88fec8b2",
		          "o_h": 800
		        },
		        {
		          "h_to_w": 1.2999999523162842,
		          "loc": [
		            0.24687500298023224,
		            0.11418269574642181,
		            0.7171875238418579,
		            0.848557710647583
		          ],
		          "crawl_date": 1460604062.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "MEILISHUO",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 640,
		          "cat": "LONGDRESSES",
		          "price": 88.0,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.6424997448921204,
		          "buy_url": "http://m.meilishuo.com/share/item/4078919471?ad_tag=0_0_0_0_0-1895952159-1_0-0_0-0-0_bb4f64d9e0859fcb3b33eb786ca1429f&d_r=6__0-27-9-10",
		          "pic_uid": "7878f238e101bf001c11c3b8e095f10a0b5a9e45",
		          "prod_uid": "3ced22bb69679ced74b27c2f99cc2805",
		          "o_h": 832
		        },
		        {
		          "h_to_w": 1.0,
		          "loc": [
		            0.2800000011920929,
		            0.19374999403953552,
		            0.35249999165534973,
		            0.6937500238418579
		          ],
		          "crawl_date": 1460835340.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "TAOBAO",
		          "orig_id": null,
		          "open_iid": "None",
		          "o_w": 800,
		          "cat": "LONGDRESSES",
		          "price": 1178.0,
		          "currency": "CNY",
		          "fl_app_url": "None",
		          "score": 0.6521418690681458,
		          "buy_url": "http://a.m.taobao.com/i530222159803.htm?&sid=da5e603a821bc5ee668777c472acf305",
		          "pic_uid": "a8cc0416528f1fc8cc8e57a00ba1dc62d0564c28",
		          "prod_uid": "4288ffe1d6aaf47b1698762b3729f789",
		          "o_h": 800
		        },
		        {
		          "h_to_w": 1.314062476158142,
		          "loc": [
		            0.0625,
		            0.17479191720485687,
		            0.7015625238418579,
		            0.8240190148353577
		          ],
		          "crawl_date": 1460602822.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "MEILISHUO",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 640,
		          "cat": "LONGDRESSES",
		          "price": 820.0,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.6539337038993835,
		          "buy_url": "http://m.meilishuo.com/share/item/3858234313?ad_tag=0_0_0_0_0-1748109023-1_0-0_0-0-0_f0d501a78a216cc77e92cec686451de9&d_r=6__0-7-6-15",
		          "pic_uid": "80fbe1cab3a8a7b5979c0038a182dcca23f8695e",
		          "prod_uid": "806383c3a8848ae2cdbbf317f3e19d6e",
		          "o_h": 841
		        },
		        {
		          "h_to_w": 1.0,
		          "loc": [
		            0.3050000071525574,
		            0.21875,
		            0.4612500071525574,
		            0.75
		          ],
		          "crawl_date": 1462258143.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "YOUGOU",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 800,
		          "cat": "LONGDRESSES",
		          "price": 69.0,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.6539363861083984,
		          "buy_url": "http://m.yougou.com/c-huaimei/sku-bh3359c6535-100446490",
		          "pic_uid": "bfb1c171328d0b3b5b4dfc1fd7a3888edc490630",
		          "prod_uid": "2aaf19106285f73a41136f7e4b9b6952",
		          "o_h": 800
		        },
		        {
		          "h_to_w": 1.2999999523162842,
		          "loc": [
		            0.03125,
		            0.17908653616905212,
		            0.7796875238418579,
		            0.786057710647583
		          ],
		          "crawl_date": 1460600577.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "MEILISHUO",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 640,
		          "cat": "LONGDRESSES",
		          "price": 65.0,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.6541748642921448,
		          "buy_url": "http://m.meilishuo.com/share/item/3688904555?ad_tag=0_0_0_0_0-1684927915-1_0-0_0-0-0_353741f6774a2c9b45e1e17cd3117e98&d_r=6__0-1-2-7",
		          "pic_uid": "cb41bfaa5f6b5188eee64b124abaecf50cb2de5c",
		          "prod_uid": "f9a227b404cf6a0db1ad9ec4c94ed5f9",
		          "o_h": 832
		        },
		        {
		          "h_to_w": 1.2999999523162842,
		          "loc": [
		            0.4078125059604645,
		            0.23076923191547394,
		            0.4078125059604645,
		            0.7596153616905212
		          ],
		          "crawl_date": 1460603800.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "MEILISHUO",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 640,
		          "cat": "LONGDRESSES",
		          "price": 177.66000366210938,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.6608092784881592,
		          "buy_url": "http://m.meilishuo.com/share/item/4011478979?ad_tag=0_0_0_0_0-1827895811-1_0-0_0-0-0_14ea0f77b359c8a5aa2fa0c70c7e93e2&d_r=6__0-22-4-19",
		          "pic_uid": "dcab2aa5b3f2f37bd25f70dc66720263dc77ee53",
		          "prod_uid": "9a28a465f47572ad2fe097f86b6c3fc7",
		          "o_h": 832
		        },
		        {
		          "h_to_w": 1.5579999685287476,
		          "loc": [
		            0.2639999985694885,
		            0.18485237658023834,
		            0.4320000112056732,
		            0.6598202586174011
		          ],
		          "crawl_date": 1458579571.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "D2CMALL",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 1000,
		          "cat": "ONEPIECES",
		          "price": 3290.0,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.6613346338272095,
		          "buy_url": "http://m.d2cmall.com/product/113096",
		          "pic_uid": "b5365de9872cbe87549f7e6cefd6b5aaf80d22ed",
		          "prod_uid": "80b681138927548ca8c663c48484c114",
		          "o_h": 1558
		        },
		        {
		          "h_to_w": 1.5579999685287476,
		          "loc": [
		            0.335999995470047,
		            0.087933249771595,
		            0.37400001287460327,
		            0.8671373724937439
		          ],
		          "crawl_date": 1458594426.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "D2CMALL",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 1000,
		          "cat": "ONEPIECES",
		          "price": 3199.0,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.661349356174469,
		          "buy_url": "http://m.d2cmall.com/product/106996",
		          "pic_uid": "1bc3948a616cf0ca90f34b608d0c6d500aafd6dd",
		          "prod_uid": "d04c165ccf0065d03b524dae284d0354",
		          "o_h": 1558
		        },
		        {
		          "h_to_w": 1.2999999523162842,
		          "loc": [
		            0.08124999701976776,
		            0.2944711446762085,
		            0.753125011920929,
		            0.6887019276618958
		          ],
		          "crawl_date": 1460603452.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "MEILISHUO",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 640,
		          "cat": "LONGDRESSES",
		          "price": 184.0,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.664218544960022,
		          "buy_url": "http://m.meilishuo.com/share/item/3590772991?ad_tag=0_0_0_0_0-1655271801-1_0-0_0-0-0_308abb4d5dd3446b1b586b7faeb13a4a&d_r=6__0-17-4-20",
		          "pic_uid": "543bac87e75f09374548cf2e79583ca615369dd1",
		          "prod_uid": "c57feceba312b224acfa69571641673a",
		          "o_h": 832
		        },
		        {
		          "h_to_w": 1.3333333730697632,
		          "loc": [
		            0.18133333325386047,
		            0.21400000154972076,
		            0.6986666917800903,
		            0.6570000052452087
		          ],
		          "crawl_date": 1462784999.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "YOHOBUY",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 750,
		          "cat": "LONGDRESSES",
		          "price": 589.0,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.6679589748382568,
		          "buy_url": "http://item.yohobuy.com/product/pro_377309_481475/YOUPPIETiaoWenLianYiQunYAUN205013.html?from=list-c-31_32_35",
		          "pic_uid": "43d8025a119aad6ef8377b694d718a7551fd77b0",
		          "prod_uid": "ae6d74da7ac6cbf263b66ba7e11cbac6",
		          "o_h": 1000
		        },
		        {
		          "h_to_w": 1.0,
		          "loc": [
		            0.3087500035762787,
		            0.2150000035762787,
		            0.4000000059604645,
		            0.643750011920929
		          ],
		          "crawl_date": 1461785062.0,
		          "off_market": false,
		          "fl_web_url": "None",
		          "store_name": "JD",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 800,
		          "cat": "ABOVEKNEEDRESSES",
		          "price": 188.0,
		          "currency": "CNY",
		          "fl_app_url": "None",
		          "score": 0.6681935787200928,
		          "buy_url": "http://item.m.jd.com/product/10266225534.html",
		          "pic_uid": "5e8d6acd87c6ebe3d81d4f6dce53a7ae2f01a44e",
		          "prod_uid": "62a100dc56c2906233e30d27e3a5de4e",
		          "o_h": 800
		        },
		        {
		          "h_to_w": 1.0,
		          "loc": [
		            0.2524999976158142,
		            0.17749999463558197,
		            0.36250001192092896,
		            0.8162500262260437
		          ],
		          "crawl_date": 1461619105.0,
		          "off_market": false,
		          "fl_web_url": "None",
		          "store_name": "JD",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 800,
		          "cat": "LONGDRESSES",
		          "price": 3366.0,
		          "currency": "CNY",
		          "fl_app_url": "None",
		          "score": 0.6813556551933289,
		          "buy_url": "http://item.m.jd.com/product/10272051763.html",
		          "pic_uid": "3c77e81c24845603d4549f35cc4915cb21be02af",
		          "prod_uid": "206eef76a74e569d0e3a716a4a2d837a",
		          "o_h": 800
		        },
		        {
		          "h_to_w": 1.3333333730697632,
		          "loc": [
		            0.25066667795181274,
		            0.2619999945163727,
		            0.4959999918937683,
		            0.6269999742507935
		          ],
		          "crawl_date": 1462784814.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "YOHOBUY",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 750,
		          "cat": "LONGDRESSES",
		          "price": 288.0,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.6814574599266052,
		          "buy_url": "http://item.yohobuy.com/product/pro_413765_524943/LUNALIMITEDChaoBaoXianShouDARKSKIRTHeiLianYiQunJinKouMianLiaoLY00545.html?from=list-c-31_3_10",
		          "pic_uid": "7bf28ed2532c5c884ed2be2122acee7b7e395476",
		          "prod_uid": "3b66cbfc288294119e260fe20d9df6e2",
		          "o_h": 1000
		        },
		        {
		          "h_to_w": 1.3125,
		          "loc": [
		            0.3187499940395355,
		            0.14523810148239136,
		            0.578125,
		            0.7666666507720947
		          ],
		          "crawl_date": 1460602458.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "MEILISHUO",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 640,
		          "cat": "LONGDRESSES",
		          "price": 387.8999938964844,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.6824392080307007,
		          "buy_url": "http://m.meilishuo.com/share/item/4118302829?ad_tag=0_0_0_0_0-1921681459-1_0-0_0-0-0_ddbdcc13fe570cd4985b1dc5a21d9ce4&d_r=6__0-2-2-5",
		          "pic_uid": "efca3dfc63499039df58a20bdec7c30bac058478",
		          "prod_uid": "78ae391cdb2780db6284c118a7db6e41",
		          "o_h": 840
		        },
		        {
		          "h_to_w": 1.2999999523162842,
		          "loc": [
		            0.3031249940395355,
		            0.27163460850715637,
		            0.37968748807907104,
		            0.5757211446762085
		          ],
		          "crawl_date": 1460603633.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "MEILISHUO",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 640,
		          "cat": "LONGDRESSES",
		          "price": 79.0,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.6827711462974548,
		          "buy_url": "http://m.meilishuo.com/share/item/4075090143?ad_tag=0_0_0_0_0-1893460345-1_0-0_0-0-0_cf9864527562e630e1464a78e5917912&d_r=6__0-23-7-13",
		          "pic_uid": "f6e7df790ec11046230adb9688d1a5d4f6399228",
		          "prod_uid": "817856b13575eb45f707350bf8ec0216",
		          "o_h": 832
		        },
		        {
		          "h_to_w": 1.2999999523162842,
		          "loc": [
		            0.3140625059604645,
		            0.18028846383094788,
		            0.4609375,
		            0.6862980723381042
		          ],
		          "crawl_date": 1460602648.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "MEILISHUO",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 640,
		          "cat": "LONGDRESSES",
		          "price": 198.0,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.6831571459770203,
		          "buy_url": "http://m.meilishuo.com/share/item/4025233075?ad_tag=0_0_0_0_0-1837176137-1_0-0_0-0-0_b366d8c3cc22a08c00b7cafada5a3872&d_r=6__0-5-3-4",
		          "pic_uid": "6c390930a0c2e8711f5d736caac26e0c5a32ecbd",
		          "prod_uid": "063e43b6ee703fc4e2b1e51fcb021003",
		          "o_h": 832
		        },
		        {
		          "h_to_w": 1.0,
		          "loc": [
		            0.23375000059604645,
		            0.22374999523162842,
		            0.47749999165534973,
		            0.6775000095367432
		          ],
		          "crawl_date": 1461632044.0,
		          "off_market": false,
		          "fl_web_url": "None",
		          "store_name": "JD",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 800,
		          "cat": "LONGDRESSES",
		          "price": 210.0,
		          "currency": "CNY",
		          "fl_app_url": "None",
		          "score": 0.6870915293693542,
		          "buy_url": "http://item.m.jd.com/product/10184907469.html",
		          "pic_uid": "a0dfe61c8f5046bba1c988b4b6df21c00bb14330",
		          "prod_uid": "eeaf7c549058488db3644c22387b23b6",
		          "o_h": 800
		        },
		        {
		          "h_to_w": 1.2999999523162842,
		          "loc": [
		            0.28437501192092896,
		            0.1899038404226303,
		            0.47968751192092896,
		            0.7067307829856873
		          ],
		          "crawl_date": 1460601120.0,
		          "off_market": false,
		          "fl_web_url": "",
		          "store_name": "MEILISHUO",
		          "orig_id": null,
		          "open_iid": "",
		          "o_w": 640,
		          "cat": "LONGDRESSES",
		          "price": 29.899999618530273,
		          "currency": "CNY",
		          "fl_app_url": "",
		          "score": 0.6883234977722168,
		          "buy_url": "http://m.meilishuo.com/share/item/4124560025?ad_tag=0_0_0_0_0-1924990187-1_0-0_0-0-0_cbd25619a9cd31e6acf537873087c786&d_r=6__0-10-7-11",
		          "pic_uid": "15d0c033c8e447e121299e255f25376458a40d7c",
		          "prod_uid": "10dd3207b9ac796356ef29fe950c32a5",
		          "o_h": 832
		        }
		      ],
		      "is_err": false,
		      "other": [],
		      "time": "0.038",
		      "suggested_filters": [
		        "G_TOPS",
		        "G_OUTERWEAR",
		        "G_BOTTOMS",
		        "G_FOOTWEAR",
		        "G_ONEPIECES",
		        "G_ACCESSORIES",
		        "G_BAGS"
		      ],
		      "ds": "items_2016_06_99"
		    }
		  ]
		}
		
### TaoBao

* 找同款接口

    URL：/taobao?imglink=
    
    请求方式：GET、POST
    
    POST：
    
        用于重新框选主体，需要先GET请求，然后获取tfsid
        
        args = {
        
            "tfsid":"TB1IOGSOXXXXXXEXVXXXXXXXXXX",
            "region":"187,542,14,586"
        }
    
    返回结果：
    
		{
		  "status": 0, //状态，0为正常
		  "data": [ //数组，固定只有两个元素，第一个为整理后数据，第二个为原始数据
		    {
		      "imgid": "11070495057390352989",
		      "imgsize": "800*800",
		      "imglink": "http://pic.adkalava.com/img005/989/99a24c99c7783a5d.jpg", //原图链接
		      "tfsid": "TB1IOGSOXXXXXXEXVXXXXXXXXXX", // 淘宝在第一次上传图片后，就将图片链接转为自己的图片链接，如果需要重新框选，需要使用这个淘宝的图片id
		      "match": [ //为适用我们的接口返回多个匹配结果的情况，这是一个匹配结果的数组
		        {
		          "box": {
		            "y": "542",
		            "x": "187",
		            "w": "14",
		            "h": "586"
		          },
		          "good_list": [ // 匹配商品的列表
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB2mdoNXR_xQeBjy0FhXXbAoFXa_!!2860759430.png",
		              "good_url": "http://item.taobao.com/item.htm?id=537270605580&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB28tJBaai5V1BjSspfXXapiXXa_!!1689955526.jpg",
		              "good_url": "http://detail.tmall.com/item.htm?id=538050019280&ns=1"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB2zJ_DbMCN.eBjSZFoXXXj0FXa_!!86159518.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=541091180619&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB1RrmPMVXXXXXBXpXXXXXXXXXX_!!0-item_pic.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=537301094150&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB2ZkSib5GO.eBjSZFjXXcU9FXa_!!1014742123.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=541180646269&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB2002JbxaJ.eBjSsziXXaJ_XXa_!!2106631474.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=541151940814&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB19843OXXXXXa6XXXXXXXXXXXX_!!0-item_pic.jpg",
		              "good_url": "http://detail.tmall.com/item.htm?id=521333924828&ns=1"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB1IldaOXXXXXcaXpXXXXXXXXXX_!!0-item_pic.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=540865031317&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB11YAFMVXXXXcbXXXXYXGcGpXX_M2.SS2",
		              "good_url": "http://item.taobao.com/item.htm?id=537329020494&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search1.alicdn.com/img/bao/uploaded/i4/TB2sMh4XGi5V1BjSszdXXXUJXXa_!!111586496.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=537945658698&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search1.alicdn.com/img/bao/uploaded/i4/TB2Y5aHXX95V1Bjy0FeXXXyfpXa_!!611005706.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=537685539404&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB1smp0OXXXXXcKaFXXXXXXXXXX_!!2-item_pic.png",
		              "good_url": "http://detail.tmall.com/item.htm?id=524963319429&ns=1"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB2uAYPsVXXXXbzXXXXXXXXXXXX_!!2354025371.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=535663699890&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB2Zhw1bg1J.eBjy0FpXXaMoXXa_!!2830065191.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=541073271072&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB1D0MpKVXXXXaFXXXXXXXXXXXX_!!0-item_pic.jpg",
		              "good_url": "http://detail.tmall.com/item.htm?id=535730447011&ns=1"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB2UsIFbhmI.eBjy0FlXXbgkVXa_!!0-taoxiaopu_sell.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=541071154256&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB22gQsXfPB11BjSsppXXcjYVXa_!!70115247.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=538603889851&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB2zm4sXssb61BjSszbXXcvMpXa_!!2377829241.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=539467796098&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB256pyjVXXXXbDXXXXXXXXXXXX_!!1791686127.jpg",
		              "good_url": "http://detail.tmall.com/item.htm?id=526413126343&ns=1"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB2QkuBXnka61Bjy0FoXXb1sFXa_!!2229750200.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=539390385921&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB1aWW4NVXXXXaaaXXXXXXXXXXX_!!0-item_pic.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=540555168677&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search1.alicdn.com/img/bao/uploaded/i4/TB2FehXaCCI.eBjy1XbXXbUBFXa_!!642792383.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=540554908445&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search1.alicdn.com/img/bao/uploaded/i4/TB1O3o0NpXXXXbzXpXXXXXXXXXX_!!0-item_pic.jpg",
		              "good_url": "http://detail.tmall.com/item.htm?id=539422624838&ns=1"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB2NThNaF_AQeBjSZFBXXX22XXa_!!2891752320.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=538451953982&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB13RjNNVXXXXc8XpXXXXXXXXXX_!!0-item_pic.jpg",
		              "good_url": "http://detail.tmall.com/item.htm?id=535487224427&ns=1"
		            },
		            {
		              "showimage": "http://g-search1.alicdn.com/img/bao/uploaded/i4/TB2bAS_Xp95V1Bjy0FdXXc5BVXa_!!2894986755.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=537805419332&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB1V8OBNFXXXXbPXFXXXXXXXXXX_!!0-item_pic.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=539758442072&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB2a_AMXNRzc1FjSZFPXXcGAFXa_!!909479546.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=541005709027&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB1t5SeNpXXXXcAXFXXXXXXXXXX_!!0-item_pic.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=538830053956&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB2UrttakWM.eBjSZFhXXbdWpXa_!!2980131781.jpg",
		              "good_url": "http://detail.tmall.com/item.htm?id=540387605135&ns=1"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB20Tq6b71M.eBjSZFOXXc0rFXa_!!1987942723.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=541201814501&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB1CUM6KVXXXXaOXpXXXXXXXXXX_!!0-item_pic.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=536100132727&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB1DgnVNFXXXXbnaXXXXXXXXXXX_!!0-item_pic.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=541186192818&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB2kYXDXsgd61BjSZFPXXbVVFXa_!!2654802945.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=539464840461&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB1aofbLpXXXXbQaFXXXXXXXXXX_!!0-item_pic.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=537334020654&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB2xzTfbb1J.eBjSszcXXbFzVXa_!!2535454443.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=541020240835&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search1.alicdn.com/img/bao/uploaded/i4/TB1Om5ENpXXXXbKXpXXXXXXXXXX_!!0-item_pic.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=541249671626&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB1Om5ENpXXXXbKXpXXXXXXXXXX_!!0-item_pic.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=539009481901&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search2.alicdn.com/img/bao/uploaded/i4/TB2cD8faOGO.eBjSZFPXXcKCXXa_!!2342003648.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=540590756379&ns=1#detail"
		            },
		            {
		              "showimage": "http://g-search3.alicdn.com/img/bao/uploaded/i4/TB2xj.AXwQc61BjSZFGXXa1DFXa_!!1767609433.jpg",
		              "good_url": "http://item.taobao.com/item.htm?id=539539389677&ns=1#detail"
		            }
		          ]
		        }
		      ],
		      "imgpath": "img005/989/99a24c99c7783a5d.jpg"
		    },
		    {
		      "pageName": "imgsearch",
		      "map": {},
		      "mods": {
		        "debugbar": {
		          "status": "hide",
		          "export": false
		        },
		        "header": {
		          "status": "show",
		          "export": false,
		          "data": {
		            "img": {
		              "tfsid": "TB1IOGSOXXXXXXEXVXXXXXXXXXX", // tfsid，就是淘宝的图片id
		              "picUrl": "//g-search1.alicdn.com/img/bao/uploaded/i4/TB1IOGSOXXXXXXEXVXXXXXXXXXX"
		            },
		            "dropdown": [
		              {
		                "url": "/search",
		                "text": "宝贝",
		                "type": "item",
		                "isActive": true
		              },
		              {
		                "url": "//shopsearch.taobao.com/search",
		                "text": "店铺",
		                "type": "shop",
		                "isActive": false
		              }
		            ],
		            "uploadUrl": "/image",
		            "q": "",
		            "imgBtn": true,
		            "tabParams": {
		              "initiative_id": "staobaoz_20161107",
		              "stats_click": "search_radio_all%3A1",
		              "ie": "utf8",
		              "js": "1"
		            }
		          }
		        },
		        "sharebar": {
		          "status": "show",
		          "export": false,
		          "data": {
		            "comment": "我通过拍立淘找到宝贝啦，淘宝有了新技能——用图片也能搜商品，同款商品还能比价格，赶紧试试吧！",
		            "thumb": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB1IOGSOXXXXXXEXVXXXXXXXXXX"
		          }
		        },
		        "banner": {
		          "status": "show",
		          "export": false,
		          "data": {
		            "tabTraceName": "imgsearch_gender",
		            "tabs": [
		              {
		                "value": "1:1",
		                "imggender": "all",
		                "selected": true,
		                "name": "全部",
		                "key": "pictproperty"
		              },
		              {
		                "value": "1:2",
		                "imggender": "female",
		                "name": "女",
		                "key": "pictproperty"
		              },
		              {
		                "value": "1:4",
		                "imggender": "male",
		                "name": "童",
		                "key": "pictproperty"
		              }
		            ],
		            "region": "187,542,14,586", // 默认的框
		            "mainPic": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB1IOGSOXXXXXXEXVXXXXXXXXXX",
		            "imgBtn": true,
		            "cats": [
		              {
		                "value": "0",
		                "name": "上衣",
		                "key": "cat",
		                "imgcat": "coat"
		              },
		              {
		                "value": "1",
		                "selected": true,
		                "name": "裙装",
		                "key": "cat",
		                "imgcat": "skirt"
		              },
		              {
		                "value": "2",
		                "name": "下装",
		                "key": "cat",
		                "imgcat": "xiazhuang"
		              },
		              {
		                "value": "3",
		                "name": "箱包",
		                "key": "cat",
		                "imgcat": "bag"
		              },
		              {
		                "value": "4",
		                "name": "鞋",
		                "key": "cat",
		                "imgcat": "shoes"
		              },
		              {
		                "value": "5",
		                "name": "配饰",
		                "key": "cat",
		                "imgcat": "more"
		              },
		              {
		                "value": "6",
		                "name": "零食",
		                "key": "cat",
		                "imgcat": "null"
		              },
		              {
		                "value": "7",
		                "name": "美妆",
		                "key": "cat",
		                "imgcat": "null"
		              },
		              {
		                "value": "8",
		                "name": "瓶饮",
		                "key": "cat",
		                "imgcat": "null"
		              },
		              {
		                "value": "9",
		                "name": "家具",
		                "key": "cat",
		                "imgcat": "null"
		              },
		              {
		                "value": "20",
		                "name": "玩具",
		                "key": "cat",
		                "imgcat": "null"
		              },
		              {
		                "value": "21",
		                "name": "内衣",
		                "key": "cat",
		                "imgcat": "null"
		              },
		              {
		                "value": "22",
		                "name": "数码",
		                "key": "cat",
		                "imgcat": "null"
		              },
		              {
		                "value": "88888888",
		                "name": "其他",
		                "key": "cat",
		                "imgcat": "null"
		              }
		            ],
		            "catTraceName": "imgsearch_cat"
		          }
		        },
		        "itemlist": { // 匹配商品列表
		          "status": "show",
		          "export": false,
		          "data": {
		            "collections": [
		              {
		                "trace": "imgauction",
		                "spmModId": "999",
		                "isRecommend": false,
		                "auctions": [
		                  {
		                    "category": "50010850",
		                    "raw_title": "大码女装2016年秋装新款韩版时尚卡通图案衬衣领显瘦连衣裙女潮",
		                    "user_id": "2860759430",
		                    "title": "大码女装2016年秋装新款韩版时尚卡通图案衬衣领显瘦连衣裙女潮",
		                    "shopcard": {
		                      "encryptedUserId": "UvCgLvmcbOFQGvNTT",
		                      "service": [
		                        486,
		                        1,
		                        3872
		                      ],
		                      "sellerCredit": 6,
		                      "isTmall": false,
		                      "delivery": [
		                        483,
		                        1,
		                        2939
		                      ],
		                      "totalRate": 9705,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        480,
		                        1,
		                        3146
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "168.00",
		                    "pid": "-2043988624",
		                    "nid": "537270605580",
		                    "nick": "幸福衣家yy",
		                    "comment_count": "65",
		                    "view_price": "59.99",
		                    "view_fee": "0.00",
		                    "view_sales": "104人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=537270605580&ns=1#detail", // 商品链接
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2860759430", // 店铺链接
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB2mdoNXR_xQeBjy0FhXXbAoFXa_!!2860759430.png", //showimage
		                    "comment_url": "//item.taobao.com/item.htm?id=537270605580&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "Jossepon/组士邦2016胖mm秋装新款卡通图案衬衣领显瘦连衣裙5595",
		                    "user_id": "1689955526",
		                    "title": "Jossepon/组士邦2016胖mm秋装新款卡通图案衬衣领显瘦连衣裙5595",
		                    "shopcard": {
		                      "encryptedUserId": "UvFx4OFkbMF8yMgTT",
		                      "service": [
		                        478,
		                        1,
		                        741
		                      ],
		                      "sellerCredit": 13,
		                      "isTmall": true,
		                      "delivery": [
		                        478,
		                        1,
		                        699
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        }
		                      ],
		                      "description": [
		                        478,
		                        -1,
		                        111
		                      ]
		                    },
		                    "item_loc": "广东 东莞",
		                    "reserve_price": "348.00",
		                    "pid": "-566762501",
		                    "nid": "538050019280",
		                    "nick": "jossepon旗舰店",
		                    "comment_count": "2",
		                    "view_price": "208.00",
		                    "view_fee": "8.00",
		                    "view_sales": "3人付款",
		                    "detail_url": "//detail.tmall.com/item.htm?id=538050019280&ns=1",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1689955526",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB28tJBaai5V1BjSspfXXapiXXa_!!1689955526.jpg",
		                    "comment_url": "//detail.tmall.com/item.htm?id=538050019280&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "尚天猫，就购了~",
		                        "dom_class": "icon-service-tianmao",
		                        "show_type": "0",
		                        "url": "//www.tmall.com/",
		                        "html": "",
		                        "innerText": "天猫宝贝",
		                        "position": "1",
		                        "icon_key": "icon-service-tianmao",
		                        "icon_category": "shop"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "2016秋冬新款韩版女装气质娃娃领中长款连衣裙显瘦包臀长袖打底裙",
		                    "user_id": "86159518",
		                    "title": "2016秋冬新款韩版女装气质娃娃领中长款连衣裙显瘦包臀长袖打底裙",
		                    "shopcard": {
		                      "encryptedUserId": "UOmxYMFkbvFgT",
		                      "service": [
		                        482,
		                        1,
		                        2028
		                      ],
		                      "sellerCredit": 8,
		                      "isTmall": false,
		                      "delivery": [
		                        491,
		                        1,
		                        6184
		                      ],
		                      "totalRate": 9629,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        475,
		                        1,
		                        1145
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "158.00",
		                    "pid": "-1943588830",
		                    "nid": "541091180619",
		                    "nick": "缘木求财",
		                    "comment_count": "0",
		                    "view_price": "158.00",
		                    "view_fee": "0.00",
		                    "view_sales": "2人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=541091180619&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=86159518",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB2zJ_DbMCN.eBjSZFoXXXj0FXa_!!86159518.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=541091180619&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "当季新品宝贝",
		                        "dom_class": "icon-service-new",
		                        "show_type": "0",
		                        "url": "//service.taobao.com/support/knowledge-1138476.htm",
		                        "html": "",
		                        "innerText": "当季新品宝贝",
		                        "position": "1",
		                        "icon_key": "icon-service-new",
		                        "icon_category": "cat_special"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "我不是妖怪整垮前女友宋妍霏美人为馅同款杨蓉白锦曦杨幂连衣裙秋",
		                    "user_id": "267656551",
		                    "title": "我不是妖怪整垮前女友宋妍霏美人为馅同款杨蓉白锦曦杨幂连衣裙秋",
		                    "shopcard": {
		                      "encryptedUserId": "UvCxuMC8LMF8Y",
		                      "service": [
		                        473,
		                        -1,
		                        87
		                      ],
		                      "sellerCredit": 7,
		                      "isTmall": false,
		                      "delivery": [
		                        475,
		                        0,
		                        0
		                      ],
		                      "totalRate": 9377,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        463,
		                        -1,
		                        171
		                      ]
		                    },
		                    "item_loc": "广东 东莞",
		                    "reserve_price": "163.00",
		                    "pid": "-552455053",
		                    "nid": "537301094150",
		                    "nick": "xiexiaowei198209",
		                    "comment_count": "0",
		                    "view_price": "99.00",
		                    "view_fee": "15.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=537301094150&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=267656551",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB1RrmPMVXXXXXBXpXXXXXXXXXX_!!0-item_pic.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=537301094150&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "冬秋装韩版立领修身显瘦女装加绒加厚中长款套头打底衫长袖连衣裙",
		                    "user_id": "1014742123",
		                    "title": "冬秋装韩版立领修身显瘦女装加绒加厚中长款套头打底衫长袖连衣裙",
		                    "shopcard": {
		                      "encryptedUserId": "UvFNYMmc0vCHyvWTT",
		                      "service": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "sellerCredit": 9,
		                      "isTmall": false,
		                      "delivery": [
		                        499,
		                        1,
		                        9629
		                      ],
		                      "totalRate": 9916,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        500,
		                        1,
		                        10000
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "240.00",
		                    "pid": "-1119857423",
		                    "nid": "541180646269",
		                    "nick": "保证小卖家",
		                    "comment_count": "0",
		                    "view_price": "88.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=541180646269&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1014742123",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB2ZkSib5GO.eBjSZFjXXcU9FXa_!!1014742123.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=541180646269&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "2677 实拍秋装女新款加绒加厚 大码韩版印花宽松中长款",
		                    "user_id": "2106631474",
		                    "title": "2677 实拍秋装女新款加绒加厚 大码韩版印花宽松中长款",
		                    "shopcard": {
		                      "encryptedUserId": "UvCHWMCxGvFQuMNTT",
		                      "service": [
		                        429,
		                        -1,
		                        1014
		                      ],
		                      "sellerCredit": 5,
		                      "isTmall": false,
		                      "delivery": [
		                        429,
		                        -1,
		                        1000
		                      ],
		                      "totalRate": 9944,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        }
		                      ],
		                      "description": [
		                        429,
		                        -1,
		                        916
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "60.00",
		                    "pid": "-1643429744",
		                    "nid": "541151940814",
		                    "nick": "三月彩蝶",
		                    "comment_count": "0",
		                    "view_price": "60.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=541151940814&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2106631474",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB2002JbxaJ.eBjSsziXXaJ_XXa_!!2106631474.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=541151940814&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "韩都衣舍短裙2016秋装新款女装假两件人物印花宽松长袖连衣裙包臀",
		                    "user_id": "2197565554",
		                    "title": "韩都衣舍短裙2016秋装新款女装假两件人物印花宽松长袖连衣裙包臀",
		                    "shopcard": {
		                      "encryptedUserId": "UvCHSMG8LMF8bMNTT",
		                      "service": [
		                        476,
		                        0,
		                        0
		                      ],
		                      "sellerCredit": 10,
		                      "isTmall": true,
		                      "delivery": [
		                        475,
		                        0,
		                        0
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        478,
		                        -1,
		                        121
		                      ]
		                    },
		                    "item_loc": "山东 济南",
		                    "reserve_price": "248.00",
		                    "pid": "-1960203917",
		                    "nid": "521333924828",
		                    "nick": "韩都衣舍众合亿鑫专卖店",
		                    "comment_count": "54",
		                    "view_price": "248.00",
		                    "view_fee": "0.00",
		                    "view_sales": "3人付款",
		                    "detail_url": "//detail.tmall.com/item.htm?id=521333924828&ns=1",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2197565554",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB19843OXXXXXa6XXXXXXXXXXXX_!!0-item_pic.jpg",
		                    "comment_url": "//detail.tmall.com/item.htm?id=521333924828&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "尚天猫，就购了~",
		                        "dom_class": "icon-service-tianmao",
		                        "show_type": "0",
		                        "url": "//www.tmall.com/",
		                        "html": "",
		                        "innerText": "天猫宝贝",
		                        "position": "1",
		                        "icon_key": "icon-service-tianmao",
		                        "icon_category": "shop"
		                      },
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "卖家赠送退货运费险",
		                        "dom_class": "icon-service-yunfeixian",
		                        "show_type": "0",
		                        "url": "//www.taobao.com/go/act/baoxian/yunfeixian.php",
		                        "html": "",
		                        "innerText": "赠送运费险",
		                        "position": "3",
		                        "icon_key": "icon-service-yunfeixian",
		                        "icon_category": "cat_special"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "韩都衣舍2016韩版女秋新款印花假两件宽松H型长袖连衣裙子",
		                    "user_id": "845317796",
		                    "title": "韩都衣舍2016韩版女秋新款印花假两件宽松H型长袖连衣裙子",
		                    "shopcard": {
		                      "encryptedUserId": "UOmQbvGHuMGkL",
		                      "service": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "sellerCredit": 7,
		                      "isTmall": false,
		                      "delivery": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        500,
		                        1,
		                        10000
		                      ]
		                    },
		                    "item_loc": "山东 济南",
		                    "reserve_price": "248.00",
		                    "pid": "",
		                    "nid": "540865031317",
		                    "nick": "tb2547666",
		                    "comment_count": "0",
		                    "view_price": "248.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=540865031317&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=845317796",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB1IldaOXXXXXcaXpXXXXXXXXXX_!!0-item_pic.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=540865031317&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "1",
		                        "trace": "srpservice",
		                        "title": "卖家承诺：宝贝由品牌厂商直接发货，品牌厂商授权销售！",
		                        "dom_class": "icon-service-shouquan",
		                        "show_type": "0",
		                        "url": "//www.taobao.com/go/act/sale/ppsqfx.php",
		                        "html": "",
		                        "innerText": "品牌授权",
		                        "position": "3",
		                        "icon_key": "icon-service-shouquan",
		                        "icon_category": "xb"
		                      },
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "卖家赠送退货运费险",
		                        "dom_class": "icon-service-yunfeixian",
		                        "show_type": "0",
		                        "url": "//www.taobao.com/go/act/baoxian/yunfeixian.php",
		                        "html": "",
		                        "innerText": "赠送运费险",
		                        "position": "3",
		                        "icon_key": "icon-service-yunfeixian",
		                        "icon_category": "cat_special"
		                      },
		                      {
		                        "outer_text": "1",
		                        "trace": "srpservice",
		                        "title": "8天退货",
		                        "dom_class": "icon-service-7tianjia",
		                        "show_type": "0",
		                        "url": "//xiaobao.taobao.com/contract/item_contract_detail.htm?item_id=540865031317&contract_id=2",
		                        "html": "",
		                        "innerText": "8天退货",
		                        "position": "3",
		                        "icon_key": "icon-service-7tianjia",
		                        "icon_category": "xb"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "胖mm春秋装2016加肥加大码女装200斤微胖妹妹假2件显瘦长袖连衣裙",
		                    "user_id": "835403615",
		                    "title": "胖mm春秋装2016加肥加大码女装200斤微胖妹妹假2件显瘦长袖连衣裙",
		                    "shopcard": {
		                      "encryptedUserId": "UOmvbMmNGMCHb",
		                      "service": [
		                        463,
		                        -1,
		                        297
		                      ],
		                      "sellerCredit": 8,
		                      "isTmall": false,
		                      "delivery": [
		                        470,
		                        -1,
		                        120
		                      ],
		                      "totalRate": 9708,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        450,
		                        -1,
		                        458
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "175.00",
		                    "pid": "-969771136",
		                    "nid": "537329020494",
		                    "nick": "shuangtao327",
		                    "comment_count": "1",
		                    "view_price": "79.00",
		                    "view_fee": "10.00",
		                    "view_sales": "1人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=537329020494&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=835403615",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB11YAFMVXXXXcbXXXXYXGcGpXX_M2.SS2",
		                    "comment_url": "//item.taobao.com/item.htm?id=537329020494&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "夕夕家2016秋季新款韩版衬衫领长袖裙个性卡通印花假两件连衣裙女",
		                    "user_id": "111586496",
		                    "title": "夕夕家2016秋季新款韩版衬衫领长袖裙个性卡通印花假两件连衣裙女",
		                    "shopcard": {
		                      "encryptedUserId": "UvFHYMFgLMmkL",
		                      "service": [
		                        446,
		                        -1,
		                        650
		                      ],
		                      "sellerCredit": 6,
		                      "isTmall": false,
		                      "delivery": [
		                        449,
		                        -1,
		                        578
		                      ],
		                      "totalRate": 9900,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        446,
		                        -1,
		                        547
		                      ]
		                    },
		                    "item_loc": "江苏 苏州",
		                    "reserve_price": "89.00",
		                    "pid": "-1726667627",
		                    "nid": "537945658698",
		                    "nick": "pobbc",
		                    "comment_count": "0",
		                    "view_price": "89.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=537945658698&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=111586496",
		                    "pic_url": "//g-search1.alicdn.com/img/bao/uploaded/i4/TB2sMh4XGi5V1BjSszdXXXUJXXa_!!111586496.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=537945658698&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "2016新款韩版秋装女装秋裙秋款长袖裙子潮 秋天学生秋季连衣裙女",
		                    "user_id": "611005706",
		                    "title": "2016新款韩版秋装女装秋裙秋款长袖裙子潮 秋天学生秋季连衣裙女",
		                    "shopcard": {
		                      "encryptedUserId": "UMCHYvmNbMGNL",
		                      "service": [
		                        476,
		                        1,
		                        238
		                      ],
		                      "sellerCredit": 10,
		                      "isTmall": false,
		                      "delivery": [
		                        480,
		                        1,
		                        2208
		                      ],
		                      "totalRate": 9500,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        471,
		                        0,
		                        0
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "215.00",
		                    "pid": "-1207828681",
		                    "nid": "537685539404",
		                    "nick": "520yuguohang",
		                    "comment_count": "6",
		                    "view_price": "45.00",
		                    "view_fee": "10.00",
		                    "view_sales": "13人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=537685539404&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=611005706",
		                    "pic_url": "//g-search1.alicdn.com/img/bao/uploaded/i4/TB2Y5aHXX95V1Bjy0FeXXXyfpXa_!!611005706.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=537685539404&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "1",
		                        "trace": "srpservice",
		                        "title": "8天退货",
		                        "dom_class": "icon-service-7tianjia",
		                        "show_type": "0",
		                        "url": "//xiaobao.taobao.com/contract/item_contract_detail.htm?item_id=537685539404&contract_id=2",
		                        "html": "",
		                        "innerText": "8天退货",
		                        "position": "3",
		                        "icon_key": "icon-service-7tianjia",
		                        "icon_category": "xb"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "尚古主义女装秋装假两件连衣裙2016新款印花A字裙翻领长袖打底裙",
		                    "user_id": "773733058",
		                    "title": "尚古主义女装秋装假两件连衣裙2016新款印花A字裙翻领长袖打底裙",
		                    "shopcard": {
		                      "encryptedUserId": "UMGcGMGvGvm84",
		                      "service": [
		                        479,
		                        1,
		                        930
		                      ],
		                      "sellerCredit": 16,
		                      "isTmall": true,
		                      "delivery": [
		                        478,
		                        1,
		                        878
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-jinguan"
		                        }
		                      ],
		                      "description": [
		                        484,
		                        0,
		                        0
		                      ]
		                    },
		                    "item_loc": "广东 东莞",
		                    "reserve_price": "189.00",
		                    "pid": "-1408111906",
		                    "nid": "524963319429",
		                    "nick": "尚古主义旗舰店",
		                    "comment_count": "88",
		                    "view_price": "159.00",
		                    "view_fee": "0.00",
		                    "view_sales": "1人付款",
		                    "detail_url": "//detail.tmall.com/item.htm?id=524963319429&ns=1",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=773733058",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB1smp0OXXXXXcKaFXXXXXXXXXX_!!2-item_pic.png",
		                    "comment_url": "//detail.tmall.com/item.htm?id=524963319429&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "尚天猫，就购了~",
		                        "dom_class": "icon-service-tianmao",
		                        "show_type": "0",
		                        "url": "//www.tmall.com/",
		                        "html": "",
		                        "innerText": "天猫宝贝",
		                        "position": "1",
		                        "icon_key": "icon-service-tianmao",
		                        "icon_category": "shop"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "121452038",
		                    "raw_title": "2016秋装中大女童韩版中大童假两件翻领卡通印花A字裙子",
		                    "user_id": "2354025371",
		                    "title": "2016秋装中大女童韩版中大童假两件翻领卡通印花A字裙子",
		                    "shopcard": {
		                      "encryptedUserId": "UvCvbMmNyMFvuvQTT",
		                      "service": [
		                        495,
		                        1,
		                        7181
		                      ],
		                      "sellerCredit": 7,
		                      "isTmall": false,
		                      "delivery": [
		                        490,
		                        1,
		                        4603
		                      ],
		                      "totalRate": 9906,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        483,
		                        1,
		                        1823
		                      ]
		                    },
		                    "item_loc": "广东 佛山",
		                    "reserve_price": "99.90",
		                    "pid": "-1021750365",
		                    "nid": "535663699890",
		                    "nick": "vivi族长",
		                    "comment_count": "2",
		                    "view_price": "69.90",
		                    "view_fee": "0.00",
		                    "view_sales": "2人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=535663699890&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2354025371",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB2uAYPsVXXXXbzXXXXXXXXXXXX_!!2354025371.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=535663699890&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "卖家赠送退货运费险",
		                        "dom_class": "icon-service-yunfeixian",
		                        "show_type": "0",
		                        "url": "//www.taobao.com/go/act/baoxian/yunfeixian.php",
		                        "html": "",
		                        "innerText": "赠送运费险",
		                        "position": "3",
		                        "icon_key": "icon-service-yunfeixian",
		                        "icon_category": "cat_special"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "加肥加大码女装秋装胖mm印花翻领显瘦连衣裙加绒加厚",
		                    "user_id": "2830065191",
		                    "title": "加肥加大码女装秋装胖mm印花翻领显瘦连衣裙加绒加厚",
		                    "shopcard": {
		                      "encryptedUserId": "UvCgGvmNLMFHSvQTT",
		                      "service": [
		                        470,
		                        -1,
		                        145
		                      ],
		                      "sellerCredit": 4,
		                      "isTmall": false,
		                      "delivery": [
		                        467,
		                        -1,
		                        200
		                      ],
		                      "totalRate": 9896,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        }
		                      ],
		                      "description": [
		                        462,
		                        -1,
		                        214
		                      ]
		                    },
		                    "item_loc": "广东 佛山",
		                    "reserve_price": "55.90",
		                    "pid": "-335244048",
		                    "nid": "541073271072",
		                    "nick": "杨青禾5988",
		                    "comment_count": "0",
		                    "view_price": "55.90",
		                    "view_fee": "0.00",
		                    "view_sales": "1人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=541073271072&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2830065191",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB2Zhw1bg1J.eBjy0FpXXaMoXXa_!!2830065191.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=541073271072&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "当季新品宝贝",
		                        "dom_class": "icon-service-new",
		                        "show_type": "0",
		                        "url": "//service.taobao.com/support/knowledge-1138476.htm",
		                        "html": "",
		                        "innerText": "当季新品宝贝",
		                        "position": "1",
		                        "icon_key": "icon-service-new",
		                        "icon_category": "cat_special"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "2016新款女款韩版秋装女装女裙 秋款长袖裙子潮印花秋季连衣裙女",
		                    "user_id": "2057678929",
		                    "title": "2016新款女款韩版秋装女装女裙 秋款长袖裙子潮印花秋季连衣裙女",
		                    "shopcard": {
		                      "encryptedUserId": "UvCNbMGxuOmkyOQTT",
		                      "service": [
		                        479,
		                        1,
		                        825
		                      ],
		                      "sellerCredit": 12,
		                      "isTmall": true,
		                      "delivery": [
		                        479,
		                        1,
		                        1218
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        }
		                      ],
		                      "description": [
		                        484,
		                        1,
		                        359
		                      ]
		                    },
		                    "item_loc": "广东 东莞",
		                    "reserve_price": "238.00",
		                    "pid": "-937269694",
		                    "nid": "535730447011",
		                    "nick": "qe旗舰店",
		                    "comment_count": "221",
		                    "view_price": "89.00",
		                    "view_fee": "0.00",
		                    "view_sales": "70人付款",
		                    "detail_url": "//detail.tmall.com/item.htm?id=535730447011&ns=1",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2057678929",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB1D0MpKVXXXXaFXXXXXXXXXXXX_!!0-item_pic.jpg",
		                    "comment_url": "//detail.tmall.com/item.htm?id=535730447011&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "尚天猫，就购了~",
		                        "dom_class": "icon-service-tianmao",
		                        "show_type": "0",
		                        "url": "//www.tmall.com/",
		                        "html": "",
		                        "innerText": "天猫宝贝",
		                        "position": "1",
		                        "icon_key": "icon-service-tianmao",
		                        "icon_category": "shop"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "2016秋冬加绒加厚哺乳连衣裙女孩印花时尚小翻领宽松孕妇裙子",
		                    "user_id": "1686619538",
		                    "title": "2016秋冬加绒加厚哺乳连衣裙女孩印花时尚小翻领宽松孕妇裙子",
		                    "shopcard": {
		                      "encryptedUserId": "UvFx4MCxYOF8GONTT",
		                      "service": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "sellerCredit": 0,
		                      "isTmall": false,
		                      "delivery": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [],
		                      "description": [
		                        500,
		                        1,
		                        10000
		                      ]
		                    },
		                    "item_loc": "山东 潍坊",
		                    "reserve_price": "89.00",
		                    "pid": "-148192585",
		                    "nid": "541071154256",
		                    "nick": "bxy别具一格",
		                    "comment_count": "0",
		                    "view_price": "89.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=541071154256&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1686619538",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB2UsIFbhmI.eBjy0FlXXbgkVXa_!!0-taoxiaopu_sell.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=541071154256&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "小鸟依人 秋季新品 藏青色翻领假两件印花连衣裙",
		                    "user_id": "70115247",
		                    "title": "小鸟依人 秋季新品 藏青色翻领假两件印花连衣裙",
		                    "shopcard": {
		                      "encryptedUserId": "UMGNYvF8yMmcT",
		                      "service": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "sellerCredit": 6,
		                      "isTmall": false,
		                      "delivery": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "totalRate": 9838,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        500,
		                        1,
		                        10000
		                      ]
		                    },
		                    "item_loc": "上海",
		                    "reserve_price": "129.00",
		                    "pid": "-871718509",
		                    "nid": "538603889851",
		                    "nick": "a452238049",
		                    "comment_count": "0",
		                    "view_price": "129.00",
		                    "view_fee": "15.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=538603889851&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=70115247",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB22gQsXfPB11BjSsppXXcjYVXa_!!70115247.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=538603889851&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "2016新款女裙女装韩版冬装休闲裙子女款冬裙冬天修身长袖连衣裙女",
		                    "user_id": "2377829241",
		                    "title": "2016新款女裙女装韩版冬装休闲裙子女款冬裙冬天修身长袖连衣裙女",
		                    "shopcard": {
		                      "encryptedUserId": "UvCvuMGgyOFI0vQTT",
		                      "service": [
		                        424,
		                        -1,
		                        1109
		                      ],
		                      "sellerCredit": 6,
		                      "isTmall": false,
		                      "delivery": [
		                        415,
		                        -1,
		                        1280
		                      ],
		                      "totalRate": 9320,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        409,
		                        -1,
		                        1319
		                      ]
		                    },
		                    "item_loc": "四川 成都",
		                    "reserve_price": "89.00",
		                    "pid": "-1508465845",
		                    "nid": "539467796098",
		                    "nick": "金牌买家q",
		                    "comment_count": "0",
		                    "view_price": "89.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=539467796098&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2377829241",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB2zm4sXssb61BjSszbXXcvMpXa_!!2377829241.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=539467796098&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "秀谛亚2016秋新品女 韩版假两件翻领拼接打底印花宽松长袖连衣裙",
		                    "user_id": "1791686127",
		                    "title": "秀谛亚2016秋新品女 韩版假两件翻领拼接打底印花宽松长袖连衣裙",
		                    "shopcard": {
		                      "encryptedUserId": "UvFcSvFx4MCHyMWTT",
		                      "service": [
		                        476,
		                        1,
		                        87
		                      ],
		                      "sellerCredit": 15,
		                      "isTmall": true,
		                      "delivery": [
		                        476,
		                        0,
		                        0
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        }
		                      ],
		                      "description": [
		                        484,
		                        1,
		                        111
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "238.00",
		                    "pid": "-383618949",
		                    "nid": "526413126343",
		                    "nick": "秀谛亚旗舰店",
		                    "comment_count": "24",
		                    "view_price": "89.90",
		                    "view_fee": "0.00",
		                    "view_sales": "3人付款",
		                    "detail_url": "//detail.tmall.com/item.htm?id=526413126343&ns=1",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1791686127",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB256pyjVXXXXbDXXXXXXXXXXXX_!!1791686127.jpg",
		                    "comment_url": "//detail.tmall.com/item.htm?id=526413126343&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "尚天猫，就购了~",
		                        "dom_class": "icon-service-tianmao",
		                        "show_type": "0",
		                        "url": "//www.tmall.com/",
		                        "html": "",
		                        "innerText": "天猫宝贝",
		                        "position": "1",
		                        "icon_key": "icon-service-tianmao",
		                        "icon_category": "shop"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "韩都衣舍2016韩版女秋新款印花假两件宽松H型长袖连衣裙",
		                    "user_id": "2229750200",
		                    "title": "韩都衣舍2016韩版女秋新款印花假两件宽松H型长袖连衣裙",
		                    "shopcard": {
		                      "encryptedUserId": "UvCIyOFcbvmIWvNTT",
		                      "service": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "sellerCredit": 2,
		                      "isTmall": false,
		                      "delivery": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        }
		                      ],
		                      "description": [
		                        500,
		                        1,
		                        10000
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "75.00",
		                    "pid": "-668573498",
		                    "nid": "539390385921",
		                    "nick": "小蜗的彩妆",
		                    "comment_count": "0",
		                    "view_price": "75.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=539390385921&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2229750200",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB2QkuBXnka61Bjy0FoXXb1sFXa_!!2229750200.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=539390385921&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "秋冬款翻领接拼撞色假两件印花宽松韩版学生可爱长袖打底连衣裙",
		                    "user_id": "2841867741",
		                    "title": "秋冬款翻领接拼撞色假两件印花宽松韩版学生可爱长袖打底连衣裙",
		                    "shopcard": {
		                      "encryptedUserId": "UvCg0vFgLMGc0vQTT",
		                      "service": [
		                        470,
		                        -1,
		                        137
		                      ],
		                      "sellerCredit": 7,
		                      "isTmall": false,
		                      "delivery": [
		                        472,
		                        -1,
		                        80
		                      ],
		                      "totalRate": 9821,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        459,
		                        -1,
		                        279
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "135.00",
		                    "pid": "-63930609",
		                    "nid": "540555168677",
		                    "nick": "陪你过上幸孕生活",
		                    "comment_count": "0",
		                    "view_price": "48.60",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=540555168677&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2841867741",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB1aWW4NVXXXXaaaXXXXXXXXXXX_!!0-item_pic.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=540555168677&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "当季新品宝贝",
		                        "dom_class": "icon-service-new",
		                        "show_type": "0",
		                        "url": "//service.taobao.com/support/knowledge-1138476.htm",
		                        "html": "",
		                        "innerText": "当季新品宝贝",
		                        "position": "1",
		                        "icon_key": "icon-service-new",
		                        "icon_category": "cat_special"
		                      },
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "放心淘",
		                        "dom_class": "icon-service-fangxintao",
		                        "show_type": "0",
		                        "url": "//www.taobao.com/market/common/fangxintao.php",
		                        "html": "放心淘",
		                        "innerText": "放心淘",
		                        "position": "1",
		                        "icon_key": "icon-service-fangxintao",
		                        "icon_category": "cat_special"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "内搭连衣裙秋冬季长袖打底假两件韩版娃娃领印花显瘦包臀 一步裙a",
		                    "user_id": "642792383",
		                    "title": "内搭连衣裙秋冬季长袖打底假两件韩版娃娃领印花显瘦包臀 一步裙a",
		                    "shopcard": {
		                      "encryptedUserId": "UMCQyMGkyvGgG",
		                      "service": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "sellerCredit": 1,
		                      "isTmall": false,
		                      "delivery": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        }
		                      ],
		                      "description": [
		                        500,
		                        1,
		                        10000
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "68.00",
		                    "pid": "-1423414506",
		                    "nid": "540554908445",
		                    "nick": "扯元宝",
		                    "comment_count": "1",
		                    "view_price": "68.00",
		                    "view_fee": "0.00",
		                    "view_sales": "4人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=540554908445&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=642792383",
		                    "pic_url": "//g-search1.alicdn.com/img/bao/uploaded/i4/TB2FehXaCCI.eBjy1XbXXbUBFXa_!!642792383.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=540554908445&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "当季新品宝贝",
		                        "dom_class": "icon-service-new",
		                        "show_type": "0",
		                        "url": "//service.taobao.com/support/knowledge-1138476.htm",
		                        "html": "",
		                        "innerText": "当季新品宝贝",
		                        "position": "1",
		                        "icon_key": "icon-service-new",
		                        "icon_category": "cat_special"
		                      },
		                      {
		                        "outer_text": "1",
		                        "trace": "srpservice",
		                        "title": "8天退货",
		                        "dom_class": "icon-service-7tianjia",
		                        "show_type": "0",
		                        "url": "//xiaobao.taobao.com/contract/item_contract_detail.htm?item_id=540554908445&contract_id=2",
		                        "html": "",
		                        "innerText": "8天退货",
		                        "position": "3",
		                        "icon_key": "icon-service-7tianjia",
		                        "icon_category": "xb"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "娃娃领长袖连衣裙秋装潮宽松显瘦打底裙韩版学生中长款印花衬衫裙",
		                    "user_id": "1699555403",
		                    "title": "娃娃领长袖连衣裙秋装潮宽松显瘦打底裙韩版学生中长款印花衬衫裙",
		                    "shopcard": {
		                      "encryptedUserId": "UvFxSOF8bMFQWvWTT",
		                      "service": [
		                        476,
		                        1,
		                        142
		                      ],
		                      "sellerCredit": 14,
		                      "isTmall": true,
		                      "delivery": [
		                        478,
		                        1,
		                        669
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        }
		                      ],
		                      "description": [
		                        482,
		                        0,
		                        0
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "128.00",
		                    "pid": "-1489755070",
		                    "nid": "539422624838",
		                    "nick": "霓彩丽裳服饰旗舰店",
		                    "comment_count": "1",
		                    "view_price": "89.00",
		                    "view_fee": "0.00",
		                    "view_sales": "2人付款",
		                    "detail_url": "//detail.tmall.com/item.htm?id=539422624838&ns=1",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1699555403",
		                    "pic_url": "//g-search1.alicdn.com/img/bao/uploaded/i4/TB1O3o0NpXXXXbzXpXXXXXXXXXX_!!0-item_pic.jpg",
		                    "comment_url": "//detail.tmall.com/item.htm?id=539422624838&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "尚天猫，就购了~",
		                        "dom_class": "icon-service-tianmao",
		                        "show_type": "0",
		                        "url": "//www.tmall.com/",
		                        "html": "",
		                        "innerText": "天猫宝贝",
		                        "position": "1",
		                        "icon_key": "icon-service-tianmao",
		                        "icon_category": "shop"
		                      },
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "卖家赠送退货运费险",
		                        "dom_class": "icon-service-yunfeixian",
		                        "show_type": "0",
		                        "url": "//www.taobao.com/go/act/baoxian/yunfeixian.php",
		                        "html": "",
		                        "innerText": "赠送运费险",
		                        "position": "3",
		                        "icon_key": "icon-service-yunfeixian",
		                        "icon_category": "cat_special"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "韩都衣舍2016韩版女秋新款印花假两件宽松显瘦长袖连衣裙NJ6773翝",
		                    "user_id": "2891752320",
		                    "title": "韩都衣舍2016韩版女秋新款印花假两件宽松显瘦长袖连衣裙NJ6773翝",
		                    "shopcard": {
		                      "encryptedUserId": "UvCgSvFcbvCvyvNTT",
		                      "service": [
		                        463,
		                        -1,
		                        266
		                      ],
		                      "sellerCredit": 6,
		                      "isTmall": false,
		                      "delivery": [
		                        463,
		                        -1,
		                        276
		                      ],
		                      "totalRate": 9467,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        446,
		                        -1,
		                        539
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "89.00",
		                    "pid": "-2062345367",
		                    "nid": "538451953982",
		                    "nick": "oybsj87",
		                    "comment_count": "1",
		                    "view_price": "89.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=538451953982&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2891752320",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB2NThNaF_AQeBjSZFBXXX22XXa_!!2891752320.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=538451953982&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "嬉琦秋装韩版宽松休闲连衣裙女长袖可爱印花假两件方领女短裙大码",
		                    "user_id": "1881648045",
		                    "title": "嬉琦秋装韩版宽松休闲连衣裙女长袖可爱印花假两件方领女短裙大码",
		                    "shopcard": {
		                      "encryptedUserId": "UvFg4vFx0OmN0MQTT",
		                      "service": [
		                        472,
		                        -1,
		                        90
		                      ],
		                      "sellerCredit": 14,
		                      "isTmall": true,
		                      "delivery": [
		                        469,
		                        -1,
		                        146
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        }
		                      ],
		                      "description": [
		                        484,
		                        1,
		                        217
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "238.00",
		                    "pid": "-586438373",
		                    "nid": "535487224427",
		                    "nick": "嬉琦旗舰店",
		                    "comment_count": "19",
		                    "view_price": "98.00",
		                    "view_fee": "0.00",
		                    "view_sales": "4人付款",
		                    "detail_url": "//detail.tmall.com/item.htm?id=535487224427&ns=1",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1881648045",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB13RjNNVXXXXc8XpXXXXXXXXXX_!!0-item_pic.jpg",
		                    "comment_url": "//detail.tmall.com/item.htm?id=535487224427&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "尚天猫，就购了~",
		                        "dom_class": "icon-service-tianmao",
		                        "show_type": "0",
		                        "url": "//www.tmall.com/",
		                        "html": "",
		                        "innerText": "天猫宝贝",
		                        "position": "1",
		                        "icon_key": "icon-service-tianmao",
		                        "icon_category": "shop"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "OH欧韩时尚2016初秋女装新款韩版假两件人物印花宽松长袖连衣裙潮",
		                    "user_id": "2894986755",
		                    "title": "OH欧韩时尚2016初秋女装新款韩版假两件人物印花宽松长袖连衣裙潮",
		                    "shopcard": {
		                      "encryptedUserId": "UvCgSMmk4MCcbMQTT",
		                      "service": [
		                        488,
		                        1,
		                        4746
		                      ],
		                      "sellerCredit": 6,
		                      "isTmall": false,
		                      "delivery": [
		                        488,
		                        1,
		                        4912
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        488,
		                        1,
		                        5707
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "60.00",
		                    "pid": "-383710236",
		                    "nid": "537805419332",
		                    "nick": "艾魅尔时尚",
		                    "comment_count": "0",
		                    "view_price": "60.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=537805419332&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2894986755",
		                    "pic_url": "//g-search1.alicdn.com/img/bao/uploaded/i4/TB2bAS_Xp95V1Bjy0FdXXc5BVXa_!!2894986755.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=537805419332&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "卖家赠送退货运费险",
		                        "dom_class": "icon-service-yunfeixian",
		                        "show_type": "0",
		                        "url": "//www.taobao.com/go/act/baoxian/yunfeixian.php",
		                        "html": "",
		                        "innerText": "赠送运费险",
		                        "position": "3",
		                        "icon_key": "icon-service-yunfeixian",
		                        "icon_category": "cat_special"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "2016秋冬装新款长袖翻领加绒加厚打底裙女韩版宽松显瘦印花连衣裙",
		                    "user_id": "1715674384",
		                    "title": "2016秋冬装新款长袖翻领加绒加厚打底裙女韩版宽松显瘦印花连衣裙",
		                    "shopcard": {
		                      "encryptedUserId": "UvFcYMFxuMmv4MNTT",
		                      "service": [
		                        482,
		                        1,
		                        2019
		                      ],
		                      "sellerCredit": 10,
		                      "isTmall": false,
		                      "delivery": [
		                        480,
		                        1,
		                        1587
		                      ],
		                      "totalRate": 9706,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        475,
		                        1,
		                        1040
		                      ]
		                    },
		                    "item_loc": "广东 深圳",
		                    "reserve_price": "199.00",
		                    "pid": "-1623945615",
		                    "nid": "539758442072",
		                    "nick": "tb59754835",
		                    "comment_count": "1",
		                    "view_price": "59.00",
		                    "view_fee": "0.00",
		                    "view_sales": "28人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=539758442072&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1715674384",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB1V8OBNFXXXXbPXFXXXXXXXXXX_!!0-item_pic.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=539758442072&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "金牌卖家",
		                        "dom_class": "icon-service-jinpaimaijia",
		                        "show_type": "0",
		                        "url": "//www.taobao.com/go/act/jpmj.php",
		                        "html": "",
		                        "innerText": "金牌卖家",
		                        "position": "1",
		                        "icon_key": "icon-service-jinpaimaijia",
		                        "icon_category": "shop"
		                      },
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "放心淘",
		                        "dom_class": "icon-service-fangxintao",
		                        "show_type": "0",
		                        "url": "//www.taobao.com/market/common/fangxintao.php",
		                        "html": "放心淘",
		                        "innerText": "放心淘",
		                        "position": "1",
		                        "icon_key": "icon-service-fangxintao",
		                        "icon_category": "cat_special"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "2016新款女款韩版秋装女装秋裙 秋款长袖裙子潮印花秋季连衣裙女",
		                    "user_id": "909479546",
		                    "title": "2016新款女款韩版秋装女装秋裙 秋款长袖裙子潮印花秋季连衣裙女",
		                    "shopcard": {
		                      "encryptedUserId": "UOFNSMmcSMFQL",
		                      "service": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "sellerCredit": 10,
		                      "isTmall": false,
		                      "delivery": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "totalRate": 9820,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        500,
		                        1,
		                        10000
		                      ]
		                    },
		                    "item_loc": "广东 东莞",
		                    "reserve_price": "238.00",
		                    "pid": "-1357404801",
		                    "nid": "541005709027",
		                    "nick": "巧衣点",
		                    "comment_count": "0",
		                    "view_price": "238.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=541005709027&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=909479546",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB2a_AMXNRzc1FjSZFPXXcGAFXa_!!909479546.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=541005709027&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "2016秋季新款衬衣领假两件人物印花宽松加厚不倒绒长袖孕妇连衣裙",
		                    "user_id": "1898411716",
		                    "title": "2016秋季新款衬衣领假两件人物印花宽松加厚不倒绒长袖孕妇连衣裙",
		                    "shopcard": {
		                      "encryptedUserId": "UvFgSOmQYvFcYMgTT",
		                      "service": [
		                        444,
		                        -1,
		                        681
		                      ],
		                      "sellerCredit": 3,
		                      "isTmall": false,
		                      "delivery": [
		                        461,
		                        -1,
		                        316
		                      ],
		                      "totalRate": 9782,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        }
		                      ],
		                      "description": [
		                        455,
		                        -1,
		                        344
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "75.00",
		                    "pid": "-1759803889",
		                    "nid": "538830053956",
		                    "nick": "金正兵0369",
		                    "comment_count": "0",
		                    "view_price": "75.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=538830053956&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1898411716",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB1t5SeNpXXXXcAXFXXXXXXXXXX_!!0-item_pic.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=538830053956&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "大码女装秋装连衣裙加绒加肥加大加厚秋天胖mm印花翻领显瘦连衣裙",
		                    "user_id": "2980131781",
		                    "title": "大码女装秋装连衣裙加绒加肥加大加厚秋天胖mm印花翻领显瘦连衣裙",
		                    "shopcard": {
		                      "encryptedUserId": "UvCk4vmHGvFc4vQTT",
		                      "service": [
		                        490,
		                        1,
		                        5522
		                      ],
		                      "sellerCredit": 8,
		                      "isTmall": true,
		                      "delivery": [
		                        490,
		                        1,
		                        5635
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        492,
		                        1,
		                        5262
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "134.00",
		                    "pid": "-2062734523",
		                    "nid": "540387605135",
		                    "nick": "卓蕾雅旗舰店",
		                    "comment_count": "2",
		                    "view_price": "88.00",
		                    "view_fee": "0.00",
		                    "view_sales": "4人付款",
		                    "detail_url": "//detail.tmall.com/item.htm?id=540387605135&ns=1",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2980131781",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB2UrttakWM.eBjSZFhXXbdWpXa_!!2980131781.jpg",
		                    "comment_url": "//detail.tmall.com/item.htm?id=540387605135&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "当季新品宝贝",
		                        "dom_class": "icon-service-new",
		                        "show_type": "0",
		                        "url": "//service.taobao.com/support/knowledge-1138476.htm",
		                        "html": "",
		                        "innerText": "当季新品宝贝",
		                        "position": "1",
		                        "icon_key": "icon-service-new",
		                        "icon_category": "cat_special"
		                      },
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "尚天猫，就购了~",
		                        "dom_class": "icon-service-tianmao",
		                        "show_type": "0",
		                        "url": "//www.tmall.com/",
		                        "html": "",
		                        "innerText": "天猫宝贝",
		                        "position": "1",
		                        "icon_key": "icon-service-tianmao",
		                        "icon_category": "shop"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "大码女装2016年秋装新款韩版时尚卡通图案衬衣领显瘦连衣裙女潮",
		                    "user_id": "1987942723",
		                    "title": "大码女装2016年秋装新款韩版时尚卡通图案衬衣领显瘦连衣裙女潮",
		                    "shopcard": {
		                      "encryptedUserId": "UvFk4MGk0vCcyvWTT",
		                      "service": [
		                        463,
		                        -1,
		                        271
		                      ],
		                      "sellerCredit": 11,
		                      "isTmall": false,
		                      "delivery": [
		                        466,
		                        -1,
		                        204
		                      ],
		                      "totalRate": 9858,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        }
		                      ],
		                      "description": [
		                        457,
		                        -1,
		                        323
		                      ]
		                    },
		                    "item_loc": "浙江 杭州",
		                    "reserve_price": "96.00",
		                    "pid": "",
		                    "nid": "541201814501",
		                    "nick": "嘻丫丫时尚女装zool",
		                    "comment_count": "0",
		                    "view_price": "48.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=541201814501&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1987942723",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB20Tq6b71M.eBjSZFOXXc0rFXa_!!1987942723.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=541201814501&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "2016春装 韩版 娃娃领 长袖 中长款 连衣裙 卡通人物印花 打底裙",
		                    "user_id": "17016940",
		                    "title": "2016春装 韩版 娃娃领 长袖 中长款 连衣裙 卡通人物印花 打底裙",
		                    "shopcard": {
		                      "encryptedUserId": "UvFcWvFxSMmNT",
		                      "service": [
		                        473,
		                        -1,
		                        80
		                      ],
		                      "sellerCredit": 10,
		                      "isTmall": false,
		                      "delivery": [
		                        480,
		                        1,
		                        1695
		                      ],
		                      "totalRate": 9902,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        470,
		                        0,
		                        0
		                      ]
		                    },
		                    "item_loc": "江苏 苏州",
		                    "reserve_price": "88.00",
		                    "pid": "-1238475471",
		                    "nid": "536100132727",
		                    "nick": "shwebmaster",
		                    "comment_count": "0",
		                    "view_price": "67.00",
		                    "view_fee": "10.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=536100132727&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=17016940",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB1CUM6KVXXXXaOXpXXXXXXXXXX_!!0-item_pic.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=536100132727&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "胖妹妹秋装连衣裙2016潮胖mm加肥加大卡通翻领中长款打底裙",
		                    "user_id": "1987942723",
		                    "title": "胖妹妹秋装连衣裙2016潮胖mm加肥加大卡通翻领中长款打底裙",
		                    "shopcard": {
		                      "encryptedUserId": "UvFk4MGk0vCcyvWTT",
		                      "service": [
		                        463,
		                        -1,
		                        271
		                      ],
		                      "sellerCredit": 11,
		                      "isTmall": false,
		                      "delivery": [
		                        466,
		                        -1,
		                        204
		                      ],
		                      "totalRate": 9858,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        }
		                      ],
		                      "description": [
		                        457,
		                        -1,
		                        323
		                      ]
		                    },
		                    "item_loc": "浙江 杭州",
		                    "reserve_price": "96.00",
		                    "pid": "",
		                    "nid": "541186192818",
		                    "nick": "嘻丫丫时尚女装zool",
		                    "comment_count": "0",
		                    "view_price": "48.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=541186192818&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1987942723",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB1DgnVNFXXXXbnaXXXXXXXXXXX_!!0-item_pic.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=541186192818&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "外贸女装 秋装新款韩版东大门翻领卡通女孩印花显瘦长袖连衣裙女",
		                    "user_id": "2654802945",
		                    "title": "外贸女装 秋装新款韩版东大门翻领卡通女孩印花显瘦长袖连衣裙女",
		                    "shopcard": {
		                      "encryptedUserId": "UvCxbMmgWvCk0MQTT",
		                      "service": [
		                        484,
		                        1,
		                        3570
		                      ],
		                      "sellerCredit": 13,
		                      "isTmall": false,
		                      "delivery": [
		                        484,
		                        1,
		                        3488
		                      ],
		                      "totalRate": 9933,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        }
		                      ],
		                      "description": [
		                        480,
		                        1,
		                        2885
		                      ]
		                    },
		                    "item_loc": "上海",
		                    "reserve_price": "69.99",
		                    "pid": "-2062906453",
		                    "nid": "539464840461",
		                    "nick": "宝贝隆专注外贸原单",
		                    "comment_count": "1",
		                    "view_price": "69.99",
		                    "view_fee": "9.00",
		                    "view_sales": "2人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=539464840461&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2654802945",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB2kYXDXsgd61BjSZFPXXbVVFXa_!!2654802945.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=539464840461&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "金牌卖家",
		                        "dom_class": "icon-service-jinpaimaijia",
		                        "show_type": "0",
		                        "url": "//www.taobao.com/go/act/jpmj.php",
		                        "html": "",
		                        "innerText": "金牌卖家",
		                        "position": "1",
		                        "icon_key": "icon-service-jinpaimaijia",
		                        "icon_category": "shop"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "2016春新款女假两件人物印花宽松长袖连衣裙",
		                    "user_id": "693488962",
		                    "title": "2016春新款女假两件人物印花宽松长袖连衣裙",
		                    "shopcard": {
		                      "encryptedUserId": "UMCkGMmg4OFxy",
		                      "service": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "sellerCredit": 5,
		                      "isTmall": false,
		                      "delivery": [
		                        500,
		                        1,
		                        10000
		                      ],
		                      "totalRate": 9790,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        }
		                      ],
		                      "description": [
		                        500,
		                        1,
		                        10000
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "60.00",
		                    "pid": "-1189919270",
		                    "nid": "537334020654",
		                    "nick": "leiyali0526",
		                    "comment_count": "0",
		                    "view_price": "60.00",
		                    "view_fee": "10.00",
		                    "view_sales": "1人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=537334020654&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=693488962",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB1aofbLpXXXXbQaFXXXXXXXXXX_!!0-item_pic.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=537334020654&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "巨棉2016秋冬新款加绒连衣裙修身韩版女大码长袖中长款打底衫裙子",
		                    "user_id": "2535454443",
		                    "title": "巨棉2016秋冬新款加绒连衣裙修身韩版女大码长袖中长款打底衫裙子",
		                    "shopcard": {
		                      "encryptedUserId": "UvC8GMFQbMmQ0vWTT",
		                      "service": [
		                        476,
		                        0,
		                        0
		                      ],
		                      "sellerCredit": 9,
		                      "isTmall": false,
		                      "delivery": [
		                        476,
		                        0,
		                        0
		                      ],
		                      "totalRate": 9668,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        468,
		                        -1,
		                        70
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "115.00",
		                    "pid": "-1724723023",
		                    "nid": "541020240835",
		                    "nick": "子情贝轩",
		                    "comment_count": "0",
		                    "view_price": "49.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=541020240835&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2535454443",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB2xzTfbb1J.eBjSszcXXbFzVXa_!!2535454443.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=541020240835&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "加肥加大码女装秋装百搭印花翻领显瘦连衣裙加绒加厚短裙子打底裙",
		                    "user_id": "2750187557",
		                    "title": "加肥加大码女装秋装百搭印花翻领显瘦连衣裙加绒加厚短裙子打底裙",
		                    "shopcard": {
		                      "encryptedUserId": "UvCcbvmH4MG8bMWTT",
		                      "service": [
		                        487,
		                        1,
		                        4346
		                      ],
		                      "sellerCredit": 2,
		                      "isTmall": false,
		                      "delivery": [
		                        491,
		                        1,
		                        6350
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-xin"
		                        }
		                      ],
		                      "description": [
		                        491,
		                        1,
		                        6920
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "105.00",
		                    "pid": "",
		                    "nid": "541249671626",
		                    "nick": "鸿杰靓衣",
		                    "comment_count": "0",
		                    "view_price": "58.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=541249671626&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2750187557",
		                    "pic_url": "//g-search1.alicdn.com/img/bao/uploaded/i4/TB1Om5ENpXXXXbKXpXXXXXXXXXX_!!0-item_pic.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=541249671626&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "韩都衣舍2016韩版女秋新款印花假两件宽松H型长袖连衣裙NJ6773翝",
		                    "user_id": "1930154169",
		                    "title": "韩都衣舍2016韩版女秋新款印花假两件宽松H型长袖连衣裙NJ6773翝",
		                    "shopcard": {
		                      "encryptedUserId": "UvFkGvmHbMmHLOQTT",
		                      "service": [
		                        476,
		                        0,
		                        0
		                      ],
		                      "sellerCredit": 9,
		                      "isTmall": false,
		                      "delivery": [
		                        468,
		                        -1,
		                        172
		                      ],
		                      "totalRate": 9701,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-zuan"
		                        }
		                      ],
		                      "description": [
		                        465,
		                        -1,
		                        133
		                      ]
		                    },
		                    "item_loc": "浙江 杭州",
		                    "reserve_price": "275.00",
		                    "pid": "-66938142",
		                    "nid": "539009481901",
		                    "nick": "艾米源c",
		                    "comment_count": "4",
		                    "view_price": "55.00",
		                    "view_fee": "0.00",
		                    "view_sales": "17人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=539009481901&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1930154169",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB1Om5ENpXXXXbKXpXXXXXXXXXX_!!0-item_pic.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=539009481901&ns=1&on_comment=1",
		                    "icon": []
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "冬装上新 韩版新款女装加绒加厚打底衫中长款修身显瘦打底连衣裙",
		                    "user_id": "2342003648",
		                    "title": "冬装上新 韩版新款女装加绒加厚打底衫中长款修身显瘦打底连衣裙",
		                    "shopcard": {
		                      "encryptedUserId": "UvCv0vCNWvGx0ONTT",
		                      "service": [
		                        472,
		                        -1,
		                        96
		                      ],
		                      "sellerCredit": 12,
		                      "isTmall": false,
		                      "delivery": [
		                        472,
		                        -1,
		                        91
		                      ],
		                      "totalRate": 9874,
		                      "levelClasses": [
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        },
		                        {
		                          "levelClass": "icon-supple-level-guan"
		                        }
		                      ],
		                      "description": [
		                        465,
		                        -1,
		                        145
		                      ]
		                    },
		                    "item_loc": "广东 东莞",
		                    "reserve_price": "95.00",
		                    "pid": "-970877020",
		                    "nid": "540590756379",
		                    "nick": "衣莉斯女装",
		                    "comment_count": "0",
		                    "view_price": "45.00",
		                    "view_fee": "0.00",
		                    "view_sales": "1人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=540590756379&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2342003648",
		                    "pic_url": "//g-search2.alicdn.com/img/bao/uploaded/i4/TB2cD8faOGO.eBjSZFPXXcKCXXa_!!2342003648.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=540590756379&ns=1&on_comment=1",
		                    "icon": [
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "当季新品宝贝",
		                        "dom_class": "icon-service-new",
		                        "show_type": "0",
		                        "url": "//service.taobao.com/support/knowledge-1138476.htm",
		                        "html": "",
		                        "innerText": "当季新品宝贝",
		                        "position": "1",
		                        "icon_key": "icon-service-new",
		                        "icon_category": "cat_special"
		                      },
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "金牌卖家",
		                        "dom_class": "icon-service-jinpaimaijia",
		                        "show_type": "0",
		                        "url": "//www.taobao.com/go/act/jpmj.php",
		                        "html": "",
		                        "innerText": "金牌卖家",
		                        "position": "1",
		                        "icon_key": "icon-service-jinpaimaijia",
		                        "icon_category": "shop"
		                      },
		                      {
		                        "outer_text": "0",
		                        "trace": "srpservice",
		                        "title": "卖家赠送退货运费险",
		                        "dom_class": "icon-service-yunfeixian",
		                        "show_type": "0",
		                        "url": "//www.taobao.com/go/act/baoxian/yunfeixian.php",
		                        "html": "",
		                        "innerText": "赠送运费险",
		                        "position": "3",
		                        "icon_key": "icon-service-yunfeixian",
		                        "icon_category": "cat_special"
		                      }
		                    ]
		                  },
		                  {
		                    "category": "50010850",
		                    "raw_title": "2016秋冬新款 娃娃领可爱小女孩印花卫衣 加厚孕妇连衣裙",
		                    "user_id": "1767609433",
		                    "title": "2016秋冬新款 娃娃领可爱小女孩印花卫衣 加厚孕妇连衣裙",
		                    "shopcard": {
		                      "encryptedUserId": "UvFcLMGxWOFQGvWTT",
		                      "service": [
		                        0,
		                        0,
		                        0
		                      ],
		                      "sellerCredit": 0,
		                      "isTmall": false,
		                      "delivery": [
		                        0,
		                        0,
		                        0
		                      ],
		                      "totalRate": 10000,
		                      "levelClasses": [],
		                      "description": [
		                        0,
		                        0,
		                        0
		                      ]
		                    },
		                    "item_loc": "广东 广州",
		                    "reserve_price": "58.00",
		                    "pid": "-803367078",
		                    "nid": "539539389677",
		                    "nick": "时尚潮流y店",
		                    "comment_count": "0",
		                    "view_price": "58.00",
		                    "view_fee": "0.00",
		                    "view_sales": "0人付款",
		                    "detail_url": "//item.taobao.com/item.htm?id=539539389677&ns=1#detail",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1767609433",
		                    "pic_url": "//g-search3.alicdn.com/img/bao/uploaded/i4/TB2xj.AXwQc61BjSZFGXXa1DFXa_!!1767609433.jpg",
		                    "comment_url": "//item.taobao.com/item.htm?id=539539389677&ns=1&on_comment=1",
		                    "icon": []
		                  }
		                ],
		                "title": "外观相似宝贝"
		              },
		              {
		                "trace": "imgrecauction",
		                "spmModId": "998",
		                "isRecommend": true,
		                "auctions": [
		                  {
		                    "raw_title": "紧身包臀裙连衣裙2016夏季气质修身显瘦短袖性感大码女装打底短裙",
		                    "view_sales": "23人付款",
		                    "user_id": "404350915",
		                    "title": "紧身包臀裙连衣裙2016夏季气质修身显瘦短袖性感大码女装打底短裙",
		                    "reserve_price": "160.0",
		                    "nid": "532936639824",
		                    "view_price": "160.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=532936639824&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=404350915",
		                    "pic_url": "//img.alicdn.com/i3/404350915/TB2MjTupVXXXXX0XFXXXXXXXXXX_!!404350915.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "2016秋季新款气质女装针织长袖连衣裙修身显瘦包臀长裙大码打底裙",
		                    "view_sales": "1647人付款",
		                    "user_id": "1765122917",
		                    "title": "2016秋季新款气质女装针织长袖连衣裙修身显瘦包臀长裙大码打底裙",
		                    "reserve_price": "138.0",
		                    "nid": "524366302317",
		                    "view_price": "138.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=524366302317&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1765122917",
		                    "pic_url": "//img.alicdn.com/i1/T1QsSuFdxXXXXXXXXX_!!0-item_pic.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "2016秋冬蝙蝠袖v领显瘦系带收腰针织中长款包臀长袖打底连衣裙女",
		                    "view_sales": "113人付款",
		                    "user_id": "1608865903",
		                    "title": "2016秋冬蝙蝠袖v领显瘦系带收腰针织中长款包臀长袖打底连衣裙女",
		                    "reserve_price": "198.0",
		                    "nid": "528218030733",
		                    "view_price": "198.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=528218030733&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1608865903",
		                    "pic_url": "//img.alicdn.com/i3/TB1Dt2xLVXXXXXpapXXXXXXXXXX_!!0-item_pic.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "新款秋装2016韩版女装名媛修身包臀中长款春秋长裙气质长袖连衣裙",
		                    "view_sales": "3716人付款",
		                    "user_id": "1672645612",
		                    "title": "新款秋装2016韩版女装名媛修身包臀中长款春秋长裙气质长袖连衣裙",
		                    "reserve_price": "219.0",
		                    "nid": "524981806758",
		                    "view_price": "59.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=524981806758&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1672645612",
		                    "pic_url": "//img.alicdn.com/i4/TB1LVinLpXXXXciXpXXXXXXXXXX_!!0-item_pic.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "2016春装新款连衣裙两件套装女装春秋修身长袖圆领卡通春季短裙子",
		                    "view_sales": "26人付款",
		                    "user_id": "905403607",
		                    "title": "2016春装新款连衣裙两件套装女装春秋修身长袖圆领卡通春季短裙子",
		                    "reserve_price": "58.0",
		                    "nid": "527647247131",
		                    "view_price": "58.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=527647247131&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=905403607",
		                    "pic_url": "//img.alicdn.com/i4/905403607/TB2LpMhkVXXXXaaXpXXXXXXXXXX_!!905403607.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "2016春秋新款压褶几何图案收腰连衣裙中长款长袖打底女韩版长裙",
		                    "view_sales": "2346人付款",
		                    "user_id": "1749295688",
		                    "title": "2016春秋新款压褶几何图案收腰连衣裙中长款长袖打底女韩版长裙",
		                    "reserve_price": "280.0",
		                    "nid": "525746275959",
		                    "view_price": "280.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=525746275959&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1749295688",
		                    "pic_url": "//img.alicdn.com/i4/TB17xhoOXXXXXXDXVXXXXXXXXXX_!!0-item_pic.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "2016秋冬新款韩版显瘦卡通时尚潮流加绒加厚连帽卫衣裙长袖连衣裙",
		                    "view_sales": "1278人付款",
		                    "user_id": "899017856",
		                    "title": "2016秋冬新款韩版显瘦卡通时尚潮流加绒加厚连帽卫衣裙长袖连衣裙",
		                    "reserve_price": "269.0",
		                    "nid": "537197493609",
		                    "view_price": "269.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=537197493609&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=899017856",
		                    "pic_url": "//img.alicdn.com/i3/TB1oUV7OXXXXXX8aVXXXXXXXXXX_!!0-item_pic.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "女装秋装2016新款潮韩版修身长袖印花连衣裙中长款秋冬a字裙气质",
		                    "view_sales": "2118人付款",
		                    "user_id": "122533505",
		                    "title": "女装秋装2016新款潮韩版修身长袖印花连衣裙中长款秋冬a字裙气质",
		                    "reserve_price": "369.0",
		                    "nid": "538961986864",
		                    "view_price": "369.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=538961986864&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=122533505",
		                    "pic_url": "//img.alicdn.com/i1/122533505/TB2U_amacHA11Bjy0FiXXckfVXa_!!122533505.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "2016新款韩版修身不规则雪纺连衣裙短袖女直筒裙印花a字中裙子夏",
		                    "view_sales": "20人付款",
		                    "user_id": "1135742648",
		                    "title": "2016新款韩版修身不规则雪纺连衣裙短袖女直筒裙印花a字中裙子夏",
		                    "reserve_price": "129.0",
		                    "nid": "530430149385",
		                    "view_price": "129.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=530430149385&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1135742648",
		                    "pic_url": "//img.alicdn.com/i6/TB1vkZVMpXXXXaYXVXXYXGcGpXX_M2.SS2",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "2016秋冬新款中长款针织衫女套头韩版宽松大码毛衣女士打底连衣裙",
		                    "view_sales": "2941人付款",
		                    "user_id": "2257341963",
		                    "title": "2016秋冬新款中长款针织衫女套头韩版宽松大码毛衣女士打底连衣裙",
		                    "reserve_price": "588.0",
		                    "nid": "538177129448",
		                    "view_price": "138.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=538177129448&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2257341963",
		                    "pic_url": "//img.alicdn.com/i1/TB1.sPcNpXXXXa3XXXXXXXXXXXX_!!0-item_pic.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "新款连衣裙冬2016早秋新款女装修身加绒加厚套装裙子两件套短裙女",
		                    "view_sales": "247人付款",
		                    "user_id": "2052895028",
		                    "title": "新款连衣裙冬2016早秋新款女装修身加绒加厚套装裙子两件套短裙女",
		                    "reserve_price": "229.0",
		                    "nid": "535690452084",
		                    "view_price": "229.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=535690452084&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2052895028",
		                    "pic_url": "//img.alicdn.com/i3/2052895028/TB2AQ4bsVXXXXXgXpXXXXXXXXXX_!!2052895028.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "秋季女装2016新款时尚套装裙子两件套短裙韩版显瘦长袖秋冬连衣裙",
		                    "view_sales": "227人付款",
		                    "user_id": "764138847",
		                    "title": "秋季女装2016新款时尚套装裙子两件套短裙韩版显瘦长袖秋冬连衣裙",
		                    "reserve_price": "175.0",
		                    "nid": "538147115284",
		                    "view_price": "175.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=538147115284&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=764138847",
		                    "pic_url": "//img.alicdn.com/i3/764138847/TB2.gJKap95V1Bjy0FbXXawipXa_!!764138847.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "欧昵雪2016秋装新款打底针织连衣裙时尚百搭绣花长袖秋冬A字短裙",
		                    "view_sales": "281人付款",
		                    "user_id": "1040428670",
		                    "title": "欧昵雪2016秋装新款打底针织连衣裙时尚百搭绣花长袖秋冬A字短裙",
		                    "reserve_price": "298.0",
		                    "nid": "538199079284",
		                    "view_price": "248.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=538199079284&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1040428670",
		                    "pic_url": "//img.alicdn.com/i2/TB1PgJ5OXXXXXagapXXXXXXXXXX_!!0-item_pic.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "【天天特价】2016秋新款女装韩版翻领卡通女孩印花显瘦长袖连衣裙",
		                    "view_sales": "28人付款",
		                    "user_id": "931660660",
		                    "title": "【天天特价】2016秋新款女装韩版翻领卡通女孩印花显瘦长袖连衣裙",
		                    "reserve_price": "118.0",
		                    "nid": "538578132169",
		                    "view_price": "118.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=538578132169&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=931660660",
		                    "pic_url": "//img.alicdn.com/i4/931660660/TB25PyqXezz11Bjy1XdXXbfqVXa_!!931660660.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "2016秋装新款韩版冬季连帽卫衣连衣裙女休闲秋冬加厚长袖修身a型",
		                    "view_sales": "173人付款",
		                    "user_id": "2107512745",
		                    "title": "2016秋装新款韩版冬季连帽卫衣连衣裙女休闲秋冬加厚长袖修身a型",
		                    "reserve_price": "198.0",
		                    "nid": "538883376117",
		                    "view_price": "99.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=538883376117&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2107512745",
		                    "pic_url": "//img.alicdn.com/i4/TB1ljiuNpXXXXcnXpXXXXXXXXXX_!!0-item_pic.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "初语 秋冬学生长袖套头印花连衣裙女宽松卫衣女裙时尚包臀打底裙",
		                    "view_sales": "339人付款",
		                    "user_id": "761679524",
		                    "title": "初语 秋冬学生长袖套头印花连衣裙女宽松卫衣女裙时尚包臀打底裙",
		                    "reserve_price": "239.0",
		                    "nid": "533019445308",
		                    "view_price": "239.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=533019445308&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=761679524",
		                    "pic_url": "//img.alicdn.com/i2/TB1kYOdOXXXXXXpXpXXXXXXXXXX_!!0-item_pic.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "当天发货 摩亦定制2016夏新款奥利弗亮片印花V领休闲连衣裙",
		                    "view_sales": "132人付款",
		                    "user_id": "2672532832",
		                    "title": "当天发货 摩亦定制2016夏新款奥利弗亮片印花V领休闲连衣裙",
		                    "reserve_price": "178.0",
		                    "nid": "533846179064",
		                    "view_price": "178.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=533846179064&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=2672532832",
		                    "pic_url": "//img.alicdn.com/i2/2672532832/TB2o1RgqFXXXXbuXpXXXXXXXXXX_!!2672532832.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "秀谛亚韩版2016秋新款女 假两件翻领打底裙子 印花宽松长袖连衣裙",
		                    "view_sales": "1人付款",
		                    "user_id": "1030091157",
		                    "title": "秀谛亚韩版2016秋新款女 假两件翻领打底裙子 印花宽松长袖连衣裙",
		                    "reserve_price": "238.0",
		                    "nid": "526430776393",
		                    "view_price": "238.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=526430776393&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=1030091157",
		                    "pic_url": "//img.alicdn.com/i3/TB1jxtjOXXXXXXGaFXXXXXXXXXX_!!0-item_pic.jpg",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "韩都衣舍旗舰店女装秋装2016新款潮印花宽松裙子假两件长袖连衣裙",
		                    "view_sales": "50人付款",
		                    "user_id": "58152263",
		                    "title": "韩都衣舍旗舰店女装秋装2016新款潮印花宽松裙子假两件长袖连衣裙",
		                    "reserve_price": "248.0",
		                    "nid": "528142204997",
		                    "view_price": "248.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=528142204997&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=58152263",
		                    "pic_url": "//img.alicdn.com/i4/58152263/TB22oAeaJAvbeFjSspbXXbcOFXa_!!58152263.png",
		                    "icon": []
		                  },
		                  {
		                    "raw_title": "欧洲站2016秋装女装新款欧货潮红色连衣裙修身长袖中长款打底裙子",
		                    "view_sales": "196人付款",
		                    "user_id": "367039997",
		                    "title": "欧洲站2016秋装女装新款欧货潮红色连衣裙修身长袖中长款打底裙子",
		                    "reserve_price": "868.0",
		                    "nid": "43253167607",
		                    "view_price": "868.00",
		                    "detail_url": "//item.taobao.com/item.htm?scm=1007.11224.29491.0&id=43253167607&pvid=1e68dea3-a736-43ae-9cbe-9faf6c654cf5",
		                    "shopLink": "//store.taobao.com/shop/view_shop.htm?user_number_id=367039997",
		                    "pic_url": "//img.alicdn.com/i1/TB1pH1qNFXXXXbSXpXXXXXXXXXX_!!0-item_pic.jpg",
		                    "icon": []
		                  }
		                ],
		                "title": "您可能会喜欢"
		              }
		            ]
		          }
		        }
		      },
		      "feature": {
		        "webpOff": false,
		        "retinaOff": false,
		        "shopcardOff": false
		      },
		      "mainInfo": {
		        "currentUrl": "//www.pailitao.com/search?app=imgsearch&tfsid=TB1IOGSOXXXXXXEXVXXXXXXXXXX",
		        "srpGlobal": {
		          "machine": "3-71042",
		          "style": "grid",
		          "sp_url": "vaHR0cDoLjEwLzEw2My4yNi4o5MDE3Njbi9zL2JpcHA9cD9hcGljdHVyZidHM9ZSCJTdEJTdByJmNvbXh0dHBnPWyemlwJnNcy1zYz1zfcGFpcnB8wbGl0YWYxMTEyMjNzEwNDIuuc3QzJnVT1waXF1ZkdWN0cm9tfJnJhbmXBjc3JjPRfJnBpY3mNoc2VhcXJsPTEmdlPPVRCMU1NPWFhYRWFhYRVhWWFhYWFhYYWCZuWFhPTQ0Jm91ZtdD1qdGc29u",
		          "bucketid": 12,
		          "buckets": "",
		          "cat": "",
		          "q": "",
		          "s": 0,
		          "multi_bucket": "12_10_7_0_0_0_0_0",
		          "encode_q": "",
		          "srpName": "imgsearchsrp",
		          "tnk": "",
		          "utf8_q": ""
		        },
		        "traceInfo": {
		          "traceData": {
		            "allMonthSales": [
		              "104",
		              "3",
		              "2",
		              "0",
		              "0",
		              "0",
		              "3",
		              "0",
		              "1",
		              "0",
		              "13",
		              "1",
		              "2",
		              "1",
		              "70",
		              "0",
		              "0",
		              "0",
		              "3",
		              "0",
		              "0",
		              "4",
		              "2",
		              "0",
		              "4",
		              "0",
		              "28",
		              "0",
		              "0",
		              "4",
		              "0",
		              "0",
		              "0",
		              "2",
		              "1",
		              "0",
		              "0",
		              "17",
		              "1",
		              "0",
		              "0",
		              "2",
		              "0",
		              "9"
		            ],
		            "allPrices": [
		              "59.99",
		              "208.00",
		              "158.00",
		              "99.00",
		              "88.00",
		              "60.00",
		              "248.00",
		              "248.00",
		              "79.00",
		              "89.00",
		              "45.00",
		              "159.00",
		              "69.90",
		              "55.90",
		              "89.00",
		              "89.00",
		              "129.00",
		              "89.00",
		              "89.90",
		              "75.00",
		              "48.60",
		              "68.00",
		              "89.00",
		              "89.00",
		              "98.00",
		              "60.00",
		              "59.00",
		              "238.00",
		              "75.00",
		              "88.00",
		              "48.00",
		              "67.00",
		              "48.00",
		              "69.99",
		              "60.00",
		              "49.00",
		              "58.00",
		              "55.00",
		              "45.00",
		              "58.00",
		              "62.00",
		              "158.00",
		              "65.00",
		              "178.00"
		            ],
		            "recommendPrices": [
		              "160.00",
		              "138.00",
		              "198.00",
		              "59.00",
		              "58.00",
		              "280.00",
		              "269.00",
		              "369.00",
		              "129.00",
		              "138.00",
		              "229.00",
		              "175.00",
		              "248.00",
		              "118.00",
		              "99.00",
		              "239.00",
		              "178.00",
		              "238.00",
		              "248.00",
		              "868.00"
		            ],
		            "recommendNids": [
		              "532936639824",
		              "524366302317",
		              "528218030733",
		              "524981806758",
		              "527647247131",
		              "525746275959",
		              "537197493609",
		              "538961986864",
		              "530430149385",
		              "538177129448",
		              "535690452084",
		              "538147115284",
		              "538199079284",
		              "538578132169",
		              "538883376117",
		              "533019445308",
		              "533846179064",
		              "526430776393",
		              "528142204997",
		              "43253167607"
		            ],
		            "colo": "st3",
		            "at_colo": "st3",
		            "query": "",
		            "allNids": [
		              "537270605580",
		              "538050019280",
		              "541091180619",
		              "537301094150",
		              "541180646269",
		              "541151940814",
		              "521333924828",
		              "540865031317",
		              "537329020494",
		              "537945658698",
		              "537685539404",
		              "524963319429",
		              "535663699890",
		              "541073271072",
		              "535730447011",
		              "541071154256",
		              "538603889851",
		              "539467796098",
		              "526413126343",
		              "539390385921",
		              "540555168677",
		              "540554908445",
		              "539422624838",
		              "538451953982",
		              "535487224427",
		              "537805419332",
		              "539758442072",
		              "541005709027",
		              "538830053956",
		              "540387605135",
		              "541201814501",
		              "536100132727",
		              "541186192818",
		              "539464840461",
		              "537334020654",
		              "541020240835",
		              "541249671626",
		              "539009481901",
		              "540590756379",
		              "539539389677",
		              "538262357227",
		              "540300830026",
		              "538804529644",
		              "540159450964"
		            ],
		            "at_host": "pailitao011226171042.st3",
		            "allMainPics": [
		              "TB2mdoNXR_xQeBjy0FhXXbAoFXa_!!2860759430.png",
		              "TB28tJBaai5V1BjSspfXXapiXXa_!!1689955526.jpg",
		              "TB2zJ_DbMCN.eBjSZFoXXXj0FXa_!!86159518.jpg",
		              "TB1RrmPMVXXXXXBXpXXXXXXXXXX_!!0-item_pic.jpg",
		              "TB2ZkSib5GO.eBjSZFjXXcU9FXa_!!1014742123.jpg",
		              "TB2002JbxaJ.eBjSsziXXaJ_XXa_!!2106631474.jpg",
		              "TB19843OXXXXXa6XXXXXXXXXXXX_!!0-item_pic.jpg",
		              "TB1IldaOXXXXXcaXpXXXXXXXXXX_!!0-item_pic.jpg",
		              "TB11YAFMVXXXXcbXXXXYXGcGpXX_M2.SS2",
		              "TB2sMh4XGi5V1BjSszdXXXUJXXa_!!111586496.jpg",
		              "TB2Y5aHXX95V1Bjy0FeXXXyfpXa_!!611005706.jpg",
		              "TB1smp0OXXXXXcKaFXXXXXXXXXX_!!2-item_pic.png",
		              "TB2uAYPsVXXXXbzXXXXXXXXXXXX_!!2354025371.jpg",
		              "TB2Zhw1bg1J.eBjy0FpXXaMoXXa_!!2830065191.jpg",
		              "TB1D0MpKVXXXXaFXXXXXXXXXXXX_!!0-item_pic.jpg",
		              "TB2UsIFbhmI.eBjy0FlXXbgkVXa_!!0-taoxiaopu_sell.jpg",
		              "TB22gQsXfPB11BjSsppXXcjYVXa_!!70115247.jpg",
		              "TB2zm4sXssb61BjSszbXXcvMpXa_!!2377829241.jpg",
		              "TB256pyjVXXXXbDXXXXXXXXXXXX_!!1791686127.jpg",
		              "TB2QkuBXnka61Bjy0FoXXb1sFXa_!!2229750200.jpg",
		              "TB1aWW4NVXXXXaaaXXXXXXXXXXX_!!0-item_pic.jpg",
		              "TB2FehXaCCI.eBjy1XbXXbUBFXa_!!642792383.jpg",
		              "TB1O3o0NpXXXXbzXpXXXXXXXXXX_!!0-item_pic.jpg",
		              "TB2NThNaF_AQeBjSZFBXXX22XXa_!!2891752320.jpg",
		              "TB13RjNNVXXXXc8XpXXXXXXXXXX_!!0-item_pic.jpg",
		              "TB2bAS_Xp95V1Bjy0FdXXc5BVXa_!!2894986755.jpg",
		              "TB1V8OBNFXXXXbPXFXXXXXXXXXX_!!0-item_pic.jpg",
		              "TB2a_AMXNRzc1FjSZFPXXcGAFXa_!!909479546.jpg",
		              "TB1t5SeNpXXXXcAXFXXXXXXXXXX_!!0-item_pic.jpg",
		              "TB2UrttakWM.eBjSZFhXXbdWpXa_!!2980131781.jpg",
		              "TB20Tq6b71M.eBjSZFOXXc0rFXa_!!1987942723.jpg",
		              "TB1CUM6KVXXXXaOXpXXXXXXXXXX_!!0-item_pic.jpg",
		              "TB1DgnVNFXXXXbnaXXXXXXXXXXX_!!0-item_pic.jpg",
		              "TB2kYXDXsgd61BjSZFPXXbVVFXa_!!2654802945.jpg",
		              "TB1aofbLpXXXXbQaFXXXXXXXXXX_!!0-item_pic.jpg",
		              "TB2xzTfbb1J.eBjSszcXXbFzVXa_!!2535454443.jpg",
		              "TB1Om5ENpXXXXbKXpXXXXXXXXXX_!!0-item_pic.jpg",
		              "TB1Om5ENpXXXXbKXpXXXXXXXXXX_!!0-item_pic.jpg",
		              "TB2cD8faOGO.eBjSZFPXXcKCXXa_!!2342003648.jpg",
		              "TB2xj.AXwQc61BjSZFGXXa1DFXa_!!1767609433.jpg",
		              "TB2uTVqaqi5V1BjSszdXXXUJXXa_!!0-taoxiaopu_sell.jpg",
		              "TB2Nr5IX5GO.eBjSZFpXXb3tFXa_!!1768327736.jpg",
		              "TB2SivfXM_z11Bjy1XbXXaScFXa_!!747478098.jpg",
		              "TB25dE0XwGI.eBjSspbXXcWoVXa_!!415060235.jpg"
		            ],
		            "spu_combo": "",
		            "allTotalSales": [
		              "184",
		              "15",
		              "2",
		              "0",
		              "0",
		              "0",
		              "128",
		              "0",
		              "3",
		              "0",
		              "25",
		              "345",
		              "15",
		              "1",
		              "587",
		              "0",
		              "0",
		              "0",
		              "78",
		              "0",
		              "0",
		              "4",
		              "3",
		              "2",
		              "44",
		              "0",
		              "30",
		              "0",
		              "0",
		              "4",
		              "0",
		              "0",
		              "0",
		              "3",
		              "2",
		              "0",
		              "0",
		              "21",
		              "1",
		              "0",
		              "0",
		              "2",
		              "0",
		              "9"
		            ],
		            "allBackCats": [
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "121452038",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850",
		              "50010850"
		            ],
		            "hostname": "pailitao011226171042.st3",
		            "docsReturn": "44",
		            "multi_bucket": "12_10_7_0_0_0_0_0",
		            "if_tank": "0",
		            "nick": "",
		            "auctionNids": [
		              "537270605580",
		              "538050019280",
		              "541091180619",
		              "537301094150",
		              "541180646269",
		              "541151940814",
		              "521333924828",
		              "540865031317",
		              "537329020494",
		              "537945658698",
		              "537685539404",
		              "524963319429",
		              "535663699890",
		              "541073271072",
		              "535730447011",
		              "541071154256",
		              "538603889851",
		              "539467796098",
		              "526413126343",
		              "539390385921",
		              "540555168677",
		              "540554908445",
		              "539422624838",
		              "538451953982",
		              "535487224427",
		              "537805419332",
		              "539758442072",
		              "541005709027",
		              "538830053956",
		              "540387605135",
		              "541201814501",
		              "536100132727",
		              "541186192818",
		              "539464840461",
		              "537334020654",
		              "541020240835",
		              "541249671626",
		              "539009481901",
		              "540590756379",
		              "539539389677"
		            ],
		            "totalHits": "1603866",
		            "qp_bury": "",
		            "rn": "71ea2b26347c991a6d4d3c51acbd776a",
		            "multivariate": "",
		            "bucketId": "10",
		            "rewrite_bury": "",
		            "catdirectForMaidian": "",
		            "allUserIds": [
		              "2860759430",
		              "1689955526",
		              "86159518",
		              "267656551",
		              "1014742123",
		              "2106631474",
		              "2197565554",
		              "845317796",
		              "835403615",
		              "111586496",
		              "611005706",
		              "773733058",
		              "2354025371",
		              "2830065191",
		              "2057678929",
		              "1686619538",
		              "70115247",
		              "2377829241",
		              "1791686127",
		              "2229750200",
		              "2841867741",
		              "642792383",
		              "1699555403",
		              "2891752320",
		              "1881648045",
		              "2894986755",
		              "1715674384",
		              "909479546",
		              "1898411716",
		              "2980131781",
		              "1987942723",
		              "17016940",
		              "1987942723",
		              "2654802945",
		              "693488962",
		              "2535454443",
		              "2750187557",
		              "1930154169",
		              "2342003648",
		              "1767609433",
		              "2042118330",
		              "1768327736",
		              "747478098",
		              "415060235"
		            ],
		            "remoteip": "103.250.225.118",
		            "catdirect": "",
		            "querytype_bury": "",
		            "auctionPrices": [
		              "59.99",
		              "208.00",
		              "158.00",
		              "99.00",
		              "88.00",
		              "60.00",
		              "248.00",
		              "248.00",
		              "79.00",
		              "89.00",
		              "45.00",
		              "159.00",
		              "69.90",
		              "55.90",
		              "89.00",
		              "89.00",
		              "129.00",
		              "89.00",
		              "89.90",
		              "75.00",
		              "48.60",
		              "68.00",
		              "89.00",
		              "89.00",
		              "98.00",
		              "60.00",
		              "59.00",
		              "238.00",
		              "75.00",
		              "88.00",
		              "48.00",
		              "67.00",
		              "48.00",
		              "69.99",
		              "60.00",
		              "49.00",
		              "58.00",
		              "55.00",
		              "45.00",
		              "58.00"
		            ],
		            "catLevelOne": "",
		            "srppage": "1",
		            "from_pos": "",
		            "allSkuPics": [],
		            "allUserTypes": [
		              "0",
		              "1",
		              "0",
		              "0",
		              "0",
		              "0",
		              "1",
		              "0",
		              "0",
		              "0",
		              "0",
		              "1",
		              "0",
		              "0",
		              "1",
		              "0",
		              "0",
		              "0",
		              "1",
		              "0",
		              "0",
		              "0",
		              "1",
		              "0",
		              "1",
		              "0",
		              "0",
		              "0",
		              "0",
		              "1",
		              "0",
		              "0",
		              "0",
		              "0",
		              "0",
		              "0",
		              "0",
		              "0",
		              "0",
		              "0",
		              "0",
		              "0",
		              "0",
		              "0"
		            ],
		            "statsClick": "",
		            "at_lflog": "0-0-0-0-2-1603866-0-all|",
		            "cat": "",
		            "alitrackid": "",
		            "lastAlitrackid": "",
		            "sortExprValues": [
		              "11010294.000000",
		              "310262.093750",
		              "210526.640625",
		              "10180.949219",
		              "10134.002930",
		              "10100.500000",
		              "10098.283203",
		              "10092.117188",
		              "10009.516602",
		              "141.044235",
		              "140.113251",
		              "133.056442",
		              "131.129517",
		              "121.617027",
		              "119.124458",
		              "116.504616",
		              "113.078194",
		              "111.294281",
		              "108.680359",
		              "105.948128",
		              "105.910248",
		              "103.430916",
		              "101.141777",
		              "97.574104",
		              "91.718674",
		              "90.269516",
		              "84.854271",
		              "83.708397",
		              "82.961311",
		              "81.557281",
		              "81.097382",
		              "80.159538",
		              "79.804672",
		              "79.054771",
		              "73.389565",
		              "73.373558",
		              "73.373558",
		              "73.373558",
		              "72.695168",
		              "70.617966",
		              "70.542702",
		              "67.670769",
		              "64.520866",
		              "63.229755"
		            ],
		            "catpredict_bury": "",
		            "sort2": "",
		            "at_bucketid": "10",
		            "noResultCode": "0"
		          },
		          "pvStat": "vers=j&searchurl=1&cat=&direct_cat=&at_lflog=0-0-0-0-2-1603866-0-all|&at_bucketid=10&multi_bucket=12_10_7_0_0_0_0_0&at_colo=st3&at_host=pailitao011226171042.st3&at_alitrackid=&last_alitrackid=&stats_show=&rn=71ea2b26347c991a6d4d3c51acbd776a&nick=&multivariate=&srppage=1&s_query="
		        },
		        "remainMods": [],
		        "modLinks": {
		          "default": "//www.pailitao.com/search?app=imgsearch&tfsid=TB1IOGSOXXXXXXEXVXXXXXXXXXX",
		          "filter": "//www.pailitao.com/search?app=imgsearch&tfsid=TB1IOGSOXXXXXXEXVXXXXXXXXXX&fs=1",
		          "breadcrumb": "//www.pailitao.com/search?app=imgsearch&tfsid=TB1IOGSOXXXXXXEXVXXXXXXXXXX",
		          "nav": "//www.pailitao.com/search?app=imgsearch&tfsid=TB1IOGSOXXXXXXEXVXXXXXXXXXX&cps=yes",
		          "tab": "//www.pailitao.com/search?app=imgsearch&tfsid=TB1IOGSOXXXXXXEXVXXXXXXXXXX",
		          "sortbar": "//www.pailitao.com/search?app=imgsearch&tfsid=TB1IOGSOXXXXXXEXVXXXXXXXXXX",
		          "pager": "//www.pailitao.com/search?app=imgsearch&tfsid=TB1IOGSOXXXXXXEXVXXXXXXXXXX"
		        }
		      }
		    }
		  ]
		}
		
### Kalava

* 找同款接口

    URL：/kalava?imglink=
    
    请求方式：GET
    
    返回结果：
    
		{
		  "status": 0, //状态，0为正常
		  "data": [ //数组，固定只有两个元素，第一个为整理后数据，第二个为原始数据
		    {
		      "match": [ //为适用我们的接口返回多个匹配结果的情况，这是一个匹配结果的数组
		        {
		          "box": {
		            "y": 0.0225,
		            "x": 0.275,
		            "w": 0.6175,
		            "h": 0.9125
		          },
		          "good_list": [ // 匹配商品的列表
		            {
		              "showimage": "/data/disk3/img/img005/906/7c972e4405df1102.jpg",
		              "good_url": "https://detail.tmall.com/item.htm?id=537322954034"
		            },
		            {
		              "showimage": "/data/disk3/img/img005/697/cf6b3241ac9312a1.jpg",
		              "good_url": "https://detail.tmall.com/item.htm?id=537322954034"
		            },
		            {
		              "showimage": "/data/disk3/img/img005/955/d6c703febb575443.jpg",
		              "good_url": "http://shop.mogujie.com/detail/1k299tq"
		            }
		          ]
		        }
		      ],
		      "imgid": "11070495057390352989",
		      "imgsize": "800*800",
		      "imglink": "http://pic.adkalava.com/img005/989/99a24c99c7783a5d.jpg", //原图链接
		      "imgpath": "img005/989/99a24c99c7783a5d.jpg"
		    },
		    { // 原始数据
		      "errno": 0,
		      "time_cost_server": 7.6686,
		      "time_cost_core": 7.5073,
		      "combiner_id": "6100",
		      "time_stamp": 1478501597.708279,
		      "image_file": "/data/disk3/faster_rcnn_train/image_server_data/5d3a78c7994ca299b3fd738b33936abb.jpeg",
		      "data": {
		        "detect": [
		          {
		            "box": {
		              "y": 0.0225,
		              "x": 0.275,
		              "w": 0.6175,
		              "h": 0.9125
		            },
		            "id": "71553",
		            "score": 0.9999,
		            "name": "连衣裙",
		            "child": {
		              "match": [
		                {
		                  "name": "https://detail.tmall.com/item.htm?id=537322954034",
		                  "showimage": "/data/disk3/img/img005/906/7c972e4405df1102.jpg",
		                  "score": 0.15908571109534445,
		                  "showbox": {
		                    "y": 1,
		                    "x": 106,
		                    "w": 249,
		                    "h": 386
		                  },
		                  "showimages": [
		                    [
		                      "/data/disk3/img/img005/906/7c972e4405df1102.jpg",
		                      [
		                        66.0,
		                        1.0,
		                        329.0,
		                        387.0
		                      ],
		                      6.285919666290283
		                    ],
		                    [
		                      "/data/disk3/img/img005/187/a7608069dd27d25b.jpg",
		                      [
		                        35.0,
		                        1.0,
		                        328.0,
		                        385.0
		                      ],
		                      11.177762031555176
		                    ],
		                    [
		                      "/data/disk3/img/img005/931/d48a24daaeabcc2b.jpg",
		                      [
		                        27.0,
		                        9.0,
		                        333.0,
		                        391.0
		                      ],
		                      14.60973072052002
		                    ]
		                  ],
		                  "id": "495714497453753816"
		                },
		                {
		                  "name": "https://detail.tmall.com/item.htm?id=537322954034",
		                  "showimage": "/data/disk3/img/img005/697/cf6b3241ac9312a1.jpg",
		                  "score": 0.06299732967156228,
		                  "showbox": {
		                    "y": 12,
		                    "x": 125,
		                    "w": 179,
		                    "h": 377
		                  },
		                  "showimages": [
		                    [
		                      "/data/disk3/img/img005/697/cf6b3241ac9312a1.jpg",
		                      [
		                        44.0,
		                        0.0,
		                        340.0,
		                        400.0
		                      ],
		                      15.873688697814941
		                    ]
		                  ],
		                  "id": "495714497453753816"
		                },
		                {
		                  "name": "http://shop.mogujie.com/detail/1k299tq",
		                  "showimage": "/data/disk3/img/img005/955/d6c703febb575443.jpg",
		                  "score": 0.05293918669896472,
		                  "showbox": {
		                    "y": 16,
		                    "x": 43,
		                    "w": 343,
		                    "h": 648
		                  },
		                  "showimages": [
		                    [
		                      "/data/disk3/img/img005/955/d6c703febb575443.jpg",
		                      [
		                        0.0,
		                        89.0,
		                        428.0,
		                        503.0
		                      ],
		                      18.889598846435547
		                    ]
		                  ],
		                  "id": "9910694794997682587"
		                }
		              ],
		              "classify": [
		                [
		                  {
		                    "score": 0.9624,
		                    "name": "176598;一步裙"
		                  }
		                ],
		                [
		                  {
		                    "score": 0.9973,
		                    "name": "159308;A型"
		                  }
		                ],
		                [],
		                [
		                  {
		                    "score": 0.9998,
		                    "name": "159321;短裙"
		                  }
		                ]
		              ]
		            }
		          }
		        ]
		      },
		      "ID": "28101c92-147f-4fd1-be6e-eb097d16e77c",
		      "errmsg": null
		    }
		  ]
		}