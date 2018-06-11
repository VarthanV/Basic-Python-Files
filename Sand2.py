def orders(**sandwich):
	sand={}
	for category,toppings in sandwich.items():
		sand[category]=toppings
		return sand 
o=orders(cheese='extra',toppings='mushroom')
print(o)
def makepizza(size,*toppings):
	print("The "+str(size)+"inch pizza is prepared with following toppings")
	for topping in toppings:
		print(topping)
	

				
makepizza(16,'cheese','pepperoni','mushroom')	
makepizza(200,'macroni','paneer','onion')
	
def f():
	s='Hi'
	print(s)
s='Hello'
f()
from functools import partial
def add(a,b,c):
	return 100*a+10*b+1*c
s= partial(add,3,1)
print(s(5))		
def recieve(*num):
	
		print(num)
		for nums in num:
			print(nums)
recieve(3,4,5,6,7)
recieve(100,200,300,500,50,50)
s=100.555
print(str(int(s))+"is good")


m='Thug'
print("The list is ",end='')
print(list(m))
print("The set is",end='')
print(set(m))
print(set(sorted(m)))

