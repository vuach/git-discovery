import r2r_dac as r2r
import signal_gen as sg
import time
import RPi.GPIO as GPIO
import smbus

amp = 3.2
sif = 10
saf = 1000
leds = [16,20,21,25,26,17,27,22]
dynamic_range=3.14
start = float(time.time())

def triag(per, amp=2048):
    bus = smbus.SMBus(1)
    addr=0x61
    def set_dac(val1):
        val1 = max(0, min(4095, int(val1)))
        bus.write_i2c_block_data(addr, 0x40|((val1>>8)&0x0F), [val1&0xFF])

    haf = per/2
    steps=100
    try:
        while True:
            for i in range(steps):
                val = int((i/steps)*amp)
                set_dac(val)
                time.sleep(haf/steps)
            for i in range(steps):
                val = int(amp*(1-(i/steps)))
                set_dac(val)
                time.sleep(haf/steps)   
    except KeyboardInterrupt:
        set_dac(0)
        bus.close()
        print('Done')


if __name__ == '__main__':
    try:
        triag(5)
    finally:
        dac.deinit()