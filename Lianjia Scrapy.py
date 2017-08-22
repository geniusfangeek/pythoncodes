# coding:utf-8

import requests
from lxml import etree
import time
import pymongo
import numpy as np
import pandas as pd

HEADER = {
    'Cookie':'iknew_callEsay=true; lianjia_uuid=180c13bd-b575-4fc5-bebe-62b97c0b06d2; gr_user_id=1a776d5f-0952-4820-b9f6-0879cd4f6c41; pt_393d1d99=uid=rq1pcnqvZpHb4t/CbiLJWA&nid=1&vid=2NBc02oIeeobc2wwH2tbHQ&vn=1&pvn=1&sact=1489836595102&to_flag=0&pl=BQXIhBjD9KsEcyeg1MbfJQ*pt*1489836595102; _ga=GA1.3.494647510.1487482488; UM_distinctid=15c734b2c0c1df-03b5fdd0878efa-5393662-1fa400-15c734b2c0d25c; aliyungf_tc=AQAAABVrHRumxwoA4fCh0wPk8qACpLw0; lianjia_token=2.0059fbb75420fc7be748569e653166ab51; select_city=310000; cityCode=sh; _gat=1; _gat_u=1; _ga=GA1.2.494647510.1487482488; gr_session_id_970bc0baee7301fa=6dc7c92c-14c2-49e3-80fd-7fef591fbecf; gr_cs1_6dc7c92c-14c2-49e3-80fd-7fef591fbecf=userid%3A2000000008692063; ubt_load_interval_b=1502005501991; ubt_load_interval_c=1502005501991; lianjia_ssid=8345762b-6317-549b-86ed-4b9ed1885aa9; lianjia_userId=2000000008692063; ubta=2299869246.1147910229.1487482488636.1502005500886.1502005502235.648; ubtb=2299869246.1147910229.1502005502238.1F566CBC0B4B6D352CD451038C0D55FE; ubtc=2299869246.1147910229.1502005502238.1F566CBC0B4B6D352CD451038C0D55FE; ubtd=9',
    'Host':'sh.lianjia.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

lj_origin = "http://sh.lianjia.com/ershoufang/d"


for i in range(1,3):
    lj_url = lj_origin+str(i)
    z0 = requests.get(lj_url).content
    html = etree.HTML(z0)

houseid = []

house_ref = html.xpath('//ul/li/div/div/a/@href')
# 此处插入房屋ID，即shxxxxx
house_id = []

for x in house_ref:
    house_detail_url = 'http://sh.lianjia.com' + x
    z1 = requests.get(house_detail_url).content
    html2 = etree.HTML(z1)
    house_resident = html2.xpath('//ul[@class = "maininfo-minor maininfo-item"]/li/span/span/a[1]/text()')
    house_id.append(house_resident)
    house_address = html2.xpath('//ul[@class = "maininfo-minor maininfo-item"]/li[5]/span[2]/text()')
    house_totalprice = html2.xpath('//div[2]/aside/div[1]/div[1]/span[1]/text()')
    house_unitprice = html2.xpath('//div[2]/aside/div[1]/div[2]/p/span/text()')
    house_structure = html2.xpath('//div[1]/div[@class = "module-col baseinfo-col2"]/ul[@class = "baseinfo-tb"]/li[1]/span[@class = "item-cell"]/text()')
    house_height = html2.xpath('//div[1]/div[@class = "module-col baseinfo-col3"]/ul[@class = "baseinfo-tb"]/li[1]/span[@class = "item-cell"]/text()')
    house_space = html2.xpath('//div[1]/div[@class = "module-col baseinfo-col2"]/ul[@class = "baseinfo-tb"]/li[3]/span[@class = "item-cell"]/text()')
    house_orientation = html2.xpath('//div[1]/div[@class = "module-col baseinfo-col3"]/ul[@class = "baseinfo-tb"]/li[3]/span[@class = "item-cell"]/text()')
    house_certificate_period = html2.xpath('//div[2]/div[@class = "module-col baseinfo-col2"]/ul[@class = "baseinfo-tb"]/li[2]/span[@class = "item-cell"]/text()')
    house_type = html2.xpath('//div[2]/div[@class = "module-col baseinfo-col3"]/ul[@class = "baseinfo-tb"]/li[2]/span[@class = "item-cell"]/text()')


df = pd.DataFrame(house_id)
print df






