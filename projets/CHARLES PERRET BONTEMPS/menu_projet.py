from tkinter import *

def quitter():
    root.destroy()








def vrai_faux():
    root.state('iconic')
    import random

    def lancerJeu():
        Fenetre1.destroy()
        Fenetre2 = Tk()## Deuxième fenêtre
        Fenetre2.geometry('300x450')
        Fenetre2.title("Lancement du jeu")
        text1=Label(Fenetre2, text="Votre pseudo")
        text1.place(x=180, y=140)
        w=Entry(Fenetre2)
        w.place(x=50,y=150)
        pseudo=w.get()
        Bouton_cliquez=Button(Fenetre2,text="Ok", command=choixUnivers, bg="gray")
        Bouton_cliquez.place(x=75,y=250)
        Fenetre2.mainloop()
        #pseudo = input('Veuillez entrer votre pseudo\n')

    def choixUnivers():
        Fenetre2.destroy() #ici est le problème...
        Fenetre3 = Tk()
        text1=Label(Fenetre3, text="pseudo")
        text1.place(x=180, y=100)
        Fenetre3.title("Choix de l'univers")
        pseudo2 = pseudo
        pseudo = 'score_' + pseudo + '.txt'
        choix_univers = input('Nous avons deux thèmes à vous proposer, jeux video(1) ou histoire de France(2)\nchoisissez'
                              ' votre univers : 1 ou 2\n')
        if choix_univers == '1':
            Fichier_lecture = open('univers_jeu_video.txt', 'r')
        else:
            Fichier_lecture = open('univers_histoire.txt', 'r')
        print("----------Vous pouvez arrêter votre partie quand vous le voulez, il vous suffit d'écrire 'non' lors d'une "
              "réponse à une question.---------\n"
              "--------------------------Votre score sera enregistré et vous pourrez l'observer lors de votre prochain "
              "essai--------------------------\n")
        contenu = Fichier_lecture.read()
        ligne = contenu.split('/')
        question_pose = []
        affirmation = 1
        score = 0
        nb_question = len(ligne) - 1
        print('Il y a', nb_question, 'questions dans le thème choisi')
        nb_question = int(input('Combien de question voulez vous avoir ?\nchoisissez : '))
        arret_questionnaire = 'non'

        for loop in range(nb_question):
            numero = ''
            reponse = ''
            reponse2 = ''
            question = ''
            flag_reponse2 = False
            flag_question = False
            flag_numero = True
            flag_reponse = False
            x = random.randint(0, nb_question - 1)
            while x in question_pose:
                x = random.randint(0, nb_question - 1)
            question_pose.append(x)

            for lettre in ligne[x]:
                if lettre == ')':
                    flag_numero = False
                    flag_reponse = True
                elif flag_numero == True:
                    numero = numero + lettre
                elif flag_reponse == True:
                    reponse = reponse + lettre
                if lettre == '|':
                    flag_reponse2 = True
                    flag_reponse = False
                elif flag_reponse2 == True:
                    reponse2 = reponse2 + lettre
                if lettre == '(':
                    flag_question = True
                    flag_reponse2 = False
                elif flag_question == True:
                    question = question + lettre

            print('affirmation', affirmation, ':', question)
            affirmation = affirmation + 1
            reponse = str(reponse[:-1])
            reponse2 = str(reponse2[:-1])
            rep = input("Vrai ou Faux ? \n ")

            if rep == 'non':
                arret_questionnaire = 'oui'

            if reponse == rep:
                print("Bravo")
                score = score + 1
            else:
                print("Dommage =) <3")
                print('La réponse était', reponse, '\n', reponse2)
            contenu[x + 1]
            x = x + 1
            print('')
            if arret_questionnaire == 'oui':
                break
        print('Vous avez finis le questionnaire, votre score est de', score, 'bonnes réponses sur', nb_question, 'questions')
        if score > nb_question / 2:
            print('Félicitation')
        else:
            print('Vous ferez mieux la prochaine fois')


            #def quitter():
            #   rootC.destroy()
            #   root.state('normal')


            fichier_score=open(pseudo,'w')

            fichier_score.write(pseudo2)
            fichier_score.write( ", lors de votre dernière partie, vous aviez choisi l'univers ")
            fichier_score.write(str(choix_univers))
            fichier_score.write('\n')
            fichier_score.write("Vous aviez alors eut ")
            fichier_score.write(str(nb_question))
            fichier_score.write(" questions")
            fichier_score.write('\n')
            fichier_score.write("Votre score était de : ")
            fichier_score.write(str(score))

            fichier_score.close

            fichier_score=open(pseudo, 'a')
            fichier_score.write('')


    Fenetre1 = Tk() ##première fenêtre
    Fenetre1.geometry('300x450')
    Fenetre1.title("Vrai ou Faux ?")
    Bouton_cliquez=Button(Fenetre1,text="Lancer le jeu Vrai ou Faux", command=lancerJeu, bg="gray")
    Bouton_cliquez.place(x=75,y=250)
    Fenetre1.mainloop()









def calculatrice():
    root.state('iconic')

    def quitter():
        rootC.destroy()
        root.state('normal')

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




root = Tk()
root.title('Multi-jeux')


image = PhotoImage(file='menu jeu.gif')

canvas = Canvas(root)
canvas.pack(fill='both', expand=1)
canvas.create_image(770, 400, image=image, anchor=CENTER)
root.geometry('1920x1080')





button=Button(root, text="Quitter", command=quitter, bg="red", font=10)
button2=Button(root, text="Vrai ou Faux", command=vrai_faux, bg="light blue", font=10)
button3=Button(root, text="calculatrice", command=calculatrice, bg="light blue", font=10)
button4=Button(root, text="Pendu", bg="light blue", font=10)
button5=Button(root, text="Démineur", bg="light blue", font=10)



button.place(x=1290, y=690)
button2.place(x=180, y=230)
button3.place(x=180, y=500)
button4.place(x=1230, y=210)
button5.place(x=1230, y=480)

root.mainloop()

