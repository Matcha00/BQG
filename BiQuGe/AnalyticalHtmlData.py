import requests
from bs4 import BeautifulSoup
from DBHelp import *
db = DBHelp(host="localhost",port=3306,user='root',password='123456',database='BQG',charset='utf8')

url = "http://www.biquge.cm/paihangbang/allvote.html"
header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie":"__cfduid=dc333734c30600ce7da3b412dce7e88101551851831; UM_distinctid=1695193cf353e3-00fb4c3e875422-36607102-1fa400-1695193cf36723; CNZZDATA1271465101=402203686-1551851591-%7C1551851591",
"Host": "www.biquge.cm",
"Referer": "http://www.biquge.cm/paihangbang/",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
htmlText = requests.get(url, headers = header);
htmlText.encoding = "gbk";
print(htmlText.text)
bs = BeautifulSoup(htmlText.text,"lxml").find("div",id="main").find_all('li')
for aa in bs:
    print(aa.find('a'))
    if aa.find('a') != None:
        a_url = aa.find('a')['href']
        a_title = aa.find('a').string
        print(a_url)
        print(a_title)


        sql = "INSERT INTO pystroy (storyurl,storyname,status) VALUES (%s,%s,%s)"
        data = (a_url, a_title, 1)
        db.cud(sql, data)