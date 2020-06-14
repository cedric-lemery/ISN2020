from tkinter import*

def quitter():
    Fenetre.destroy()

Fenetre=Tk()
Fenetre.title('Mastermind.exe')
Fenetre.wm_attributes("-fullscreen","1")
Fenetre.configure(bg="royalblue")

w,h = Fenetre.winfo_screenwidth(), Fenetre.winfo_screenheight()

Mon_boutonQuitter = Button(Fenetre,text="Quitter", bg= 'red', fg='white', command=quitter)
Mon_boutonQuitter.place(x=int(w*0),y=int(h*0),width=60,height=20)


#BOUTONS REPONSES
Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.05), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.05), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.05), width=20, height=20)




Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.10), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.10), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.10), width=20, height=20)




Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.15), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.15), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.15), width=20, height=20)



Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.20), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.20), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.20), width=20, height=20)



Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.25), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.25), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.25), width=20, height=20)



Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.30), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.30), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.30), width=20, height=20)



Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.35), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.35), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.35), width=20, height=20)



Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.40), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.40), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.40), width=20, height=20)



Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.45), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.45), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.45), width=20, height=20)



Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.50), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.50), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.50), width=20, height=20)



Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.55), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.55), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.55), width=20, height=20)



Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.60), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.60), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.60), width=20, height=20)



Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.65), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.65), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.65), width=20, height=20)



Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.70), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.70), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.70), width=20, height=20)



Mon_canvasNoir = Canvas(bg='black')
Mon_canvasNoir.place(x=int(w*0.75), y=int(h*0.75), width=20, height=20)

Mon_canvasBlanc = Canvas(bg='white')
Mon_canvasBlanc.place(x=int(w*0.80), y=int(h*0.75), width=20, height=20)

Mon_canvasRouge = Canvas(bg='red')
Mon_canvasRouge.place(x=int(w*0.85), y=int(h*0.75), width=20, height=20)







#BOUTONS JOUEURS
Mon_canvasJoueur1 = Canvas()
Mon_canvasJoueur1.place(x=int(w*0.20), y=int(h*0.05), width=20, height=20)

Mon_canvasJoueur2 = Canvas()
Mon_canvasJoueur2.place(x=int(w*0.25), y=int(h*0.05), width=20, height=20)

Mon_canvasJoueur3 = Canvas()
Mon_canvasJoueur3.place(x=int(w*0.30), y=int(h*0.05), width=20, height=20)

Mon_canvasJoueur4 = Canvas()
Mon_canvasJoueur4.place(x=int(w*0.35), y=int(h*0.05), width=20, height=20)



Mon_canvasJoueur5 = Canvas()
Mon_canvasJoueur5.place(x=int(w*0.20), y=int(h*0.10), width=20, height=20)

Mon_canvasJoueur6 = Canvas()
Mon_canvasJoueur6.place(x=int(w*0.25), y=int(h*0.10), width=20, height=20)

Mon_canvasJoueur7 = Canvas()
Mon_canvasJoueur7.place(x=int(w*0.30), y=int(h*0.10), width=20, height=20)

Mon_canvasJoueur8 = Canvas()
Mon_canvasJoueur8.place(x=int(w*0.35), y=int(h*0.10), width=20, height=20)



Mon_canvasJoueur9 = Canvas()
Mon_canvasJoueur9.place(x=int(w*0.20), y=int(h*0.15), width=20, height=20)

Mon_canvasJoueur10 = Canvas()
Mon_canvasJoueur10.place(x=int(w*0.25), y=int(h*0.15), width=20, height=20)

Mon_canvasJoueur11= Canvas()
Mon_canvasJoueur11.place(x=int(w*0.30), y=int(h*0.15), width=20, height=20)

Mon_canvasJoueur12= Canvas()
Mon_canvasJoueur12.place(x=int(w*0.35), y=int(h*0.15), width=20, height=20)



