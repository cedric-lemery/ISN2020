import pygame
import os

from enemies import *

class Jeu:
    def __init__(self):
        self.width = 1100
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemy = []
        self.tour = []
        self.vie = 10
        self.argent = 100
        self.bg = pygame.image.load(os.path.join("assets", "bg.png"))  #  analogue à pygame.image.load('assets\bg.png')
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))


    def run(self) :
        run = True
        clock = pygame.time.Clock()
        compteur=0
        enemy1 = Enemy(10,10,5,5,1,1)
        while run:
            enemy1.draw(g.win)
##            clock.tick(60)
            compteur+=1
            if(compteur==100):
                run=False
            for event in pygame.event.get() :
                if event.type == pygame.QUIT:
                    run  = False
            self.draw()
        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))
        pygame.display.update()

g = Jeu()
g.run()

