### MENU SELECTION
import os
import pickle
from core.fonction import espacer

def menuSelection():
    espacer('',1,100)
    print("--- SELECTION DE PERSONNAGE ---")
    espacer("",0.5,1)
    print("Bienvenue dans le mode sélection de personnage")
    espacer("",0.5,1)
    
### Lecture des personnages 
    print("Veuillez choisir un personnage : ")
    espacer("",0.5,1)
    
      
    fichiers = os.listdir("core/personnage")
    for fichier in fichiers:
        nomFichier, extension = os.path.splitext(fichier)
        print(nomFichier)
    
### Selection du personnage
    espacer("",0.5,2)
    persoSelected = input(" > ")

    if f"{persoSelected}.data" in fichiers:
        with open(f"core/personnage/{persoSelected}.data", "rb") as fic:
            get_record = pickle.Unpickler(fic)
            Joueur = get_record.load()
            
### Afficher les valeurs
        espacer("",1,3)
        print(f" --->>> FICHE DU PERSONNAGE : {Joueur.nom}, {Joueur.titre}") 
        espacer("",0.5,1)
        print(f" NOM : {Joueur.nom}")
        print("")
        print(f" TITRE : {Joueur.titre}")
        espacer("",1,1)
        print("Votre personnage a pour statistiques :")
        espacer("",0.5,1)
        print(f" FOR : {Joueur.force}")
        print("")
        print(f" CON : {Joueur.constitution}")
        print("")
        print(f" DEX : {Joueur.dexterite}")
        print("")
        print(f" SAG : {Joueur.sagesse}")
        print("")
        print(f" INT : {Joueur.intelligence}")
        print("")
        print(f" CHA : {Joueur.charisme}")
        print("")
        espacer("",0.5,3)
        
 ### Démarrage du jeu       
        while True :
            print("Voulez vous continuer votre partie ? (oui/non)")
            espacer("",0.5,1)
            answer = input("> ")
            if answer == "oui" :
                while True:
                    try:
                        ###ouverture du jeu en fonction de la sauvegarde
                        module_name = f'game.game{Joueur.save}'
                        function_name = f'game{Joueur.save}'
                        game_module = __import__(module_name, fromlist=[function_name])
                        game_function = getattr(game_module, function_name)
                        game_function()
                        ### Implémentation de la nouvelle variable sauvegarde//
                        Joueur.save += 1
                        with open(f"core/personnage/{Joueur.nom}.data", "wb") as fic:
                            record = pickle.Pickler(fic)
                            record.dump(Joueur)
                        continue

                    except ImportError:
                        from game.game0 import game0
                        game0()
                        break
                break
  
            elif answer == "non" :
                print("")
                print("Dommage ! A très bientôt, alors !")
                espacer("",1,3)
                break
                
            else :
                print("")
                print("Je ne suis pas sûr d'avoir compris, vous pouvez répeter ?")
                espacer("",0.5,1)
                continue     
    
    
    else:
        print("Personnage non trouvé.")
    
