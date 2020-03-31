import random

ListeMots=["banane", "hippopotame", "gendarmerie", "election", "codage",
"imprimmante", "mars", "virus", "continent", "numerique", "tatouages", "permis",
"ordinateur", "panda", "bibliotheque", "camion", "point", "avion", "pont",
"prise"]

Mot=random.choice(ListeMots)
MotCache=[lettre for lettre in Mot]

def lettre():
    choix_lettre = input("Proposez une lettre: ")
    choix_lettre = choix_lettre.lower()
    global choix_lettre
    if len(lettre)>1:
        print("Votre lettre n'est pas valable")
        return lettre()
    else:
        return lettre

idx=0
for lettre in range(len(Mot)):
    MotCache[idx]='_'
    idx=idx+1
print(MotCache)


nombrtentative=10
print("Vous avez",nombrtentative,"tentatives")
for loop in range(nombrtentative):
    lettre= lettre()
    utilisateur=deviner_mot(Mot, MotCache, choix_lettre)
    nombrtentative=nombrtentative-1
    print("Vous avez",nombrtentative,"tentatives")


##for loop in range(nombrtentative):
##    if recup_lettre in MotCache:
##        print("Bravo, vous avez une des lettres")
##        deviner_mot(Mot,MotCache, choix_lettre)
##    else:
##        nombrtentative=nombrtentative-1
##        print("Il vous reste",nombrtentative,"tentatives")
##    if nombrtentative==0:
##        print("Vous avez perdu")


