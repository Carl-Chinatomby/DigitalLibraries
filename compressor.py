"""
"""

class Compressor():
	"""
	"""
	def __init__(self):
		"""
		"""
		self.data = []
		self.rledata_enc = []
		self.rledata_dec = ""
	
	def read(self, filename):
		"""
		"""
		try:
			data = open(filename, 'rb').read()
			self.data = open(filename, 'rb').read()
		except IOError:
			print "Error Opening file %s! Exiting!" % filename
			raise SystemExit
		
		return self.data
	
	def rle_encode(self):
		"""
		"""
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
		"""
		for char, count in self.rledata_enc:
			for i in range (count):
				self.rledata_dec += char
		print self.rledata_dec
		return self.rledata_dec
	
	def huffman_encode(self):
		"""
		"""
		pass
	
	def huffman_decode(self):
		"""
		"""
		pass
	
if __name__ == "__main__":
	comp = Compressor()
	print comp.read("testdata.txt")
	comp.rle_encode()
	comp.rle_decode()
	