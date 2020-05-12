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
    text=font.render(chaine,1,(255,50,50))
    fenetre.blit(text,(130,110))

def msgrejouer():
    chaine='Pour rejouer appuyer sur "R"'
    chaine1= 'Pour retourner au menu principal appuyer sur "Echap"'
    font=pygame.font.SysFont("Lobster",60,bold=False,italic=False)
    text=font.render(chaine,1,(255,180,10))
    text1=font.render(chaine1,1,(255,180,10))
    fenetre.blit(text,(300,550))
    fenetre.blit(text1,(45,500))

def gameover(points) :
    songameover = pygame.mixer.Sound("gameover.ogg")
    songameover.play()
    msgfin()
    msgrejouer()
    msgscoremax(points)

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
            if event.key==K_ESCAPE :
                return lancement()
        return None

def score(points):
    chaine= str(points)
    font=pygame.font.SysFont("Lobster",100,bold=False,italic=False)
    text=font.render(chaine,1,(100,10,200))
    fenetre.blit(text,(580,50))

def msgscoremax(points) :
    fichier = open("datascore.rtf", "r")
    scoremax= int(fichier.read())
    if scoremax<points:
        scoremax=points
        fichier = open("datascore.rtf", "w")
        fichier.write(str(scoremax))
    chaine= 'votre meilleur score est : '+ str(scoremax)
    font=pygame.font.SysFont("Lobster",100,bold=False,italic=False)
    text=font.render(chaine,1,(220,50,10))
    fenetre.blit(text,(160,350))
    fichier.close()




def msgargent():
    chaine= 'prenez une piece pour gagner 5  points'
    font=pygame.font.SysFont("Lobster",50,bold=False,italic=False)
    text=font.render(chaine,1,(50,100,218))
    fenetre.blit(text,(250,10))

def jeux():
    temps.tick(30)
    sonsucces = pygame.mixer.Sound("succes.ogg")
    sonpiece = pygame.mixer.Sound("piece.ogg")
    xtuyau=largeur
    ytuyau= randint(-490,-220)
    espacement= 400
    vitesse= 2
    points=0
    xpiece=randint(4000,7000)
    ypiece= randint(20,500)

    perso= pygame.image.load("perso.png").convert_alpha()
    perso.set_colorkey((255,255,255))
    perso=pygame.transform.scale(perso,(80,60))
    persorect= perso.get_rect()
    persorect= persorect.move(100,100)

    piece = pygame.image.load("piece.png").convert_alpha()
    piece =pygame.transform.scale(piece,(70,70))
    piecerect= piece.get_rect()
    piecerect= piecerect.move(xpiece,ypiece)

    tuyau0= pygame.image.load("tuyau0.png").convert_alpha()
    tuyau0rect= tuyau0.get_rect()
    tuyau1= pygame.image.load("tuyau1.png").convert_alpha()
    tuyau1rect= tuyau1.get_rect()


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
            gameover(points)
        if persorect.top<0:
            gameover(points)
        if persorect.right==1200:
            gameover(points)

        tuyau0rect.x= xtuyau
        tuyau1rect.x= tuyau0rect.x
        tuyau1rect.y = ytuyau

        fenetre.blit(tuyau1,tuyau1rect)
        ytuyau0=ytuyau+400+espacement
        tuyau0rect.y=ytuyau0
        fenetre.blit(tuyau0,tuyau0rect)
        xtuyau -= vitesse

        collisiontuyau= [tuyau0rect,tuyau1rect]
        if persorect.collidelist(collisiontuyau)==0 :
            gameover(points)
        if persorect.collidelist(collisiontuyau)==1 :
            gameover(points)
        if tuyau0rect.x == persorect.x :
            sonsucces.play()
            points+=1
        if tuyau0rect.x +50 ==0:
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
            sonpiece.play()
            points+=5
            piecerect=piecerect.move(xpiece,0)
            piecerect.y =randint(20,550)
        if piecerect.x ==0:
            piecerect= piecerect.move(xpiece,0)
            piecerect.y= randint(20,550)

        pygame.display.flip()




def lancement():
    points=0
    commencer = 1
    fenetre.blit(fond,(0,0))
    chaine='- Appuyer sur "ESPACE" pour commencer et sauter'
    chaine1= '- Appuyer sur "SUPPR" pour réinitialiser votre meilleur score'
    chaine2= 'MENU PRINCIPAL'
    chaine3='- Appuyer sur "S" pour stopper la musique et "J" pour la jouer'
    chaine5= '- Appuyer sur "ENTRER" pour voir les informations'
    font=pygame.font.SysFont("Lobster",50,bold=False,italic=False)
    font2=pygame.font.SysFont("Lobster",150,bold=False,italic=False)
    text=font.render(chaine,1,(50,130,50))
    text1= font.render(chaine1,1,(50,130,50))
    text2= font2.render(chaine2,1,(10,20,200))
    text3=font.render(chaine3,1,(50,130,50))
    text5=font.render(chaine5,1,(50,130,50))
    fenetre.blit(text,(10,200))
    fenetre.blit(text1,(10,420))
    fenetre.blit(text2,(150,10))
    fenetre.blit(text3,(10,250))
    fenetre.blit(text5,(10,550))
    msgscoremax(points)
    pygame.display.flip()
    while commencer :
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==KEYDOWN :
                if event.key==K_DELETE :
                    fichier = open("datascore.rtf", "w")
                    fichier.write(str(0))
                    fichier.close()
                    fenetre.blit(fond,(0,0))
                    msgscoremax(points)
                    fenetre.blit(text,(10,200))
                    fenetre.blit(text1,(10,420))
                    fenetre.blit(text2,(150,10))
                    fenetre.blit(text3,(10,250))
                    fenetre.blit(text5,(10,550))
                    pygame.display.flip()

                if event.key==K_SPACE :
                    jeux()
                if event.key==K_s :
                    pygame.mixer.pause()
                if event.key==K_j :
                    pygame.mixer.unpause()

                if event.key == K_RETURN:
                    fenetre.blit(fond,(0,0))
                    chaine4='JEUX PROGRAMMÉ PAR TRISTAN ET AUDRIC'
                    chaine6=' -Appuyer sur "Echap" pour revenir au menu principal'
                    font4=pygame.font.SysFont("Lobster",65,bold=True,italic=False)
                    text4=font4.render(chaine4,1,(0,0,0))
                    text6=font.render(chaine6,1,(50,130,50))
                    fenetre.blit(text4,(30,250))
                    fenetre.blit(text6,(10,550))
                    pygame.display.flip()
                if event.key == K_ESCAPE:
                    lancement()




try :
    sonfond = pygame.mixer.Sound("musique.ogg")
    sonfond.play(loops=-1)
    lancement()
except :
    print("A bientot !")
finally:
    pygame.quit()
    exit()
