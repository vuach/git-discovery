import numpy
import time

def get_sin_wave_amplitude(freq, time):
    sin_val = math.sin(2*math.pi*freq*time)
    return int(sin_val+1)/2

def wait(f):
    time.sleep(1/f)


