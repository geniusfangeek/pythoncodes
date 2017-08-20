import requests
from lxml import etree
import time
import pandas as pd
import string

HEADER = {
    'Cookie':'iknew_callEsay=true; lianjia_uuid=180c13bd-b575-4fc5-bebe-62b97c0b06d2; gr_user_id=1a776d5f-0952-4820-b9f6-0879cd4f6c41; pt_393d1d99=uid=rq1pcnqvZpHb4t/CbiLJWA&nid=1&vid=2NBc02oIeeobc2wwH2tbHQ&vn=1&pvn=1&sact=1489836595102&to_flag=0&pl=BQXIhBjD9KsEcyeg1MbfJQ*pt*1489836595102; _ga=GA1.3.494647510.1487482488; UM_distinctid=15c734b2c0c1df-03b5fdd0878efa-5393662-1fa400-15c734b2c0d25c; aliyungf_tc=AQAAABVrHRumxwoA4fCh0wPk8qACpLw0; lianjia_token=2.0059fbb75420fc7be748569e653166ab51; select_city=310000; cityCode=sh; _gat=1; _gat_u=1; _ga=GA1.2.494647510.1487482488; gr_session_id_970bc0baee7301fa=6dc7c92c-14c2-49e3-80fd-7fef591fbecf; gr_cs1_6dc7c92c-14c2-49e3-80fd-7fef591fbecf=userid%3A2000000008692063; ubt_load_interval_b=1502005501991; ubt_load_interval_c=1502005501991; lianjia_ssid=8345762b-6317-549b-86ed-4b9ed1885aa9; lianjia_userId=2000000008692063; ubta=2299869246.1147910229.1487482488636.1502005500886.1502005502235.648; ubtb=2299869246.1147910229.1502005502238.1F566CBC0B4B6D352CD451038C0D55FE; ubtc=2299869246.1147910229.1502005502238.1F566CBC0B4B6D352CD451038C0D55FE; ubtd=9',
    'Host':'sh.lianjia.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

lj_url = "http://sh.lianjia.com/ershoufang/"

for n in range(1,3):
    if n ==1:
        url = lj_url
        z1 = requests.get(url,headers=HEADER).content
    if n > 1:
        url = lj_url + 'd' + str(n)
        z2 = requests.get(url,headers=HEADER).content
        z1 = z1 + z2

    #time.sleep(0.1)


lj_resource =  etree.HTML(z1)


id = lj_resource.xpath('//ul[@class = "js_fang_list"]/li/a/@href')
raw_house_details  = lj_resource.xpath('//div/div/span[@class ="info-col row1-text"]/text()')
house_details = []
community = lj_resource.xpath('//div/span/a[@class = "laisuzhou" ]/span/text()')
unit_price = lj_resource.xpath('//div/span[@class = "info-col price-item minor"]/text()')
total_price = lj_resource.xpath('//div/div[@class = "info-col price-item main"]/span[@class = "total-price strong-num"]/text()')

for i in raw_house_details:
    hd = i.string().replace('n','')
    house_details.append(hd)

print house_details
# house_list = pd.DataFrame({'house_href':id,'community':community,'unit_price':unit_price,'total_price':total_price})
# house_list.to_csv('d:\house_list.csv',encoding='GBK')