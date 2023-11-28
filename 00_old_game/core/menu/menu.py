#MENU PRINCIPAL
import pickle
from core.menu.creation import menuCreation
from core.menu.selection import menuSelection
from  core.menu.effacer import menuDelete

def menuPrincipal():
    
    while True:
        print("")
        print("--- MENU PRINCIPAL ---")
        print("")
        print("Veuillez choisir l'option désirée ( A / B / C )")
        print("")
        print("A. Créer un nouveau personnage")
        print("B. Sélectionner un personnage existant")
        print("C. Effacer un personnage existant")
        print("")
        mainMenuCheck = input("> ")

        ######## CREATION
        if mainMenuCheck == ("A"):
            print(" ")
            menuCreation()

        ######## SELECTION
        elif mainMenuCheck == "B":
            print(" ")
            menuSelection()
            continue

        ######## SUPPRESSION
        elif mainMenuCheck == "C":
            print(" ")
            menuDelete()
            continue

        else : 
            print("Je suis désolé, la commande entrée est incorrecte. Veuillez indiquer la lettre contenue dans le menu")
            print("")
