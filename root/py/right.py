import time
import sys
import RPi.GPIO as GPIO
import logging

try:

	logging.basicConfig(filename='/root/py/right.txt', level=logging.DEBUG)
	#logging.basicConfig(filename='/root/py/right.txt', level=logging.INFO)

	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
 
	args = sys.argv

	GPIO.setup(4, GPIO.OUT)
 
	p = GPIO.PWM(4, 50)
 
	for i in range(10):
		n = (float(args[1]) + 1) - ((i + 1) * 0.1)
		p.start(0.0)
		p.ChangeDutyCycle(n)
		logging.debug(n)
		time.sleep(0.1)
	GPIO.cleanup()

	exit(0)
except Exception as e:
	print(e)
