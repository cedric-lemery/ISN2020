# Créé par erago, le 19/05/2020 en Python 3.4
from tkinter import*

def quitter():
    Fenetre.destroy()



Fenetre=Tk()
Fenetre.title('Mastermind.exe')
Fenetre.wm_attributes("-fullscreen","1")
Fenetre.configure(bg="black")

background_image = PhotoImage(file="D:\Guilhem\Mes documents\ISN\image feu.png")

Mon_bouton5 = Button(Fenetre,text="  Quitter  ",command=quitter,bg="red")
Mon_bouton5.place(x=0,y=0)

playbutton = Button(Fenetre,text=" JOUER ",bg="red")
playbutton.place(x=810,y=730, width=300,height=100)

Label(Fenetre,)

Fenetre.mainloop()
