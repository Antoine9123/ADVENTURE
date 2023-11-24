import pygame
import sys

from character.char_sheet import Personnage
from screen.fight_menu import FightMenu



class Fight:
    def __init__(self, display, gameStateManager, SCREENWIDTH, SCREENHEIGHT):
        self.display = display
        self.gameStateManager = gameStateManager
        self.SCREENWIDTH = SCREENWIDTH
        self.SCREENHEIGHT = SCREENHEIGHT
        
        self.font = pygame.font.Font(None, 50)
        
        self.player = Personnage("Efty","Le héros", 20,14,20,20,20,20,10)
        self.ennemy = Personnage("Dragon","L'ancien",10,10,10,10,10,10,1)
        
        self.turn = True

        self.load_background()
        self.load_players_screen()
        self.turn_counter()
        self.menuFight = FightMenu(self.display, self.turn)
        self.menuFight.display()
        
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
        
        

        self.display.blit(self.background, (0, 0))
        self.display.blit(self.player_image, (-50,self.SCREENHEIGHT-300))
        self.display.blit(self.ennemy_image, (self.SCREENWIDTH -350,50))
        self.display.blit(self.life_player, (25, 360))
        self.display.blit(self.mana_player, (25, 400))
        self.display.blit(self.life_ennemy, (650, 50))
        self.display.blit(self.mana_ennemy, (650, 90))
        self.display.blit(self.turn_counter, (50, 50))
        self.menuFight.run()
    
    def load_players_screen(self):
        
        self.life_player = self.font.render(f'{self.player.nom} - HP :{self.player.pointVie}', True, (250, 250, 210))
        self.mana_player = self.font.render(f'Mana :{self.player.mana}', True, (250, 250, 210))
        
        self.life_ennemy = self.font.render(f'{self.ennemy.nom} - HP :{self.ennemy.pointVie}', True, (250, 250, 210))
        self.mana_ennemy = self.font.render(f'Mana :{self.ennemy.mana}', True, (250, 250, 210))
        
    def turn_counter(self):
        self.turn_counter = self.font.render(f"C'est au tour de XXX", True, (250,250,210))
    
        
        
    
        
        
        







