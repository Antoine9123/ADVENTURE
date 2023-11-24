import pygame
import sys



class MenuStart:
    def __init__(self, display, gameStateManager, SCREENWIDTH, SCREENHEIGHT):
        self.display = display
        self.gameStateManager = gameStateManager
        self.SCREENWIDTH = SCREENWIDTH
        self.SCREENHEIGHT = SCREENHEIGHT

        self.load_background()
        self.load_menu()


    def load_menu(self):
        self.title_font = pygame.font.Font('GAME/font/MorrisRomanBlack.otf', 90)
        self.menu_font = pygame.font.Font('GAME/font/MorrisRomanBlack.otf', 40)
        self.title_surface = self.title_font.render('Adventure Game', True, (250, 250, 210))

        self.create_surface = self.menu_font.render('< PRESS SPACE >', True, (250, 250, 210))
        self.create_rect = self.create_surface.get_rect()
        self.create_rect.center = (self.SCREENWIDTH // 2, self.SCREENHEIGHT -50)


    def load_background(self):
        self.background = pygame.image.load('GAME/img/menu/background_menu.jpg')
        self.background = pygame.transform.scale(self.background, (self.SCREENWIDTH, self.SCREENHEIGHT))

    def run(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.gameStateManager.set_state('fight')
                        

        self.display.blit(self.background, (0, 0))
        self.display.blit(self.title_surface, (50, 50))
        self.display.blit(self.create_surface, self.create_rect)






