import requests
from bs4 import BeautifulSoup

url = "http://www.biquge.cm/paihangbang/allvote.html"
header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie":"__cfduid=dde15d9931ebc00af12e2f79cc87a663b1551713464; UM_distinctid=1694954c8ee19d-04a1c9a712605f-36607102-fa000-1694954c8ef23c; CNZZDATA1271465101=1834752202-1551709448-null%7C1551709448",
"Host": "www.biquge.cm",
"Referer": "http://www.biquge.cm/paihangbang/",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
htmlText = requests.get(url, headers = header);
htmlText.encoding = "gbk";
bs = BeautifulSoup(htmlText.text,"lxml").find("div",class_="box b4").find_all('a');
for a in bs:
    a_url = a['href']
    a_title = a.string

#a_title = a.find('a').get("title")
    print(a_url)
    print(a_title)