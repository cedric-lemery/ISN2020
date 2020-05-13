from tkinter import*

def quitter():
    Fenetre.destroy()
x0=10
y0=10
xpas=110
x1=18
y1=18


Fenetre=Tk()
Fenetre.title('Mastermind.exe')
Fenetre.wm_attributes("-fullscreen","1")
Fenetre.configure(bg="royalblue")
w,h = Fenetre.winfo_screenwidth(), Fenetre.winfo_screenheight()

Mon_boutonQuitter = Button(Fenetre,text="Quitter", bg= 'red', fg='white', command=quitter)
Mon_boutonQuitter.place(x=int(w*0),y=int(h*0),width=80,height=30)


Mon_boutonValider = Button(Fenetre,text="Valider", bg='white', fg='black')
Mon_boutonValider.place(x=int(w*0.50),y=int(h*0.30),width=80,height=30)

Mon_boutonCyan = Button(Fenetre, bg='cyan', fg='cyan')
Mon_boutonCyan.place(x=int(w*0.45),y=int(h*0.15),width=18,height=18)

Mon_boutonOrange = Button(Fenetre, bg='orange', fg='orange')
Mon_boutonOrange.place(x=int(w*0.50),y=int(h*0.15),width=18,height=18)

Mon_boutonBleu = Button(Fenetre, bg='blue', fg='blue')
Mon_boutonBleu.place(x=int(w*0.55),y=int(h*0.15),width=18,height=18)

Mon_boutonMarron = Button(Fenetre, bg='saddlebrown', fg='saddlebrown')
Mon_boutonMarron.place(x=int(w*0.60),y=int(h*0.15),width=18,height=18)

Mon_boutonJaune = Button(Fenetre, bg='yellow', fg='yellow')
Mon_boutonJaune.place(x=int(w*0.45),y=int(h*0.20),width=18,height=18)

Mon_boutonVert = Button(Fenetre, bg='green', fg='green')
Mon_boutonVert.place(x=int(w*0.50),y=int(h*0.20),width=18,height=18)

Mon_boutonViolet = Button(Fenetre, bg='purple', fg='purple')
Mon_boutonViolet.place(x=int(w*0.55),y=int(h*0.20),width=18,height=18)

Mon_boutonRose= Button(Fenetre, bg='pink', fg='pink')
Mon_boutonRose.place(x=int(w*0.60),y=int(h*0.20),width=18,height=18)







Mon_canvasJoueur = Canvas(bg='black')

Mon_canvasJoueur.place(x=int(w*0.1), y=int(h*0.10), width=int(w*0.3), height=int(h*0.80))


Rect = []
for i in range(4):
    Rect.append(Mon_canvasJoueur.create_rectangle(x0+i*xpas,y0,x0+i*xpas+x1,y0+y1,fill='white'))


Mon_canvasReponses = Canvas(bg='black')
Mon_canvasReponses.place(x=int(w*0.70),y=int(h*0.10),width=250,height=500)

Fenetre.mainloop()
