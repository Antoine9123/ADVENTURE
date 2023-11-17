import pygame

class MenuCreate:
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


        #self.text_surface = self.back_font.render(self.text, True, (250, 250, 210))
        #self.text_rect = self.back_surface.get_rect(topleft=(200, 200))


        self.submenu_surface = pygame.Surface((1100,450))
        self.submenu_surface.fill('black')
        self.submenu_surface.set_alpha(50)
        self.submenu_rect = self.submenu_surface.get_rect(topleft=(80, 160))


    def load_background(self):
        self.background = pygame.image.load('img/menu/background_menu.jpg')
        self.background = pygame.transform.scale(self.background, (self.SCREENWIDTH, self.SCREENHEIGHT))


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == event.KEYDOWN:
                    print("oui")






            if self.back_rect.collidepoint(pygame.mouse.get_pos()):
                self.back_surface = self.back_font.render('< Back', True, (0,0,0))
                if pygame.mouse.get_pressed() == (1,0,0):
                    self.gameStateManager.set_state('start')
            else:
                self.back_surface = self.back_font.render('< Back', True, (250, 250, 210))


            self.display.blit(self.background, (0, 0))
            self.display.blit(self.title_surface, (50, 50))
            self.display.blit(self.back_surface, self.back_rect)
            self.display.blit(self.submenu_surface, self.submenu_rect)
            #self.display.blit(self.text_surface, self.text_rect)
            return

