
while(True):
   c= input("Enter the guest name \n")
   if(c=='q'or c=='quit'):
       break 

   else:
       file='Guest.txt'
       with open(file,'a') as text:
           text.write(c + "\n")

