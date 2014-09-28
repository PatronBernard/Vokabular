import random,numpy
import matplotlib.pyplot as plt

#This is a class that allows you to start off with a uniform distribution for any discrete amount of elements, modify
#said distribution and get random elements from that distribution.

class DynamicRNG:

	def __init__(self):
		self.PDF=[1]
		pass

	def getCDF(self):
		CDF=[sum(self.PDF[:i]) for i in range(1,len(self.PDF))]
		#The last element of the CDF should be 1, so we do this manually to avoid floating-point errors.
		return CDF+[1]
	
	def normalize(self):
		self.PDF=[x/sum(self.PDF) for x in self.PDF]

	def addElements(self,N):
		for i in range(N): self.PDF.append(max(self.PDF))
		self.normalize()

	def increaseRelativeChance(self,index,factor):
		self.PDF[index]=self.PDF[index]*factor
		self.normalize()

	def getRandomIndex(self):
		#Inverse transform technique to get a random integer according to the PDF
		u=random.uniform(0,1)
		return min(range(len(self.getCDF())), key=lambda i: abs(self.getCDF()[i]-u))

def main():
	#Do some testing
	dRNG=DynamicRNG()
	dRNG.normalize()
	dRNG.addElements(50)
	print(dRNG.PDF)
	dRNG.increaseRelativeChance(25,10)
	print(dRNG.getCDF())
	sample=[]
	for i in range(1000):
		sample.append(dRNG.getRandomIndex())

	n, bins, patches = plt.hist(sample, 51, normed=True, facecolor='green', alpha=0.75)
	plt.show()

if __name__=='__main__':
	main()