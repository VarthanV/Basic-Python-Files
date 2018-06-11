class  Man:
	def __init__(self,name,age,height):
		self.name=name
		self.age=age
		self.height=height
		
		
	def name(self):
		print(self.name.title())
		
		
	def age(self):
		print(str(self.age))
		
		
	def height(self):
		print(self.height)
		
		
	def s(self):
		print(self)
		
			
a=Man('Tom',11,133)

print(a.name)


print(a.age)

print(a.height)

					
