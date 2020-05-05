from tkinter import *
import random
import time

class Interface(Frame):

    def __init__(self, fenetre):
        self.univers = 0
        Frame.__init__(self, fenetre, width = 768, height=576)
        self.pack()
        self.message = Label(self, text="Votre pseudo : ")
        self.message.pack()
        self.entry = Entry(fenetre)
        self.entry.pack(side="top")
        self.message2 = Label(self, text='')
        self.message2.pack(side="top")
        self.message3 = Label(self, text='')
        self.message3.pack(side="top")
        self.stop = ''
        self.boutonQuitter = Button(self, text="Quitter", command=self.quit)
        self.boutonQuitter.pack(side="left")

        self.boutonCliquer = Button(self, text="Valider", fg="red", command=self.Jeu)
        self.boutonCliquer.pack(side="right")

        self.bouton1 = Button(self, text="", state=DISABLED, )
        self.bouton1.pack(side="top")

        self.bouton2 = Button(self, text="", state=DISABLED, )
        self.bouton2.pack(side="top")

        self.boutonStop = Button(self, text="Stop", state=DISABLED, command=self.Stop)
        self.boutonStop.pack(side="top")



    def Vrai(self):
        self.rep = "Vrai"

    def Faux(self):
        self.rep = "Faux"

    def Stop(self):
        self.stop = "STOP"

    def Jeu(self):
        self.rep = ''
        self.pseudo = self.entry.get()

        self.message2["text"] = "Vous trouverez dans vos dossier un fichier joignant vos résultats" #problème d'affichage

        self.message["text"] = "Choix de l'univers"
        self.pseudo2 = self.pseudo
        self.pseudo = 'score_' + self.pseudo + '.txt'
        self.message3["text"] = "Nous avons deux thèmes à vous proposer, jeux video(1) ou histoire de France(2)\n" \
                                "choisissez votre univers : 1 ou 2"


        liste = Listbox(fenetre)
        liste.insert(1, "Jeux Vidéo")
        liste.insert(2, "histoire de France")
        liste.pack()


    def Suite(self):

        if self.univers == 1:
            Fichier_lecture = open('univers_jeu_video.txt', 'r')
        elif self.univers == 2:
            Fichier_lecture = open('univers_histoire.txt', 'r')
        self.message2["text"] = "----------Vous pouvez arrêter votre partie quand vous le voulez, il vous suffit " \
                                "d'appuyer sur le bouton Stop.---------\n"\
                                "--------------------------Votre score sera enregistré et vous pourrez l'observer" \
                                "lors de votre prochain essai--------------------------\n"


        contenu = Fichier_lecture.read()
        ligne = contenu.split('/')
        nb_question = len(ligne) - 1
        self.question_pose = []
        self.affirmation = 1
        self.score = 0
        self.message["text"] = "Il y a", nb_question, "questions dans le thème choisi"
        self.message2["text"] = "combien de question voulez vous avoir ?\n" \
                                "choisissez : "

        self.nb_question = self.entry.get()

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

            self.message["text"] = "affirmation", affirmation, ':', question
            affirmation = affirmation + 1
            reponse = str(reponse[:-1])
            reponse2 = str(reponse2[:-1])
            self.bouton1["text"] = "Vrai"
            self.bouton1["command"] = self.Vrai
            self.bouton1["state"] = NORMAL
            self.bouton2["text"] = "Faux"
            self.bouton2["command"] = self.Faux
            self.bouton2["state"] = NORMAL
            self.boutonStop["state"] = NORMAL

            if self.stop == 'STOP':
                arret_questionnaire = 'oui'

            if reponse == self.rep:
                self.message3["text"] = "Bravo"
                score = score + 1
            else:
                self.message3["text"] = "Dommage =) <3 \n"\
                                        "La réponse était", reponse, "\n", reponse2
            contenu[x + 1]
            x = x + 1
            if arret_questionnaire == 'oui':
                break
        self.message["text"] = "Vous avez finis le questionnaire, votre score est de", score, "bonnes réponses sur", \
                                nb_question, "questions"
        if score > nb_question / 2:
            self.message2["text"] = "Félicitations"
        else:
            self.message2["text"] = "Vous ferez mieux la prochaine fois"

            # def quitter():
            #   rootC.destroy()
            #   root.state('normal')

            fichier_score = open(self.pseudo, 'w')

            fichier_score.write(self.pseudo2)
            fichier_score.write(", lors de votre dernière partie, vous aviez choisi l'univers ")
            fichier_score.write(str(choix_univers))
            fichier_score.write('\n')
            fichier_score.write("Vous aviez alors eut ")
            fichier_score.write(str(nb_question))
            fichier_score.write(" questions")
            fichier_score.write('\n')
            fichier_score.write("Votre score était de : ")
            fichier_score.write(str(score))

            fichier_score.close

            fichier_score = open(self.pseudo, 'a')
            fichier_score.write('')


fenetre = Tk()
fenetre.geometry('300x150')
interface = Interface(fenetre)

interface.mainloop()
interface.destroy




