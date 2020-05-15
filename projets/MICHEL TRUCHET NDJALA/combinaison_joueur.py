import random
def combi_joueur():
    ListeNbre = [1,2,3,4,5,6,7,8] # vous auriez pu l'avoir avec ListeNbre = [i for i in range(1,9)]
    Joueur1=0
    while Joueur1 not in ListeNbre:
        Joueur1=int(input('Choisis un premier nombre compris entre 1 et 8'))
    Joueur2=0
    while Joueur2 not in ListeNbre:
        Joueur2=int(input('Choisis un second nombre compris entre 1 et 8'))
    Joueur3=0
    while Joueur3 not in ListeNbre:
        Joueur3=int(input('Choisis un troisième nombre compris entre 1 et 8'))
    Joueur4=0
    while Joueur4 not in ListeNbre:
        Joueur4=int(input('Choisis un quatrième nombre compris entre 1 et 8'))
        ListeChoix=[Joueur1, Joueur2, Joueur3, Joueur4]
    return ListeChoix

ListeJoueur= combi_joueur()

print(ListeJoueur)



