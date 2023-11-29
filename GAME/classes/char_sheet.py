import pygame

from GAME.functions import *
from GAME.classes.weapons import Weapon
from GAME.classes.armor import Armor
from GAME.classes.spell import Spell

class Personnage:
    def __init__(self, name, title, strenght, constitution, dexterity, wisdom, intelligence, charisma, level) :
        #Set de base ----------------------------------------------------->
        self.clock = pygame.time.Clock()
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
        self.armor = Armor("casual",1)
        self.spell = Spell("FireBall",10,1)
        
        self.healthPoint = (10*self.level)+ modifier(self.constitution)
        self.armorClass = 10 + modifier(self.constitution)+ self.armor.classArmureBonus
        self.magicPoint = modifier(self.intelligence)+self.level

        

        
    def attackDamage(self, ennemy, objet):
        attackRoll = rollDice(20,self.strenght)
        if attackRoll > ennemy.armorClass:
            damageRoll = rollDice(self.weapon.degat,self.strenght)
            objet.set_text(f"{damageRoll} damage")
            ennemy.healthPoint -= damageRoll
        else:
            objet.set_text("miss")

    
    def magicDamage(self, ennemy, objet):
        self.magicPoint -= self.spell.cout
        savingThrow = rollDice(20,ennemy.intelligence)
        difficultyClass = 8 + modifier(self.intelligence)
        if difficultyClass >= savingThrow:   
            damageRoll = rollDice(self.spell.degat)
            objet.set_text(f"You did {damageRoll} damage !")
            ennemy.healthPoint -= damageRoll
        else:
            objet.set_text("miss")

    
    def delay(self,milliseconds):
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < milliseconds:
            pygame.event.pump()
    