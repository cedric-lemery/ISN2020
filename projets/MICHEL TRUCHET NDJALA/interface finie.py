# Créé par erago, le 19/05/2020 en Python 3.4
from tkinter import*


##Création de la fenêtre:
Interface=Tk()
Interface.title('Mastermind.exe')
Interface.wm_attributes("-fullscreen","1")
Interface.configure(bg="blue")
Fenetre=Tk()

##Fonctions:
def quitter():
    Interface.destroy()

def continuer1():
    playbutton.destroy()
    fond.destroy()
    Message1.place(x=300,y=400)
    startbutton.place(x=1400,y=920,width=300,height=100)

def continuer2():
    Message1.destroy()
    startbutton.destroy()
    newFenetre = Toplevel(Fenetre)
    Interface.destroy()
##Canvas d'images:
fond =Canvas(Interface,width=1920,height=1080, bg="DeepSkyBlue3")
background_image = PhotoImage(file="cerveau.png")
fond.create_image(960,520,image=background_image)
fond.pack()

fond2 = Canvas(Interface,width=1920,height=1080, bg="DeepSkyBlue3")
background_image2 = PhotoImage(file="gamerules.png")
fond2.create_image(960,540,image=background_image2)
fond2.pack()

##Widgets:
quitbutton = Button(Interface,text="  Quitter  ",command=quitter,bg="red")
quitbutton.place(x=0,y=0)

Message1= Label(Interface,text=" Bienvenue dans le célèbre jeu MASTERMIND 2.0 !\nVotre objectif :\n	-Réussir à trouver une combinaison secrète en 15 coups maximum.\n\n	Pour cela, l’ordinateur va choisir de manière aléatoire un code qui déterminera une combinaison.\n	Puis il vous faudra trouver ce code composé de 4 couleurs en cliquant sur les boutons de différentes couleurs.\n\nCEPENDANT, le jeu vous aidera en indiquant si vos couleurs sont bonnes et si elles sont à la bonne place (MAIS sans vous indiquer lesquelles!!)\n	- ROUGE : une couleur bonne et à la bonne place\n	-BLANC : une couleur est bonne mais pas à la bonne place\n	-NOIR : couleur pas bonne\nremarque : ces indications seront affichées à cotés de la ligne correspondante.\n\nVous gagnez uniquement si vous trouver la combinaison secrète en maximum 15 coups ; dans ce cas un message de victoire s’affichera, sinon ce sera un message de défaite… malheureusement pour vous... ")

playbutton = Button(Interface,text=" JOUER ",bg="grey",command=continuer1)
playbutton.place(x=810,y=730, width=300,height=100)

startbutton =Button(Interface,text=" C'EST PARTIT ! ",bg="yellow",command=continuer2)

Interface.mainloop()
