from tkinter import *
import random
from tkinter.messagebox import *

def vouf ():

    class Interface:            #Déclaration de la classe permettant d'utiliser les variables entre les méthodes, sans déclarer les varibales en global.

        def __init__(self):         #Déclaration du constructeur de la fenêtre principale pour déclarer tous les widgets inclus dans cette fenêtre.
            self.fenetre = Tk()         #Déclaration de la fenêtre avec tkinter.
            frame1 = Frame(self.fenetre, borderwidth=2, )           #Déclaration des frames(cadres) pour une zone texte.
            frame1.pack(side=TOP, padx=100, pady=30)
            frame2 = Frame(self.fenetre)            #Une zone boutons pour le quizz.
            frame2.pack(side=TOP, padx=100, pady=30)
            frame3 = Frame(self.fenetre)            #Une zone boutons fixe, quitter et valider.
            frame3.pack(side=BOTTOM, padx=30, pady=30)

            self.fenetre.title("Vrai/Faux")         #Titre de la fenêtre.
            self.message = Label(frame1, text="Votre pseudo : ")
            self.message.pack()
            self.entry = Entry(frame1)          #Zone d'entrée de texte par l'utilisateur pour le pseudo.
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

            self.rep = StringVar()

            self.bouton1 = Radiobutton(frame2, variable=self.rep, text="Vrai", value="Vrai")
            self.bouton2 = Radiobutton(frame2, variable=self.rep, text="Faux", value="Faux")

            self.boutonStop = Button(frame2, text="Stop", state=DISABLED, command=self.Fin)

            self.boutonSuivant = Button(frame2, text="", state=DISABLED, command=self.Suite2)

            self.varBut = IntVar()
            self.br = Radiobutton(frame2, variable=self.varBut, text="Jeux Vidéo", value=1)
            self.br2 = Radiobutton(frame2, variable=self.varBut, text="Histoire de France", value=2)

            self.nb_question = IntVar()
            self.nbQuestion = Scale(frame2, orient="vertical")

            self.univers = 0

            self.fenetre.mainloop()

        def quit(self):         #Fonction pour quitter le jeu.
            self.fenetre.destroy()

        def Jeu(self):          #Début du "Jeu" principale.
            self.pseudo = self.entry.get()          #Récupération du pseudo de l'entry après avoir appuyé sur le bouton.
            self.entry.pack_forget()            #Cache la zone d'entrée de texte.


            self.message["text"] = self.pseudo + " , choisissez votre univers : "
            self.pseudo2 = self.pseudo
            self.pseudo = 'score_' + self.pseudo + '.txt'           #Nom du fichier .txt enregistrant le score du joueur.
            self.message3["text"] = "Nous avons deux thèmes à vous proposer, Jeux Vidéo ou Histoire de France"

            self.br.pack(side="top", expand=1)         #Affiche les boutons de choix d'univers.
            self.br2.pack(side="left", expand=1)
            self.boutonValider["command"] = self.Suite

        def Suite(self):

            self.message3.pack_forget()
            self.univers = IntVar()
            self.univers = self.varBut.get()        #Récupère la variable.


            self.br.pack_forget()           #Cache les boutons de choix d'univers.
            self.br2.pack_forget()

            if self.univers == 1:           #Condition pour ouvrir le bon fichier de questions en fonction de l'univers.
                Fichier_lecture = open('univers_jeu_video.txt', 'r')
            elif self.univers == 2:
                Fichier_lecture = open('univers_histoire.txt', 'r')


            self.contenu = Fichier_lecture.read()           #Enregistre le contenu du fichier dans la variable.
            self.ligne = self.contenu.split('/')            #Permet de délimiter les questions avec le /
            nb_question = len(self.ligne) - 1
            self.question_pose = []
            self.affirmation = 1
            self.score = 0
            nb_question=str(nb_question)            #Conversion de "int" en "str" pour l'affichage en "str".
            self.message["text"] = "Il y a " + nb_question + " questions dans le thème choisi"
            self.message2["text"] = "combien de questions voulez vous avoir ?\n" \
                                    "choisissez : "

            nb_question=int(nb_question)            #Puis reconversion en "int".
            self.nbQuestion.configure(from_=1, to=nb_question,          #Scale qui permet de choisir le nombre de questions.
                                    resolution=1, tickinterval=1, length=150,
                                    label="Nombres de question(s)")
            self.nbQuestion.pack(side="right")          #Affichage de la scale.
            self.boutonValider["command"] = self.recupNbQuestion            #Modification de la commande du bouton Valider pour lancer la suite du programme.

        def recupNbQuestion(self):
            self.message3["text"] = "---------- Vous pouvez arrêter votre partie quand vous le voulez, il vous suffit " \
                                    "d'appuyer sur le bouton Stop ---------\n"\
                                    "-------- Votre score sera enregistré dans un fichier texte --------"
            self.message3.pack()
            self.message.pack_forget()
            self.message2.pack_forget()
            self.boutonValider.pack_forget()

            self.nb_question = self.nbQuestion.get()            #En permettant de récupérer la valeur de la scale (nb de questions).
            self.nbQuestion.pack_forget()
            self.boutonSuivant.pack()
            self.boutonSuivant.configure(text="Commencer le jeu", command=self.Suite2, state=NORMAL)           #Reconfiguration du bouton Suivant.

            self.nbQuestions = 0

        def Suite2(self):

            self.boutonValider.pack(side="right", padx=150, pady=10)
            self.boutonValider["state"] = NORMAL

            if self.nbQuestions < self.nb_question:         #Condition pour lancer autant de questions que voulu, avec un compteur de questions posé(es).
                numero = ''
                self.reponse = ''
                self.reponse2 = ''
                question = ''
                flag_reponse2 = False           #Définit les flag des questions et réponses pour la reconnaissance de celles-çi.
                flag_question = False
                flag_numero = True
                flag_reponse = False
                self.x = random.randint(0, self.nb_question - 1)            #Générateur de chiffre aléatoire pour questions aléatoires.
                while self.x in self.question_pose:                     #Condition pour ne pas reposer deux fois la même question.
                    self.x = random.randint(0, self.nb_question - 1)
                self.question_pose.append(self.x)

                for lettre in self.ligne[self.x]:           #Boucle de reconnaissances des numéros de question, du vrai/faux, réponses et questions dans le fichier .txt.
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
                self.message3["text"] = "Affirmation " +  self.affirmation +  ' : ' + question           #Affichage de la question.
                self.message3.pack(side=BOTTOM)
                self.affirmation = int(self.affirmation)
                self.affirmation = self.affirmation + 1
                self.reponse = str(self.reponse[:-1])
                self.reponse2 = str(self.reponse2[:-1])
                self.boutonSuivant["state"] = DISABLED          #Tant que l'utilisateur ne valide pas de réponse, il ne peut pas passer à la question suivante.
                self.boutonSuivant["text"] = "Question suivante"
                self.bouton1.pack(side="top", expand=1)
                self.bouton2.pack(side="top", expand=1)
                self.bouton1.select()
                self.boutonSuivant.pack(side="bottom", pady=10)
                self.boutonStop.pack(side="bottom", pady=5)
                self.boutonStop["state"] = NORMAL
                self.boutonValider["command"] = self.Suite3         #Modification de la commande du bouton Valider pour aller à la vérification de la réponse de l'utilisateur (suite du programme).

            else :
                self.boutonStop.pack_forget()     #Condition quand le quizz touche à sa fin.
                self.boutonValider.pack_forget()
                self.bouton1.pack_forget()
                self.bouton2.pack_forget()
                self.message["text"] = "ERROR 404"
                self.message.pack(side=TOP)
                self.message2["text"] = "¯\_(ツ)_/¯ "
                self.message2.pack(side=TOP)
                self.message3["text"] = "Appuyez une nouvelle fois sur le bouton 'Suivant'"         #La première action du bouton suivant vérifie le nombre de question et change la commande.
                self.message3.pack()
                self.boutonSuivant.configure(text="Suivant", command=self.Fin)          #La deuxième action du bouton suivant lance la fin du programme.


        def Suite3(self):
            self.repo = self.rep.get()        #Récupération de la réponse de l'utilisateur par les radioboutons vrai et faux.
            self.boutonValider["state"] = DISABLED

            if self.repo == self.reponse:          #Condition pour reconnaitre la réponse vrai ou fausse.
                self.message3["text"] = "Bravo"
                self.score = self.score + 1

            elif self.repo != self.reponse:
                self.message3["text"] = "Dommage =)   \n"\
                                        "La réponse était " + self.reponse + "\n" + self.reponse2

            self.boutonSuivant.configure(text="Question suivante", command=self.Suite2, state=NORMAL)           #Changement de la commande du bouton suivant pour retourner à la méthode suite2, pour poser la question suivante, ou la fin du porgramme.
            self.nbQuestions = self.nbQuestions + 1         #Incrémentation pour le compteur du nb de questions posé(es).
            self.contenu[self.x + 1]
            self.x = self.x + 1



        def Fin(self):

            self.boutonSuivant.pack_forget()            #Cache tous les boutons et messages inutiles à la fin du programme, pour éviter toutes action intempestives des boutons.
            self.boutonSuivant["state"] = DISABLED
            self.boutonValider.pack_forget()
            self.boutonValider["state"] = DISABLED
            self.bouton1.pack_forget()
            self.bouton2.pack_forget()
            self.message3.pack_forget()
            self.boutonStop.pack_forget()
            self.score=str(self.score)
            self.nb_question = str(self.nb_question)
            if self.nb_question == "1":         #Condition pour l'affichage pluriel du texte en fonction du nb de question(s).
                self.message["text"] = "Vous avez fini le questionnaire, votre score est de " + self.score +" bonne réponse sur " + \
                                        self.nb_question + " question"           #Affiche la proportion de bonne réponse par rapport au nombre de questions choisit.
            else:
                self.message["text"] = "Vous avez fini le questionnaire, votre score est de " + self.score + " bonne(s) réponse(s) sur " + \
                              self.nb_question + " questions"           #Pareil
            self.score = int(self.score)
            self.nb_question = int(self.nb_question)
            if self.score > self.nb_question / 2:           #Condition pour félicitation si le joueur a plus de la moyenne de bonne réponse.
                self.message2["text"] = "Félicitations"
            else:
                self.message2["text"] = "Vous ferez mieux la prochaine fois !"

            showinfo(title="INFORMATION", message="N'oubliez pas de vous essayer maintenant au calcul mental avec notre calculatrice graphique !")            #Petite alerte pour inciter l'utilisateur à utiliser les autres applications.
            fichier_score = open(self.pseudo, 'w')          #Ouvre le fichier score propre au joueur et inscrit le score.

            fichier_score.write(self.pseudo2)
            fichier_score.write(", lors de votre dernière partie, vous aviez choisi l'univers ")
            fichier_score.write(str(self.univers))
            fichier_score.write('\n')
            fichier_score.write("Vous aviez alors eu ")
            fichier_score.write(str(self.nb_question))
            fichier_score.write(" questions")
            fichier_score.write('\n')
            fichier_score.write("Votre score était de : ")
            fichier_score.write(str(self.score))

            fichier_score.close

            fichier_score = open(self.pseudo, 'a')
            fichier_score.write('')


    f=Interface()           #Définit la classe interface dans la fenêtre tkinter.
vouf()
