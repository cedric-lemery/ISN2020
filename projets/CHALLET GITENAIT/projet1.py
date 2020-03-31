#tristan
#audric

#Flappy bird

import pygame
import traceback
import random
import time
from pygame.locals import *
pygame.init()




def jeux():
    largeur= 1200
    hauteur= 600
    fenetre= pygame.display.set_mode((largeur,hauteur))
    pygame.display.set_caption("Flappy Bird")
    fond=pygame.image.load("fond.png").convert()
    fond=pygame.transform.scale(fond,(largeur,hauteur))
    fenetre.blit(fond,(0,0))
    perso= pygame.image.load("perso.png").convert_alpha()
    perso=pygame.transform.scale(perso,(100,100))
    persorect= perso.get_rect()
    persorect= persorect.move(100,200)
    fenetre.blit(perso, persorect)
    pygame.display.flip()
    continuer=1
    while continuer:
        for event in pygame.event.get():
            if event.type==QUIT:
                continuer=0
            if event.type==KEYDOWN :
                if event.key==K_SPACE :
                    persorect= persorect.move(0,-200)
        persorect= persorect.move(0,1)
        fenetre.blit(fond,(0,0))
        if persorect.bottom>600:

            chaine="Game over"
            continuer=0
            font=pygame.font.SysFont("Lobster",250,bold=False,italic=False)
            text=font.render(chaine,1,(255,100,100))
            fenetre.blit(text,(100,110))
            pygame.time.wait
        if persorect.bottom<0:
            chaine="Game over"
            continuer=0
            font=pygame.font.SysFont("Lobster",250,bold=False,italic=False)
            text=font.render(chaine,1,(255,100,100))
            fenetre.blit(text,(100,110))
            pygame.time.wait



        fenetre.blit(perso,persorect)
        pygame.display.flip()


try :
    jouer=True
    while(jouer):
        jeux()
        rejouer=input("voulez-vous rejouer (oui/non)?")
        if rejouer==non:
            jouer=False

except :
    traceback.print_exc()
finally:
    pygame.quit()
    exit()