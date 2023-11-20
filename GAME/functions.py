##### FONCTION ESPACE
def espacer(message, tempsTotal, nombre) :
    from time import sleep
    pause = tempsTotal / nombre
    while nombre > 0 :
        print(message)
        sleep(pause)
        nombre -= 1
        continue

##### CREATION STAT PERSO
def creationNewStat(pointRestant):
     while True:
            statMin = 0
            statMax = 20
            
            newStats = input("> ")

            try:
                newStats = int(newStats)  
            except ValueError:
                espacer("", 0.5, 1)
                print("La valeur indiquée doit être un nombre entier.")
                espacer("", 0.5, 1)
                continue  

            if newStats < statMin or newStats > statMax:
                espacer("", 0.5, 1)
                print(f"La valeur indiquée doit être un nombre entier compris entre {statMin} et {statMax}.")
                espacer("", 0.5, 1)
                print("Quelle valeur choisissez-vous ?")
                espacer("", 0.5, 1)
                
            elif pointRestant - newStats < 0:
                espacer("", 0.5, 1)
                print("Il ne vous reste plus assez de points pour utiliser cette valeur.")
                espacer("", 0.5, 1)
                print("Quelle valeur choisissez-vous ?")
                espacer("", 0.5, 1)
            else:
                return newStats
            
#### Jet de sauvegarde
def rollDice(nbrFace:int,relationStatistique=10):
    import random
    resultat = random.randint(1,nbrFace) + modificateur(relationStatistique)
    return resultat

#### Modificateur
def modificateur(stat):
        import math
        modificateurStat = math.floor((stat-10)/2)
        return modificateurStat
    
    
            
            