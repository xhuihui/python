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
def getPhone(url):
	webhtml=requests.get(url)
		soup = BeautifulSoup(webhtml.text)
		phoneDiv=soup.find_all("span", class_="phoneNum-style")
		print(phoneDiv[0].text)

#二手物品列表
def getErshouList(url):
	http://bj.ganji.com/jiaju/o15/
	webhtml=requests.get(url)
		soup = BeautifulSoup(webhtml.text)
		phoneDiv=soup.find_all("span", class_="phoneNum-style")
		print(phoneDiv[0].text)



