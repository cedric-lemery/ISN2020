import pygame
from random import *
from threading import Timer


pygame.init()

surface = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("mario bros")

blue = (100, 100, 255)

fond = pygame.image.load("fond.png").convert()
img = pygame.image.load("mario2.jpg")
brickmario = pygame.image.load("brick_mario.png")
brickmove = pygame.image.load("petite_brick_mario.png")

fontScore=pygame.font.Font(None, 50)


def score(compte):
    texte=fontScore.render("score : " + str(compte), True, (0,0,0))
    surface.blit(texte,[10,0])


def fonde(xf, yf):
    surface.blit(fond, (xf,yf))
def mario(x, y, image):
    surface.blit(image, (x,y))
def brick(xb,yb):
    for loop in range(6):
        surface.blit(brickmario, (xb,yb))
        xb+=300
def petitebrick(xp,yp):
    surface.blit(brickmove, (xp,yp))




def menu():
    def gameOver():
        pygame.quit()
        quit()

    window_resolution = (1400, 800)
    pygame.display.set_caption("jouer du son")
    window_surface = pygame.display.set_mode(window_resolution)


    son_menu = pygame.mixer.Sound("Title Theme - New Super Mario Bros..ogg")
    son_menu.play(loops=-1)

    pygame.display.flip()

    font=pygame.font.Font(None, 60)
    text = font.render("appuyer sur entrée pour commencer",1,(0,0,0))
    text2 = font.render("appuyer sur échap pour quitter",1,(0,0,0))
    text3 = font.render("maintenir espace pour éviter les cubes volants",1,(0,0,0))

    game_over=False
    fond_menu = pygame.image.load("menu2.3.jpg").convert()
    xm=0
    ym=0
    xt=350
    yt=400
    def fondmenu(xm,ym):
        surface.blit(fond_menu, (xm,ym))

    def texte(xt,yt):
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
    xgo=0
    ygo=0
    xt=350
    yt=600
    def texte(xt,yt):
        surface.blit(text, (xt,yt))

    font=pygame.font.Font(None, 60)
    text = font.render("appuyer sur échap pour continuer",1,(255,255,255))

    imggo = pygame.image.load("img_gameover.jpg").convert()

    son_jeu = pygame.mixer.Sound("Lose Life - New Super Mario Bros..ogg")
    son_jeu.play()
    pygame.display.flip()

    def imagego(xgo,ygo):
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
    xl=0
    yl=0
    pygame.mixer.pause()
    son_jeu = pygame.mixer.Sound("Overworld Theme - New Super Mario Bros..ogg")
    son_jeu.play(loops=-1)
    pygame.display.flip()

    fondl = pygame.image.load("loading.png").convert()
    def fondm(xl,yl):
        surface.blit(fondl, (xl,yl))

    font=pygame.font.Font(None, 100)
    imgc = font.render("appuyer sur espace pour commencer",1,(0,0,0))
    def imagec(xc,yc):
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

        print(xp,x-50,xp+p_vitesse,xp<(x-50)<xp+p_vitesse)
        if xp<(x-50)<xp+p_vitesse:
            score_actuel+=1
            print('ok')



        fonde(xf, yf)
        mario(x, y, img)
        brick(xb,yb)
        petitebrick(xp,yp)
        score(score_actuel)


        pygame.display.update()





menu()
pygame.quit()
quit()


