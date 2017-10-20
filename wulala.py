# -*- coding: utf-8 -*-
from aip import AipSpeech

import requests
import re
from bs4 import BeautifulSoup
import time
'''
爬取天气网-无锡
http://www.weather.com.cn/weather/101190201.shtml
'''
def getHtmlText(url,code='utf-8'):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = code
		return r.text
	except:
		return ''
def makeSoup(html):
	wstr = ''
	try:
		soup = BeautifulSoup(html,'html.parser')
		soup1 = soup.find_all('li',attrs = {'class':'on'})[1]
		str1 = re.findall(r'>(.*)</',str(soup1))
		b = ''
		try:
			slist = re.findall(r'^(.*)</span>(.*)<i>(.*)$',str1[4])
			for x in range(len(slist[0])):
				b += slist[0][x]
		except:
			b = str1[4]
		if '/' in b:
			b = b.replace('/','-')
		str1[4] = '无锡的温度是'+b
		#print(str1[4])
		str1[6] = '小风风是'+str1[6]
		for i in str1:
			if i != '':
				wstr = wstr +i
		if '雨' in wstr:
			wstr += '今天别忘记带雨伞哦！'
		#加入一些比叫人性化的词语
		#print(wstr)
		return wstr
	except:
		return '哎呀~今天我也不知道无锡天气了'
'''
用百度的AIP
把文字变成mp3文件
'''
def stringToMp3(strings_txt):
	strings_txt = '起床呀~辣鸡~起床啊~辣鸡~起床啦~辣鸡~今天是' + strings_txt
	APPID = '9938968'
	APIKey = 'QCV3ZhkXUK70ofAe1nPjbgbb'
	SecretKey = 'e80a19172d6206f84714925c9bca2b56'

	aipSpeech = AipSpeech(APPID,APIKey,SecretKey)
	result = aipSpeech.synthesis(strings_txt,'zh','1',\
								{'vol':8,
								'per':4,
								'spd':5})
	if not isinstance(result,dict):
		with open('test_tmp.mp3','wb') as f:
			f.write(result)

'''
执行的主函数
'''
def main():
	url = 'http://www.weather.com.cn/weather/101190201.shtml'
	html=getHtmlText(url)
	stringToMp3(makeSoup(html))

if __name__ == '__main__':
	main()
