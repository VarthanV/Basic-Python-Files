name=input("Enter your name")
age=int(input("Enter your age"))
if(age<3):
    print(name.title()+",you are free to go")
elif(age<=12):
        print(name.title()+"ticket costs 10 dollars")
elif(age>12):
        print(name.title()+"ticket costs 15 dollars")
    
    
print("Enjoy the movie")   
top=""
tomato=False
while(top!='q'):
    top=input("enter a topping")
    if(top=='tomato'):
        continue
    else:
        print(top.title()+"is added") 
        break
active=True
while(active!=True):
    print("no")
else:    
        print("execute")    
confirmed=[]
unconfirmed=['Harish','Selva','Gokul','Rahul','Rahul']
new=[]
while(unconfirmed):
     c=unconfirmed.pop()
     confirmed.append(c)

for user in confirmed:

     print(user.title()+"welcome")     

while('Rahul'in confirmed):
    confirmed.remove('Rahul')
confirmed.sort(reverse=True)
print(confirmed)    