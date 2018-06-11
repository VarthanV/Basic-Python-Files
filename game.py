import pygame 
from pygame import game_display
import random
width=800
height=600
white=(255,255,255)
blue=(0,0,255)

game_display=pygame.game_displaylay.set_mode((width,height))
white=(255,255,255)
blue=(0,0,255)
pygame.game_displaylay.set_caption("Bounce")
clock=pygame.time.Clock()


class Bounce:
    def __init__(self,color):
        self.color=color
        self.x=random.randrange(0,width)
        self.y=random.randrange(0,height)
        self.size=random.randrange(4,8)
    def move(self):
        self.x_modified=(-1,2)
        self.y_modified=(-1,2)
        if self.x<0:
             self.x=0 
        elif self.x >width:
            self.c=width


        if(self.y <0):
            self.y=0 
        elif self.y>height:
            self.y=height
    def draw(self,bounce):
        game_display.fill(white)
        pygame.draw.circle(game_display,bounce.color,[bounce.x,bounce.y],bounce.size)
        pygame.game_displaylay.update()
        bounce.move()
    def main():
        bounce=Bounce(blue)
        while(True):
            for event in pygame.events.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
        draw(bounce)
        clock.tick(60) 
if __name__ == '__main___':
    main()                   




  
