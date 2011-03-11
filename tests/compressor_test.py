"""
This is a test file for the compressor module
Can be run as a standalone program or as a nosetests
"""
import os, sys
diglib_path = os.path.abspath('..')
sys.path.append(diglib_path)
from compressor import Compressor

class Compressor_Test():
	"""
	"""
	def __init__(self):
		self.datapath = diglib_path+"/data/"
	
	def rle_test(self):
		filename = "testdata.txt"
		comp = Compressor(self.datapath + filename)
		origdata = open(self.datapath + filename, 'rb').read()
		print "Begining RLE Test!",
		comp.rle_encode()
		assert origdata == comp.rle_decode()
		print "..Passed"

if __name__ == "__main__":
	test = CompressorTest()
	test.rle_test()