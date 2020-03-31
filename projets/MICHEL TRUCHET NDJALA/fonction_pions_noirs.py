import random

ListeJoueur=[6,7,8,4]
ListeAlea=[0,1,2,3]

def Fonc_Noir():
    Nnoir=0

    if ListeJoueur[0] not in ListeAlea:
        Nnoir= Nnoir + 1

    if ListeJoueur[1] not in ListeAlea:
        Nnoir= Nnoir + 1

    if ListeJoueur[2] not in ListeAlea:
        Nnoir= Nnoir + 1

    if ListeJoueur[3] not in ListeAlea:
        Nnoir= Nnoir + 1
    return Nnoir

z= Fonc_Noir()
print(z)

