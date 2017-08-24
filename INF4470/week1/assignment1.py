import jupyter 
from numpy import *
import matplotlib.pyplot as plt

t=linspace(-1,2.5,1000)

plt.subplot(2,2,1)
func=cos(2*pi*t)
plt.plot(t,func)

plt.subplot(2,2,2)
func=cos(2*pi*t+pi)
plt.plot(t,func)

plt.subplot(2,2,3)
func=cos(8*pi*t)
plt.plot(t,func)

plt.subplot(2,2,4)
func=cos(4*pi*t- pi/3)
plt.plot(t,func)


plt.show()

print('hello world')
