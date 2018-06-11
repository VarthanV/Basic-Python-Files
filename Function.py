def greet(user):
	 print(user.title()+''+"Welcome home")

	
users=['Rajaram','Pavan','Harish','Gokul','Selva','Bala']
for user in users:
	(greet(user))
def message(name):
    print(name.title()+''+"you are nice")
for user in users:
     message(user)
results={}
f=True
while(f):
     name=input("Enter your names")
     place=input("Which place you like to go")
     resp=input("Enter 'q' to quit or y to continue adding people")

     results[name]=place
     if( resp=='q'):
	        f=False
     elif(resp=='y'):
         continue       
else:
	for n,p in results.items():
	    print(n .title() +  "liked to goto"+ p)
print(results) 
 
def details(name,age,height):
    print("Your name is"+ name)
    print("Your age is"+ str(age))
    print("Your height is "+str(height))

for user in users:
    details(user,12,132)    
    

	 
	    
    
    
	
	

	
		
	
