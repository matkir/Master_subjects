import integrator
import numba_integrator
import numpy_integrator
import cython_integrator
from timeit import default_timer as timer
from math import sin,pi

def print_midpoint_integral_of_function():  
    print("############",file=fil6)
    print("#midpoint f#",file=fil6)
    print("############",file=fil6)
    print(file=fil6)
    def f(x):
        return sin(x)
    
    expected_answer=2
    print("f(x)=sin(x)",file=fil6)
    N=int(5E5)
    print("iterations={}".format(N),file=fil6)
    eps=1E-10
    print("eps={}".format(eps),file=fil6)
    print(file=fil6)
    
    
    start = timer()
    integral1=integrator.midpoint_integrate(f, 0, pi, N)
    end = timer()
    print("midpoint regular integral:",file=fil6)
    print(end-start," seconds",file=fil6)
    print(file=fil6)
  
     
    start = timer()
    integral2=numpy_integrator.midpoint_numpy_integrate(f, 0, pi, N)
    end = timer()
    print("midpoint numpy integral:",file=fil6)
    print(end-start," seconds",file=fil6)
    print(file=fil6)
  
    start = timer()
    integral3=numba_integrator.midpoint_numba_integrate(f, 0, pi, N)
    end = timer()
    print("midpoint numba integral:",file=fil6)
    print(end-start," seconds",file=fil6)
    print(file=fil6)
    
  
   
    start = timer()
    integral4=cython_integrator.midpoint_cython_integrate(f, 0, pi, N)
    end = timer()
    print("midpoint cython integral:",file=fil6)
    print(end-start," seconds",file=fil6)
    print(file=fil6)
  
   
fil6=open('reports/report6.txt','w')
print_midpoint_integral_of_function()
fil6.close()