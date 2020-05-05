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
tuyau0= pygame.image.load("tuyau0.png").convert_alpha()
tuyau1= pygame.image.load("tuyau1.png").convert_alpha()


def msgfin():
    chaine="Game over"
    font=pygame.font.SysFont("Lobster",250,bold=False,italic=False)
    text=font.render(chaine,1,(255,50,50))
    fenetre.blit(text,(100,110))

def msgrejouer():
    chaine='Pour rejouer appuyer sur "R"'
    font=pygame.font.SysFont("Lobster",100,bold=False,italic=False)
    text=font.render(chaine,1,(255,180,10))
    fenetre.blit(text,(100,500))

def msgscoremax(scoremax,points):
    if scoremax<points :
        scoremax=points
    chaine= 'Ton meilleur score est de : '+ str(scoremax)
    font=pygame.font.SysFont("Lobster",100,bold=False,italic=False)
    text=font.render(chaine,1,(255,90,40))
    fenetre.blit(text,(100,300))

def gameover(scoremax,points) :
    songameover = pygame.mixer.Sound("gameover.ogg")
    songameover.play()
    msgfin()
    msgrejouer()
    msgscoremax(scoremax,points)
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

def tuyaux(xtuyau,ytuyau,espacement):
    fenetre.blit(tuyau1,(xtuyau,ytuyau))
    ytuyau0=ytuyau+400+espacement
    fenetre.blit(tuyau0,(xtuyau,ytuyau0))

def score(points):
    chaine= str(points)
    font=pygame.font.SysFont("Lobster",100,bold=False,italic=False)
    text=font.render(chaine,1,(100,10,200))
    fenetre.blit(text,(580,50))

def msgargent():
    chaine= 'appuyer sur "E" pour prendre la pièce et gagner 5  points'
    font=pygame.font.SysFont("Lobster",50,bold=False,italic=False)
    text=font.render(chaine,1,(50,100,218))
    fenetre.blit(text,(120,10))

def jeux():
    temps.tick(60)
    sonsucces = pygame.mixer.Sound("succes.ogg")
    sonpiece = pygame.mixer.Sound("piece.ogg")
    xtuyau=largeur
    ytuyau= randint(-490,-220)
    espacement= 400
    vitesse= 2
    scoremax=0
    points=0
    xpiece=randint(4000,7000)

    perso= pygame.image.load("perso.png").convert_alpha()
    perso.set_colorkey((255,255,255))
    perso=pygame.transform.scale(perso,(80,60))
    persorect= perso.get_rect()
    persorect= persorect.move(100,100)

    piece = pygame.image.load("piece.png").convert_alpha()
    piece =pygame.transform.scale(piece,(70,70))
    piecerect= piece.get_rect()
    piecerect= piecerect.move(xpiece,300)

    fenetre.blit(fond,(0,0))
    fenetre.blit(perso, persorect)
    fenetre.blit(piece,piecerect)

    pygame.display.flip()
    continuer=1

    while continuer:
        for event in pygame.event.get():
            if event.type==QUIT:
                continuer=0
            if event.type==KEYDOWN :
                if event.key==K_SPACE :
                    persorect= persorect.move(0,-100)
        persorect= persorect.move(0,1)
        piecerect = piecerect.move(-2,0)
        fenetre.blit(fond,(0,0))
        fenetre.blit(perso,persorect)
        fenetre.blit(piece,piecerect)
        score(points)
        msgargent()

        if persorect.bottom>600:
            gameover(scoremax,points)
        if persorect.top<0:
            gameover(scoremax,points)
        if persorect.right==1200:
            gameover(scoremax,points)

        tuyaux(xtuyau,ytuyau,espacement)
        xtuyau -= vitesse
        if xtuyau< persorect.x+50< xtuyau+50 :
            if 0 <persorect.y< ytuyau+500:
                gameover(scoremax,points)
            if ytuyau+espacement+350 < persorect.y < 600 :
                gameover(scoremax,points)
        if xtuyau == persorect.x :
            sonsucces.play()
            points+=1
        if xtuyau+50 ==0:
            xtuyau = largeur
            ytuyau= randint(-490,-220)

        if points== 20:
            espacement= 350
        if points== 40:
            espacement= 300
        if points== 60:
            espacement= 250
        if points== 90:
            espacement= 220


        collision=[piecerect]
        if persorect.collidelist(collision) :
            points +=0
        else :
            if event.type==KEYDOWN :
                if event.key==K_e :
                    sonpiece.play()
                    points+=5
                    piecerect=piecerect.move(xpiece,0)
        if piecerect.x ==0:
            piecerect= piecerect.move(xpiece,0)

        pygame.display.flip()

try :
    jeux()
except :
        print
finally:
    pygame.quit()
    exit()
