"""
*******************
Compressor
By Carl Chinatomby
*******************

This file contains the Compressor class that 
contains many compression algorithms for 
ascii data files. 

"""

class Compressor():
	"""
	Contains algorithms to read in data and encode/decode the data
	using various compression schemes. Every scheme has it's encoding
	stored in separate variables so you may use different encodings
	on the same data for comparison
	"""
	def __init__(self, filepath):
		"""
		Constructor, reads in the file and sets its contents as data
		"""
		self.data = self.read(filepath)
		self.rledata_enc = []
		self.rledata_dec = ""
	
	def get_data(self):
		"""
		returns the current data that is stored
		"""
		return self.data
	
	def reset(self):
		"""
		Empties all the data and encodeing/decoding variables
		"""
		self.data = ""
		self.rledata_enc=[]
		self.rledata_dec = ""
		
	def read(self, filename):
		"""
		Reads in filename and stores it's contents into data
		"""
		#self.reset()
		try:
			data = open(filename, 'rb').read()
			self.data = open(filename, 'rb').read()
		except IOError:
			print "Error Opening file %s! Exiting!" % filename
			raise SystemExit
		
		return self.data
	
	def rle_encode(self):
		"""
		Uses run-length encoding on the data and returns the encoding 
		as a list of tuples of the form [(a 3) (b 4)] where the original
		data was aaabbbb. The first element of the tuple denotes the 
		character and the 2nd element denotes the length. 
		"""
		self.rledata_enc = []
		prev = None
		for char in self.data:
			if prev == None:
				prev = char
				count = 1
			elif prev == char:
				count += 1
			else:
				rle = (prev, count)
				self.rledata_enc.append(rle)
				prev = char
				count = 1
		
		#insert last run
		rle = (prev, count)
		self.rledata_enc.append(rle)
		
		return self.rledata_enc
	
	def rle_decode(self):
		"""
		Converts the run_length encoding back to the a 
		string containing the full length. rle_encode() 
		must be called prior to this function call.
		Example:
			
			[(a 3) (b 4)] will return aaabbbb
		"""
		for char, count in self.rledata_enc:
			for i in range (count):
				self.rledata_dec += char
		return self.rledata_dec
	
	def huffman_encode(self):
		"""
		Not Implemented yet
		"""
		pass
	
	def huffman_decode(self):
		"""
		Not Implemented yet
		"""
		pass
	
if __name__ == "__main__":
	path = "data/"
	filename = "testdata.txt"
	comp = Compressor(path+filename)
	print comp.get_data()
	print comp.rle_encode()
	print comp.rle_decode()
	