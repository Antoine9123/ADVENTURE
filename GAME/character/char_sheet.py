import pygame
from time import sleep
from functions import *

from item.weapons import Arme
from item.armor import Armure
from item.spell import Magie

class Personnage:
    def __init__(self, nom, titre, force, constitution, dexterite, sagesse, intelligence, charisme, level) :
        #Set de base ----------------------------------------------------->
        self.clock = pygame.time.Clock()
        self.nom = nom
        self.titre = titre
        self.force = force
        self.constitution = constitution
        self.dexterite = dexterite
        self.sagesse = sagesse
        self.intelligence = intelligence
        self.charisme = charisme
        self.level = level

        self.arme = Arme("main",6)
        self.armure = Armure("normal",1)
        
        self.pointVie = (10*self.level)+ modificateur(self.constitution)
        self.classeArmure = 10 + modificateur(self.constitution)+ self.armure.classArmureBonus
        self.mana = modificateur(self.intelligence)+self.level

        self.magie1 = Magie("Boule de feu",10,1)
        self.magie2 = Magie("Boule de feu",10,1)
        self.magie3 = False
        
        self.inventaire = [[],[],[],[]]
        
    def attaquePhysique(self, adversaire, objet):
        jetAttaque = rollDice(20,self.force)
        if jetAttaque > adversaire.classeArmure:
            jetDegats = rollDice(self.arme.degat,self.force)
            objet.set_text(f"{jetDegats} damage")
            adversaire.pointVie -= jetDegats
        else:
            objet.set_text("miss")

    
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
    
    def delay(self,milliseconds):
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < milliseconds:
            pygame.event.pump()
    