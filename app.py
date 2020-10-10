import pygame
from pygame import display,event

pygame.init()

pygame.display.set_caption("Memory Game")
screen=pygame.display.set_mode((600,600))
status=True
x=0 
y=0
while status==True:
    pygame.time.delay(40)
    events=event.get()
    for curr_event in events:
        if curr_event.type==pygame.QUIT:
            status= False
        if curr_event.type==pygame.KEYDOWN: # for keyboard 
            if curr_event.key==K_ESCAPE:
             status=False         


    pygame.display.update()
print("GAME END")

