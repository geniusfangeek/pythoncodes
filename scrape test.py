from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page111.html')

# bsObj = BeautifulSoup(html.read(),'lxml')
# print(bsObj.h1)
# print(bsObj.html.body.h1)
# print(bsObj.body.h1)
# print(bsObj.html.h1)