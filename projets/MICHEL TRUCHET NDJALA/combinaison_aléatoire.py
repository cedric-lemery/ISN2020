import random
import os

def combi_aleatoire():
    ListeNbre = [1,2,3,4,5,6,7,8]
    random.shuffle(ListeNbre)
    Ordi1= ListeNbre[0]
    Ordi2= ListeNbre[1]
    Ordi3= ListeNbre[2]
    Ordi4= ListeNbre[3]
    ListeOrdi = [Ordi1,Ordi2,Ordi3,Ordi4]
    # si on veut une liste de type ["cyan", "orange", etc.]
    #on peut utiliser une liste couleur=['red','blue','cyan', etc.]
    #et on écrit ListeOrdi = [couleur[Ordi1],couleur[Ordi2],... ]
    return ListeOrdi

if __name__ == "__main__":

    ListeAlea=combi_aleatoire()

    print(ListeAlea)
    #os.system("pause")








