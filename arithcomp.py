"""
********************
By Carl Chinatomby
********************
Implements Adaptive Arithmetic Encoding and Decoding. 
Initially all characters are all the same frequency.
For simplicity the alphabet only consists of lowercase 
characters and 10 digits. As new characters present the
domains assigned to the symbols are changed accordingly.


To run this program you would simply do:
	
	    python arithcomp.py <inputfile> <outputfile>
		
For example running:
	    python arithcomp.py data/arithtest.txt data/encarith.txt
will calculate the code for arithtest.txt and output the code in enarith.txt
				
"""
import sys
from math import floor, trunc

class ArithComp():
	"""
	"""
	def __init__(self, infile, outfile):
		"""
		"""
		self.infile = infile
		self.outfile = outfile
		self.charset = {}
		self.ranges = {}
		self.prob = {}
		self.cumfreq = {}
		self.initfreq = 1
		self.code = 0.0
		self.decdata = ''
		
		#create initial frequency of digits
		for number in xrange(0, 9+1):
			self.charset[number] = self.initfreq
		#create initial frequency for letters
		for letter in xrange(ord('a'), ord('z')+1):
			self.charset[chr(letter)] = self.initfreq
		self.charsetlen = len(self.charset)
		self.totalchars = self.charsetlen
		self.charcount = 0
		#calculate ranges and probabiities
		prev_high = 0
		curcumfreq = self.initfreq		
		for char in self.charset:
			self.prob[char] = self.charset[char]/float(self.charsetlen)
			self.ranges[char] = [prev_high, prev_high+self.prob[char]]
			prev_high = prev_high + self.prob[char]
			self.cumfreq[char] = curcumfreq 
			curcumfreq += self.initfreq
		self.data = open(self.infile, 'r').read()
		self.output = open(self.outfile, 'w')

		self.initcharset = self.charset.copy()
		self.initranges = self.ranges.copy()
		self.initprob = self.prob.copy()
		self.initcumfreq = self.cumfreq.copy()
		self.initcharsetlen = self.charsetlen
		self.inittotalchars = self.totalchars
	
	def print_table(self):
		print "Char, Frequency, Probability, Range, CumFreq"
		for char in self.charset:
			if self.charset[char]:
				print str(char) + ', \t' + str(self.charset[char]) + ', \t' + \
				str(self.prob[char]) + ', \t' + str(self.ranges[char]) + ' \t' + \
				str(self.cumfreq[char])

	def print_table2(self):
		print "Char, Frequency, Probability, Range, CumFreq"
		for char in self.initcharset:
			if self.initcharset[char]:
				print str(char) + ', \t' + str(self.initcharset[char]) + ', \t' + \
				str(self.initprob[char]) + ', \t' + str(self.initranges[char]) + ' \t' + \
				str(self.initcumfreq[char])

	def print_prob_sum(self):
		sum = 0
		for c in self.prob:
			sum += self.prob[c]
		print "The Sum is " + str(sum)
			
	def add_char(self, c):
		self.totalchars += 1
		
		#update frequency table			
		self.charset[c] += 1
		
		#update probabilities
		self.prob[c] = float(self.charset[c])/self.totalchars
		
		#update ranges
		prev_high = 0
		curcumfreq = 0
		for char in self.charset:		
			self.prob[char] = float(self.charset[char])/self.totalchars
			self.ranges[char] = [prev_high, prev_high + self.prob[char]]
			self.cumfreq[char] = curcumfreq + self.charset[char]
			curcumfreq = self.cumfreq[char]
			prev_high = self.ranges[char][0] + self.prob[char]

			
	def add_initchar(self, c):
		self.inittotalchars += 1
		
		#update frequency table			
		self.initcharset[c] += 1
		
		#update probabilities
		self.initprob[c] = float(self.initcharset[c])/self.inittotalchars
		
		#update ranges
		prev_high = 0
		curcumfreq = 0
		for char in self.initcharset:		
			self.initprob[char] = float(self.initcharset[char])/self.inittotalchars
			self.initranges[char] = [prev_high, prev_high + self.initprob[char]]
			self.initcumfreq[char] = curcumfreq + self.initcharset[char]
			curcumfreq = self.initcumfreq[char]
			prev_high = self.initranges[char][0] + self.initprob[char]

			
	def remove_char(self, c):
		"""
		Removes a character from the table and updates probabilities
		This function is currently now used because decoding builds it's own table
		"""
		self.totalchars -= 1

		if self.totalchars < 1:
			#reset all variables
			return

		#update frequency table			
		self.charset[c] -= 1
		
		#update probabilities
		self.prob[c] = float(self.charset[c])/self.totalchars
		
		#update ranges
		found = False
		prev_high = 0
		for char in self.charset:		
			self.prob[char] = float(self.charset[char])/self.totalchars
			self.ranges[char] = [prev_high, prev_high + self.prob[char]]
			prev_high = self.ranges[char][0] + self.prob[char]

	def encode(self):
		"""
		"""
		low = 0
		high = 1
		print "The original data is: " + self.data
		for i, c in enumerate(self.data):	
			range = high - low
			if c.isalpha():
				high = low + range * self.ranges[c.lower()][1] 
				low = low + range * self.ranges[c.lower()][0]
				self.charcount += 1
				self.add_char(c.lower())
			else:
				self.charcount += 1
				high = low + range * self.ranges[int(c)][1] 
				low = low + range * self.ranges[int(c)][0]
				self.add_char(int(c))
			self.code = low			
			
		self.print_prob_sum()
		self.print_table()
		print "The code is: " + str(self.code)
		raw_input("Encoding Complete, Press Enter to Decode")
		
		self.output.write(str(self.charcount) +','+str(self.code))
		return self.code
	
	def getnextrange(self, prevhigh):
		for c in self.ranges:
			if self.ranges[c][0] == prevhigh:
				return c
	
	def getinitnextrange(self, prevhigh):
		for c in self.initranges:
			if self.initranges[c][0] == prevhigh:
				return c
		
	
	def decode(self, code):
		"""
		"""
		data = self.data.split(',')
		curcode = code
		
		#this part of the code is when you want to read it from a file,
		#but there are problems since precision gets lost
		#self.charcount = int(data[0])
		#curcode = float(data[1])

		print "The Code is: " + str(curcode)
		count = 0
		while (curcode > 0 and (count < self.charcount)):				
			count += 1
			for char in self.ranges:
				if curcode >= self.initranges[char][0] and curcode < self.initranges[char][1]:
					range = self.initranges[char][1] - self.initranges[char][0]
					curcode -= self.initranges[char][0]
					curcode /= range
					self.add_initchar(char)
					self.decdata += str(char)
					break
		self.print_table()
		print "The Decoded Data is : " + self.decdata

def main():
	"""
	"""
	if len(sys.argv) < 3:
		print "Please start the program with parameters are follows: \n\n python arithcomp.py <inputfile> <outputfile>"
		exit(0)
						
	infile = sys.argv[1]
	outfile = sys.argv[2]
	comp = ArithComp(infile, outfile)
	code = comp.encode()
	comp.decode(code)
	
if __name__=="__main__":
	main()