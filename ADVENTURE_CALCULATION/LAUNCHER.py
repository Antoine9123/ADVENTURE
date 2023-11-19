from time import sleep
from core.fonction import espacer
from core.menu.menu import menuPrincipal
# SCRIPT MAIN
print("LANCEMENT DU PROGRAMME...")
espacer('.',2,4)


print("OPTIMISATION DE L'INTERFACE GRAPHIQUE...")
espacer(".",4,60)

print("CHARGEMENT DU MENU...")
sleep(3)
espacer("",1,60)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("Bonjour, bienvenue dans", '"Une aventure pour un aventurier"', "!")
sleep(1)
print("")
print("Un jeu créant une aventure, pour un aventurier. ")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
sleep(1)


espacer("",0,3)
sleep(1)

# VERS MENU

menuPrincipal()