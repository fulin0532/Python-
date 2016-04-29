#coding=utf-8
import urllib,urllib2
import re
from bs4 import BeautifulSoup
import time
import sys
reload(sys)  
sys.setdefaultencoding('utf-8')
#获取要下载图片的整个页面的信息
def getHtml(url):
    page=urllib2.urlopen(url)
    html=page.read()
    # print html
    return html
 #筛选数据并打印到本地
def getImg(html):
    soup=BeautifulSoup(html,'html.parser')
    dls=soup.find_all('dl',attrs={'class':'feed_list'})
    for index in range(len(dls)):
        p=dls[index].find_all('p')[0]
        print p.text
    f=open("testname.txt","a")
    for index in range(len(dls)):
        nicheng=dls[index].find_all('p')[0].text
        f.write(nicheng)
        f.write('\r\n')
    f.close()
user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12'
headers={"User-Agent":user_agent}
page=59
length=0
while page<70:
    url='http://www.qzone.cc/wangming/day/list_'+str(page)+'.html'
    print "正在爬取第"+str(page)+"页......."
    # print "这里呢"
    request=urllib2.Request(url,headers=headers)
    html=getHtml(request)
    # soup=BeautifulSoup(open('nextmingzi.html'),"html.parser")
    soup=BeautifulSoup(html,"html.parser")
    li=soup.find_all('li',attrs={'class':'next'})[0]
    a=li.find_all('a')[0]['href']
    print str(a)
    getImg(html)
    if(str(a)=='javascript:;'):
        print "最后一页啦........"
        break
    else:
        page=page+1
        continue
    time.sleep(0.5)
f=open('testname.txt','r')
lines=f.readlines()
print "当前一共"+str(len(lines))+"条昵称"
f.close()
