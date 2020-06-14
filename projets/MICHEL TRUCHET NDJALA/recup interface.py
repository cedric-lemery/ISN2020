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
# Mon_canvasJoueur.place(x=int(w*0.1), y=int(h*0.10), width=300, height=500) 
# comme la taille de la fenêtre dépend de la résolution de l'écran, tu pourrais penser width & height comme étant proportionnel à w & h :
Mon_canvasJoueur.place(x=int(w*0.1), y=int(h*0.10), width=int(w*0.3), height=int(h*0.80)) 
# par exemple

Rect1 =Mon_canvasJoueur.create_rectangle(x0,y0,x1,y1,fill='white') #x0 n'existe pas ?
Rect2 =Mon_canvasJoueur.create_rectangle(x0+1,y0,x1,y1,fill='white')
Rect3 =Mon_canvasJoueur.create_rectangle(x0+2,y0,x1,y1,fill='white')
Rect4 =Mon_canvasJoueur.create_rectangle(x0+3,y0,x1,y1,fill='white')

# il faut initialiser des valeurs que tu utilises ailleurs :
x0=10
y0=10
xpas=30
width=10
height=10
# comme ça on aura les coordonnées des x0, y0, x1, y1 par x0+i*xpas, y0, x0+i*xpas+width, y0+height

#Pour récupérer les rectangles ailleurs, tu pourrais faire :
Rect= [] # déclaration d'une liste
for i in range(4): #pour faire 4 rectangle
    Rect.append(Mon_canvasJoueur.create_rectangle(x0+i*xpas,y0,x0+i*xpas+width,y0+height,fill='white'))
    # Tu vois l'idée ?
    # ainsi, tu pourras accéder au rectangle n°i par Rect[i]

Mon_canvasReponses = Canvas(bg='black')
Mon_canvasReponses.place(x=int(w*0.70),y=int(h*0.10),width=250,height=500)

Fenetre.mainloop()