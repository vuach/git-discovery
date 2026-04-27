import mcp3021
import adc_plot
import time
adc = mcp3021.MCP3021(3.143)
volts = []
times = []
duration = 10.0

try:
    start = time.time()
    while time.time() - start < duration:
        volts.append(adc.get_voltage())
        times.append(time.time() - start)
    adc_plot.plot_volt_vs_time(times, volts, 3.2)
    adc_plot.plot_sampling_period_hist(times)
finally:
    adc.deinit()