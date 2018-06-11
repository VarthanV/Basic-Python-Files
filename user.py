class User:
	def __init__(self,name,age,height,attempts):
		self.name=name 
		self.age=age
		self.height=height
		self.attempts=attempts
	def describe (self):
		print("My name is "+self.name)
		print("My age is"+str(self.age))
class Admin(User):
	def __init__(self,name,age,height,attempts):	
			super().__init__(name,age,height,attempts)
	def privileges(self):
		if(self.name=='admin'):
			priv=['Can add','can edit','can post']
			for prop in priv:
				print(prop)
		else:
			print("no homie")
a=Admin('admin',17,170,3)							
a.privileges()

