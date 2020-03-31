import random
def combi_aleatoire():
    ListeNbre = [1,2,3,4,5,6,7,8]
    random.shuffle(ListeNbre)
    Ordi1= ListeNbre[0]
    Ordi2= ListeNbre[1]
    Ordi3= ListeNbre[2]
    Ordi4= ListeNbre[3]
    ListeOrdi = [Ordi1,Ordi2,Ordi3,Ordi4]
    return ListeOrdi

ListeAlea=combi_aleatoire()

print(ListeAlea)








