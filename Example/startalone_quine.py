#!/usr/bin/python
import math

#Minterm Maxterm class
#Author: Pongsakorn Sommalai
#Detail: Use for management logic term
class term:
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
	def setTerm(self, term=[], type="", bit=0):
		if type=="maxterm":
			self.term = term.sort()
			self.type = type
		else:
			self.term = term.sort()
			self.type = "minterm"
	
	def getBit(self):
		return self.bit
	
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

#Minterm Maxterm class
#Author: Pongsakorn Sommalai
#Detail: Use for abbreviated offseason a logic term
class quine:
	#constucter
	def __init__(self, objterm=None, minterm=[], bit=0):
		if objterm!=None:
			self.term=objterm
		else:
			self.term=term(minterm, "minterm", bit)

	#check 1 bit not match
	def __check1bit(self, a, b):
		c = 0
		for i in range(0, self.term.getBit()):
			if a[i]!=b[i]:
				c = c+1
		
		if c==1:
			return True
		
		return False
	
	#match group
	def __matchGroup(self, group1, group2):
		newGroup=[]
		ngroup1=[]
		ngroup2=[]
		for term1 in group1:
			for term2 in group2:
				if self.__check1bit(term1, term2):
					newterm = ""
					for i in range(0, self.term.getBit()):
						if term1[i]!=term2[i]:
							newterm = newterm+"-"
						else:
							newterm = newterm+term1[i]
					
					newterm = newterm+"-"
					if term1[:-1]+'+' not in ngroup1:
						ngroup1.append(term1[:-1]+'+')
					if term2[:-1]+'+' not in ngroup2:
						ngroup2.append(term2[:-1]+'+')
					
					if newterm not in newGroup:
						newGroup.append(newterm)
		
		for term1 in group1:
			if term1[:-1]+'+' not in ngroup1:
				ngroup1.append(term1)
		
		for term2 in group2:
			if term2[:-1]+'+' not in ngroup2:
				ngroup2.append(term2)
		
		return [ngroup1,ngroup2,newGroup]
	
	#Set term
	def setTerm(self, objterm=None, minterm=[], bit=0):
		if objterm==None:
			self.term=objterm
		else:
			self.term=term(minterm, "minterm", bit)
	
	#Sort group
	def sortGroup(self, terms):
		out = []
		for i in range(0, terms.getBit()+1):
			out.append([]) 
		for term in terms.getMintermByBinary():
			out[term.count('1')].append(term+"-")
		c=0
		for o in out:
			if o==[]:
				del out[c]
			
			c = c+1

		return out
	
	#Start quine return list of logic term
	def start(self):
		groups = self.sortGroup(self.term)
		c = 99
		newgroups = []
		ng = []
		end = []
		while c==1 or c==99:
			ng = []
			if c==99:
				newgroups = groups

			c=0
			for i in range (0,len(newgroups)-1):
				result = self.__matchGroup(newgroups[i], newgroups[i+1])
				newgroups[i+1] = result[1]
				end.append(result[0])
				if result[2]!=[]:
					c=1
					ng.append(result[2])
			
			if len(newgroups)-1==0:
				end.append(newgroups[i])
			elif c==0:
				end.append(result[1])
				
			newgroups = ng
		
		merge = []
		for e in end:
			merge = merge+e
		
		out = []
		for m in merge:
			if m[-1]=='-':
				out.append(m[:-1])
				
		return out
	
	#Change list of term to string term
	def getTermByAlphabet(self, term):
		alfa = "abcdefghijklmnopqrstuvwxyz"
		alfa = list(alfa)
		
		out = ""
		for i in term:
			c=0
			for j in list(i):
				if j == "0":
					out = out+alfa[c]+"\'"
				elif j == "-":
					c = c+1
					continue
				else:
					out = out+alfa[c]
				c = c+1
			
			out = out+'+'
		return out[:-1]
		
#Main
####################Input###########################
bit = raw_input("Enter the number of variables> ")
sminterm = raw_input("Enter the set of minterms> ")
bit = int(bit)
sminterm = sminterm.split(',')
minterm = []
for m in sminterm:
	minterm.append(int(m))
####################################################

####################Procress#########################
objTerm = term(term=minterm, type="minterm", bit=bit)
objQuine = quine(objterm=objTerm)
result = objQuine.start()
#####################################################

#############################Output###################################
print "\nOutput the function is > "+objQuine.getTermByAlphabet(result)
######################################################################