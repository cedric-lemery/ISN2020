from tkinter import*

def quitter():
    Fenetre.destroy()



Fenetre=Tk()
Fenetre.title('Mastermind.exe')
Fenetre.wm_attributes("-fullscreen","1")
Fenetre.configure(bg="royalblue")
w,h = Fenetre.winfo_screenwidth(), Fenetre.winfo_screenheight()

Mon_boutonQuitter = Button(Fenetre,text="Quitter", bg= 'red', fg='white', command=quitter)
Mon_boutonQuitter.place(x=int(w*0),y=int(h*0),width=80,height=30)

 #VALIDER #manque fonction
Mon_boutonValider = Button(Fenetre,text="Valider", bg='white', fg='black')
Mon_boutonValider.place(x=int(w*0.50),y=int(h*0.30),width=80,height=30)

Mon_canvasJoueur = Canvas(bg='black')
Mon_canvasJoueur.place(x=int(w*0.1), y=int(h*0.10), width=300, height=500)
Rect1 =Mon_canvasJoueur.create_rectangle(x0,y0,x1,y1,fill='white') #x0 n'existe pas ?
Rect2 =Mon_canvasJoueur.create_rectangle(x0+1,y0,x1,y1,fill='white')
Rect3 =Mon_canvasJoueur.create_rectangle(x0+2,y0,x1,y1,fill='white')
Rect4 =Mon_canvasJoueur.create_rectangle(x0+3,y0,x1,y1,fill='white')

Mon_canvasReponses = Canvas(bg='black')
Mon_canvasReponses.place(x=int(w*0.70),y=int(h*0.10),width=250,height=500)

Fenetre.mainloop()