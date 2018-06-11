class Die():
    def __init__(self,sides=6):
        self.sides=6
    def roll_die(self) :
        from random import randint
        for i in range(1,11):
            x=randint(1,self.sides)
            print(x)

        
        
a=Die()
a.roll_die()
b=Die()
b.roll_die()