#### Jet de sauvegarde
def rollDice(nbrFace:int,relationStatistique=10): #I fixed the relStat to 10, because I know that modifier 10 = 0. So it allows to just throw a dice.
    import random
    resultat = random.randint(1,nbrFace) + modifier(relationStatistique)
    return resultat

#### Modificateur
def modifier(stat):
        import math
        modificateurStat = math.floor((stat-10)/2)
        return modificateurStat     
