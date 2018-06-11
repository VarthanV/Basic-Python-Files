resp={}
active=True
while(active):
    name=input("What is your name")
    age=int(input("How old are you?"))
    resp[name]=age
    dec=input("Do you want to add another member")
    if (dec=='quit'):
        active=False
print(resp) 
for n,a in resp.items():
    print("Age of"+ n+"is"+str(a))

          