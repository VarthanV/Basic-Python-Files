toppings=['mushroom','nachos','sweer corn']
a=input("enter a topping")
if(a in toppings):
    print(a.title()+"is available please wait a second")
else:
    print(a.title()+"is not available enter diffferent")
    input()  
            