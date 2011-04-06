"""
Implements the LZW dictionary based compression algorithm
"""
import sys

class DictComp():
	"""
	"""
	def __init__(self, filename):
		"""
		"""
		self.table = {}
		self.invtable = {}
		self.tablesize = 255
		self.data = open(filename, 'r').read()
		self.encdata = []
		self.decdata = ''
		for val in xrange(self.tablesize+1):
			self.table[chr(val)] = val
			self.invtable[val] = chr(val)
	
	def print_table(self):
		print "Name, Values"
		for i in range(len(self.invtable)):
			print str(self.invtable[i]) + ', ' + str(i)
			
	def compress(self):
		"""
		"""
		print "Starting Compression of " + str(self.data)
		newcode  = ''
		for i, c in enumerate(self.data):
			print "newcode is " + newcode
			if newcode+c in self.table:
				newcode += c
			else:
				print str(newcode) + " became " + str(self.table[newcode])
				self.encdata.append(self.table[newcode])
				self.table[newcode+c] = max(self.table.values())+1
				newcode = c
		#
		print "newcode is " + newcode
		self.encdata.append(self.table[newcode])
		return self.encdata
	
	def decompress(self, code):
		"""
		"""
		print "Starting Decompression of " + str(code)
		
		for ind, val in enumerate(code):
			self.decdata += self.invtable[val]
			print str(val) + " decoded " + str(self.invtable[val])
			if ind+1 < len(code):
				nextcode = code[ind+1]
				if nextcode in self.invtable:
					self.invtable[max(self.invtable.keys())+1] = self.invtable[val] +self.invtable[nextcode][0]
				else:
					self.invtable[max(self.invtable.keys())+1] = self.invtable[val] + self.invtable[val][0]
				print "added " + str(max(self.invtable.keys())) + ": " + self.invtable[max(self.invtable.keys())] + " to the table"
				print "output: " +  self.decdata
				
		return self.decdata
	
def main():
	"""
	"""
	filename = "data/lzwtest.txt"
	comp = DictComp(filename)
	code = comp.compress()
	print code
	ptxt = comp.decompress(code)	
	print "the decoded data is: " + ptxt
	#comp.print_table()
	
if __name__=="__main__":
	main()