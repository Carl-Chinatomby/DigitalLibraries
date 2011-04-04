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
		self.charset = {}
		self.initfreq = 0
		
		#create initial frequency of digits
		for number in xrange(0, 9+1):
			self.charset[number] = self.initfreq
		#create initial frequency for letters
		for letter in xrange(ord('a'), ord('z')+1):
			self.charset[chr(letter)] = self.initfreq
		self.charsetlen = len(self.charset)
		
		#put try/catch statement here 
		self.data = open(self.filename).read()
	
	def print_table(self):
		print "Char, Frequency"
		for char in self.charset:
			print str(char) + ', ' + str(self.charset[char])
		
	def adaptive_encode(self):
		"""
		"""
		for i, c in enumerate(self.data):
			if c.isalpha():
				self.charset[c.lower()] += 1
			else:
				self.charset[int(c)] += 1
		
		self.print_table()
	
	def adaptive_decode(self):
		"""
		"""
		pass

def main():
	"""
	"""
	#filename = sys.argv[1]
	filename = "data/arithtest.txt"
	comp = ArithComp(filename)
	comp.adaptive_encode()

if __name__=="__main__":
	main()