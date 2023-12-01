import pygame


class FightMenu:
    def __init__(self, parent):
        self.parent = parent
        
    def display(self):
        self.menu_font = pygame.font.Font('GAME/font/Magic.ttf', 50)
        
        self.atk_surface = self.menu_font.render('- Attack', True, (20,20,20))
        self.mgk_surface = self.menu_font.render('- Spell', True, (20,20,20))
        
        self.atk_rect = self.atk_surface.get_rect()
        self.mgk_rect = self.mgk_surface.get_rect()
                    
        self.atk_rect.topleft = (400, 580)
        self.mgk_rect.topleft = (400, 620)
        
        self.cadre_rect = pygame.Rect(390, 580, 240, 120)
        self.cadre_surface = pygame.Surface((self.cadre_rect.width, self.cadre_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(self.cadre_surface, (0, 0, 0,90), (0, 0, self.cadre_rect.width, self.cadre_rect.height))
 
    
    def run(self):
        self.parent.blit(self.cadre_surface, self.cadre_rect.topleft)
        self.parent.blit(self.atk_surface, self.atk_rect)
        self.parent.blit(self.mgk_surface, self.mgk_rect)

            