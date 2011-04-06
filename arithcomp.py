"""
Implements Adaptive Arithmetic Encoding and Decoding. 
Initially all characters are all the same frequency.
For simplicity the alphabet only consists of lowercase 
characters and 10 digits. As new characters present the
domains assigned to the symbols are changed accordingly.
"""
import sys
from math import floor, trunc

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

		#calculate ranges and probabiities
		prev_high = 0
		curcumfreq = self.initfreq		
		for char in self.charset:
			self.prob[char] = self.charset[char]/float(self.charsetlen)
			self.ranges[char] = [prev_high, prev_high+self.prob[char]]
			prev_high = prev_high + self.prob[char]
			self.cumfreq[char] = curcumfreq 
			curcumfreq += self.initfreq
		#put try/catch statement here 
		self.data = open(self.filename).read()
		
		self.initcharset = self.charset
		self.initranges = self.ranges
		self.initprob = self.prob
		self.initcumfreq = self.cumfreq
		self.initcharsetlen = self.charsetlen
		self.inittotalchars = self.totalchars
	
	def print_table(self):
		print "Char, Frequency, Probability, Range, CumFreq"
		for char in self.charset:
			if self.charset[char]:
				print str(char) + ', \t' + str(self.charset[char]) + ', \t' + \
				str(self.prob[char]) + ', \t' + str(self.ranges[char]) + ' \t' + \
				str(self.cumfreq[char])
	
	def print_prob_sum(self):
		sum = 0
		for c in self.prob:
			sum += self.prob[c]
		print "The Sum is " + str(sum)
			
	#Generalize these two functions they share soem of the same code
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

	def adaptive_encode(self):
		"""
		"""
		low = 0
		#high = 1
		high = 9999
		for i, c in enumerate(self.data):	
			#range = high - low
			range = high - low +1
			print "table before: "
			self.print_table()
			print "just read: " + str(c)
			if c.isalpha():
				#low = low + range*self.cumfreq[c.lower()]/float(max(self.cumfreq.values()))
				print "the cum freq for this char is" + str(self.cumfreq[c.lower()])
				print "the max is " + str(float(max(self.cumfreq.values())))
				print "the division is" + str(self.cumfreq[c.lower()]/float(max(self.cumfreq.values())))
				print "the character used for high is " + chr(ord(c.lower())+1)
				print "the total chars is" + str(float(max(self.cumfreq.values())))
				#high= low + range*self.cumfreq[chr(ord(c.lower())+1)]/float((max(self.cumfreq.values())-1))
				nextchar = self.getnextrange(self.ranges[c.lower()][1])
				#print "the next cahr is " + str(nextchar)
				#high = low + range*self.cumfreq[nextchar]/float((max(self.cumfreq.values()))) - 1 
				low = low + trunc(range*self.cumfreq[c.lower()]/max(self.cumfreq.values()))
				high = low + trunc(range*self.cumfreq[nextchar]/max(self.cumfreq.values())) - 1
				print "the cum freq for the next char is " + str(self.cumfreq[chr(ord(c.lower())+1)])
				#high = low + range * self.ranges[c.lower()][1] 
				#low = low + range * self.ranges[c.lower()][0]
				#high = low + range * self.ranges[c.lower()][1] - 1 
				#low = low + range * self.ranges[c.lower()][0]
				print "the high is : " + str(high)
				print "the low is : " + str(low)
				self.add_char(c.lower())	
			else:
				high = low + range * self.ranges[int(c)][1] 
				low = low + range * self.ranges[int(c)][0]
				self.add_char(int(c))
			self.code = low			
			self.print_table()
			self.print_prob_sum()
			
			print "The total chars is " + str(self.totalchars)
			print "The Code is " + str(self.code)
			print "the high is : " + str(high)
			print "the low is : " + str(low)

			raw_input("Press Any Key for next input")
			
		#write the code and the condensed symbol table to a file
		#remember to remove all the useless characters as it
		#just increases space
		
		return self.code
	
	def getnextrange(self, prevhigh):
		for c in self.ranges:
			if self.ranges[c][0] == prevhigh:
				return c
		
	
	def adaptive_decode(self, code):
		"""
		"""
		curcode = code
		#while (curcode > 0 and self.totalchars > 0):
		#	#print "the curcode is " + str(curcode)				
		#	for char in self.ranges:
		#		if curcode > self.ranges[char][0] and curcode < self.ranges[char][1]:
		#			#print char
		#			#self.print_table()
		#			#self.print_prob_sum()
		#			range = self.ranges[char][1] - self.ranges[char][0]
		#			curcode -= self.ranges[char][0]
		#			curcode /= range
		#			self.remove_char(char)
		#			self.decdata += str(char)
		count = 36
		#while (curcode >0 and curcode < 1.0):
		while (curcode > 0 and count < self.totalchars):
			print "the curcode is " + str(curcode)				
			for char in self.initranges:
				if curcode > self.initranges[char][0] and curcode < self.initranges[char][1]:
					print char
					self.print_table()					
					#self.print_prob_sum()
					range = self.initranges[char][1] - self.initranges[char][0]
					print "range is " + str(range)
					curcode -= self.initranges[char][0]
					print "curcode is now" + str(curcode)
					curcode /= range
					self.add_initchar(char)
					self.decdata += str(char)
					count += 1
					print "the curcode is: " + str(curcode)
					raw_input("waiting")
			

		
		
		self.code = 0
		print "The decoded data is " + self.decdata

def main():
	"""
	"""
	#filename = sys.argv[1]
	filename = "data/arithtest.txt"
	comp = ArithComp(filename)
	comp.print_table()
	code = comp.adaptive_encode()
	comp.adaptive_decode(code)
	
if __name__=="__main__":
	main()