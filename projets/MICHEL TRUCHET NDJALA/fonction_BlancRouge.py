import random

ListeJoueur=[0,7,3,4]
ListeAlea=[0,1,3,7]

def Fonc_BlancRouge():
    Nblanc=0
    Nrouge=0

    if ListeJoueur[0] in ListeAlea:
        if ListeJoueur[0] == ListeAlea[0]:
            Nrouge=Nrouge+1
        else:
            Nblanc=Nblanc+1
    if ListeJoueur[1] in ListeAlea:
        if ListeJoueur[1] == ListeAlea[1]:
            Nrouge=Nrouge+1
        else:
            Nblanc=Nblanc+1
    if ListeJoueur[2] in ListeAlea:
        if ListeJoueur[2] == ListeAlea[2]:
            Nrouge=Nrouge+1
        else:
            Nblanc=Nblanc+1
    if ListeJoueur[3] in ListeAlea:
        if ListeJoueur[3] == ListeAlea[3]:
            Nrouge=Nrouge+1
        else:
            Nblanc=Nblanc+1
    return Nblanc,Nrouge



z= Fonc_BlancRouge()
print(z)