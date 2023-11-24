from time import sleep
from functions import *

from item.weapons import Arme
from item.armor import Armure
from item.spell import Magie

class Personnage:
    def __init__(self, nom, titre, force, constitution, dexterite, sagesse, intelligence, charisme, save) :
        #Set de base ----------------------------------------------------->
        self.nom = nom
        self.titre = titre
        self.force = force
        self.constitution = constitution
        self.dexterite = dexterite
        self.sagesse = sagesse
        self.intelligence = intelligence
        self.charisme = charisme
        self.save = save

        self.arme = Arme("main",6)
        self.armure = Armure("normal",-10)
        
        self.pointVie = (10*self.save)+ modificateur(self.constitution)
        self.classeArmure = 10 + modificateur(self.constitution)+ self.armure.classArmureBonus
        self.mana = modificateur(self.intelligence)+self.save

        self.magie1 = Magie("Boule de feu",10,1)
        self.magie2 = Magie("Boule de feu",10,1)
        self.magie3 = False
        
        self.inventaire = [[],[],[],[]]
        
    def attaquePhysique(self, adversaire, objet):
        jetAttaque = rollDice(20,self.force)
        objet.set_text(f"Vous obtenez un jet d'attaque de {jetAttaque}")
        # sleep(1)
        # objet.set_text(f"La classe d'armure de l'adversaire est de {adversaire.classeArmure}")
        # sleep(1)
        # objet.set_text("")
        # if jetAttaque > adversaire.classeArmure:
        #     jetDegats = rollDice(self.arme.degat,self.force)
        #     objet.set_text(f"Vous infligez {jetDegats} dégâts")
        #     adversaire.pointVie -= jetDegats
        #     sleep(1)
        # else:
        #     objet.set_text("Votre attaque n'a pas fait mouche.")
        #     objet.set_text("")
        # sleep(1)
    
    def attaqueMagique(self, adversaire, magie):
        jetSauvegarde = rollDice(20,adversaire.intelligence)
        degreDifficulte = 8 + modificateur(self.intelligence)
        print(f"Le degré de difficulté du sort est de {degreDifficulte}\n")
        sleep(1)
        print(f"Le jet de sauvegarde est de {jetSauvegarde}")
        sleep(1)
        print("")
        if degreDifficulte >= jetSauvegarde:   
            jetDegats = rollDice(magie.degat)
            print(f"{self.nom} {magie.text}")
            print(f"Vous infligez {jetDegats} dégâts\n\n")
            adversaire.pointVie -= jetDegats
            sleep(1)
        else:
            print("Votre sort n'a pas touché l'adversaire.")
            print("")
        sleep(1)