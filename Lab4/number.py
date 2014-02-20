class Integer(object):
	def __init__(self,y,Positive):
		self.y=y
		self.Positive=Positive
	def display(self):
		if(self.Positive and self.y>0):
			print self.y
		else:
			print self.y*-1
	def returnY(self):
		return self.y
	def add(self,y2):
		return Integer(self.y+y2.returnY(),True)
	def subtract(self,y2):
		return Integer(self.y-y2.returnY(),True)
	def multiply(self,y2):
		return Integer(self.y*y2.returnY(),True)
	def divide(self,y2):
		return Integer(self.y/y2.returnY(),True)
	
class NegativeInteger(Integer):
	def __init__(self,y):
		super(NegativeInteger,self).__init__(y,False)
	def display(self):
		Integer.display(self)
		#print "This is an object of the Negative Integer class"
	
		

if __name__=="__main__":
	#print "Michele"
	#test=Integer(21,False)
	#test.display()
	#test2=NegativeInteger(60)
	#test2.display()
	#L=[test,test2]
	#for i in L:
		#i.display()
	#print "give a positive number "
	#test=Integer(input(),False)
	#print "and after this a negative one!"
	#test2=NegativeInteger(input())
	L=[]
	
	print "How many numbers do you want to create?"
	for i in range (0,input()):
		print "P or N number?"
		x=raw_input()
		if (x=="P"):
			print "Enter the number:"
			L.append(Integer(input(),True))
		elif (x=="N"):	
			print "Enter the number:"
			L.append(NegativeInteger(input()))
	for i in L:
		i.display()
		
	
	
	
		


