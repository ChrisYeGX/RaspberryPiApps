#! /usr/bin/python3
# coding:utf-8

import RPi.GPIO as GPIO
import time

#init GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
def ledone():
	try:
		GPIO.output(11, 1)
		time.sleep(0.5)
		GPIO.output(11, 0)
		time.sleep(0.5)
	except:
		print('...')
def main():
	for tmp_a in range(60):
	#大概60s
		ledone()
	GPIO.cleanup()
if __name__ == '__main__':
	main()
