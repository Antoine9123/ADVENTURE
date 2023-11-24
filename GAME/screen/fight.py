import pygame
import sys


class Fight:
    def __init__(self, display, gameStateManager, SCREENWIDTH, SCREENHEIGHT):
        self.display = display
        self.gameStateManager = gameStateManager
        self.SCREENWIDTH = SCREENWIDTH
        self.SCREENHEIGHT = SCREENHEIGHT

        self.load_background()
        self.load_fight()


    def load_fight(self):
        pass


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







