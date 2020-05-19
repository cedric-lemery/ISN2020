import pygame
from random import *
from threading import Timer

def init_game(folderImag):
    global surface,blue,son_menu, fond_menu, imggo, son_jeu, fondl, fond, img, brickmove, brickmario, son_go
    pygame.init()

    surface = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption("mario bros")

    blue = (100, 100, 255)

    fond = pygame.image.load(folderImag+"fond.png").convert()

    img = pygame.image.load(folderImag+"mario2.jpg")
    brickmario = pygame.image.load(folderImag+"brick_mario.png")
    brickmove = pygame.image.load(folderImag+"petite_brick_mario.png")
    fond_menu = pygame.image.load(folderImag+"menu2.3.jpg").convert()
    imggo = pygame.image.load(folderImag+"img_gameover.jpg").convert()
    fondl = pygame.image.load(folderImag+"loading.png").convert()

    son_menu = pygame.mixer.Sound(folderImag+"Title Theme - New Super Mario Bros..ogg")
    son_go = pygame.mixer.Sound(folderImag+"Lose Life - New Super Mario Bros..ogg")
    son_jeu = pygame.mixer.Sound(folderImag+"Overworld Theme - New Super Mario Bros..ogg")



def score(compte):
    font=pygame.font.Font(None, 50)
    texte=font.render("score : " + str(compte), True, (0,0,0))
    surface.blit(texte,[10,0])


def fonde(xf, yf):
    global surface
    surface.blit(fond, (xf,yf))
def mario(x, y, image):
    global surface
    surface.blit(image, (x,y))
def petitebrick(xp,yp):
    global surface
    surface.blit(brickmove, (xp,yp))




def menu():
    global son_menu
    def gameOver():
        pygame.quit()
        quit()

    window_resolution = (1400, 800)
    pygame.display.set_caption("jouer du son")
    window_surface = pygame.display.set_mode(window_resolution)


    son_menu.play(loops=-1)
    son_menu.set_volume(0.1)

    pygame.display.flip()

    font=pygame.font.Font(None, 60)
    text = font.render("appuyer sur entrée pour commencer",1,(0,0,0))
    text2 = font.render("appuyer sur échap pour quitter",1,(0,0,0))
    text3 = font.render("maintenir espace pour éviter les cubes volants",1,(0,0,0))

    game_over=False

    xm=0
    ym=0
    xt=350
    yt=400
    def fondmenu(xm,ym):
        global surface, fond_menu
        surface.blit(fond_menu, (xm,ym))

    def texte(xt,yt):
        global surface
        surface.blit(text, (xt,yt))
        yt=500
        xt=400
        surface.blit(text2, (xt,yt))
        yt=600
        xt=250
        surface.blit(text3, (xt,yt))


    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameOver()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    principale()




        fondmenu(xm,ym)
        texte(xt,yt)
        pygame.display.update()


def gameover():
    pygame.mixer.pause()
    global son_jeu
    xgo=0
    ygo=0
    xt=350
    yt=600
    def texte(xt,yt):
        global surface
        surface.blit(text, (xt,yt))

    font=pygame.font.Font(None, 60)
    text = font.render("appuyer sur échap pour continuer",1,(255,255,255))


    son_go.play()
    son_go.set_volume(0.1)
    pygame.display.flip()

    def imagego(xgo,ygo):
        global surface, imggo
        surface.blit(imggo, (xgo,ygo))

    game_over = False
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return menu()

        imagego(xgo,ygo)
        texte(xt,yt)
        pygame.display.update()


def principale():
    global blue, son_jeu, fondl
    xl=0
    yl=0
    pygame.mixer.pause()

    son_jeu.play(loops=-1)
    son_jeu.set_volume(0.1)
    pygame.display.flip()


    def fondm(xl,yl):
        global surface
        surface.blit(fondl, (xl,yl))

    font=pygame.font.Font(None, 100)
    imgc = font.render("appuyer sur espace pour commencer",1,(0,0,0))
    def imagec(xc,yc):
        global surface
        surface.blit(imgc, (xc,yc))
    xc=100
    yc=250
    surface.fill(blue)
    game_over = False
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jeu()
        fondm(xl,yl)
        imagec(xc,yc)
        pygame.display.update()



def jeu():
    global surface,blue
    x=200
    y=200
    xf=0
    yf=0
    xb=1400
    yb=700
    xp=1400
    yp=randint(0, 600)
    p_vitesse=2
    y_move=0
    x_move=0
    score_actuel=0
    surface.fill(blue)
    game_over = False
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True


            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gameover()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    xb =-1


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_move = -5
            if event.type == pygame.KEYUP:
                y_move = 3

        if x+300 > xp+20:
            if y < yp+50-50:
                if x < xp+50-20:
                    if y+300 > yp+50+50:
                        gameover()
        xp -= p_vitesse
        y+= y_move
        if y>800-40 or y<-200:
            gameover()
        if xp<(-50):
            xp=1400
            yp=randint(0, 600)


        if 3<=score_actuel<6:
            p_vitesse=3
        if 6<=score_actuel<9:
            p_vitesse=4
        if 9<=score_actuel<12:
            p_vitesse=5
        if 12<=score_actuel<15:
            p_vitesse=6
        if 15<=score_actuel<18:
            p_vitesse=7
        if 18<=score_actuel<21:
            p_vitesse=8
        if 21<=score_actuel<24:
            p_vitesse=9
        if 24<=score_actuel<27:
            p_vitesse=10
        if 27<=score_actuel<30:
            p_vitesse=15
        if 30<=score_actuel<100:
            p_vitesse=20



        fonde(xf, yf)
        mario(x, y, img)

        petitebrick(xp,yp)

        if xp<x<=xp+p_vitesse:
            score_actuel+=1

        score(score_actuel)

        pygame.display.update()


if __name__ == "__main__":
    init_game('./')
    menu()

    pygame.quit()
    quit()

