"""
A math class used to implement various math algorithms
The power functions are currently untested for fractional
exponents. Need to calculate nth root of base, 
see "nth root algorithm" on wikipedia for fractional exp. 
"""
class MyMath():
	"""
	"""	
	def pow_rec(self, a, n):
		"""
		Computes a^n. Uses the trick a^n = a^(n/2) * a^(n/2) and 
		a^n = a^(n-1) * a to compute this result recursively.
		Works correctly for negative numbers.
		"""
		negative = True if n < 0 else False
		if n==0:
			return 1
		elif n==1:
			return a
		elif negative:
			return 1.0/pow(a, abs(n))
		else:
			halfpow = self.pow_rec(a, n/2)
			return halfpow * halfpow if n%2 == 0 else halfpow * halfpow * a
	
	def pow_tditr(self, a, n):
		"""
		Computes a^n. Works correctly for negative numbers. Uses 
		an interative top-down approach to calculate teh result
		"""
		negative = True if n < 0 else False
		oddres = 1
		result = a
		if n == 0:
			return 1
		elif negative == True:
			n = abs(n)
		while (n > 1):
			remainder = n%2
			if remainder > 0:
				oddres *= result
			n = (n-remainder)/2
			result *= result
		return result * oddres if not negative else 1.0/(result*oddres)
	
	
	def pow_buitr(self, a, n):
		"""
		Computes a^n using an iterative bottom up approach. Keeps doubling 
		the result as long as it is smaller than a^n. Then uses a lookup
		array of the previously computed values to get the final result.
		
		ie: a^7 will double until a^4, and then use the table to multiply
		a^4 * a^2 * a = a^7.
		"""
		cache = {0:1, 1:a};
		negative = True if n<0 else False
		if n==0:
			return 1
		elif n==1: 
			return a
		else:
			n = abs(n) if negative else n
			result = a
			m=1
			while (2*m <= n):
				result *= result
				m *=2
				cache[m] = result
			
			#reuse our saved data to increase by the highest power of 2
			i = m/2
			while (n-m > 1):
				if (i <= n-m):
					result *=cache[i]
					m += i
				i = i/2
					
			#handle the odd case		
			if n-m == 1:
				result *= a
		return result if not negative else 1.0/result
		

if __name__ == "__main__":
	math = MyMath()
	a = 2
	bound = 21
	for n in xrange(bound):
		res1 = math.pow_rec(a,n)
		res2 = math.pow_buitr(a,n)
		res3 = math.pow_tditr(a,n)
		print "%d^%d using pow_rec is: %s" % (a, n, res1)
		print "%d^%d using pow_itr is: %s" % (a, n, res2)
		print "%d^%d using pow_tditr is: %s" % (a, n, res3)