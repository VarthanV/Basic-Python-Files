class Car():
	def __init__(self,name,model,year,mileage):
		self.name=name 
		self.model=model
		self.year=year
		self.mileage=mileage
	def describe(self):
		print(self.name)
		print(self.model)
		print(self.year)
	def get( self):
			a=self.mileage
			b=self.name 
			if(a>23):
				print(b+"is a good car with good mileage")
			elif(a>20):
					print(b+"is nice")	
			else:
					print("See another car homie")
	def new_mileage(self,new):
			self.mileage=new
			self.get()
class battery():
	def __init__(self,size=30):
		self.size=30
		def bat(self):
			print("This car has"+str(self.battery)+"and can run upto 5 hours")
class electric(Car):
	def __init__(self,name,model,year,mileage):
		super().__init__(name,model,year,mileage)
		self.size=battery()
	
	def describe(self):
		super().describe()	

	

	
		
 
