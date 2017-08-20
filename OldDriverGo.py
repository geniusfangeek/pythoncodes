import requests as s
from lxml import etree

HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'d_c0="AHBCi8suVQuPTv_qlRMbDr4deEiBre3RSAQ=|1487475081"; _zap=3606d7ed-24a5-478f-8ccc-3e098e8cff1f; q_c1=1859a4e5077d42cb930189326ce85a4c|1501899634000|1487475080000; r_cap_id="YzZlM2JhYTc1NzhiNDIzMDhhMzM4NDk3ZmU0Y2E1OTk=|1501899634|278730e7adbcc86202f83c7c66aa4ec62ca9c75e"; cap_id="NjEwMTExNzZhZmIxNDQ2ZWEyYjg3MTM4MDdlNDg4OTk=|1501899634|f33f370f997b2fe6db0e747ef5b2324d5805de6f"; z_c0=Mi4wQUFDQTJUUWlBQUFBY0VLTHl5NVZDeGNBQUFCaEFsVk5mYmlzV1FBQ0IyWDhsRDcwbjVlUUdSY1JsWEFINnR0X3hn|1501899645|0893454c684fac51973003f4bb8a42b2fead7809; aliyungf_tc=AQAAAH49A06KugUAYfCh0wIsnSU0ppvn; _xsrf=11181d1d-c2cb-4204-9d40-4bbc742aeca6; __utma=51854390.40316710.1501899610.1501928328.1501983212.3; __utmc=51854390; __utmz=51854390.1501928328.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20131212=1^3=entry_date=20131212=1; XSRF-TOKEN=2|34d8ef93|05e9deab05bcdef719bbddf056f5dba104ecc2aa50ecdfbe00ba8df003ecddf251bb8ea5|1501984552',
    'Host':'zhuanlan.zhihu.com',
    'Referer':'https://zhuanlan.zhihu.com/p/25301841',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
url = 'https://www.zhihu.com/question/63139209/answer/206017894'
data = {'type':'up'}
z = s.post(url,data = data, headers = HEADERS)
z.status_code
z.content