Mon_canvasJoueur13 = Canvas()
Mon_canvasJoueur13.place(x=int(w*0.20), y=int(h*0.20), width=20, height=20)

Mon_canvasJoueur14 = Canvas()
Mon_canvasJoueur14.place(x=int(w*0.25), y=int(h*0.20), width=20, height=20)

Mon_canvasJoueur15 = Canvas()
Mon_canvasJoueur15.place(x=int(w*0.30), y=int(h*0.20), width=20, height=20)

Mon_canvasJoueur16 = Canvas()
Mon_canvasJoueur16.place(x=int(w*0.35), y=int(h*0.20), width=20, height=20)



Mon_canvasJoueur17 = Canvas()
Mon_canvasJoueur17.place(x=int(w*0.20), y=int(h*0.25), width=20, height=20)

Mon_canvasJoueur18 = Canvas()
Mon_canvasJoueur18.place(x=int(w*0.25), y=int(h*0.25), width=20, height=20)

Mon_canvasJoueur19 = Canvas()
Mon_canvasJoueur19.place(x=int(w*0.30), y=int(h*0.25), width=20, height=20)

Mon_canvasJoueur20 = Canvas()
Mon_canvasJoueur20.place(x=int(w*0.35), y=int(h*0.25), width=20, height=20)



Mon_canvasJoueur21 = Canvas()
Mon_canvasJoueur21.place(x=int(w*0.20), y=int(h*0.30), width=20, height=20)

Mon_canvasJoueur22 = Canvas()
Mon_canvasJoueur22.place(x=int(w*0.25), y=int(h*0.30), width=20, height=20)

Mon_canvasJoueur23 = Canvas()
Mon_canvasJoueur23.place(x=int(w*0.30), y=int(h*0.30), width=20, height=20)

Mon_canvasJoueur24 = Canvas()
Mon_canvasJoueur24.place(x=int(w*0.35), y=int(h*0.30), width=20, height=20)



Mon_canvasJoueur25 = Canvas()
Mon_canvasJoueur25.place(x=int(w*0.20), y=int(h*0.35), width=20, height=20)

Mon_canvasJoueur26 = Canvas()
Mon_canvasJoueur26.place(x=int(w*0.25), y=int(h*0.35), width=20, height=20)

Mon_canvasJoueur27 = Canvas()
Mon_canvasJoueur27.place(x=int(w*0.30), y=int(h*0.35), width=20, height=20)

Mon_canvasJoueur28 = Canvas()
Mon_canvasJoueur28.place(x=int(w*0.35), y=int(h*0.35), width=20, height=20)



Mon_canvasJoueur29 = Canvas()
Mon_canvasJoueur29.place(x=int(w*0.20), y=int(h*0.40), width=20, height=20)

Mon_canvasJoueur30 = Canvas()
Mon_canvasJoueur30.place(x=int(w*0.25), y=int(h*0.40), width=20, height=20)

Mon_canvasJoueur31 = Canvas()
Mon_canvasJoueur31.place(x=int(w*0.30), y=int(h*0.40), width=20, height=20)

Mon_canvasJoueur32 = Canvas()
Mon_canvasJoueur32.place(x=int(w*0.35), y=int(h*0.40), width=20, height=20)



Mon_canvasJoueur33 = Canvas()
Mon_canvasJoueur33.place(x=int(w*0.20), y=int(h*0.45), width=20, height=20)

Mon_canvasJoueur34 = Canvas()
Mon_canvasJoueur34.place(x=int(w*0.25), y=int(h*0.45), width=20, height=20)

Mon_canvasJoueur35 = Canvas()
Mon_canvasJoueur35.place(x=int(w*0.30), y=int(h*0.45), width=20, height=20)

Mon_canvasJoueur36 = Canvas()
Mon_canvasJoueur36.place(x=int(w*0.35), y=int(h*0.45), width=20, height=20)



