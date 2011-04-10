"""
******************
By Carl Chinatomby
******************
Implements the soft sequential kmeans algorithm assuming the
threshold to create a new cluster is d and the maximum number
of clusters to be found is K. A post processing is needed to
refine the clustering decisions made on the fly. 

This file requires the numpy library to be installed.
"""
import random
import time
import numpy as np
import math 

class Kmeans():
	"""
	"""
	def __init__(self):
		"""
		"""
		random.seed(time.time())
		print "Please Enter in a N for the NxN Matrix"
		self.N = int(raw_input())
		self.data = np.zeros((self.N,self.N))
		self.result = np.zeros((self.N,self.N))
		
		for i in xrange(self.N):
			for j in xrange(self.N):
				self.data[i][j] = random.random()

		print self.data

	def get_kmeans(self, k, d):
		means = np.zeros(k)
		for i in xrange(k):
			means[i] = random.random()
			
		counts = np.zeros(k)
		for i in xrange(self.N):
			for j in xrange(self.N):
				dist, prob = self.get_dist_prob(self.data[i][j], means)
				ind = np.argmin(dist)
				counts[ind] +=1
				#means[ind] += (1.0/counts[ind])*(dist[ind]) 
				#means[ind] = prob[ind]*(data[i][j]/dist[ind])
				weight = np.sum(prob[:]*self.data[i][j])
				if weight > d:
					means[ind] = weight
		return means

	def get_dist_prob(self, point, means):
		distances = np.zeros(means.size)
		probabilities = np.zeros(means.size)
		
		distances[:] = abs(point - means[:])
		#probabilities = 1.0/distances[:]
		probabilities = distances[:]/np.sum(distances)
		return distances, probabilities
				
def main():
	"""
	"""
	alg = Kmeans()
	print "Please enter in values for k [0, N]: "
	k = int(raw_input())
	print "please enter a value for the thresh [0.0 1.0]: "
	d = float(raw_input())
	kmeans = alg.get_kmeans(k,d)
	print "The kmeans is" + str(kmeans) 

if __name__=="__main__":
	main()