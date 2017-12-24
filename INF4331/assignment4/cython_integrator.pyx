#cython: boundscheck=False
#cython: wraparound=False
                        
cpdef cython_integrate(object f,double a,double b,int N):
            """ integrates f from a to b with N points"""
            cdef double dx=(b-a)/(N)
            cdef double retsum=0
            cdef int i
            for i in range(int(N)):
                        retsum += f(a+i*dx)
            return retsum*dx

cpdef midpoint_cython_integrate(object f,double a,double b,int N):
            """ integrates f from a to b with N points"""
            cdef double dx=(b-a)/(N)
            cdef double retsum=0
            cdef int i 
            cdef double half=dx/2
            for i in range(int(N)):
                        retsum += f(half+a+i*dx)
            return retsum*dx
