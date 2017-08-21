# coding:utf-8

from lxml import etree
import requests
import time
import pymongo

'''
通过xpath获得链家数据
通过多线程实现快速爬去
通过mongodb存入数据库
'''

def lj_html(url):
    z1 = requests.get(url).content
    html = etree.HTML(z1)
    return html


url = 'http://sh.lianjia.com/ershoufang'
print lj_html(url)