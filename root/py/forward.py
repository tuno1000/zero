import RPi.GPIO as GPIO
from time import sleep

#ＧＰＩＯのポートを設定
R_VREF=13
R_IN1=19
R_IN2=26

GPIO.setmode(GPIO.BCM)
GPIO.setup([R_VREF,R_IN1,R_IN2],GPIO.OUT)

#モーターを回す
#回転速度を指定
pwm_r = GPIO.PWM(R_VREF,100)
pwm_r.start(100)
    
#時計回りにモーターを回す
GPIO.output(R_IN1,GPIO.HIGH)
GPIO.output(R_IN2,GPIO.LOW)
sleep(5)
#モーターを停止する
GPIO.output(R_IN1,GPIO.LOW)
GPIO.output(R_IN2,GPIO.LOW)
sleep(1) 

GPIO.cleanup()
