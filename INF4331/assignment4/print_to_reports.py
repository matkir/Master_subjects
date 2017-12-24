import integrator
import numba_integrator
import numpy_integrator
import cython_integrator
from timeit import default_timer as timer
from math import sin,pi


def print_integral_of_constant_function():

    print("############",file=fil3)
    print("############",file=fil4)
    print("############",file=fil5)
    print("#Constant f#",file=fil3)
    print("#Constant f#",file=fil4)
    print("#Constant f#",file=fil5)
    print("############",file=fil3)
    print("############",file=fil4)
    print("############",file=fil5)
    print(file=fil3)
    print(file=fil4)
    print(file=fil5)
    
    def f(x):
        return 2
    
    
    expected_answer=4
    print("f(x)=2",file=fil3)
    print("f(x)=2",file=fil4)
    print("f(x)=2",file=fil5)
    N=int(2E7)
    print("iterations={}".format(N),file=fil3)
    print("iterations={}".format(N),file=fil4)
    print("iterations={}".format(N),file=fil5)
    eps=1E-10
    print("eps={}".format(eps),file=fil3)
    print("eps={}".format(eps),file=fil4)
    print("eps={}".format(eps),file=fil5)
    print('',file=fil3)
    print('',file=fil4)
    print('',file=fil5)
    
    start1 = timer()
    integral1=integrator.integrate(f, 0, 2, N)
    end1 = timer()
    print("regular integral:",file=fil3)
    print("regular integral:",file=fil4)
    print("regular integral:",file=fil5)
    print(end1-start1," seconds",file=fil3)
    print(end1-start1," seconds",file=fil4)
    print(end1-start1," seconds",file=fil5)
    print('',file=fil3)
    print('',file=fil4)
    print('',file=fil5)



    
    start2 = timer()
    integral2=numpy_integrator.numpy_integrate(f, 0, 2, N)
    end2 = timer()
    print("numpy integral:",file=fil3)
    print(end2-start2, " seconds",file=fil3)
    print((end1-start1)/(end2-start2), " speedup",file=fil3)
    print(file=fil3)
   
   
    start3 = timer()
    integral3=numba_integrator.numba_integrate(f, 0, 2, N)
    end3 = timer()
    print("numba integral:",file=fil4)
    print(end3-start3," seconds",file=fil4)
    print((end1-start1)/(end3-start3), " speedup",file=fil4)
    print(file=fil4)
    
    
    start4 = timer()
    integral4=cython_integrator.cython_integrate(f, 0, 2, N)
    end4 = timer()
    print("cython integral:",file=fil5)
    print(end4-start4, " seconds",file=fil5)
    print((end1-start1)/(end4-start4), " speedup",file=fil5)
    print(file=fil5)
     
    

def print_integral_of_linear_function():
    print("############",file=fil3)
    print("############",file=fil4)
    print("############",file=fil5)
    print("##linear f##",file=fil3)
    print("##linear f##",file=fil4)
    print("##linear f##",file=fil5)
    print("############",file=fil3)
    print("############",file=fil4)
    print("############",file=fil5)
    print(file=fil3)
    print(file=fil4)
    print(file=fil5)
    
    def f(x):
        return 2*x
    expected_answer=1
    print("f(x)=2x",file=fil3)
    print("f(x)=2x",file=fil4)
    print("f(x)=2x",file=fil5)
    N=int(2E7)
    print("iterations={}".format(N),file=fil3)
    print("iterations={}".format(N),file=fil4)
    print("iterations={}".format(N),file=fil5)
    eps=1E-10
    print("eps={}".format(eps),file=fil3)
    print("eps={}".format(eps),file=fil4)
    print("eps={}".format(eps),file=fil5)
    print('',file=fil3)
    print('',file=fil4)
    print('',file=fil5)
    
    start1 = timer()
    integral1=integrator.integrate(f, 0, 1, N)
    end1 = timer()
    print("regular integral:",file=fil3)
    print("regular integral:",file=fil4)
    print("regular integral:",file=fil5)
    print(end1-start1," seconds",file=fil3)
    print(end1-start1," seconds",file=fil4)
    print(end1-start1," seconds",file=fil5)
    print('',file=fil3)
    print('',file=fil4)
    print('',file=fil5)
    
    start2 = timer()
    integral2=numpy_integrator.numpy_integrate(f, 0, 1, N)
    end2 = timer()
    print("numpy integral:",file=fil3)
    print(end2-start2, " seconds",file=fil3)
    print((end1-start1)/(end2-start2), " speedup",file=fil3)
    print(file=fil3)

    
    start3 = timer()
    integral3=numba_integrator.numba_integrate(f, 0, 1, N)
    end3 = timer()
    print("numba integral:",file=fil4)
    print(end3-start3, " seconds",file=fil4)
    print((end1-start1)/(end3-start3), " speedup",file=fil4)
    print(file=fil4)
    print("Numba is better than numpy with the fact that you dont have to change you code (ideally) \n You only need to add @jit",file=fil4)
    

   
    start4 = timer()
    integral4=cython_integrator.cython_integrate(f, 0, 1, N)
    end4 = timer()
    print("cython integral:",file=fil5)
    print(end4-start4, " seconds",file=fil5)
    print((end1-start1)/(end4-start4), " speedup",file=fil5)
    print(file=fil5)

   
   
   
   
fil3=open('reports/report3.txt','w')
fil4=open('reports/report4.txt','w')
fil5=open('reports/report5.txt','w')
print_integral_of_constant_function()
print_integral_of_linear_function()
fil3.close()
fil4.close()
fil5.close()