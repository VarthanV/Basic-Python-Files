magicians=['Harry','Saketh','Siddarth','Mowli']
def show(magicians):
    print("The great magicians are")
    for magician in magicians:
		print(magician.title())
       
       
mag=magicians[:]
def makegreat(mag):
    for magician in mag:
       (mag.append("Great"+magician))
       
       

        
print(magicians)
print(mag)
show(magicians)
makegreat(mag)
print(makegreat(mag))

