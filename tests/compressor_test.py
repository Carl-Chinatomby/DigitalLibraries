"""
"""
from ..DigitalLibraries import compresser
import sys
sys.path.append("..")

class CompresserTest():
	"""
	"""
	def __init__(self):
		pass
	
	def rle_test(self):
		comp = Compressor()
		
		origdata = open("testdata.txt", 'rb').read()
		comp.read(testdata.txt)
		comp.rle_encode
		assert(origdata == comp.rle_decode)