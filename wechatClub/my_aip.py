# -*- coding: utf-8 -*-

import os
import requests
from aip import AipSpeech

class StringToMp3:
	'''
	用百度的AIP
	把文字变成mp3文件
	'''
	def __init__(self, strings_txt, out_path):		
		self.APPID = '你百度ai的APPID'
		self.APIKey = '你百度ai的APIKey'
		self.SecretKey = '你百度ai的SecretKey'
		self.strings_txt = strings_txt
		self.out_path = out_path

	def run(self):
		client = AipSpeech(self.APPID, self.APIKey, self.SecretKey)
		result = client.synthesis(self.strings_txt,'zh','1',\
									{'vol':8,\
									'per':4,\
									'spd':7})
		if not isinstance(result,dict):
			with open(self.out_path, 'wb') as f:
				f.write(result)
	
	def playMp3(self):
		self.run()
		os.system('mplayer {0} &'.format(self.out_path))


if __name__ == '__main__':
	StringToMp3("测试测试testingtesting", "./weather_info.mp3").playMp3()