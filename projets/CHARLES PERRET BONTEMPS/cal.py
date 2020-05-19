
from tkinter import *
def calcul():


    def quitter():
        rootC.destroy()

    def add():
        x=w.get()
        y=z.get()
        t=ajouter(x,y)
        label2.config(text="Résultat: "+str(t))

    def ajouter(x,y):
        try:
            e=float(x)+float(y)
        except ValueError:
            e=str(x)+str(y)
        except TypeError:
            return False
        return e

    def div():
        x=w.get()
        y=z.get()
        t=division(x,y)
        label2.config(text="Résultat: "+str(t))

    def division(x,y):
        try:
            r=float(x)/float(y)
        except ValueError:
            return "impossible de divisé par une chaine de caractère"
        except TypeError:
            return False
        except ZeroDivisionError:
            return "imposible de divisé par 0"
        return r

    def mult():
        x=w.get()
        y=z.get()
        t=multiplication(x,y)
        label2.config(text="Résultat: "+str(t))

    def multiplication(x,y):
        try:
            p=float(x)*float(y)
        except TypeError:
            return False
        except ValueError:
            return "vous ne pouvez pas multiplié par une chaine de caractère"
        return p

    def sous():
        x=w.get()
        y=z.get()
        t=soustraction(x,y)
        label2.config(text="Résultat: "+str(t))

    def soustraction(x,y):
        try:
            p=float(x)-float(y)
        except TypeError:
            return False
        except ValueError:
            return "vous ne pouvez pas soustraire une chaine de caractère"
        return p

    def pourcent():
        x=w.get()
        y=z.get()
        t=pourcentage(x,y)
        label2.config(text="Résultat: "+str(t))
    def pourcentage(x,y):
        try:
            p=float(x)/100
        except ValueError:
            return "impossible de mettre une chaine de caractère en %"
        except TypeError:
            return False
        return p



    rootC=Tk()
    rootC.title('calculatrice sécurisée')
    rootC.geometry("370x350")
    rootC.configure(bg = "light blue")

    label = Label(rootC, text="Inscrivez vos valeurs", bg="light green")
    label2 = Label(rootC, text="Résultat: ", bg="yellow")
    button=Button(rootC, text="Addition", command=add, fg="blue")
    button2=Button(rootC, text="Soustraction", command=sous, fg="blue")
    button3=Button(rootC, text="Division", command=div, fg="blue")
    button4=Button(rootC, text="Multiplication", command=mult, fg="blue")
    button5=Button(rootC, text="Quitter", command=quitter, bg="red")
    button6=Button(rootC, text="%", command=pourcent, fg="blue")
    w = Entry(rootC)
    z = Entry(rootC)


    button.place(x=10, y=150)
    button2.place(x=90, y=150)
    button3.place(x=190, y=150)
    button4.place(x=270, y=150)
    button5.place(x=300, y=300)
    button6.place(x=10, y=200)
    label.place(x=130, y=50)
    label2.place(x=0, y=250)
    w.place(x=50, y=100)
    z.place(x=200, y=100)
    rootC.mainloop()
calcul()