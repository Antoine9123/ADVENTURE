import pygame



class MenuStart:
    def __init__(self, display, gameStateManager, SCREENWIDTH, SCREENHEIGHT):
        self.display = display
        self.gameStateManager = gameStateManager
        self.SCREENWIDTH = SCREENWIDTH
        self.SCREENHEIGHT = SCREENHEIGHT

        self.load_background()

        self.menu_font = pygame.font.Font(None,50)
        self.text_surface = self.menu_font.render('Adventure Game', True, (250,250,210))

    def load_background(self):
        self.background = pygame.image.load('img/menu/background_menu.jpg')
        self.background = pygame.transform.scale(self.background, (self.SCREENWIDTH, self.SCREENHEIGHT))

    def run(self):
        
        self.display.blit(self.background, (0, 0))
        self.display.blit(self.text_surface, (50, 50))
