#tristan
#audric

#Flappy bird

import pygame
import traceback
from random import randint
import time
from pygame.locals import *

pygame.init()


temps = pygame.time.Clock()
largeur= 1200
hauteur= 600
fenetre= pygame.display.set_mode((largeur,hauteur))
pygame.display.set_caption("Flappy Bird")
fond=pygame.image.load("fond.png").convert()
fond=pygame.transform.scale(fond,(largeur,hauteur))




def msgfin():
    chaine="Game over"
    font=pygame.font.SysFont("Lobster",250,bold=False,italic=False)
    text=font.render(chaine,1,(255,100,100))
    fenetre.blit(text,(100,110))

def msgrejouer():
    chaine="Pour rejouer appuyer sur 'r'"
    font=pygame.font.SysFont("Lobster",100,bold=False,italic=False)
    text=font.render(chaine,1,(255,180,100))
    fenetre.blit(text,(100,400))

def gameover() :
    msgfin()
    msgrejouer()
    pygame.display.flip()
    while choix() == None:
        temps.tick
    jeux()

def choix():
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN :
            if event.key==K_r :
                return event.key
        return None



def jeux():
    y=0
    perso= pygame.image.load("perso.png").convert_alpha()
    perso.set_colorkey((255,255,255))
    perso=pygame.transform.scale(perso,(80,80))
    persorect= perso.get_rect()
    persorect= persorect.move(100,100)
    tuyau0= pygame.image.load("tuyau0.png").convert_alpha()
    tuyau0rect= tuyau0.get_rect()
    tuyau0rect= tuyau0rect.move(600,500)
    tuyau1= pygame.image.load("tuyau1.png").convert_alpha()
    tuyau1rect= tuyau1.get_rect()
    tuyau1rect= tuyau1rect.move(600,-170)
    tuyau3= pygame.image.load("tuyau0.png").convert_alpha()
    tuyau3rect= tuyau3.get_rect()
    tuyau3rect= tuyau3rect.move(1200,500)
    tuyau4= pygame.image.load("tuyau1.png").convert_alpha()
    tuyau4rect= tuyau4.get_rect()
    tuyau4rect= tuyau4rect.move(1200,-170)
    collisions= [tuyau0rect,tuyau1rect,tuyau3rect,tuyau4rect]
    fenetre.blit(fond,(0,0))
    fenetre.blit(perso, persorect)
    fenetre.blit(tuyau0, tuyau0rect)
    fenetre.blit(tuyau1, tuyau1rect)
    fenetre.blit(tuyau3, tuyau3rect)
    fenetre.blit(tuyau4, tuyau4rect)

    pygame.display.flip()
    continuer=1

    while continuer:
        for event in pygame.event.get():
            if event.type==QUIT:
                continuer=0
            if event.type==KEYDOWN :
                if event.key==K_SPACE :
                    persorect= persorect.move(0,-150)

        persorect= persorect.move(0,1)
        tuyau0rect= tuyau0rect.move(-1,0)
        tuyau1rect= tuyau1rect.move(-1,0)
        tuyau3rect= tuyau3rect.move(-1,0)
        tuyau4rect= tuyau4rect.move(-1,0)
        collisions= [tuyau0rect,tuyau1rect,tuyau3rect,tuyau4rect]
        fenetre.blit(fond,(0,0))
        fenetre.blit(perso,persorect)
        fenetre.blit(tuyau0, tuyau0rect)
        fenetre.blit(tuyau1, tuyau1rect)
        fenetre.blit(tuyau3, tuyau3rect)
        fenetre.blit(tuyau4, tuyau4rect)

        if persorect.collidelist(collisions)==0:
            gameover()
        if persorect.collidelist(collisions)==1:
            gameover()
        if persorect.collidelist(collisions)==2:
            gameover()
        if persorect.collidelist(collisions)==3:
            gameover()

        if persorect.bottom>600:
            gameover()
        if persorect.top<0:
            gameover()
        if persorect.right==1200:
            gameover()

        pygame.display.flip()

        if tuyau0rect.right ==0:
            tuyau0rect= tuyau0rect.move(1200,0)
            tuyau1rect= tuyau1rect.move(1200,0)


        if tuyau3rect.right ==0 :
            tuyau3rect= tuyau3rect.move(1200,0)
            tuyau4rect= tuyau4rect.move(1200,0)




try :
    jeux()



except :
    traceback.print_exc()
finally:
    pygame.quit()
    exit()
