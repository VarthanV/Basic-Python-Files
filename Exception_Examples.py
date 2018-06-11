def count(a):

        try:
             with open(a) as files:
                lines=files.read()
                print("Success")
        
            
        except FileNotFoundError:
                pass  
        else:
             count=lines.split()
             c= len(lines) 
             print(c)   
count('Guests.txt')  


while (True):
        a=input("enter num \t")
        b=input("enter num \t")
        try:
            c=int(a)+int(b)
        except ValueError:
            pass
        else:
            print(c)
            break   
import json
num=[1,2,3,4,5,6]
fil='num.json'
with open(fil,'w')  as a:
    json.dump(num,a)
result={'1234':100,'1733':10}
a=input("enter reg no")
for reg_No,marks in result.items():
    if(a == reg_No):
        print(reg_No+"scored"+str(marks))
        
        break
else:
        print(a+"is not available")    

   
    

