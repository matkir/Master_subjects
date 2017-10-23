import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft,ifft
import numpy as np
rate, data = wav.read('baddolly .wav')

fft_out = np.fft.fft2(data)

#fft_out[9000:10000]=0
#fft_out[-10000:9000]=0
for a,i in enumerate(fft_out):
    for j in i:
        if abs(j) > 5E8:
            print(a)
            fft_out[a]=0
        

plt.plot(np.abs(fft_out))
plt.show()
new=np.int16(np.fft.ifft2(fft_out))

wav.write('test.wav', rate, new)
