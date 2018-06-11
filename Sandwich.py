finished_sandwich=[]
sandwich_orders=['pastrami','Pepperoni','Mushroom','Paneer','pastrami','pastrami']

while(sandwich_orders):
    new=sandwich_orders.pop()
    name=finished_sandwich.append(new)
    print(new.title()+"sandwich is ready")
sandwich_orders=['pastrami','Pepperoni','Mushroom','Paneer','pastrami','pastrami']

count=0
while('pastrami' in sandwich_orders):
	sandwich_orders.remove('pastrami')
	count=count+1
print(str(count)+"has been removed")
print(sandwich_orders)	
	    
        
