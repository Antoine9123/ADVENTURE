from GAME.functions import *
from GAME.item.weapons import Arme
from GAME.item.armor import Armure
from GAME.item.spell import Magie

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

    def set_attribute():
        pass

    def get_atttribute():
        pass

    def save_char():
        pass

    def load_char():
        pass