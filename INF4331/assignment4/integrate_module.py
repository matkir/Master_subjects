import integrator
import numba_integrator
import numpy_integrator
import cython_integrator
from timeit import default_timer as timer
import sys
import os
sys.path.append(os.path.abspath('../assignment3'))
from polynomilas import Polynomial as Polynomial

class Integrate:
    def __init__(self):
        pass    
    def __call__(self,f,a,b,N,method='midpoint',implimentation='regular'):
        if type(f)==type([]):
            print("converting list to polynomial...")
            if implimentation=='numba':
                print("warning: numba does not support list format")
                return False
            
            f=Polynomial(f)
            
        
        if implimentation=='regular':
            if method=='midpoint':
                return integrator.midpoint_integrate(f, a, b, N)
            else:
                return integrator.integrate(f, a, b, N)
        
        elif implimentation=='numpy':
            if method=='midpoint':
                return numpy_integrator.midpoint_numpy_integrate(f, a, b, N)
            else:
                return numpy_integrator.numpy_integrate(f, a, b, N)
        
        elif implimentation=='numba':
            if method=='midpoint':
                return numba_integrator.midpoint_numba_integrate(f, a, b, N)
            else:
                return numba_integrator.numba_integrate(f, a, b, N)
        
        elif implimentation=='cython':
            if method=='midpoint':
                return cython_integrator.midpoint_cython_integrate(f, a, b, N)
            else:
                return cython_integrator.cython_integrate(f, a, b, N)
        else:
            print("error, no correct module")


if __name__=='__main__':
    a=Integrate()
    print(a(lambda x:x**2,0,1,10000,implimentation="numba"))
        