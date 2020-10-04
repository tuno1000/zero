import RPi.GPIO as GPIO
from time import sleep

#ＧＰＩＯのポートを設定
R1_VREF=18
R1_IN1=15
R1_IN2=14
R2_VREF=13
R2_IN1=19
R2_IN2=26

GPIO.setmode(GPIO.BCM)
GPIO.setup([R1_VREF,R1_IN1,R1_IN2,R2_VREF,R2_IN1,R2_IN2],GPIO.OUT)

#モーターを回す
#回転速度を指定
pwm_r1 = GPIO.PWM(R1_VREF,100)
pwm_r1.start(100)
pwm_r2 = GPIO.PWM(R2_VREF,100)
pwm_r2.start(100)
    
#時計回りにモーターを回す
GPIO.output(R1_IN1,GPIO.LOW)
GPIO.output(R1_IN2,GPIO.HIGH)
GPIO.output(R2_IN1,GPIO.LOW)
GPIO.output(R2_IN2,GPIO.HIGH)
sleep(5)
#モーターを停止する
GPIO.output(R1_IN1,GPIO.LOW)
GPIO.output(R1_IN2,GPIO.LOW)
GPIO.output(R2_IN1,GPIO.LOW)
GPIO.output(R2_IN2,GPIO.LOW)
sleep(1) 

GPIO.cleanup()
