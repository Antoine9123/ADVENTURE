import pygame


class FightMenu:
    def __init__(self, parent, turn):
        self.parent = parent
        self.turn = turn
        
    def display(self):
        self.menu_font = pygame.font.Font(None, 45)
        
        self.atk_surface = self.menu_font.render('- Attaquer', True, (0,0,0))
        self.mgk_surface = self.menu_font.render('- Magie', True, (0,0,0))
        
        self.atk_rect = self.atk_surface.get_rect()
        self.mgk_rect = self.mgk_surface.get_rect()
                    
        self.atk_rect.topleft = (400, 580)
        self.mgk_rect.topleft = (400, 620)
        
        self.cadre_rect = pygame.Rect(390, 570, 220, 90)
        self.cadre_surface = pygame.Surface((self.cadre_rect.width, self.cadre_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(self.cadre_surface, (250, 250, 210), (0, 0, self.cadre_rect.width, self.cadre_rect.height))
 
    
    def run(self):
        if self.turn:
            self.parent.blit(self.cadre_surface, self.cadre_rect.topleft)
            self.parent.blit(self.atk_surface, self.atk_rect)
            self.parent.blit(self.mgk_surface, self.mgk_rect)

            