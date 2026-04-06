import RPi.GPIO as GPIO
import time
from random import randint
GPIO.setmode(GPIO.BCM)
leds = [16,20,21,25,26,17,27,22]
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
    GPIO.output(leds, 0)
    time.sleep(0.15)


class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    def set_number(self, number):
        return[int(el) for el in bin(number)[2:].zfill(8)]
    def set_voltage(self, voltage): pass
