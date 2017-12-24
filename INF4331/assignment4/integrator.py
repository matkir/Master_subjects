import matplotlib.pyplot as plt
from timeit import default_timer as timer
from profiler import do_cprofile


#@do_cprofile
def integrate(f, a, b, N):
            """ integrates f from a to b with N points"""
            dx=(b-a)/(N)
            retsum=0
            for i in range(int(N)):
                        retsum += f(a+i*dx)
            return retsum*dx

def midpoint_integrate(f, a, b, N):
            """ integrates f from a to b with N points"""
            dx=(b-a)/(N)
            retsum=0
            half=dx/2
            for i in range(int(N)):
                        retsum += f(half+a+i*dx)
            return retsum*dx

def error_func(f,a,b,true_val):

            val_list=[]
            err_list=[]
            c=[2**(i+1) for i in range(22)]
            
            start = timer()
            for i in c:
                        val=integrate(f,a,b,i)
                        val_list.append(val)
                        err_list.append(abs(val-true_val))
            
            end = timer()
            print(end-start)            
            
            plt.semilogx(c,err_list)
            plt.xlabel('N')
            plt.ylabel('Accuracy')
            plt.title('Error Plot')
            plt.savefig('reports/quadratic_error.png')
            plt.show()
            
if __name__ =='__main__':
            def f(x):
                        return x**2
            a=0
            b=1
            true_val=1/3
            error_func(f,a,b,true_val)            