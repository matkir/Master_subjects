import integrator
import numba_integrator
import numpy_integrator
import cython_integrator
from timeit import default_timer as timer
from numba import jit
from math import sin,pi



def calc(f,a,b,N,reprfunc):
    start = timer()
    integral=numba_integrator.midpoint_numba_integrate(f, a, b, N)
    end = timer()
    print(file=fil1)
    print("numba integral of: {} is:".format(reprfunc),file=fil1)
    print(integral,file=fil1)
    print("in ", end-start, " seconds",file=fil1)
    print(file=fil1)

def contest(a,b,N):


    def f(x):
        return 1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x 

    calc(f, a, b, N,"1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x")
    
    def f(x):
        return 1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x

    calc(f, a, b, N,"1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x")

    def f(x):
        return 1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x * 9*sin(x/9)/x * 11*sin(x/11)/x

    calc(f, a, b, N,"1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x * 9*sin(x/9)/x * 11*sin(x/11)/x")


    def f(x):
        return 1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x * 9*sin(x/9)/x * 11*sin(x/11)/x * 13*sin(x/13)/x

    calc(f, a, b, N,"1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x * 9*sin(x/9)/x * 11*sin(x/11)/x * 13*sin(x/13)/x")
    
    
    def f(x):
        return 1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x * 9*sin(x/9)/x * 11*sin(x/11)/x * 13*sin(x/13)/x * 15*sin(x/15)/x

    calc(f, a, b, N,"1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x * 9*sin(x/9)/x * 11*sin(x/11)/x * 13*sin(x/13)/x * 15*sin(x/15)/x")

    def f(x):
        return 1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x * 9*sin(x/9)/x * 9*sin(x/9)/x

    calc(f, a, b, N,"1/pi * sin(x)/x * 3*sin(x/3)/x * 5*sin(x/5)/x * 7*sin(x/7)/x * 9*sin(x/9)/x * 9*sin(x/9)/x")





a=10e-20
b=10e7
N=int(7E7)
fil1=open('reports/report.txt','w')
print("N=",N,file=fil1)
contest(a,b,N)
fil1.close()


