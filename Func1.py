def Tshirt(size,message):
    print("The size of the T-shirt wll be"+str(size)) #Prints the size
    
    print("The message printed will be"+message)  #Prints the name
Tshirt(13,'I am a Programmer') 
def large(size=13,message='I love python'):
    print(size)
    print(message)
large()    
def describe_city(city,country='India'):
    print(city+"is in"+ country  )
describe_city('Coimbatore')
describe_city('Georgia','USA')
def city_country(city,country):
    format=print(""+city+","+""+country)
    return format
city_country('nile','egypt')  
survey={}
track_count=0

def artists(artist,song):
    survey[artist]=song


artists('Anirudh','Aako')
artists('Ed sheeran','Shape of you')
artists('Justin','Baby')  
for track in survey:
    track_count=track_count+1
print("The number of tracks are"+str(track_count))       
for name,songs in survey.items():
    print(name.title()+"created"+songs)

     