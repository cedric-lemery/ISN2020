from tkinter import*

def Quitter():
    Fenetre.destroy()

def facile():
    Fenetre2=Tk()
    Fenetre2.title('Niveau Facile')
    Fenetre2.geometry('500x500')
    Bouton_quitter2=Button(Fenetre2,text="Quitter", command=Fenetre2.destroy)
    Bouton_quitter2.place(x=445,y=460)

def moyen():
    Fenetre3=Tk()
    Fenetre3.title('Niveau Moyen')
    Fenetre3.geometry('500x500')
    Bouton_quitter3=Button(Fenetre3,text="Quitter", command=Fenetre3.destroy)
    Bouton_quitter3.place(x=445,y=460)

def difficile():
    Fenetre4=Tk()
    Fenetre4.title('Niveau Difficile')
    Fenetre4.geometry('500x500')
    Bouton_quitter4=Button(Fenetre4,text="Quitter", command=Fenetre4.destroy)
    Bouton_quitter4.place(x=445,y=460)

Fenetre=Tk()
Fenetre.title('4 images 1 mot')
Fenetre.geometry('500x500')

Texte_a_afficher=Label(Fenetre,text="Bonjour et bienvenue sur 4 images 1 mot !!!")
Texte_a_afficher.pack()
Texte_a_afficher2=Label(Fenetre,text="Quelle difficulté veut tu essayer ??")
Texte_a_afficher2.pack()

Bouton_facile=Button(Fenetre,text="Facile", command=facile)
Bouton_facile.place(x=230,y=150)
Bouton_Moyen=Button(Fenetre,text="Moyen", command=moyen)
Bouton_Moyen.place(x=230,y=250)
Bouton_Difficile=Button(Fenetre,text="Difficile", command=difficile)
Bouton_Difficile.place(x=230,y=350)

Bouton_quitter=Button(Fenetre,text="Quitter", command=Quitter)
Bouton_quitter.place(x=445,y=460)

Fenetre.mainloop()