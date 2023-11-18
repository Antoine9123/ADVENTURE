import sys

import pygame
import pygame_gui

from menu.menu_start import MenuStart
from menu.menu_create import MenuCreate
from menu.menu_select import MenuSelect
from menu.menu_delete import MenuDelete


if __name__ == "__main__":

    SCREENWIDTH, SCREENHEIGHT = 1280,720
    FPS = 144
    MANAGER = pygame_gui.UIManager((SCREENWIDTH, SCREENHEIGHT))

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
            self.menuCreate = MenuCreate(self.screen, self.gameStateManager, SCREENWIDTH, SCREENHEIGHT, MANAGER)
            self.menuSelect = MenuSelect(self.screen, self.gameStateManager, SCREENWIDTH, SCREENHEIGHT)
            self.menuDelete = MenuDelete(self.screen, self.gameStateManager, SCREENWIDTH, SCREENHEIGHT)
            #self.level = Level(self.screen, self.gameStateManager)

            self.states = {'start': self.menuStart,
                           'create': self.menuCreate,
                           'select': self.menuSelect,
                           'delete': self.menuDelete}

        def run(self):
            while True:
                UI_REFRESH_RATE = self.clock.tick(60)/1000
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    MANAGER.process_events(event)
                MANAGER.update(UI_REFRESH_RATE)

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

    if __name__ == "__main__":
        game = Game()
        game.run()

