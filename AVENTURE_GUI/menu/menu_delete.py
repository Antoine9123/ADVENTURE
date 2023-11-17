import pygame

class MenuDelete:
    def __init__(self, display, gameStateManager, SCREENWIDTH, SCREENHEIGHT):
        self.display = display
        self.gameStateManager = gameStateManager
        self.SCREENWIDTH = SCREENWIDTH
        self.SCREENHEIGHT = SCREENHEIGHT

        self.load_background()
        self.load_menu()


    def load_menu(self):
        self.title_font = pygame.font.Font('font/MorrisRomanBlack.otf', 90)
        self.back_font = pygame.font.Font('font/MorrisRomanBlack.otf', 30)
        self.title_surface = self.title_font.render('Adventure Game', True, (250, 250, 210))

        self.back_surface = self.back_font.render('< Back', True, (250, 250, 210))
        self.back_rect = self.back_surface.get_rect(topleft=(80, 650))





    def load_background(self):
        self.background = pygame.image.load('img/menu/background_menu.jpg')
        self.background = pygame.transform.scale(self.background, (self.SCREENWIDTH, self.SCREENHEIGHT))

    def run(self):
        if self.back_rect.collidepoint(pygame.mouse.get_pos()):
            self.back_surface = self.back_font.render('< Back', True, (0,0,0))
            if pygame.mouse.get_pressed() == (1,0,0):
                self.gameStateManager.set_state('start')
        else:
            self.back_surface = self.back_font.render('< Back', True, (250, 250, 210))

        self.display.blit(self.background, (0, 0))
        self.display.blit(self.title_surface, (50, 50))
        self.display.blit(self.back_surface, self.back_rect)


