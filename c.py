def make():
    
    c=input("Enter the dir name")
    import os
    res=input("It is here"+os.getcwd()+"currently,if you ant really")
    if(res=='y'or 'yes'):


         os.chdir("/home/vishnu/Desktop")

         os.makedirs(os.path.join("/home/vishnu/Desktop",c))
         print("dir created")
    else:
        print("Not possible")
make()