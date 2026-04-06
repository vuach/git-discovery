import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
#button = 13
#GPIO.setup(6, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.1)
    duty+=1.0
    if duty>100:
        duty=0.0