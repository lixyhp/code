# -*- coding:utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup

url = r'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read()
page_info = page_info.decode('gbk')

soup = BeautifulSoup(page_info, 'html.parser')  

titles = soup.find_all('a', 'title')
for title in titles:
	print(title)
