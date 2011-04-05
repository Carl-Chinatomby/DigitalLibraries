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
		#table will be a dictionary mapping to lists: 'char':[freq, low, high, prob]
		self.table = {}
		
		self.charset = {}
		self.ranges = {}
		self.prob = {}
		self.totalchars = 0
		self.initfreq = 0
		self.code = 0
		
		#create initial frequency of digits
		for number in xrange(0, 9+1):
			self.charset[number] = self.initfreq
		#create initial frequency for letters
		for letter in xrange(ord('a'), ord('z')+1):
			self.charset[chr(letter)] = self.initfreq
		self.charsetlen = len(self.charset)
		
		#calculate ranges and probabiities
		prev_high = 0
		for char in self.charset:
			self.prob[char] = self.charset[char]/self.charsetlen
			self.ranges[char] = [prev_high, prev_high+self.prob[char]]
			prev_high = prev_high + self.prob[char]
		#put try/catch statement here 
		self.data = open(self.filename).read()
	
	def print_table(self):
		print "Char, Frequency, Probability, Range"
		for char in self.charset:
			print str(char) + ', \t' + str(self.charset[char]) + ', \t' + \
			str(self.prob[char]) + ', \t' + str(self.ranges[char])
	
	def print_prob_sum(self):
		sum = 0
		for c in self.prob:
			sum += self.prob[c]
		print "The Sum is " + str(sum)
			
	def update_table(self, c):
		self.totalchars += 1
		
		#update frequency table			
		self.charset[c] += 1
		
		#update probabilities
		self.prob[c] = float(self.charset[c])/self.totalchars
		
		#update ranges
		found = False
		prev_high = 0
		for char in self.charset:		
			self.prob[char] = float(self.charset[char])/self.totalchars
			self.ranges[char] = [prev_high, prev_high + self.prob[char]]
			prev_high = self.ranges[char][0] + self.prob[char]
		
		
		
	def adaptive_encode(self):
		"""
		"""
		low = 0
		high = 1
		for i, c in enumerate(self.data):	
			range = high - low
			if c.isalpha():
				self.update_table(c.lower())
				high = low + range * self.ranges[c.lower()][1] 
				low = low + range * self.ranges[c.lower()][0]
			else:
				self.update_table(int(c))
				high = low + range * self.ranges[int(c)][1] 
				low = low + range * self.ranges[int(c)][0]
			self.code = low
			
			
		self.print_table()
		self.print_prob_sum() 
		print "The total chars is " + str(self.totalchars)
		print "The Code is " + str(self.code)
	
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