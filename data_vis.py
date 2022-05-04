from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np

# parse the .wav file into frequency and time arrays
samplerate, data = read('./data/output.wav')
duration = len(data)/samplerate
time = np.arange(0,duration,1/samplerate)

# create the plot
plt.plot(time,data)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('output.wav')
plt.show()