class Restaurant:
	def __init__(self,name,cuisine,served):
		
		self.name=name 
		self.cuisine=cuisine
		self.served=10
	def des(self):
			print("Welcome our restaurant name is"+self.name.title())
			print("The cuisine we are special is"+self.cuisine.title())
			print("We serve"+str(self.served))
			return 
	def alter(self,new):
		self.served=new
		print("we have updated our database")
		self.des()
	def increment(self,val):
		self.served+=val
		print("New base")
		self.des()
		
					
a=Restaurant('annapoorna','indian',120)
a.des()
a.alter(130)
a.increment(20)
			
		
