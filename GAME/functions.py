#### Jet de sauvegarde
def rollDice(nbrFace:int,relationStatistique=10):
    import random
    resultat = random.randint(1,nbrFace) + modifier(relationStatistique)
    return resultat

#### Modificateur
def modifier(stat):
        import math
        modificateurStat = math.floor((stat-10)/2)
        return modificateurStat     