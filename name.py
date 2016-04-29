#coding=utf-8
import urllib2
import re
from bs4 import BeautifulSoup
import sys
reload(sys)  
sys.setdefaultencoding('utf-8') 
def getHtml(url):
 	page=urllib2.urlopen(url)
 	html=page.read()
 	return html
def getAllUrl(url):
	html=getHtml(url)
	soup=BeautifulSoup(html,'html.parser')
	ul=soup.find_all('ul',attrs={'class':'e3'})[0]
	a=ul.find_all('a')
	# for i in a:
	# 	urls=i['href']
	# 	print urls
	# print "一共有"+str(len(a))
	return a
url='http://www.yw11.com/namelist.php'
user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/8.0.7 Safari/600.7.12'
headers={"User-Agent":user_agent}
urls=getAllUrl(url)
f=open('name.txt','a')
for index in range(len(urls)):
	lianjie=urls[index]['href']
	mingzi=urls[index].text
	print "正在抓取姓"+mingzi +"的名字......"
	request=urllib2.Request(lianjie,headers=headers)
	html=getHtml(request)
	soup=BeautifulSoup(html,'html.parser')
	divs=soup.find_all('div',attrs={"class":"listbox1_text"})[0]
	ul=divs.find_all('ul')[0]
	lis=ul.find_all('li')
	for index in range(len(lis)):
		name=lis[index].text.lstrip()#左对齐
		f.write(name)
		f.write('\r\n')
	print "抓取了"+（str(index)+1）+"个"+mingzi+"名字"
f.close()
f=open('name.txt','r')
lines=f.readlines()
print "当前一共有"+str(len(lines))
f.close()