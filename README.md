# ISN2020
le dépôt pour partager les codes ISN du lycée du Forez

## Mode d'emploi

github est un service très très utilisé par les développeurs pour travailler de manière collaborative. Il est basé sur git, un service de versionning qui permet lorsqu'on modifie des fichiers de garder des traces des modifications. C'est Linus Torvalds le créateur de linux qui l'a inventé.

Il y a quelques concepts majeurs à comprendre :

* le **dépôt** est l'ensemble des fichiers
* un **commit** est un instantané du *dépôt*. Une fois qu'on a modifié des fichiers, on lance une commande qui permet de faire comme une photographie des fichiers. Ce qui est cool c'est qu'on garde la trace de nos modifs, de l'état du dépôt à ce moment. Les commits s'alignent donc les uns derrière les autres, ils forment un continuum d'évolution du dépôt
* pour ouvrir une nouvelle évolution du *dépôt*, on peut créer une **branche**. Cela permet de faire des modifications du *dépôt* tout en conservant l'état dans d'autres branches

![Principe des branches](ressources/feature-branches.png "Principe des branches")

* pour comprendre comment fonctionne github, vous pouvez jeter un oeil au [guide de git](https://guides.github.com/activities/hello-world/). Surtout les étapes 2, 3 & 4.

## Ce qu'il faut faire

* Créer une branche dont le nom est projetXYZ où XYZ correspondent aux initiales des membres du groupe.
* Déposer vos fichiers dans le dossier correspondant à votre travail
* faire un 1er commit sur votre branche avec comme *commentaire* "dépôt initial"