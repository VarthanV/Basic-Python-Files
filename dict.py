new={'jen':'c', 'bob':'Python','joe':'java'}
for name,lan in new.items():
	print(name.title()+ "likes"+lan)
if(new['jen']=='c'):
		print('True')
else:
	print("False")
n={'jen':[20,163,'introvert'],'joe':[13,152,'extrovert']}
for name ,details in n.items():
	print(name.title() +"   "+ "is")
	for detail in details:
		print(detail)
age={'hari':19,'pavaan':20}
if(age['hari']==19):
	age['pavan']=23
	print(age)
else:
	print("Fail")
print("This code is used to find divisibility")
def div (a):

		
		for i in range(1,101):
	
			if(a%i==0):
					print(str(a)+"is divisible by"+str(i))
					
			else:
					print(str(a)+"is not divisible"+str(i))	
print(div(3))
mill=[i for i in range(0,10000001)]
print(sum(mill))
c=sum(mill)
times=0
while(int(c)>3):
	print("Loop works")
	times=0+1
	resp=input("enter q to exit")
	if(resp=='q'):
		break
	else:
		continue	
		
		
	
	

	


		

	
		

		 


		

