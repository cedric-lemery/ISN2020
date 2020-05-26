from tkinter import*

def Quitter():
    Fenetre.destroy()

def ajout(lettre):
    global lettre1, label_reponse
    lettre1+=lettre
    label_reponse.config(text=lettre1)

def E():
    ajout('E')
    Bouton_E.place_forget()

def E1():
    ajout('E')
    Bouton_E1.place_forget()

def T():
    ajout('T')
    Bouton_T.place_forget()
    Bouton_E.place(x=300,y=450)


def valid():
    global mot
    if lettre1==mot:
        resultat=Label(Fenetre,text='Bravo!!')
        resultat.pack()
    else:
        resultat=Label(Fenetre,text='Perdu!!')
        resultat.pack()

def facile():
    global lettre1, photo, label_reponse, mot
    lettre1=''
    mot='ETE'

    zone_dessin = Canvas(Fenetre,width=300,height=300,bd=8,relief="ridge")
    zone_dessin.create_image(250,250,image=photo)
    zone_dessin.pack()

    label_reponse=Label(Fenetre,text='')
    label_reponse.place(x=250,y=400)
    Bouton_E.place(x=300,y=450)
    Bouton_E1.place(x=200,y=450)
    Bouton_T.place(x=100,y=450)
    Bouton_Valid.place(x=400,y=450)

Fenetre=Tk()
Fenetre.title('4 images 1 mot')
Fenetre.geometry('500x500')

photo=PhotoImage(file="108.png")

Texte_a_afficher=Label(Fenetre,text="Bonjour et bienvenue sur 4 images 1 mot !!!")
Texte_a_afficher.pack()
Texte_a_afficher2=Label(Fenetre,text="Quelle difficulté veut tu essayer ??")
Texte_a_afficher2.pack()

Bouton_facile=Button(Fenetre,text="Facile", command=facile)
Bouton_facile.place(x=230,y=150)

Bouton_quitter=Button(Fenetre,text="Quitter", command=Quitter)
Bouton_quitter.place(x=445,y=450)

Bouton_E=Button(Fenetre,text='E',command=E)
Bouton_E1=Button(Fenetre,text='E',command=E1)
Bouton_T=Button(Fenetre,text='T',command=T)
Bouton_Valid=Button(Fenetre,text='Validé',command=valid)

Fenetre.mainloop()