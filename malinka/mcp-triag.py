import smbus
import time
import math

bus = smbus.SMBus(1)
addr=0x60

def write(val):
    val=int(max(0, min(4095, val)))
    hig = 0x40|((val>>8)&0x0F)
    low=val&0xFF
    bus.write_i2c_block_data(addr, hig, [low])

try:
    while True:
        for value in range(4096):
            write(val)
            time.sleep(0.001)
        for value in range(4094, 1, -1):
            write(val)
            time.sleep(0.001)




