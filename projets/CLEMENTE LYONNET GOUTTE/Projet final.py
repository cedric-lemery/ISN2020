from tkinter import*

def Quitter():
    Fenetre.destroy()

def facile():
    Fenetre2=Tk()
    Fenetre2.title('Niveau Facile')
    Fenetre2.geometry('500x500')
    Bouton_quitter2=Button(Fenetre2,text="Quitter", command=Fenetre2.destroy)
    Bouton_quitter2.place(x=450,y=475)

    lettre1=''
    mot='ETE'
    def Quitter():
        Fenetre2.destroy()
    def ajout(lettre):
        global lettre1
        lettre1+=lettre
        label['text']=lettre1
    def E():
        ajout('E')
        Bouton_E.destroy()
    def E1():
        ajout('E')
        Bouton_E1.destroy()
    def T():
        ajout('T')
        Bouton_T.destroy()

    photo=PhotoImage(file="108.png.png")
    zone_dessin = Canvas(Fenetre2,width=300,height=300,bd=8,relief="ridge")
    zone_dessin.create_image(250,250,image=photo)
    zone_dessin.pack()

    label=Label(Fenetre2,text='')
    label.place(x=250,y=400)
    Bouton_E=Button(Fenetre2,text='E',command=E)
    Bouton_E.place(x=300,y=450)
    Bouton_E1=Button(Fenetre2,text='E',command=E1)
    Bouton_E1.place(x=200,y=450)
    Bouton_T=Button(Fenetre2,text='T',command=T)
    Bouton_T.place(x=100,y=450)
    Bouton_Valid=Button(Fenetre2,text='Validé',command=valid)
    Bouton_Valid.place(x=400,y=450)

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