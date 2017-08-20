from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html,'lxml')
names = bsObj.find_all('span',{'class':'green'})

for name in names:
    print name.get_text()   # 将find出来的信息进行处理，提取文本内容