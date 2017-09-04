import matplotlib.pyplot as plt
from numpy import *

n=linspace(-20,20,1000)
omega0=pi
theta0=pi/5
a=cos(omega0*n+theta0)
plt.plot(n,a)
plt.show()
