import pygame

from screen.menu_start import MenuStart
from screen.fight import Fight


SCREENWIDTH, SCREENHEIGHT = 1280,720
FPS = 144

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        pygame.display.set_caption("Adventure Game")

        #icon = pygame.image.load("img/icone.jpg")
        #pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('start')
        self.menuStart = MenuStart(self.screen, self.gameStateManager, SCREENWIDTH, SCREENHEIGHT)
        self.menuFight = Fight(self.screen, self.gameStateManager, SCREENWIDTH, SCREENHEIGHT)


        self.states = {'start': self.menuStart, 'fight': self.menuFight}

    def run(self):
        while True:
            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state

game = Game()
game.run()

