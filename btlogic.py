#!/usr/bin/python
import math

#Minterm Maxterm class
class logicterm:
	def __init__(self, term=[], type="", bit=0):
		if type=="maxterm":
			self.term = term
			self.type = type
		else:
			self.term = term
			self.type = "minterm"
		
		self.bit=bit
		self.term.sort()
		
	def __m2m(self):
		out = []
		if self.bit==0:
			return []
		
		for i in range(0,int(math.pow(2,self.bit))):
			if i not in self.term:
				out.append(i)
		
		return out
	
	def __dec2bin(self, dec,bit):
		return ('0'*(bit-len(bin(dec)[2:])))+bin(dec)[2:]	
		
	#Set variable
	def setTerm(self, term, type, bit):
		if type=="maxterm":
			self.term = term.sort()
			self.type = type
		else:
			self.term = term.sort()
			self.type = "minterm"
	
	#Return minterm by list
	def getMinterm(self):
		if self.type == "minterm":
			return self.term
		else:
			return self.__m2m()
	
	#Return maxterm by list
	def getMaxterm(self):
		if self.type == "maxterm":
			return self.term
		else:
			return self.__m2m()
	
	#Return minterm by string
	def getMintermByAlphabet(self):
		alfa = "abcdefghijklmnopqrstuvwxyz"
		alfa = list(alfa)
		
		if self.type == "maxterm":
			term = self.__m2m()
		else:
			term = self.term
		
		out = ""
		for i in term:
			binterm=self.__dec2bin(i, self.bit)
			c=0
			for j in list(binterm):
				if j == "0":
					out = out+alfa[c]+"\'"
				else:
					out = out+alfa[c]
				c = c+1
			
			out = out+'+'
		return out[:-1]
	
	#Return maxterm by string
	def getMaxtermByAlphabet(self):
		alfa = "abcdefghijklmnopqrstuvwxyz"
		alfa = list(alfa)
		
		if self.type == "minterm":
			term = self.__m2m()
		else:
			term = self.term
		
		out = ""
		for i in term:
			out = out+'('
			binterm=self.__dec2bin(i, self.bit)
			c=0
			for j in list(binterm):
				if j == "1":
					out = out+alfa[c]+"\'"
				else:
					out = out+alfa[c]
				
				out = out+'+'
				c = c+1
			
			out = out[:-1]+')'
		return out
	
	#Return minterm in binary
	def getMintermByBinary(self):
		alfa = "abcdefghijklmnopqrstuvwxyz"
		alfa = list(alfa)
		
		if self.type == "maxterm":
			term = self.__m2m()
		else:
			term = self.term
		
		out = []
		for i in term:
			out.append(self.__dec2bin(i, self.bit))
			
		return out
	
	#Return maxterm in binary
	def getMaxtermByBinary(self):
		alfa = "abcdefghijklmnopqrstuvwxyz"
		alfa = list(alfa)
		
		if self.type == "minterm":
			term = self.__m2m()
		else:
			term = self.term
		
		out = []
		for i in term:
			out.append(self.__dec2bin(i, self.bit))
			
		return out
	
	#Set to not term
	def opposite(self):
		self.term=self.__m2m()


'''class quina:
	def __init__(self, term=None){
		self.term=term
		
	def setTerm(self, term) {
		self.term=term'''
	

		