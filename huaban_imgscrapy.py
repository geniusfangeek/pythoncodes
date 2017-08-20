import requests
from parsel import Selector

url = "http://huaban.com/favorite/beauty/"
params = {
    'j6095gb1':'',
    'since':'24431205',
    'limit':'100',
    'wfl':'1'
}

HEADER = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'Accept':'application/json',
    'X-Request':'JSON',
    'X-Requested-With':'XMLHttpRequest'
}

z1 = requests.get(url,params=params,headers=HEADER)
# print z1.status_code
# print z1.json()

for i in z1.json()['pins']:
    print i['pin_id']

# sel = Selector(text=z1.text)
# # print sel.xpath('//a[@class="img x layer-view loaded"]/@href')
# print sel.xpath('//*[@id="waterfall"]/div[3]/a')