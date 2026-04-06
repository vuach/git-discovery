import RPi.GPIO as GPIO
import time
from random import randint
GPIO.setmode(GPIO.BCM)
leds = [16,12,25,17,27,23,22,24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

dynamic_range=3.3
def voltage_to_number(voltage):
    if not(0.0<=voltage<=dynamic_range):
        print('Напряжение за рамками диапазона, сброс до 0.0 В')
        return 0
    return int(voltage/dynamic_range*255)

def dec2bin(val):
    return[int(el) for el in bin(val)[2:].zfill(8)]


while True:
    voltage = randint(0,255)
    n = dec2bin(voltage)
    GPIO.output(leds, n)
    print(voltage)
    time.sleep(0.3)