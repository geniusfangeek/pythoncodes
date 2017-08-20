from urllib import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
       return None
    try:
        bsObj = BeautifulSoup(html.read(),'lxml')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://sh.lianjia.com/ershoufang/sh4731504.html') # 此处网页可以随意替代
if title == None:
    print('Title could not found')
else:
    print(title)