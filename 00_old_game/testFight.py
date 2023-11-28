from core.combat import *
from core.classe import *

Joueur = Personnage("Joueur", "le fou", 18,16,15,11,12,13,1)
Ennemi = Personnage("Ennemi", "le fou", 10,10,10,10,10,10,2)

Fight(Joueur,Ennemi).fight()