from matplotlib import pyplot as plt

def plot_volt_vs_time(time, volt, max_volt):
    plt.figure(figsize=(10,6))
    plt.plot(time, volt)
    plt.grid()
    plt.ylim(0, max_volt)
    plt.show()
def plot_sampling_period_hist(time):
    samp_per = []
    for i in range(1, len(time)):
        samp_per.append(time[i]-time[i-1])
    plt.figure(figsize=(10,6))
    plt.hist(samp_per)
    plt.show()