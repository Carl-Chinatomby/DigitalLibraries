"""
"""

class Compresser():
	"""
	"""
	def __init__(self):
		"""
		"""
		pass
	
	def read_data(self, filename):
		"""
		"""
		try:
			self.data = open(filename, 'rb').read()
		except IOError:
			print "Error Opening file %s! Exiting!" % filename
			raise SystemExit
	
	def rle_encode(self):
		"""
		"""
		print self.data
	
	def rle_decode(self):
		"""
		"""
		pass
	
	def huffman_encode:
		"""
		"""
		pass
	
	def huffman_decode:
		"""
		"""
		pass
	
if __name__ == "__main__":
	comp = Compresser()
	comp.read("testfile.txt")