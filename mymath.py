"""
"""
class MyMath():
	"""
	"""
	def __init__(self):
		"""
		"""
		pass
	
	def pow_rec(self, a, n):
		"""
		"""
		if n==0:
			return 1
		elif n==1:
			return a
		else:
			halfpow = self.pow_rec(a, n/2)
			return halfpow * halfpow if n%2 == 0 else halfpow * halfpow * a
	
	def pow_itr(self, a, n):
		"""
		"""
		cache = {0:1, 1:a};
		if n==0:
			return 1
		elif n==1: 
			return a
		else:
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
			return result
		

if __name__ == "__main__":
	math = MyMath()
	a = 2
	#n = 13
	for n in xrange(21):
		res1 = math.pow_rec(a,n)
		res2 = math.pow_itr(a,n)
		print "%d^%d using pow_rec is: %s" % (a, n, res1)
		print "%d^%d using pow_itr is: %s" % (a, n, res2)