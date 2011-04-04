"""
Implements Adaptive Arithmetic Encoding and Decoding. 
Initially all characters are all the same frequency.
For simplicity the alphabet only consists of lowercase 
characters and 10 digits. As new characters present the
domains assigned to the symbols are changed accordingly.
"""
import sys

class ArithComp():
	"""
	"""
	def __init__(self, filename):
		"""
		"""
		self.filename = filename
		print "the filename is " + filename
		
	
	def adaptive_encode(self):
		"""
		"""
		pass
	
	def adaptive_decode(self):
		"""
		"""
		pass

def main():
	"""
	"""
	filename = sys.argv[1]
	Comp = ArithComp(filename)

if __name__=="__main__":
	main()