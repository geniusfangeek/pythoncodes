# coding:utf-8

from multiprocessing.dummy import Pool as ThreadPool
import requests
from lxml import etree
import time
import pymongo
import numpy as np
import pandas as pd

#此处插入多线程操作

# py2.7独有，ASIC编码STR，需要转化为UTF8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


HEADER = {
    'Cookie':'iknew_callEsay=true; lianjia_uuid=180c13bd-b575-4fc5-bebe-62b97c0b06d2; gr_user_id=1a776d5f-0952-4820-b9f6-0879cd4f6c41; pt_393d1d99=uid=rq1pcnqvZpHb4t/CbiLJWA&nid=1&vid=2NBc02oIeeobc2wwH2tbHQ&vn=1&pvn=1&sact=1489836595102&to_flag=0&pl=BQXIhBjD9KsEcyeg1MbfJQ*pt*1489836595102; _ga=GA1.3.494647510.1487482488; UM_distinctid=15c734b2c0c1df-03b5fdd0878efa-5393662-1fa400-15c734b2c0d25c; aliyungf_tc=AQAAABVrHRumxwoA4fCh0wPk8qACpLw0; lianjia_token=2.0059fbb75420fc7be748569e653166ab51; select_city=310000; cityCode=sh; _gat=1; _gat_u=1; _ga=GA1.2.494647510.1487482488; gr_session_id_970bc0baee7301fa=6dc7c92c-14c2-49e3-80fd-7fef591fbecf; gr_cs1_6dc7c92c-14c2-49e3-80fd-7fef591fbecf=userid%3A2000000008692063; ubt_load_interval_b=1502005501991; ubt_load_interval_c=1502005501991; lianjia_ssid=8345762b-6317-549b-86ed-4b9ed1885aa9; lianjia_userId=2000000008692063; ubta=2299869246.1147910229.1487482488636.1502005500886.1502005502235.648; ubtb=2299869246.1147910229.1502005502238.1F566CBC0B4B6D352CD451038C0D55FE; ubtc=2299869246.1147910229.1502005502238.1F566CBC0B4B6D352CD451038C0D55FE; ubtd=9',
    'Host':'sh.lianjia.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

lj_origin = "http://sh.lianjia.com/ershoufang/d"

def getsource(url):
    z0 = requests.get(url).content
    html0 = etree.HTML(z0)

urls = []

for i in range(1,5):
    lj_url = lj_origin+str(i)
    urls.append(lj_url)

    # z0 = requests.get(lj_url).content
    # html = etree.HTML(z0)

pool = ThreadPool(4)
results = pool.map(getsource, urls)
pool.close()
pool.join()
html = results


houseid = []

house_ref = html.xpath('//ul/li/div/div/a/@href')

id = []
community = []
address = []
totalprice = []
structure = []
room_space = []
certificate = []
height = []

for x in house_ref:
    house_detail_url = 'http://sh.lianjia.com' + x
    z1 = requests.get(house_detail_url).content
    html2 = etree.HTML(z1)
    house_id = 'sh'+ x.lstrip('/ershoufang/').rstrip('.html')
    id.append(house_id)
    house_resident = html2.xpath('//ul[@class = "maininfo-minor maininfo-item"]/li/span/span/a[1]/text()')[0]
    community.append(house_resident)
    house_address = html2.xpath('//ul[@class = "maininfo-minor maininfo-item"]/li[5]/span[2]/text()')[0]
    address.append(house_address)
    house_totalprice = html2.xpath('//div[2]/aside/div[1]/div[1]/span[1]/text()')[0]
    totalprice.append(house_totalprice)
    house_unitprice = html2.xpath('//div[2]/aside/div[1]/div[2]/p/span/text()')[0]
    house_structure = html2.xpath('//div[1]/div[@class = "module-col baseinfo-col2"]/ul[@class = "baseinfo-tb"]/li[1]/span[@class = "item-cell"]/text()')[0]
    structure.append(house_structure)
    house_height = html2.xpath('//div[1]/div[@class = "module-col baseinfo-col3"]/ul[@class = "baseinfo-tb"]/li[1]/span[@class = "item-cell"]/text()')[0]
    height.append(house_height)
    house_space = html2.xpath('//div[1]/div[@class = "module-col baseinfo-col2"]/ul[@class = "baseinfo-tb"]/li[3]/span[@class = "item-cell"]/text()')[0]
    room_space.append(house_space)
    house_orientation = html2.xpath('//div[1]/div[@class = "module-col baseinfo-col3"]/ul[@class = "baseinfo-tb"]/li[3]/span[@class = "item-cell"]/text()')[0]
    house_certificate_period = html2.xpath('//div[2]/div[@class = "module-col baseinfo-col2"]/ul[@class = "baseinfo-tb"]/li[2]/span[@class = "item-cell"]/text()')[0]
    certificate.append(house_certificate_period)
    house_type = html2.xpath('//div[2]/div[@class = "module-col baseinfo-col3"]/ul[@class = "baseinfo-tb"]/li[2]/span[@class = "item-cell"]/text()')[0]


df = pd.DataFrame({'序号': id,
                   '地址': address,
                   '社区': community,
                   '总价': totalprice,
                   '房型': structure,
                   '楼层': height,
                   '面积': room_space,
                   '产证': certificate})


writer = pd.ExcelWriter('Lianjia_Data.xlsx')
df.to_excel(writer,'sheet1')
writer.save()

print 'done'
# connection = pymongo.MongoClient()
# tdb = connection.LianjiaData
# post_info = tdb.test










