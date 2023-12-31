import pygame

from GAME.functions import *
from GAME.classes.weapons import Weapon
from GAME.classes.armor import Armor
from GAME.classes.spell import Spell
#from GAME.classes.event import EventDelay

class Personnage:
    def __init__(self, name, title, strenght, constitution, dexterity, wisdom, intelligence, charisma, level) :
        #Set de base ----------------------------------------------------->
        self.name = name
        self.title = title
        self.strenght = strenght
        self.constitution = constitution
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.level = level

        self.weapon = Weapon("hand",6)
        self.armor = Armor("casual",2)
        self.spell = Spell("FireBall",10,1)
        
        self.healthPoint = (10*self.level)+ modifier(self.constitution)
        self.armorClass = 10 + modifier(self.constitution)+ self.armor.classArmureBonus
        self.magicPoint = modifier(self.intelligence)+self.level

        

        
    def attackDamage(self, ennemy, objet):
        attackRoll = rollDice(20,self.strenght)
        if attackRoll > ennemy.armorClass:
            damageRoll = rollDice(self.weapon.degat,self.strenght)
            ennemy.healthPoint -= damageRoll
            return damageRoll
        else:
            return 0

    
    def magicDamage(self, ennemy,text_displayed):
        self.magicPoint -= self.spell.cout
        savingThrow = rollDice(20,ennemy.intelligence)
        difficultyClass = 8 + modifier(self.intelligence)
        if difficultyClass >= savingThrow:   
            damageRoll = rollDice(self.spell.degat)
            ennemy.healthPoint -= damageRoll
            
        else:
            return 0


    