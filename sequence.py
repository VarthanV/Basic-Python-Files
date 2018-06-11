a=[1,9,11,14]
first=a[0]
c=len(a)
d=a[c-1]-a[c-2]
if(d==a[c-3]-a[c-4]):
	print(str(d)+" is the common difference of the sequence")
else:
	print("Not")	
	
