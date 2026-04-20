import r2r_dac as r2r
import signal_gen as sg
import time


amp = 3.2
sif = 10
saf = 1000
leds = [16,12,25,17,27,23,22,24]
dynamic_range=3.3
t=0

try:
    dac = R2R.DAC