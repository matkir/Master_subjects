
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

img = cv2.imread('houses.png',cv2.IMREAD_GRAYSCALE)
img2=img
test=np.fft.fft2(img)
plt.imshow(np.log10(np.abs(test)))
plt.show()

for i in enumerate(test):
        for j in enumerate(i[1]):
                if i[0]>540/2-150 and i[0]<540/2+150 and j[0]>720/2-150 and j[0]<720/2+150:
                        test[i[0]][j[0]]=0
                if (i[0]>540-50 or i[0]<50) and (j[0]>720-50 or j[0]<50):
                        test[i[0]][j[0]]=0

plt.imshow(np.log10(np.abs(test)))
plt.show()

 
test=np.fft.ifft2(test)
plt.subplot(121)
plt.imshow(np.abs(test),cmap='gray')
plt.subplot(122)
plt.imshow(np.abs(img2),cmap='gray')
plt.show()
