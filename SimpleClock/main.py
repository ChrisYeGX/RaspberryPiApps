# -*- coding: utf-8 -*-
import os
import requests
from aip import AipSpeech

class Clock():
	def __init__(self):
		self.city = "北京"
		self.BASEDIR = os.path.dirname(os.path.abspath(__file__))
        self.clockPath = os.path.join(self.BASEDIR, 'Clock.mp3')

	def getWeatherInfo(city):
		api = "http://api.avatardata.cn/Weather/Query?key=[您申请的APPKEY]&cityname={0}".format(city)
		response = requests.get(api)
		info = response.json()
		date = info["result"]["realtime"]["date"] + "星期" +info["result"]["realtime"]["week"]
		temperature = info["result"]["realtime"]["weather"]["temperature"]
		t_info = info["result"]["realtime"]["weather"]["info"]
		wind = info["result"]["realtime"]["wind"]["direct"]+info["result"]["realtime"]["wind"]["power"]
		remind = "紫外线"+info["result"]["life"]["info"]["ziwaixian"][0]+info["result"]["life"]["info"]["ziwaixian"][1]
		if "雨" in t_info:
			remind += "{}，出门需要带雨伞。".format(t_info)
		resutl = "{date}，今天{areas}的温度是{temperature}度，{wind}，{remind}".format(date=date, areas=city, temperature=temperature, wind=wind, remind=remind)
		return resutl

	def stringToMp3(strings_txt):
		'''
		用百度的AIP
		把文字变成mp3文件
		'''
		strings_txt = '起床呀~要迟到啦!起床啦~要上课啦！今天是' + strings_txt
		APPID = '[百度语音APPID]'
		APIKey = '[百度语音APIKey]'
		SecretKey = '[百度语音SecretKey]'

		aipSpeech = AipSpeech(APPID,APIKey,SecretKey)
		result = aipSpeech.synthesis(strings_txt,'zh','1',\
									{'vol':8,
									'per':4,
									'spd':5})
		if not isinstance(result,dict):
			with open(self.clockPath,'wb') as f:
				f.write(result)

	def run():
		tmp = getWeatherInfo(self.city)
		stringToMp3(tmp)
		os.system('mplayer {0}'.format(self.clockPath))

if __name__ == '__main__':
	test = Clock()
	test.run()
