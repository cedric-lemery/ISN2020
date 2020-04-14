from tkinter import *
import pygame

def quitter():
    root.destroy()



def vrai_faux():
    root.state('iconic')


    import random
    pseudo = input('Veuillez entrer votre pseudo\n')
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




def calculatrice():
    import cal
    cal.calcul()


def Mario():
    root.destroy()
    import module1
    module1.menu()





root = Tk()
root.title('Multi-jeux')


image = PhotoImage(file='menu2.0.gif')

canvas = Canvas(root)
canvas.pack(fill='both', expand=1)
w,h = root.winfo_screenwidth(), root.winfo_screenheight()

image = image.subsample(1)
canvas.create_image(w//2, h//2, image=image, anchor=CENTER)
root.wm_attributes("-fullscreen","1")





button=Button(root, text="Quitter", command=quitter, bg="red", font=10)
button2=Button(root, text="Vrai ou Faux", command=vrai_faux, bg="light blue", font=10)
button3=Button(root, text="calculatrice", command=calculatrice, bg="light blue", font=10)
button4=Button(root, text="Pendu", bg="light blue", font=10)
button5=Button(root, text="Mario Bros", bg="light blue",command=Mario, font=10)



button.place(x=w/1.2, y=h/1.25)
button2.place(x=w/6.2, y=h/3)
button3.place(x=w/6.2, y=h/1.70)
button4.place(x=w/1.28, y=h/3.1)
button5.place(x=w/1.28, y=h/1.70)

root.mainloop()
