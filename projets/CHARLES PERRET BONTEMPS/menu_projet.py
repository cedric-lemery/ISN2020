from tkinter import *
import pygame





def quitter():
    root.destroy()



def vrai_faux():
    root.destroy()
    import vrai_ou_faux_projetISN
    vrai_ou_faux_projetISN.vouf()


def calculatrice():
    import cal
    cal.calcul()


def Mario():
    root.destroy()
    pygame.quit()
    import module1
    module1.menu()


def pendu():
    import pendu
    pendu.jeu()

pygame.init()
root = Tk()
root.title('Multi-jeux')


image = PhotoImage(file='menu2.0.gif')

canvas = Canvas(root)
canvas.pack(fill='both', expand=1)
w,h = root.winfo_screenwidth(), root.winfo_screenheight()

window_resolution = (1400, 800)
pygame.display.set_caption("jouer du son")
window_surface = pygame.display.set_mode(window_resolution)
son = pygame.mixer.Sound("epic music.ogg")
son.play(loops=-1)
son.set_volume(0.2)
pygame.display.flip()



image = image.subsample(1)
canvas.create_image(w//2, h//2, image=image, anchor=CENTER)
root.wm_attributes("-fullscreen","1")





button=Button(root, text="Quitter", command=quitter, bg="red", font=10)
button2=Button(root, text="Vrai ou Faux", command=vrai_faux, bg="light blue", font=10)
button3=Button(root, text="calculatrice", command=calculatrice, bg="light blue", font=10)
button4=Button(root, text="Pendu", bg="light blue", command=pendu, font=10)
button5=Button(root, text="Mario Bros", bg="light blue",command=Mario, font=10)



button.place(x=w/1.2, y=h/1.25)
button2.place(x=w/6.2, y=h/3)
button3.place(x=w/6.2, y=h/1.70)
button4.place(x=w/1.28, y=h/3.1)
button5.place(x=w/1.28, y=h/1.70)

root.mainloop()
pygame.quit()
quit()
