from time import sleep
import core.classe
from core.fonction import espacer, rollDice
from core.menu.menu import menuPrincipal


class Fight:
    def __init__(self, joueur, ennemi):
        self.joueur = joueur
        self.ennemi = ennemi

####    Lancement d'une bagarre !!!  --------------------------------------------------------------------------------------------->       

    def fight(self):
        espacer(".",1,5)
        print("FIGHT !!!")
        sleep(1)
        espacer("",1,100)
        firstPlayer = False
        joueurInitiative = rollDice(20,self.joueur.dexterite)
        ennemiInitiative = rollDice(20,self.ennemi.dexterite)
        if joueurInitiative >= ennemiInitiative:
            firstPlayer = True
            print("Vous êtes le premier joueur.\n")
        else:
            print("Votre adversaire commence !\n")
        sleep(1)
        
        while self.joueur.pointVie > 0 and self.ennemi.pointVie > 0 :
                print("|-------------------------------------------------")
                print(f"|{self.joueur.nom} // PV = {self.joueur.pointVie} // Mana = {self.joueur.mana}")
                print("|---")
                print(f"|{self.ennemi.nom} // PV = {self.ennemi.pointVie} // Mana = {self.ennemi.mana}")
                print("|-------------------------------------------------\n")
                sleep(0.5)
                if firstPlayer:
                    print("C'est à votre tour !\n")
                    self.menufight(self.joueur, self.ennemi)
                    firstPlayer = False
                else:
                    print("C'est au tour de votre ennemi ! \n")
                    self.menufight(self.ennemi,self.joueur)
                    firstPlayer = True
                
        if self.ennemi.pointVie <= 0:        
            print(f"{self.ennemi.nom} est mort !\n")
        else:
            print(f"Dommage, {self.joueur.nom}, {self.joueur.titre}... La mort a eu raison de vous...")
            espacer(".",5,10)
            espacer(".",1,100)
            menuPrincipal()
        

####    Lancement du menu --------------------------------------------------------------------------------------------->
        
    def menufight(self, attaquant, defenseur):
        while True:  
            magicMenu = True  
            print("Quelle action voulez-vous effectuer ?")
            espacer("",0.2,1)
            print("A. Utiliser une attaque normale")
            print("B. Utiliser de la magie")
            print("C. Utiliser un objet")
            espacer("",0.2,1)
            print("Entrez votre choix (A, B ou C):\n")
            answer = input("> ")
            espacer("",0.5,1)
        
            if answer == "A":
                attaquant.attaquePhysique(defenseur)
                break
            
            elif answer == "B":
                magicMenu = self.menuMagique(attaquant, defenseur)
                if magicMenu == False:
                    continue
                else:
                     break
                
            else:
                print("Je n'ai pas bien compris votre réponse, pouvez-vous répeter ?")
                continue

    def menuMagique(self, attaquant, defenseur):
        while True:
                    print("Quelle magie voulez-vous utiliser ? (Tapez Q pour revenir en arrière)")
                    print(f"MANA du joueur : {attaquant.mana}\n")
                    if attaquant.magie1 != False:
                        print(f"1. Sort utilitaire : {attaquant.magie1.nom} // coût = {attaquant.magie1.cout}")
                    if attaquant.magie2 != False:    
                        print(f"2. Sort supérieur : {attaquant.magie2.nom} // coût = {attaquant.magie2.cout}")
                    if attaquant.magie3 != False:
                        print(f"X. Sort des arcannes : {attaquant.magie3.nom} // coût = {attaquant.magie3.cout}")
                    print("")
                    answer = input(">")
                    if answer == "1" and attaquant.magie1 != False:
                        if attaquant.mana >= attaquant.magie1.cout:
                            attaquant.attaqueMagique(defenseur,attaquant.magie1)
                            attaquant.mana -= attaquant.magie1.cout
                            break
                        else:
                            print("\nVous n'avez plus assez de mana pour cette action\n")
                            continue
                    
                    elif answer == "2" and attaquant.magie2 != False:
                        if attaquant.mana >= attaquant.magie2.cout:
                            attaquant.attaqueMagique(defenseur,attaquant.magie2)
                            attaquant.mana -= attaquant.magie2.cout
                            break
                        else:
                            print("\nVous n'avez plus assez de mana pour cette action\n")
                            continue
                    
                    elif answer == "X" and attaquant.magie3 != False:
                        if attaquant.mana >= attaquant.magie3.cout:
                            attaquant.attaqueMagique(defenseur,attaquant.magie3)
                            attaquant.mana -= attaquant.magie3.cout
                            break
                        else:
                            print("\nVous n'avez plus assez de mana pour cette action\n")
                            continue

                    elif answer == "Q":
                        return False
                        break
                    
                    else:
                        print("\nJe n'ai pas bien compris votre réponse, pouvez-vous répeter ?\n")
                        sleep(1)
                        continue
