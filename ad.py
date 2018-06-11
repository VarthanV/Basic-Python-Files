from user import User

class Admin(User):
	def __init__(self,name,age,height,attempts):	
			super().__init__(name,age,height,attempts)
	def privileges(self):
		if(self.name=='admin'):
			priv=['Can add','can edit','can post']
			for prop in priv:
				print(prop)
		else:
			print("no homie no previliges for u")				
