import re
format=re.compile(r'(91)-(\d\d\d\d\d-\d\d\d\d\d)')
c=input("Enter a num")
if(format.search(c)):
	print("Ah! found")
	print("Will make a call to"+str(c))
	print("Calling....")
	delay(3)
	
else:
	
	 
		
	print("Crap!! not found")
	print("Cannot' make a call")
