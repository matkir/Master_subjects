from polynomials import *
def test_at_point():
	assert Polynomial([1,2,3]).__call__(2)==3*2**2+2*2+1
	assert Polynomial([1,2,3]).__call__(4)==3*4**2+2*4+1
	assert Polynomial([1,2,3]).__call__(7)==3*7**2+2*7+1
	
def test_add_2_polynomials():
	assert Polynomial([1,2,3])+Polynomial([1,2,3])==Polynomial([2,4,6])
	assert Polynomial([-1,2,3])+Polynomial([1,2,3])==Polynomial([0,4,6])
	p, q = map(Polynomial,[[1, 0, 1], [0, 2, 0]])
	assert p+q+p+p+p-1==Polynomial([3,2,4])
	

def test_sub_2_polynomials():
	assert Polynomial([2,2,2])-Polynomial([1,1,1])==Polynomial([1,1,1])
	assert Polynomial([4,2,2,2])-Polynomial([1,1,1])==Polynomial([3,1,1,2])
	assert Polynomial([-4,2,2,2])-Polynomial([1,1,1])==Polynomial([-5,1,1,2])
	p, q = map(Polynomial,[[1, 0, 1], [0, 2, 0]])
	assert p-q-p+(2*p)==Polynomial([2,-2,2])
	
def test_degree_of_polynomials():
	assert Polynomial([1,2,3,4,5]).degree()==4
	assert Polynomial([1,2,3,4,0]).degree()==3
	assert Polynomial([1,0,3,4,0]).degree()==3
	assert Polynomial([0,0,0]).degree()==-1
	assert Polynomial([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]).degree()==0
	
	#LETS GET FUNCY
	import random
	x = []
	for i in range(100000):
		x.append(0)
	some_number=random.randint(0,100000)
	x[some_number]=1
	#lets test the funcyness
	
	assert Polynomial(x).degree()==some_number

def test_repr():
	assert repr(Polynomial([-4331])) == "-4331"
	assert repr(Polynomial([5])) == "5"
	assert repr(Polynomial([9999,1])) == "x+9999"
	assert repr(Polynomial([0,0,0])) == ""
	assert repr(Polynomial([-1,-3,-8])) == "-8x^2-3x-1"