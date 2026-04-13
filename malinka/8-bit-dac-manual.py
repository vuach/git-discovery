import RPi.GPIO as GPIO
import time

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

try:
    while True:
        try:
            voltage = float(input('Введите напряжение: '))
            number = voltage_to_number(voltage)
            n = dec2bin(number)
            GPIO.output(leds, n)
            print(n)
        except ValueError:
            print('Вы ввели не число...зачем...')
            GPIO.output(leds, 0)
finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()