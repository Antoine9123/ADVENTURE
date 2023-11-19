import pygame


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

        self.create_surface = self.menu_font.render('Create Character', True, (250, 250, 210))
        self.create_rect = self.create_surface.get_rect(topleft=(80, 160))

        self.select_surface = self.menu_font.render('Select Character', True, (250, 250, 210))
        self.select_rect = self.select_surface.get_rect(topleft=(80, 230))

        self.delete_surface = self.menu_font.render('Delete Character', True, (250, 250, 210))
        self.delete_rect = self.delete_surface.get_rect(topleft=(80, 300))

    def load_background(self):
        self.background = pygame.image.load('GAME/img/menu/background_menu.jpg')
        self.background = pygame.transform.scale(self.background, (self.SCREENWIDTH, self.SCREENHEIGHT))

    def run(self):

        if self.create_rect.collidepoint(pygame.mouse.get_pos()):
            self.create_surface = self.menu_font.render('Create Character', True, (0,0,0))
            if pygame.mouse.get_pressed() == (1,0,0):
                self.gameStateManager.set_state('create')
        else:
            self.create_surface = self.menu_font.render('Create Character', True, (250, 250, 210))

        if self.select_rect.collidepoint(pygame.mouse.get_pos()):
            self.select_surface = self.menu_font.render('Select Character', True, (0,0,0))
            if pygame.mouse.get_pressed() == (1,0,0):
                self.gameStateManager.set_state('select')
        else:
            self.select_surface = self.menu_font.render('Select Character', True, (250, 250, 210))

        if self.delete_rect.collidepoint(pygame.mouse.get_pos()):
            self.delete_surface = self.menu_font.render('Delete Character', True, (0,0,0))
            if pygame.mouse.get_pressed() == (1,0,0):
                self.gameStateManager.set_state('delete')
        else:
            self.delete_surface = self.menu_font.render('Delete Character', True, (250, 250, 210))

        self.display.blit(self.background, (0, 0))
        self.display.blit(self.title_surface, (50, 50))
        self.display.blit(self.create_surface, self.create_rect)
        self.display.blit(self.select_surface, self.select_rect)
        self.display.blit(self.delete_surface, self.delete_rect)





