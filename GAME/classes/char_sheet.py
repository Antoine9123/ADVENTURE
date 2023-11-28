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

        self.magie = Magie("Boule de feu",10,1)

        
        self.inventaire = [[],[],[],[]]
        
    def attaquePhysique(self, adversaire, objet):
        jetAttaque = rollDice(20,self.force)
        if jetAttaque > adversaire.classeArmure:
            jetDegats = rollDice(self.arme.degat,self.force)
            objet.set_text(f"{jetDegats} damage")
            adversaire.pointVie -= jetDegats
        else:
            objet.set_text("miss")

    
    def attaqueMagique(self, adversaire, objet):
        jetSauvegarde = rollDice(20,adversaire.intelligence)
        degreDifficulte = 8 + modificateur(self.intelligence)
        if degreDifficulte >= jetSauvegarde:   
            jetDegats = rollDice(self.magie.degat)
            objet.set_text(f"Vous infligez {jetDegats} dégâts")
            adversaire.pointVie -= jetDegats
        else:
            objet.set_text("miss")

    
    def delay(self,milliseconds):
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < milliseconds:
            pygame.event.pump()
    