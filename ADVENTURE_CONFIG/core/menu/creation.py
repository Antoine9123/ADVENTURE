#### MENU CREATION
import pickle
from core.fonction import espacer
from core.fonction import creationNewStat


def menuCreation():
    print("")
    espacer('',1,100)
    print("--- CREATION DE PERSONNAGE ---")
    espacer("",0.5,1)
    print("Bienvenue dans le mode création de personnage.")
    espacer("",0.5,1)
    print("Nous allons commencer par lui donner un nom et un titre.")
    espacer("",0.5,4)
    while True:
        
### PROCESS NOM + TITRE   
        ### NOM
        print("Veuillez introduire le nom de votre personnage.")
        print("")
        nomJoueur = input("> ")
        espacer("",0.5,1)
        
        ### TITRE
        print("Veuillez introduire le titre de votre personnage.")
        print("")
        titreJoueur = input("> ")
        espacer("",0.5,1)
        
        
        print("")
        print(f"NOM : {nomJoueur}")
        print(f"TITRE : {titreJoueur}")
        print("")
        print(f"Autrement appelé : {nomJoueur}, {titreJoueur}")
        espacer("",0.5,1)
        print("Ce nom vous convient-il ? (oui/non)")
        print("")
        answer = input("> ")
        if answer == "oui":
            espacer("",0.5,3)
            break
        elif answer == "non" :
            espacer("",0.5,1)
            print("Aucun problème, recommençons !")
            espacer("",0.5,1)
            continue
        else : 
            espacer("",0.5,1)
            print("Je n'ai pas compris la réponse. Recommençons !")
            espacer("",0.5,3)
            continue
        

        
### PROCESS STATS  
        ### PREAMBULE
    while True:
        print("Vous ne disposez qu'un nombre de points réduits à répartir entre vos statistiques.")
        espacer("",1.5,1)
        pointsRestants = 75
        print(f"Ce nombre de point est égale à {pointsRestants}.")
        espacer("",1.5,1)
        print("Les différentes caractéristiques dans lesquels répartir vos points sont les suivantes :")
        espacer("",1.5,1)
        print("Force, Constitution, Dextérité, Sagesse, Intelligence, Charisme.")
        espacer("",1.5,1)
        print("Réfléchissez bien...")
        statFOR = 2
        statCON = 2
        statDEX = 2
        statSAG = 2
        statINT = 2
        statCHA = 2
        
        ### FORCE
        espacer("",1,3)
        print("Quelle est la valeur pour votre force (FOR) ?")
        print("nombre de points restant =", pointsRestants)
        statFOR = creationNewStat(pointsRestants)
        
        pointsRestants = int(pointsRestants) - statFOR
        print("")
        
        ### CONSTITUTION
        espacer("",0.5,1)
        print("Quelle est la valeur pour votre constitution (CON) ?")
        print("nombre de points restant =", pointsRestants)
        statCON = creationNewStat(pointsRestants)
        
        pointsRestants = int(pointsRestants) - int(statCON)
        print("")
        
        ### DEXTERITE
        espacer("",0.5,1)
        print("Quelle est la valeur pour votre dexterite (DEX) ?")
        print("nombre de points restant =", pointsRestants)
        statDEX = creationNewStat(pointsRestants)
       
        pointsRestants = int(pointsRestants) - int(statDEX)
        print("")
        
        ### SAGESSE
        espacer("",0.5,1)
        print("Quelle est la valeur pour votre sagesse (SAG) ?")
        print("nombre de points restant =", pointsRestants)
        statSAG = creationNewStat(pointsRestants)
        
        pointsRestants = int(pointsRestants) - int(statSAG)
        print("")#
        
        ## INTELLIGENCE
        espacer("",0.5,1)
        print("Quelle est la valeur pour votre intelligence (INT) ?")
        print("nombre de points restant =", pointsRestants)
        print("")
        statINT = creationNewStat(pointsRestants)
            
        pointsRestants = int(pointsRestants) - int(statINT)
        print("")
        
        ### CHARISME
        espacer("",0.5,1)
        print("Quelle est la valeur pour votre charisme (CHAR) ?")
        print("nombre de points restant =", pointsRestants)
        statCHA = creationNewStat(pointsRestants)
        
        pointsRestants = int(pointsRestants) - int(statCHA)
        espacer("",1,60)
        
        
        
### AFFICHAGE
        print("Voici les statistiques que vous avez déterminés.")
        print("")
        print(f"FOR : {statFOR}")
        print(f"CON : {statCON}")
        print(f"DEX : {statDEX}")
        print(f"SAG : {statSAG}")
        print(f"INT : {statINT}")
        print(f"CHA : {statCHA}")
        espacer("",0.5,1)
        
#Point restant
        if pointsRestants > 0:
            print(f"!!! Attention, il vous reste des points non attribués ({pointsRestants} au total). Ceux-ci seront définitivement perdus !!!")
            espacer("",0.5,1)
                   
        print("Est-ce que ces statistiques vous conviennent ? (oui/non)")
        print("")
        answer = input("> ")
    
        if answer == "oui":
            espacer(".",1,3)
            espacer(".",0.5,2)
            espacer(".",0,1)
            break
       
        elif answer == "non" :
            espacer("",0.5,1)
            print("Aucun problème, recommençons !")
            espacer("",0.5,1)
        else : 
            espacer("",0.5,1)
            print("Je n'ai pas compris la réponse. Recommençons !")
            espacer("",0.5,3)
    
        ### Intégration à la classe
    from core.classe import Personnage
    
    Joueur = Personnage(nomJoueur,titreJoueur,statFOR,statCON,statDEX,statSAG,statINT,statCHA,1)
    
        ### Enregistrement des informations
    
    with open(f"core/personnage/{Joueur.nom}.data", "wb") as fic:
        record = pickle.Pickler(fic)
        record.dump(Joueur)
    
        ### PROGRAMME ###
    
    print(f"Votre personnage {Joueur.nom}, {Joueur.titre}, a bien été créé !")
    espacer("",3,3)