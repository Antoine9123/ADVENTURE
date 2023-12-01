import pygame


class FightTxt:
    def __init__(self, parent):
        self.parent = parent
        self.txt = 'Fight !'
        
    def display(self):
        self.txt_font = pygame.font.Font("GAME/font/Destroy.ttf", 45)
        self.txt_surface = self.txt_font.render(self.txt, True, ('#800000'))
        
    
    def run(self):    
            self.parent.blit(self.txt_surface, (650, 600))
    
    def set_text(self,txt):
        self.txt = str(txt)
        self.txt_surface = self.txt_font.render(self.txt, True, ('#800000'))
        


            