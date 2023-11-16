import pygame
import sys

from menu.menu_start import MenuStart




SCREENWIDTH, SCREENHEIGHT = 1280,720 # Attention !!! Aussi dans le fichier menu_start !
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT)) 
        pygame.display.set_caption("Adventure Game")
        
        icon = pygame.image.load("img/icone.jpg")
        pygame.display.set_icon(icon)
        
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('start')
        self.menuStart = MenuStart(self.screen, self.gameStateManager, SCREENWIDTH, SCREENHEIGHT)
        self.level = Level(self.screen, self.gameStateManager)

        self.states = {'start': self.menuStart, }
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS) 

class Level:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        self.display.fill("blue")   
   

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state

if __name__ == "__main__":
    game = Game()
    game.run()

