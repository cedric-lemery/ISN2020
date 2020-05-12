from tkinter import*
import random

def Quitter():
    Fenetre_pendu.destroy()

def gagner():
    Mon_LabelP1.config(text="")
    Mon_LabelP2.config(text="")
    Mon_LabelP3.config(text="Vous avez gagné")
    Mon_LabelP4.config(text="Le mot était : "+Mot)


ListeMots=["banane", "hippopotame", "gendarmerie", "election", "codage",
"imprimmante", "mars", "virus", "continent", "numerique", "tatouages", "permis",
"ordinateur", "panda", "bibliotheque", "camion", "point", "avion", "pont",
"prise"]

Mot=random.choice(ListeMots)
Liste_Mot=[lettre for lettre in Mot]
MotCache=[lettre for lettre in Mot]

idx=0
for lettre in range(len(Mot)):
    MotCache[idx]='_'
    idx=idx+1

nombrtentative=15
def Test():
    global nombrtentative
    lettre = Mon_EntryP1.get()
    lettre = lettre.lower()
    if len(lettre) < 1:
        Mon_LabelP1.config(text="Vous n'avez rentré aucune lettre, réessayer")
        lettre = Mon_EntryP1.get()
        lettre = lettre.lower()
    if len(lettre)>1:
        if lettre==Mot:
            gagner()
    if lettre in Liste_Mot:
        for (i,j) in enumerate(Liste_Mot):
            if j == lettre:
                MotCache[i]=j
        letterfound = MotCache
        Mon_LabelP4.config(text=letterfound)
        Mon_LabelP1.config(text="Vous avez proposé une bonne lettre")
        Mon_LabelP2.config(text="Il vous reste "+ str(nombrtentative)+" tentatives")
    else:
        Mon_LabelP1.config(text="Vous n'avez pas proposé une bonne lettre, réessayez !")
        nombrtentative=nombrtentative-1
        Mon_LabelP2.config(text="Il vous reste "+ str(nombrtentative)+" tentatives")

    if MotCache == Liste_Mot :
        Mon_LabelP3.config(text="Bravo vous avez trouver le mot")
        gagner()

    if nombrtentative == 0:
        Mon_LabelP3.config(text="Vous avez épuisé toutes vos chances de gagner, vous avez donc perdu, adieu !")
        Mon_LabelP4.config(text="Le mot à trouver était :"+ Mot)
        Mon_LabelP4.place(x=200,y=130)



Fenetre_pendu=Tk()
Fenetre_pendu.title("Jeu du Pendu")
Fenetre_pendu.geometry("500x200")

Mon_LabelP1=Label(Fenetre_pendu,text="Entrez votre lettre",fg="black")
Mon_LabelP1.place(x=30,y=50)
Mon_LabelP2=Label(Fenetre_pendu,text="Il vous reste 15 tentatives",fg="purple")
Mon_LabelP2.place(x=200,y=70)
Mon_LabelP3=Label(Fenetre_pendu,text="Voici votre avancement :")
Mon_LabelP3.place(x=60,y=100)
Mon_LabelP4=Label(Fenetre_pendu,text=MotCache)
Mon_LabelP4.place(x=200,y=100)

Mon_EntryP1=Entry(Fenetre_pendu)
Mon_EntryP1.place(x=30,y=70)

Mon_bouttonPQ=Button(Fenetre_pendu, text = " Quitter", fg = "red", command = Quitter)
Mon_bouttonPQ.place(x=30, y=150, width=70)

Mon_bouttonPT=Button(Fenetre_pendu, text = "Test", fg = "green", command = Test)
Mon_bouttonPT.place(x=130, y=150, width=70)

Fenetre_pendu.mainloop()
