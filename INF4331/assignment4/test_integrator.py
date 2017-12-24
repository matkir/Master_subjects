import integrator
import numba_integrator
import numpy_integrator
import cython_integrator
import integrate_module
from timeit import default_timer as timer
from math import sin,pi

def test_integral_of_constant_function():
    def f(x):
        return 2
    
    expected_answer=4
    N=int(1E7)
    eps=1E-7
    
    integral1=integrator.integrate(f, 0, 2, N)
    assert abs(integral1-expected_answer)<eps   

    integral2=numpy_integrator.numpy_integrate(f, 0, 2, N)
    assert abs(integral2-expected_answer)<eps  
   
    integral3=numba_integrator.numba_integrate(f, 0, 2, N)
    assert abs(integral3-expected_answer)<eps  
    
    integral4=cython_integrator.cython_integrate(f, 0, 2, N)
    assert abs(integral4-expected_answer)<eps  
     

def test_integral_of_linear_function():
    def f(x):
        return 2*x

    expected_answer=1
    N=int(1E7)
    eps=1E-7
    
    integral1=integrator.integrate(f, 0, 1, N)
    assert abs(integral1-expected_answer)<eps   
    
    integral2=numpy_integrator.numpy_integrate(f, 0, 1, N)
    assert abs(integral2-expected_answer)<eps  
    
    integral3=numba_integrator.numba_integrate(f, 0, 1, N)
    assert abs(integral3-expected_answer)<eps  
   
    integral4=cython_integrator.cython_integrate(f, 0, 1, N)
    assert abs(integral4-expected_answer)<eps  
     
   
def test_midpoint_integral_of_function():  
    def f(x):
        return sin(x)
    
    expected_answer=2
    N=int(1E7)
    eps=1E-10
    
    
    integral1=integrator.midpoint_integrate(f, 0, pi, N)
    assert abs(integral1-expected_answer)<eps   
  
     
    integral2=numpy_integrator.midpoint_numpy_integrate(f, 0, pi, N)
    assert abs(integral2-expected_answer)<eps   
  
    integral3=numba_integrator.midpoint_numba_integrate(f, 0, pi, N)
    assert abs(integral3-expected_answer)<eps   
   
    integral4=cython_integrator.midpoint_cython_integrate(f, 0, pi, N)
    assert abs(integral4-expected_answer)<eps   
 
def test_integrate_module(): 
    a=integrate_module.Integrate()
    def f(x):
        return 2*x

    expected_answer=1
    N=int(1E5)
    eps=1E-2
    
    integral1=a(f, 0, 1, N,method='midpoint',implimentation='regular')
    integral2=a(f, 0, 1, N,method='endpoint',implimentation='regular')  
    integral3=a(f, 0, 1, N,method='midpoint',implimentation='numpy')
    integral4=a(f, 0, 1, N,method='endpoint',implimentation='numpy')
    integral5=a(f, 0, 1, N,method='midpoint',implimentation='numba')
    integral6=a(f, 0, 1, N,method='endpoint',implimentation='numba')
    integral7=a(f, 0, 1, N,method='midpoint',implimentation='cython')
    integral8=a(f, 0, 1, N,method='endpoint',implimentation='cython')
    assert abs(integral1-expected_answer)<eps   
    assert abs(integral2-expected_answer)<eps   
    assert abs(integral3-expected_answer)<eps   
    assert abs(integral4-expected_answer)<eps   
    assert abs(integral5-expected_answer)<eps   
    assert abs(integral6-expected_answer)<eps   
    assert abs(integral7-expected_answer)<eps   
    assert abs(integral8-expected_answer)<eps   
    
   
   
test_integral_of_constant_function()
test_integral_of_linear_function()
test_midpoint_integral_of_function()
test_integrate_module()