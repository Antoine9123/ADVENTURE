from core.combat import *
from core.classe import *





Joueur = Personnage("Joueur", "le fou", 10,10,10,10,10,10,1)
Ennemi = Personnage("Ennemi", "le fou", 10,10,10,10,10,10,2)

BouledeFeu = Magie("Boule de feu",10,1)
Joueur.ajouterItem(BouledeFeu,"magie")
Joueur.ajouterItem(Magie("Boule de glace",10,1),"magie")
Joueur.ajouterItem(Magie("Armure de glace",10,1),"magie")
Joueur.ajouterItem(Magie("Armure de feu",10,1),"magie")
Joueur.ajouterItem(Magie("Soin",10,1),"magie")

for item in Joueur.inventaire[2]:
    print(item.nom)