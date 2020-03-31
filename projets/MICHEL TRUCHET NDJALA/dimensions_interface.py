# Créé par gu.ndjalaessengue, le 10/03/2020 avec EduPython
from lycee import *

from tkinter import*

def quitter():
    Fenetre.destroy()



Fenetre=Tk()
Fenetre.title('Mastermind.exe')
Fenetre.wm_attributes("-fullscreen","1")

Fenetre.configure(bg="blue")


Texte1=Label(Fenetre,text="bienvenue dans le fameux jeu MASTERMIND !", bg="red")
Texte1.place(x=750, y=60)

Texte2=Label(Fenetre,text="Element 1", bg="red")
Texte2.place(x=50, y=30)

Texte3=Label(Fenetre,text="Element 2", bg="red")
Texte3.place(x=300, y=30)

entrée1=Entry(bg="red")
entrée1.place(x=50,y=50,width=60)

entrée2=Entry(bg="red")
entrée2.place(x=300,y=50,width=60)












Mon_bouton1 = Button(Fenetre,text="+",command=0)
Mon_bouton2 = Button(Fenetre,text="-",command=0)
Mon_bouton3 = Button(Fenetre,text="/",command=0)
Mon_bouton4 = Button(Fenetre,text="x",command=0)
Mon_bouton5 = Button(Fenetre,text="+",command=0)
Mon_bouton6 = Button(Fenetre,text="-",command=0)
Mon_bouton7 = Button(Fenetre,text="/",command=0)
Mon_bouton8 = Button(Fenetre,text="x",command=0)
Mon_bouton9 = Button(Fenetre,text="-",command=0)
Mon_bouton10 = Button(Fenetre,text="/",command=0)
Mon_bouton11 = Button(Fenetre,text="x",command=0)
Mon_bouton12 = Button(Fenetre,text="+",command=0)
Mon_bouton13 = Button(Fenetre,text="-",command=0)
Mon_bouton14 = Button(Fenetre,text="/",command=0)
Mon_bouton15 = Button(Fenetre,text="x",command=0)

Mon_bouton1.place(x=186,y=100,height=55,width=50) #width = longueur et height = largeur
Mon_bouton2.place(x=372,y=160,height=55,width=50)
Mon_bouton3.place(x=558,y=220,height=55,width=50)
Mon_bouton4.place(x=744,y=280,height=55,width=50)
Mon_bouton5.place(x=930,y=340,height=55,width=50)
Mon_bouton6.place(x=1116,y=400,height=55,width=50)
Mon_bouton7.place(x=1302,y=460,height=55,width=50)
Mon_bouton8.place(x=1488,y=520,height=55,width=50)
Mon_bouton9.place(x=372,y=580,height=55,width=50)
Mon_bouton10.place(x=558,y=640,height=55,width=50)
Mon_bouton11.place(x=744,y=700,height=55,width=50)
Mon_bouton12.place(x=930,y=760,height=55,width=50)
Mon_bouton13.place(x=1116,y=820,height=55,width=50)
Mon_bouton14.place(x=1302,y=880,height=55,width=50)
Mon_bouton15.place(x=1488,y=940,height=55,width=50)








Mon_bouton5 = Button(Fenetre,text="Quitter",command=quitter)
Mon_bouton5.place(x=350,y=170)


Fenetre.mainloop()






