"""
"""
import os, sys
#diglib_path = os.path.abspath('..')
#sys.path.append("digtlib_path")
from compressor import Compressor

class CompressorTest():
	"""
	"""
	def __init__(self):
		pass
	
	def rle_test(self):
		comp = Compressor()
		
		origdata = open("testdata.txt", 'rb').read()
		"Begining RLE Test!"
		origdata
		comp.read("testdata.txt")
		comp.rle_encode()
		assert origdata == comp.rle_decode()

if __name__ == "__main__":
	test = CompressorTest()
	test.rle_test()