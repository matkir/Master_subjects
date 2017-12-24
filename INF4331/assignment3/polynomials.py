class Polynomial:
	def __init__(self, coef):
		"""coefficients should be a list of numbers with 
		the i-th element being the coefficient a_i."""
		self.coef=coef

	def degree(self):
		"""Return the index of the highest nonzero coefficient.
		If there is no nonzero coefficient, return -1."""
		for i in enumerate(reversed(self.coef)):
			if i[1]!=0:
				return len(self.coef)-i[0]-1 
		return -1

	def coefficients(self):
		"""Return the list of coefficients. 
		The i-th element of the list should be a_i, meaning that the last 
		element of the list is the coefficient of the highest degree term."""
		return self.coef        

	def __call__(self, x):
		"""Return the value of the polynomial evaluated at the number x"""
		retval=0
		for i in enumerate(self.coef):
			retval+=i[1]*x**i[0]
		return retval

    
	def __add__(self, p):
		"""Return the polynomial which is the sum of p and this polynomial
		Should assume p is Polynomial([p]) if p is int. 
		If p is not an int or Polynomial, should raise ArithmeticError."""
		if isinstance(p,int):
			p=Polynomial([p])
		
			
		for i in p.coef:
			result=isinstance(i, int)
			if result == False:
				raise ArithmeticError		
		
		retval=[]
		tmp1=list(reversed(p.coef))
		tmp2=list(reversed(self.coef))
		diff=len(tmp1)-len(tmp2)
		if diff<0:
			tmp1=abs(diff)*[0]+tmp1
		elif diff>0:
			tmp2=diff*[0]+tmp2
		else:
			pass
		
		for i in zip(list(tmp1),list(tmp2)):
			retval.append(i[0]+i[1])
		return Polynomial(list(reversed(retval)))	
	def __sub__(self, p):
		"""Return the polynomial which is the difference of p and this polynomial
		Should assume p is Polynomial([p]) if p is int. 
		If p is not an int or Polynomial, should raise ArithmeticError."""
		if isinstance(p,int):
			p=Polynomial([p])
		
		for i in p.coef:
			result=isinstance(i, int)
			if result == False:
				raise ArithmeticError	
		
		retval=[]
		tmp1=list(reversed(p.coef))
		tmp2=list(reversed(self.coef))
		diff=len(tmp1)-len(tmp2)
		if diff<0:
			tmp1=abs(diff)*[0]+tmp1
		elif diff>0:
			tmp2=diff*[0]+tmp2
		else:
			pass
		for i in zip(list(tmp1),list(tmp2)):
			retval.append(i[1]-i[0])
		return Polynomial(list(reversed(retval)))	

	def __mul__(self, c):
		"""Return the polynomial which is this polynomial multiplied by given integer.
		 Should raise ArithmeticError if c is not an int."""
		if not isinstance(c, int):
			raise ArithmeticError	
		
		retval=[]
		for i in self.coef:
			retval.append(i*c)
		return Polynomial(retval)

	def __rmul__(self, c):
		"""Return the polynomial which is this polynomial multiplied by some integer"""
		retval=[]
		for i in self.coef:
			retval.append(i*c)
		return Polynomial(retval)

	
	def __repr__(self):
		"""Return a nice string representation of polynomial.
		
		E.g.: x^6 - 5x^3 + 2x^2 + x - 1
		"""
		retstring=""
		#0 order 
		for i in enumerate(reversed(self.coef)):
			if i[1]==0:
				continue
			#specialcase 1
			elif len(self.coef)-i[0]-1==1 and i[1]==1:
				retstring+="x".format(i[1])
			
			elif len(self.coef)-i[0]-1==1:
				retstring+="{0}x".format(i[1])
			#specialcase 2
			elif len(self.coef)-i[0]-1==0:
				retstring+="{0}".format(i[1])
				
			elif i[1]==1:
				a="x^{0}".format(len(self.coef)-i[0]-1)
				retstring+=a
			else:
				a="{0}x^{1}".format(i[1],len(self.coef)-i[0]-1)
				retstring+=a
			
			retstring+='+'
		retstring=retstring.replace("+-", "-")	
		retstring=retstring.rstrip('+ ')		
		return retstring

	def __eq__(self, p):
		"""Check if two polynomials have the same coefficients."""
		if p==self.coef:
			return True
		else:
			return False

	
			
def sample_usage():
	p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
	q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3
	print("The value of {0} at {1} is {2}".format(p, 7, p(7)))

	print("The coefficients of {} are {}".format(p, p.coefficients()))

    
	print("\nAdding {} and {} yields {}".format(p, q, p+q))

	p, q, r = map(Polynomial,
                  [
                      [1, 0, 1], [0, 2, 0], [1, 2, 1]
                  ])
    
	print("\nWill adding {} and {} be the same as {}? Answer: {}".format(p, q, r, p+q == r))
	print("\nIs {} - {} the same as {}? Answer: {}".format(p, q, r, p-q == r))

if __name__ == "__main__":
	sample_usage()
	import test_polynomials as test
	test.test_add_2_polynomials()
	test.test_sub_2_polynomials()
	test.test_at_point()
	test.test_degree_of_polynomials()
	test.test_repr()
	print("\nAll tests OK")