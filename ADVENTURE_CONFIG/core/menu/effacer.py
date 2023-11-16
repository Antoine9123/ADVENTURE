### MENU EFFACER
import os
from core.fonction import espacer

def menuDelete():
    espacer('',1,100)
    print("--- SUPPRESSION DE PERSONNAGE ---")
    espacer("",0.5,1)
    print("Bienvenue dans le mode suppression de personnage")
    espacer("",0.5,1)

    ### RECHERCHE DES PERSONNAGES
    print("Veuillez choisir un personnage : ")
    espacer("",0.5,3)

    fichiers = os.listdir("core/personnage")
    for fichier in fichiers:
        nom_fichier, extension = os.path.splitext(fichier)
        print(nom_fichier)

    ### SUPRESSION DU PERSONNAGE
    print("")
    persoSelected = input(" > ")
    
    if os.path.exists(f"core/personnage/{persoSelected}.data"):
        os.remove(f"core/personnage/{persoSelected}.data")
        espacer(".",1,3)
        espacer(".",0.5,2)
        espacer(".",0,1)
        print(f"Le personnage {persoSelected} a été supprimé.")
        espacer("",1,3)
    else:
        espacer(".",1,3)
        print(f"Le personnage {persoSelected} n'a pas été trouvé.")
