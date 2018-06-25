import car
import user
a=car.Car('Audi','A4',2016,33)
a.describe()
print("It  works")
a.get()
a.new_mileage(11)
b=car.electric("Tesla","Roadster",2017,55)
b.describe()

a1=user.User("Vishnu",17,163,5.5)
b1=user.Admin("admin",17,163,5.5)
b1.privileges()
bin(3)
print(bin(100))
