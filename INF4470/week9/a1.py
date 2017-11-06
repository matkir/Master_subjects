import numpy as np
import matplotlib.pyplot as plt

class w():
    def __init__(self,T_0,r):
        self.T_0=T_0
        self.r=r
    
    def __call__(self,t):
        if -self.T_0/2<t and t<-self.T_0/2+self.T_0/2*self.r:
            return 1/2 * (1-np.cos((t+self.T_0/2)*2*np.pi/(self.r*self.T_0)))
        elif -self.T_0/2+self.T_0/2*self.r<t and t<self.T_0/2-self.T_0/2*self.r:
            return 1
        elif self.T_0/2-self.T_0/2*self.r<t and t<self.T_0/2:
            return 1/2 * (1-np.cos((t-self.T_0/2)*2*np.pi/(self.r*self.T_0)))
        else:
            return 0
            

pl=[]
t=np.linspace(-1,1,500)
for i in [0,0.25,0.5,0.75,1]:
    tuk=w(2.8, i)
    v=np.vectorize(tuk) 
    pl.append((v(t),i))
"""
for l in pl:
    plt.plot(t,l[0])

plt.legend(["r={}".format(l[1]) for l in pl]) 
plt.show()
"""
##############
#### 7.57 ####
##############


        
def win(t):
    ret=0
    for k in range(1,K+1):
        Fk=f_l+(k-1)*(f_h-f_l)/(K-1)
        ret+=np.cos(2*np.pi*Fk*t)
    return ret
        

f_l=40
f_h=60
K=10
t=np.linspace(-100,100)
a=abs(np.fft.fft(win(t)))

plt.plot(t,a)
plt.show()

:
    