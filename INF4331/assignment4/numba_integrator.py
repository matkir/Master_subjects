from numba import jit,autojit
import matplotlib.pyplot as plt


def numba_integrate(f,a,b,N):    
    f=jit(f)
    @jit(nopython=True)
    def wrapper(a, b, N):
        dx=(b-a)/(N)
        retsum=0
        for i in range(int(N)):
            retsum += f(a+i*dx)
            #if i%10000000==0:
            #    print(i,retsum*dx)
        return retsum*dx
    return wrapper(a, b, N)

def midpoint_numba_integrate(f,a,b,N):    
    f=jit(f)
    @jit(nopython=True)
    def wrapper(a, b, N):
        dx=(b-a)/(N)
        retsum=0
        half=dx/2
        for i in range(int(N)):
            retsum += f(half+a+i*dx)
            #if i%10000000==0:
            #    print(i,retsum*dx)
        return retsum*dx
    return wrapper(a, b, N)

    