Mon_canvasJoueur37 = Canvas()
Mon_canvasJoueur37.place(x=int(w*0.20), y=int(h*0.50), width=20, height=20)

Mon_canvasJoueur38 = Canvas()
Mon_canvasJoueur38.place(x=int(w*0.25), y=int(h*0.50), width=20, height=20)

Mon_canvasJoueur39 = Canvas()
Mon_canvasJoueur39.place(x=int(w*0.30), y=int(h*0.50), width=20, height=20)

Mon_canvasJoueur40 = Canvas()
Mon_canvasJoueur40.place(x=int(w*0.35), y=int(h*0.50), width=20, height=20)



Mon_canvasJoueur41 = Canvas()
Mon_canvasJoueur41.place(x=int(w*0.20), y=int(h*0.55), width=20, height=20)

Mon_canvasJoueur42 = Canvas()
Mon_canvasJoueur42.place(x=int(w*0.25), y=int(h*0.55), width=20, height=20)

Mon_canvasJoueur43 = Canvas()
Mon_canvasJoueur43.place(x=int(w*0.30), y=int(h*0.55), width=20, height=20)

Mon_canvasJoueur44 = Canvas()
Mon_canvasJoueur44.place(x=int(w*0.35), y=int(h*0.55), width=20, height=20)



Mon_canvasJoueur45 = Canvas()
Mon_canvasJoueur45.place(x=int(w*0.20), y=int(h*0.60), width=20, height=20)

Mon_canvasJoueur46 = Canvas()
Mon_canvasJoueur46.place(x=int(w*0.25), y=int(h*0.60), width=20, height=20)

Mon_canvasJoueur47 = Canvas()
Mon_canvasJoueur47.place(x=int(w*0.30), y=int(h*0.60), width=20, height=20)

Mon_canvasJoueur48 = Canvas()
Mon_canvasJoueur48.place(x=int(w*0.35), y=int(h*0.60), width=20, height=20)



Mon_canvasJoueur49 = Canvas()
Mon_canvasJoueur49.place(x=int(w*0.20), y=int(h*0.65), width=20, height=20)

Mon_canvasJoueur50 = Canvas()
Mon_canvasJoueur50.place(x=int(w*0.25), y=int(h*0.65), width=20, height=20)

Mon_canvasJoueur51 = Canvas()
Mon_canvasJoueur51.place(x=int(w*0.30), y=int(h*0.65), width=20, height=20)

Mon_canvasJoueur52 = Canvas()
Mon_canvasJoueur52.place(x=int(w*0.35), y=int(h*0.65), width=20, height=20)



Mon_canvasJoueur53 = Canvas()
Mon_canvasJoueur53.place(x=int(w*0.20), y=int(h*0.70), width=20, height=20)

Mon_canvasJoueur54 = Canvas()
Mon_canvasJoueur54.place(x=int(w*0.25), y=int(h*0.70), width=20, height=20)

Mon_canvasJoueur55 = Canvas()
Mon_canvasJoueur55.place(x=int(w*0.30), y=int(h*0.70), width=20, height=20)

Mon_canvasJoueur56 = Canvas()
Mon_canvasJoueur56.place(x=int(w*0.35), y=int(h*0.70), width=20, height=20)



Mon_canvasJoueur57 = Canvas()
Mon_canvasJoueur57.place(x=int(w*0.20), y=int(h*0.75), width=20, height=20)

Mon_canvasJoueur58 = Canvas()
Mon_canvasJoueur58.place(x=int(w*0.25), y=int(h*0.75), width=20, height=20)

Mon_canvasJoueur59 = Canvas()
Mon_canvasJoueur59.place(x=int(w*0.30), y=int(h*0.75), width=20, height=20)

Mon_canvasJoueur60 = Canvas()
Mon_canvasJoueur60.place(x=int(w*0.35), y=int(h*0.75), width=20, height=20)









Fenetre.mainloop()