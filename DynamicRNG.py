import random

class DynamicRNG:

	def __init__(self):
		self.PDF=[1]
		pass

	def getCDF(self):
		return sum(self.PDF)
	
	def normalize(self):
		self.PDF=[x/self.getCDF() for x in self.PDF]

	def addElement(self):
		self.PDF.append(max(self.PDF))
		self.normalize()

dRNG=DynamicRNG()
dRNG.normalize()
print(dRNG.getCDF())