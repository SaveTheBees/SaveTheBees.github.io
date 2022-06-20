from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np

# parse the .wav file into frequency and time arrays
samplerate, data = read('./data/CantinaBand3.wav')
duration = len(data)/samplerate
time = np.arange(0, duration, 1.0/samplerate)

# create the plot
plt.plot(time, data)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('CantinaBand3.wav')
plt.show()
