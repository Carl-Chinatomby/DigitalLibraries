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
		self.tablesize = 255
		self.data = open(filename, 'r').read()
		self.encdata = ''
		self.decdata = ''
		for val in xrange(self.tablesize+1):
			self.table[chr(val)] = val
	
	def print_table(self):
		print "Name, Values"
		for c in self.table:
			print c + ', ' + str(self.table[c])
			
	def compress(self):
		"""
		"""
		print "Starting Compression of " + str(self.data)
		newcode  = ''
		for i, c in enumerate(self.data):
			if newcode+c in self.table:
				newcode += c
			else:
				print str(newcode) + " became " + str(self.table[newcode])
				self.encdata += str(self.table[newcode])
				self.table[newcode+c] = max(self.table.values())+1
				newcode = c
		
		return self.encdata
	
	def decompress(self, code):
		"""
		"""
		
	
def main():
	"""
	"""
	filename = "data/lzwtest.txt"
	comp = DictComp(filename)
	code = comp.compress()
	comp.decompress(code)	

if __name__=="__main__":
	main()