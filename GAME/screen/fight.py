import pygame
from pygame import mixer
import sys
import json

from GAME.classes.char_sheet import Personnage
from GAME.screen.fight_menu import FightMenu
from GAME.screen.fight_text import FightTxt



class Fight:
    def __init__(self, display, gameStateManager, SCREENWIDTH, SCREENHEIGHT):
        self.display = display
        self.gameStateManager = gameStateManager
        self.SCREENWIDTH = SCREENWIDTH
        self.SCREENHEIGHT = SCREENHEIGHT
        
        self.font = pygame.font.Font(None, 50)
        
        self.player = self.load_player()
        self.ennemy = Personnage("Python, the Elder Dragon","L'ancien",10,10,10,10,10,10,100)
        

        self.load_background()
        self.load_players_screen()
        self.menuFight = FightMenu(self.display)
        self.menuFight.display()
        self.txtFight = FightTxt(self.display)
        self.txtFight.display()
        
        mixer.music.load('GAME/sounds/battle.mp3')
        #mixer.music.play(-1)

    def load_player(self):
        with open(f"GAME/last_char.json", "r") as f:
            load_player = json.load(f)
            name = load_player['name']
            title = load_player['title']
            strenght = load_player['statSTR']
            constitution = load_player['statCON']
            dexterity = load_player['statDEX']
            wisdom = load_player['statWIS']
            intelligence = load_player['statINT']
            charisma = load_player['statCHA']
            level = load_player['level']
         
        return Personnage(name, title, strenght, constitution,dexterity, wisdom, intelligence, charisma, level)   
     
    def load_background(self):
        self.background = pygame.image.load('GAME/img/fight.png')
        self.background = pygame.transform.scale(self.background, (self.SCREENWIDTH, self.SCREENHEIGHT))
        self.player_image = pygame.image.load('GAME/img/fighter.png')
        self.player_image = pygame.transform.scale(self.player_image, (400, 400))
        self.ennemy_image = pygame.image.load('GAME/img/dragon.png')
        

    def run(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                mouse_pos = pygame.mouse.get_pos()
                self.handle_click(mouse_pos, self.menuFight)   
        
        self.display.blit(self.background, (0, 0))
        self.display.blit(self.player_image, (-50,self.SCREENHEIGHT-300))
        self.display.blit(self.ennemy_image, (self.SCREENWIDTH -350,50))
        self.display.blit(self.life_player, (25, 360))
        self.display.blit(self.mana_player, (25, 400))
        self.display.blit(self.life_ennemy, (650, 50))
        self.display.blit(self.mana_ennemy, (650, 90))
        self.menuFight.run()
        self.txtFight.run()

    
    def load_players_screen(self):
        
        self.life_player = self.font.render(f'{self.player.name} - HP :{self.player.healthPoint}', True, (250, 250, 210))
        self.mana_player = self.font.render(f'Mana :{self.player.magicPoint}', True, (250, 250, 210))
        
        self.life_ennemy = self.font.render(f'{self.ennemy.name} - HP :{self.ennemy.healthPoint}', True, (250, 250, 210))
        self.mana_ennemy = self.font.render(f'Mana :{self.ennemy.magicPoint}', True, (250, 250, 210))
        
    
    def handle_click(self, mouse_pos, objet):
        if objet.atk_rect.collidepoint(mouse_pos):
            self.player.attackDamage(self.ennemy,self.txtFight)
            self.life_ennemy = self.font.render(f'{self.ennemy.name} - HP :{self.ennemy.healthPoint}', True, (250, 250, 210))
            # self.ennemy.attaquePhysique(self.player,self.txtFight)
            # self.life_player = self.font.render(f'{self.player.nom} - HP :{self.player.pointVie}', True, (250, 250, 210))
        if objet.mgk_rect.collidepoint(mouse_pos):
            self.player.magicDamage(self.ennemy,self.txtFight)
            self.life_ennemy = self.font.render(f'{self.ennemy.name} - HP :{self.ennemy.healthPoint}', True, (250, 250, 210))
    
        
        
    
        
        
        







