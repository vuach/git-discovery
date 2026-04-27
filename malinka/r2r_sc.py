import time
import r2r_adc
import adc_plot

adc = r2r_adc.R2R_ADC(3.143, 0.0007)
volt_val = []
time_val = []
dur = 3.0
try:
    start = time.time()
    while time.time()-start<dur:
        volt_val.append(adc.seq_count())
        time_val.append(time.time()-start)
    adc_plot.plot_volt_vs_time(time_val, volt_val, 3.2)
    adc_plot.plot_sampling_period_hist(time_val)
finally:
    adc.deinit()