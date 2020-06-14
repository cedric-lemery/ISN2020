
import pygame
from pygame.locals import*

pygame.init()
screen= pygame.display.set_mode((1600,1200),0,32)
background= pygame.image.load("imageMtest.jpg").convert()

while True:
    screen.blit(background,(0,0))
    pygame.display.update()





