import random

ListeMots=["banane", "hippopotame", "gendarmerie", "election", "codage",
"imprimmante", "mars", "virus", "continent", "numerique", "tatouages", "permis",
"ordinateur", "panda", "bibliotheque", "camion", "point", "avion", "pont",
"prise"]

Mot=random.choice(ListeMots)
Liste_Mot=[lettre for lettre in Mot]
MotCache=[lettre for lettre in Mot]

def verif_lettre():
    lettre = input("Proposez une lettre: ")
    lettre = lettre.lower()
    global lettre
    if len(lettre)>=1:
        if type(lettre) == type(int):
            print("Les chiffres ne sont pas acceptés, veuillez taper une lettre !")
    if len(lettre)==1:
        if type(lettre)==type(str):
            return lettre
    return



idx=0
for lettre in range(len(Mot)):
    MotCache[idx]='_'
    idx=idx+1
print(MotCache)


nombrtentative=15
print("Vous avez",nombrtentative,"tentatives")
while nombrtentative > 0:
    lettre = verif_lettre()
    if len(lettre)>1:
        if lettre==Mot:
            print("Vous avez trouvez le bon mot !")
            break
    if lettre in Liste_Mot:
        for (i,j) in enumerate(Liste_Mot):
            if j == lettre:
                MotCache[i]=j
        letterfound = MotCache
        print("Vous avez trouvé la lettre suivante :",letterfound)
    else:
        print("Vous n'avez pas proposé une bonne lettre, réessayez !")
        nombrtentative=nombrtentative-1
##    utilisateur=deviner_mot(Mot, MotCache,lettre)
    print("Vous avez",nombrtentative,"tentatives")

    if nombrtentative == 0:
        print("Vous avez épuisé toutes vos chances de gagner, vous avez donc perdu, adieu !")






