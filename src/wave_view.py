from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt
import math

filename = '../Audios/audio1'

# Read audiofile
sample_rate, data = read(filename+'.wav')
print("Audio Frame Rate: ", sample_rate)

duration = len(data)/sample_rate
print("Duration of Audio in Seconds: ", duration)

# Plotting graph
time = np.arange(0, duration, 1/sample_rate)

chunk_size = 44100
num_chunk = len(data) // chunk_size
sn = []
for i in range(num_chunk):
    sn.append(np.mean(data[i*chunk_size:(i+1)*chunk_size]**2))
    print(sn[i])

logsn = 10*np.log10(sn)

print(logsn)


plt.plot(time,data)
plt.xlabel('Time[s]')
plt.ylabel('Amplitude')
plt.title(filename)
plt.show()