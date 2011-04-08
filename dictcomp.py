"""
*******************
BY CARL CHINATOMBY 
*******************
Implements the LZW dictionary based compression algorithm

To run this program you would simply do:
	
	python dictcomp.py <function> <inputfile> <outputfile>

For example running:
	python dictcomp.py compress data/lzwtest.txt data/enclzw.txt
	
will compress data/lzwtest.txt and store the results in data/enclzw.txt

To decompress we can do:
	python dictcomp.py decompress data/enclzw.txt data/declzw.txt
	
doing a diff on declzw.txt and lzwtest.txt should produce no output and provided
the input file has enough repeition and is large enough, the output of of compression
should result in a smaller file than the original 
"""
import sys
import struct

class DictComp():
	"""
	Implements the LZW dictionary based compression algorithm
	
	To run this program you would simply do:
		
		python dictcomp.py <function> <inputfile> <outputfile>
		
	For example running:
		python dictcomp.py compress data/lzwtest.txt data/enclzw.txt
			
	will compress data/lzwtest.txt and store the results in data/enclzw.txt

	To decompress we can do:
		python dictcomp.py decompress data/enclzw.txt data/declzw.txt
	
	doing a diff on declzw.txt and lzwtest.txt should produce no output and provided
	the input file has enough repeition and is large enough, the output of of compression
	should result in a smaller file than the original 
	"""

	def __init__(self, infile, outfile):
		"""
		Initializes everything for the compression/decompression
		Creates a table and an inverse table of the default 255 ascii char set
		"""
		self.infile = infile
		self.outfile = outfile
		self.table = {}
		self.invtable = {}
		self.tablesize = 255
		self.data = open(infile, 'rb').read()
		self.output = open(outfile, 'wb')
		self.encdata = []
		self.decdata = ''
		for val in xrange(self.tablesize+1):
			self.table[chr(val)] = val
			self.invtable[val] = chr(val)
	
	def print_table(self, table):
		"""
		Prints the table, table should be either self.table or self.invtable
		"""
		print "Name, Values"
		for i in range(len(table)):
			print str(table[i]) + ', ' + str(i)
			
	def compress(self):
		"""
		Compresses the input file and stores it as binary data in the output file
		Note: The table/dictionary is not stored in the file, It is not needed for 
		decompression
		
		Values are all stored as shorts in the compressed file
		"""
		print "Starting Compression of " + str(self.data)
		newcode  = ''
		for i, c in enumerate(self.data):
			if newcode+c in self.table:
				newcode += c
			else:
				self.encdata.append(self.table[newcode])
				self.table[newcode+c] = max(self.table.values())+1
				newcode = c
				
		self.encdata.append(self.table[newcode])
		print "\nThe encoded data is " + str(self.encdata)
		size = len(self.encdata)
		print "The size is " + str(size)
		s = struct.Struct('i'+str(size)+"h")
		buffer = s.pack(size, *self.encdata)
		self.output.write(buffer)
		return self.encdata
	
	def decompress(self):
		"""
		Decompresses the binary data in the input file and returns the data in the output file
		The dictionary is built up as characters are read, the same way it was done when encoding
		and so we don't need the dictionary to decode
		"""
		data = open(self.infile, 'rb').read()
		output = open(self.outfile,'w')
		code = []
		finished = False
		i = 0
		size = struct.unpack_from('i',data)[0]
		print "The size is " + str(size)
		fmt = 'i'+str(size)+'h'
		code = struct.unpack_from(fmt,data)[1:]
		print "The Encoded Data is: " + str(code)
		
		for ind, val in enumerate(code):
			self.decdata += self.invtable[val]
			if ind+1 < len(code):
				nextcode = code[ind+1]
				if nextcode in self.invtable:
					self.invtable[max(self.invtable.keys())+1] = self.invtable[val] +self.invtable[nextcode][0]
				else:
					self.invtable[max(self.invtable.keys())+1] = self.invtable[val] + self.invtable[val][0]
		print "\nThe decoded data is: " + self.decdata
		output.write(self.decdata)
		return self.decdata
	
def main():
	if len(sys.argv) < 4:
		print "Please start the program with parameters are follows: \n\n python dictcomp.py <function> <inputfile> <outputfile> \n\nwhere function is either 'compress' or 'decompress'"
		exit(0)

	function = sys.argv[1]
	infile = sys.argv[2]
	outfile = sys.argv[3]
	comp = DictComp(infile, outfile)
	callfct = 'code = comp.' + function + '()'
	exec callfct
	
if __name__=="__main__":
	main()