from tkinter import *
import random
from tkinter.messagebox import *


class Interface:            #déclaration de la classe permettant d'utiliser les variables entre les méthodes, sans déclarer les varibales en global

    def __init__(self):         #déclaration du constructeur de la fenêtre principale pour déclarer tout les widgets inclus dans cette fenêtre
        self.fenetre = Tk()         #déclaration de la fenêtre avec tkinter
        frame1 = Frame(self.fenetre, borderwidth=2, )           #déclaration des frames (cadres) pour une zone texte
        frame1.pack(side=TOP, padx=100, pady=30)
        frame2 = Frame(self.fenetre)            #une zone boutons pour le quizz
        frame2.pack(side=TOP, padx=100, pady=30)
        frame3 = Frame(self.fenetre)  # une zone boutons fixe, (quitter et valider)
        frame3.pack(side=BOTTOM, padx=30, pady=30)

        self.fenetre.title("Vrai/Faux")         #titre de la fenêtre
        self.message = Label(frame1, text="Votre pseudo : ")
        self.message.pack()
        self.entry = Entry(frame1)          #zone d'entrée de texte par l'utilisateur pour le pseudo
        self.entry.pack(side="top")
        self.message2 = Label(frame1, text='')
        self.message2.pack(side="top")
        self.message3 = Label(frame1, text='')
        self.message3.pack(side="top")
        self.message4 = Label(frame1, text='')
        self.stop = ''

        self.boutonQuitter = Button(frame3, text="QUITTER", command=self.quit, bg="red", fg="white")
        self.boutonQuitter.pack(side="left", padx=150, pady=10)

        self.boutonValider = Button(frame3, text="VALIDER", command=self.Jeu, bg="green", fg="white")
        self.boutonValider.pack(side="right", padx=150, pady=10)

        self.rep = IntVar()

        self.bouton1 = Radiobutton(frame2, variable=self.rep, text="Vrai", value=1)
        self.bouton2 = Radiobutton(frame2, variable=self.rep, text="Faux", value=2)

        self.boutonStop = Button(frame2, text="Stop", state=DISABLED, command=self.Fin)

        self.boutonSuivant = Button(frame2, text="", state=DISABLED, command=self.Suite2)

        self.varBut = IntVar()
        self.br = Radiobutton(frame2, variable=self.varBut, text="Jeux Vidéo", value=1, command=self.Suite)
        self.br2 = Radiobutton(frame2, variable=self.varBut, text="Histoire de France", value=2, command=self.Suite)

        self.nb_question = IntVar()
        self.nbQuestion = Scale(frame2, orient="vertical")

        self.univers = 0

        self.fenetre.mainloop()

    def quit(self):         #fonction pour quitter le jeu
        self.fenetre.destroy()

    def Jeu(self):          #début du Jeu principale
        self.pseudo = self.entry.get()          #récupération du pseudo de l'entry après avoir appuyé sur le bouton
        self.entry.pack_forget()            #cache la zone d'entrée de texte


        self.message["text"] = self.pseudo + " , choisissez votre univers : "
        self.pseudo2 = self.pseudo
        self.pseudo = 'score_' + self.pseudo + '.txt'           #nom du fichier .txt enregistrant le score du joueurs
        self.message3["text"] = "Nous avons deux thèmes à vous proposer, jeux video ou histoire de France"

        self.br.pack(side="top", expand=1)         #affiche les bouton de choix d'univers
        self.br2.pack(side="left", expand=1)

    def Suite(self):

        self.br["state"] = DISABLED             #désactive les boutons de choix d'univers
        self.br2["state"] = DISABLED
        self.univers = IntVar()
        self.univers = self.varBut.get()        #récupère la variable


        self.br.pack_forget()           #cache les boutons de choix d'univers
        self.br2.pack_forget()

        if self.univers == 1:           #condition pour ouvrir le bon fichier de questions en fonction de l'univers
            Fichier_lecture = open('univers_jeu_video.txt', 'r')
        elif self.univers == 2:
            Fichier_lecture = open('univers_histoire.txt', 'r')
        self.message3["text"] = "----------Vous pouvez arrêter votre partie quand vous le voulez, il vous suffit " \
                                "d'appuyer sur le bouton Stop.---------\n"\
                                "--------Votre score sera enregistré dans un fichier texte--------"


        self.contenu = Fichier_lecture.read()           #enregistre le contenu du fichier dans la variable
        self.ligne = self.contenu.split('/')            #permet de délimiter les question avec le /
        nb_question = len(self.ligne) - 1
        self.question_pose = []
        self.affirmation = 1
        self.score = 0
        nb_question=str(nb_question)            #conversion de int en str pour l'affichage en str
        self.message["text"] = "Il y a " + nb_question + " questions dans le thème choisi"
        self.message2["text"] = "combien de question voulez vous avoir ?\n" \
                                "choisissez : "

        nb_question=int(nb_question)            #puis reconversion en int
        self.nbQuestion.configure(from_=1, to=nb_question,          #scale qui permet de choisir le nombre de questions
                                resolution=1, tickinterval=1, length=150,
                                label="Nombres de question")
        self.nbQuestion.pack(side="right")          #affichage de la scale
        self.boutonValider["command"] = self.recupNbQuestion            #modification de la commande du bouton valider pour lancer la suite du programme

    def recupNbQuestion(self):
        self.nb_question = self.nbQuestion.get()            #en permettant de récupérer la valeur de la scale (nb de questions)
        self.nbQuestion.pack_forget()
        self.boutonSuivant.pack()
        self.boutonSuivant.configure(text="Question Suivante", command=self.Suite2, state=NORMAL)           #reconfiguration du bouton suivant

        self.nbQuestions = 0

    def Suite2(self):

        self.message["text"] = ""
        self.message2["text"] = ""
        self.message3["text"] = ""

        if self.nbQuestions < self.nb_question:         #condition pour lancer autant de questions que voulu, avec un compteur de questions posé(es)
            numero = ''
            self.reponse = ''
            self.reponse2 = ''
            question = ''
            flag_reponse2 = False           #définit les flag des questions et réponses pour la reconnaissance de celles çi
            flag_question = False
            flag_numero = True
            flag_reponse = False
            self.x = random.randint(0, self.nb_question - 1)            #générateur de chiffre aléatoire pour questions aléatoires
            while self.x in self.question_pose:                     #condition pour ne pas reposer deux fois la même question
                self.x = random.randint(0, self.nb_question - 1)
            self.question_pose.append(self.x)

            for lettre in self.ligne[self.x]:           #boucle de reconnaissances des numéros de question, du vrai/faux, réponses et questions dans le fichier .txt
                if lettre == ')':
                    flag_numero = False
                    flag_reponse = True
                elif flag_numero == True:
                    numero = numero + lettre
                elif flag_reponse == True:
                    self.reponse = self.reponse + lettre
                if lettre == '|':
                    flag_reponse2 = True
                    flag_reponse = False
                elif flag_reponse2 == True:
                    self.reponse2 = self.reponse2 + lettre
                if lettre == '(':
                    flag_question = True
                    flag_reponse2 = False
                elif flag_question == True:
                    question = question + lettre
            self.affirmation = str(self.affirmation)
            self.message3["text"] = "affirmation " +  self.affirmation +  ' : ' + question           #affichage de la question
            self.affirmation = int(self.affirmation)
            self.affirmation = self.affirmation + 1
            self.reponse = str(self.reponse[:-1])
            self.reponse2 = str(self.reponse2[:-1])
            self.boutonSuivant["state"] = DISABLED          #tant que l'utilisateur ne valide pas de réponse, il ne peut passer à la question suivante
            self.bouton1.pack(side="top", expand=1)
            self.bouton2.pack(side="top", expand=1)
            self.boutonSuivant.pack(side="bottom", pady=10)
            self.boutonStop.pack(side="bottom", pady=5)
            self.boutonStop["state"] = NORMAL
            self.boutonValider["command"] = self.Suite3         #modification de la commande du bouton valider pour aller a la vérification de la réponse de l'utilisateur (suite du programme)

        else :          #condition quand le quizz touche à sa fin
            self.message["text"] = "ERROR 404"
            self.message2["text"] = "¯\_(ツ)_/¯ "
            self.message3["text"] = "appuyez une nouvelle fois sur le bouton 'Suivant'"         #la première action du bouton suivant vérifie le nombre de question et change la commande
            self.boutonSuivant.configure(text="Suivant", command=self.Fin)          #la deuxième action du bouton suivant lance la fin du programme


    def Suite3(self):
        self.repo = self.rep.get()          #récupération de la réponse de l'utilisateur par les radioboutons vrai et faux

        if self.repo == 1:          #condition pour reconnaitre la réponse vrai ou fausse
            self.message3["text"] = "Bravo"
            self.score = self.score + 1

        elif self.repo == 2:
            self.message3["text"] = "Dommage =) \n"\
                                    "La réponse était " + self.reponse + "\n" + self.reponse2

        self.boutonSuivant.configure(text="Question suivante", command=self.Suite2, state=NORMAL)           #changement de la commande du bouton suivant pour retourner a la méthode suite2, pour poser la question suivante, ou la fin du porgramme
        self.nbQuestions = self.nbQuestions + 1         #incrémentation pour le compteur du nb de question posé(es)
        self.contenu[self.x + 1]
        self.x = self.x + 1




    def Fin(self):

        self.boutonSuivant.pack_forget()            #cache tout les boutons et messages inutile a la fin du programme, pour éviter toute action intempestive des boutons
        self.boutonSuivant["state"] = DISABLED
        self.boutonValider.pack_forget()
        self.boutonValider["state"] = DISABLED
        self.bouton1.pack_forget()
        self.bouton2.pack_forget()
        self.message3.pack_forget()
        self.boutonStop.pack_forget()
        self.score=str(self.score)
        self.nb_question = str(self.nb_question)
        self.message["text"] = "Vous avez finis le questionnaire, votre score est de " + self.score + " bonnes réponses sur " + \
                                self.nb_question + " questions"           #affiche la proportion de bonne réponse par rapport au nombre de questions choisit
        self.score = int(self.score)
        self.nb_question = int(self.nb_question)
        if self.score > self.nb_question / 2:           #condition pour félicitation si le joueur a plus de la moyenne de bonne réponse
            self.message2["text"] = "Félicitations"
        else:
            self.message2["text"] = "Vous ferez mieux la prochaine fois"

        showinfo(title = "INFORMATION", message = "N'oubliez pas de vous essayer maintenant au calcul mental avec notre calculatrice graphique")            #petite alerte pour inciter l'utilisateur à utiliser les autres applications
        fichier_score = open(self.pseudo, 'w')          #ouvre le fichier score propre au joueur et inscrit le score

        fichier_score.write(self.pseudo2)
        fichier_score.write(", lors de votre dernière partie, vous aviez choisi l'univers ")
        fichier_score.write(str(self.univers))
        fichier_score.write('\n')
        fichier_score.write("Vous aviez alors eut ")
        fichier_score.write(str(self.nb_question))
        fichier_score.write(" questions")
        fichier_score.write('\n')
        fichier_score.write("Votre score était de : ")
        fichier_score.write(str(self.score))

        fichier_score.close

        fichier_score = open(self.pseudo, 'a')
        fichier_score.write('')


f=Interface()           #définit la classe interface dans la fenetre tkinter







