from tkinter import *
lettre1=''
mot='ETE'
def Quitter():
    Fenetre.destroy()
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
def S():
    ajout("S")
    Bouton_S.destroy()
def A():
    ajout("A")
    Bouton_A.destroy()
def S1():
    ajout("S1")
    Bouton_S1.destroy()
def R():
    ajout("R")
    Bouton_R.destroy()
def valid():
    if label['text']==mot:
        resultat=Label(Fenetre,text='Bravo!!')
        resultat.pack()
    else:
        resultat=Label(Fenetre,text='Perdu!!')
        resultat.pack()
        Bouton_retry=Button(Fenetre,text='Réssayer',command=retry)
        Bouton_retry.place(x=20,y=50)
#def retry():


Fenetre=Tk()
Fenetre.title('4 Image 1 Mot')
Fenetre.geometry('500x600')

#photo1 = PhotoImage(file="plage")

#canvas = Canvas(fenetre,width=350, height=200)
#canvas.create_image(0, 0, anchor=NW, image=photo)
#canvas.pack()


label=Label(Fenetre,text='')
label.place(x=250,y=400)
Bouton_E=Button(Fenetre,text='E',command=E)
Bouton_E.place(x=300,y=450)
Bouton_E1=Button(Fenetre,text='E',command=E1)
Bouton_E1.place(x=200,y=450)
Bouton_T=Button(Fenetre,text='T',command=T)
Bouton_T.place(x=100,y=450)
Bouton_Valid=Button(Fenetre,text='Validé',command=valid)
Bouton_Valid.place(x=400,y=450)
Bouton_S=Button(Fenetre,text='S',command=S)
Bouton_S.place(x=250,y=450)
Bouton_A=Button(Fenetre,text='A',command=A)
Bouton_A.place(x=150,y=450)
Bouton_S1=Button(Fenetre,text='S',command=S1)
Bouton_S1.place(x=50,y=450)
Bouton_R=Button(Fenetre,text='R',command=R)
Bouton_R.place(x=25,y=450)


Bouton_Quitter=Button(Fenetre,text="Quitter", command=Quitter)
Bouton_Quitter.place(x=400,y=550)

Fenetre.mainloop()