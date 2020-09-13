import time
import sys
import RPi.GPIO as GPIO

try:
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
 
	args = sys.argv

	#GPIO4を出力端子設定 
	GPIO.setup(4, GPIO.OUT)
 
	#GPIO4をPWM設定、周波数は50Hz 
	p = GPIO.PWM(4, 50)
 
	#Duty Cycle 0% 
	p.start(0.0)
 
	p.ChangeDutyCycle(float(args[1]))

	time.sleep(0.4)

	GPIO.cleanup()

	exit(0)
except Exception as e:
	print(e)
