import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from profiler import do_cprofile

#@do_cprofile
def numpy_integrate(f,a ,b ,N):
            """ integrates f from a to b with N points"""
            dx=(b-a)/N
            points=np.linspace(a,b,N)
            try:
                        return np.sum(f(points)[:])*dx
            except:
                        f=np.vectorize(f)
                        return np.sum(f(points))*dx
                        
def midpoint_numpy_integrate(f,a ,b ,N):
            """ integrates f from a to b with N points"""
            dx=(b-a)/N
            half=dx/2
            points=np.linspace(a,b,N,endpoint=False)+half
            try:
                        return np.sum(f(points)[:])*dx
            except:
                        f=np.vectorize(f)
                        return np.sum(f(points))*dx          
           
            

