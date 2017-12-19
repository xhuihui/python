#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 赶集数据爬取 '

__author__ = 'liqinghui'

import json
import requests
import sys
import logging
import os
from bs4 import BeautifulSoup

def mkdir(path):
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print(path+' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False

#webhtml=requests.get("http://bj.ganji.com/ershouche/2885481042x.htm")
#mkdir('./html/')
#with open('./html/2885481042x.htm', 'w',encoding="utf-8") as f:
#    f.write(webhtml.text)

with open('./html/2885481042x.htm', 'r',encoding="utf-8") as f:
	htmlStr=f.read()
	#print(htmlStr)
	soup = BeautifulSoup(htmlStr)

phoneDiv=soup.find_all("div", class_="detail_tel_400_text")
puid=phoneDiv[0]['puid']
param = {'puid': '32336665855928'}
print(phoneDiv)
print(phoneDiv[0]['puid'])
header={'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh;q=0.9','Connection':'keep-alive','Content-Length':'19','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':'ganji_xuuid=6059982f-6902-4146-dfbe-7a1591d0e0e6.1513651515575; ganji_uuid=6226523045315378890002; cityDomain=bj; gj_footprint=%5B%5B%22%5Cu9500%5Cu552e%22%2C%22%5C%2Fzpshichangyingxiao%5C%2F%22%5D%5D; WantedListPageScreenType=1920; ErshoucheDetailPageScreenType=1920; mobversionbeta=3g; __utmganji_v20110909=0xb8619d03d85b16e25a63da9c25141c9; gr_user_id=babd8757-d45c-498f-ba67-76a1b23901a8; xxzl_deviceid=ISiZKVXWWQcerZXMyX%2FTGMrpPamFfl%2B6eh6SYqprMtTcjprksHSuFjXTFwwcjs%2B5; vehicle_list_view_type=1; Hm_lvt_8dba7bd668299d5dabbd8190f14e4d34=1513651531; Hm_lpvt_8dba7bd668299d5dabbd8190f14e4d34=1513664255; lg=1; _gl_tracker=%7B%22ca_source%22%3A%22www.google.nl%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22other_www.google.nl%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A38715659972%7D; ershouche_post_browse_history=32336665855928%2C2885481042; ershoucheDetailHistory=32336665855928-1224-105676; GANJISESSID=3151430ad451d7df64ed9e48df979412; Hm_lvt_d486038d25d7a009c28de3dca11595e2=1513651609,1513667306; Hm_lpvt_d486038d25d7a009c28de3dca11595e2=1513667306; gr_session_id_b500fd00659c602c=8d6eb078-c3c6-4ce4-a67d-b123dfcfb9bd','Host':'3g.ganji.com','Origin':'https://3g.ganji.com','Referer':'https://3g.ganji.com/bj_ershouche/32336665855928x?ca_name=zhuzhan2wap_post_detail_ershouche&wapadprurl2=adurl','User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36','X-Requested-With':'XMLHttpRequest'}
webhtml1=requests.get("http://bj.ganji.com/ajax.php?dir=vehicle&module=get_phone400",data=param,headers=header)
print("---"+webhtml1.text)

