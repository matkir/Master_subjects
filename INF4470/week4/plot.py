from numpy import *
import matplotlib.pyplot as plt

j=complex(0,1)
def f(w):
    return (0.5*exp(-1j*pi/8)*(3/4)/(5/4-cos(w-pi/8))+0.5*exp(1j*pi/8)*(3/4)/(5/4-cos(w+pi/8)))

def g(w):
    return (-2*1j*sin(w)-4j*sin(2*w)-6j*sin(3*w))

def h(w):
    return (4*exp(4j*w)+7/2*exp(3j*w)+3*exp(2j*w)+5/2*exp(j*w)+2+3/2*exp(-1j*w)+exp(-2j*w)+1/2*exp(-3j*w))

def f_f(w):
    return angle(f(w))

def g_f(w):
    return angle(g(w))

def h_f(w):
    return angle(h(w))


rng=linspace(- pi,pi,200)


plt.subplot(211)
plt.plot(rng,absolute(f(rng)))
plt.subplot(212)
plt.plot(rng,f_f(rng))
plt.savefig('f.png')
plt.show()
plt.clf


plt.subplot(211)
plt.plot(rng,absolute(g(rng)))
plt.subplot(212)
plt.plot(rng,g_f(rng))
plt.savefig('g.png')
plt.show()
plt.clf


plt.subplot(211)
plt.plot(rng,absolute(h(rng)))
plt.subplot(212)
plt.plot(rng,h_f(rng))
plt.savefig('h.png')
plt.show()
plt.clf
