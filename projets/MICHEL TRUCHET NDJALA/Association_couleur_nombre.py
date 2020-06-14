def couleur(x):
    if x==1:
        z="cyan"
    elif x==2:
        z="orange"
    elif x==3:
        z="blue"
    elif x==4:
        z="saddlebrown"
    elif x==5:
        z="yellow"
    elif x==6:
        z="green"
    elif x==7:
        z="purple"
    else:
        z="pink"
    return z

print(couleur(5))

# il y a plus simple :

##couleur=["cyan","orange","blue",....
##couleur[0] -> "cyan"