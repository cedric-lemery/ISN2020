# Créé par erago, le 07/04/2020 avec EduPython

from tkinter import*

def quitter():
    Fenetre.destroy()


Fenetre=Tk()
Fenetre.title('Mastermind.exe')
Fenetre.wm_attributes("-fullscreen","1")
Fenetre.configure(bg="royalblue")




Mon_bouton5 = Button(Fenetre,text="     X     ", bg="darkred", command=quitter)
Mon_bouton5.place(x=1850,y=20)


Fenetre.mainloop()

#pour ce petit programme le bouton quitter est bien placé mais si un autre ordinateur n'ayant pas les memes dimensions l'éxécute, le bouton change de place.
#je n'est pas compris ce que vous m'avez dit sur discord.
#jesuisbloqué
#help