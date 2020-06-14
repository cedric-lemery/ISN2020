# Créé par erago, le 07/04/2020 avec EduPython

from tkinter import*

def quitter():
    Fenetre.destroy()


Fenetre=Tk()
Fenetre.title('Mastermind.exe')
Fenetre.wm_attributes("-fullscreen","1")
Fenetre.configure(bg="royalblue")

w,h = Fenetre.winfo_screenwidth(), Fenetre.winfo_screenheight()
print('dimensions de la fenetre',w,h)




Mon_bouton5 = Button(Fenetre,text="     X     ", bg="darkred", command=quitter)
#Mon_bouton5.place(x=1850,y=20)
Mon_bouton5.place(x=int(w*0.5),y=int(h*0.5))


Fenetre.mainloop()

#pour ce petit programme le bouton quitter est bien placé mais si un autre ordinateur n'ayant pas les memes dimensions l'éxécute, le bouton change de place.
#je n'est pas compris ce que vous m'avez dit sur discord.
#jesuisbloqué
#help