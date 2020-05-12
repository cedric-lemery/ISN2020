from tkinter import*

Fenetre_pendu=Tk()
Fenetre_pendu.title("Jeu du Pendu")
Fenetre_pendu.geometry("500x300")

Mon_LabelP1=Label(Fenetre_pendu,text="Entrez votre lettre",fg="black")
Mon_LabelP1.place(x=30,y=50)
Mon_LabelP2=Label(Fenetre_pendu,text="Il vous reste 15 tentatives",fg="red")
Mon_LabelP2.place(x=70,y=70)
Mon_LabelP3=Label(Fenetre_pendu,text="Voici votre avancement :")
Mon_LabelP3.place(x=110,y=70)

Mon_EntryP1=Entry(Fenetre_pendu)
Mon_EntryP1.place(x=30,y=70)

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
print(MotCache)

Mon_LabelP4=Mabel(Fenetre_pendu,text=MotCache)
Mon_LabelP4.place(x=110,y=90)

Fenetre_pendu.mainloop()
