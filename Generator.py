
a=(90,20,30)
def combo():
    for j in range(100):
        for k in range(100):
            for l in range(100):
                yield(j,k,l)
for (j,k,l )in combo():
    if (j,k,l)==a:
        print("Found {}".format((j,k,l)))
        break
    print(j,k,l)    
    
def Picnic(dic,l,r):
	print("Picnic".center(l+r,'-'))
	for k,v in dic.items():
		print(k.ljust(l,'.')+str(v).rjust(r))
dic={'Choclates':4,'Meals':15,'Paneer':13}
Picnic(dic,15,20)
while True:
	print("Enter your age")
	age=input()
	if age.isdecimal():
		break
	print('enter')
	
