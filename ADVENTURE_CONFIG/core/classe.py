from core.fonction import *
from time import sleep

# INFORMATION CONCERNANT LES CLASSES
#   Structure :
#       A. Personnage   
#
#       B. Arme
#----------------------------------------
#       A. Personnage
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

        # Combat -------------------------------------------------------------->
    def attaquePhysique(self, adversaire):
        jetAttaque = rollDice(20,self.force)
        print(f"Le jet d'attaque a donné {jetAttaque}\n")
        sleep(1)
        print(f"La classe d'armure de l'adversaire est de {adversaire.classeArmure}")
        sleep(1)
        print("")
        if jetAttaque > adversaire.classeArmure:
            jetDegats = rollDice(self.arme.degat,self.force)
            print(f"Vous infligez {jetDegats} dégâts\n\n")
            adversaire.pointVie -= jetDegats
            sleep(1)
        else:
            print("Votre attaque n'a pas fait mouche.")
            print("")
        sleep(1)
    
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

        # Equipement --------------------------------------------------------------->
    def ajouterItem(self,objet,type):
        if type == "arme":
            self.inventaire[0].extend([objet])
        if type == "armure":
            self.inventaire[1].extend([objet])
        if type == "magie":
            self.inventaire[2].extend([objet])
        if type == "objet":
            self.inventaire[3].extend([objet])
    
    def equipItem(self):
        print("MENU ITEM")

        pass
        
        

#       B. Arme ----------------------------------------------------------------------------------------------------------->

class Arme:
    def __init__(self, nom, degat:int):
        self.nom = nom
        self.degat = degat
        
class Armure:
    def __init__(self,nom, classArmureBonus):
        self.nom = nom
        self.classArmureBonus = classArmureBonus

class Magie :
    def __init__(self,nom,degat,cout):
        self.nom = nom
        self.degat = degat
        self.cout = cout
        self.text = "balance une énorme boule de feu"
        #self.statUtilisee = a definir

class Object :
    def __init__(self, nom, bonus):
        self.nom = nom
        self.bonus = bonus

