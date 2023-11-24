import pygame


class FightTxt:
    def __init__(self, parent):
        self.parent = parent
        self.txt = "FIGHT !!!"
        
    def display(self):
        self.txt_font = pygame.font.Font(None, 45)
        self.txt_surface = self.txt_font.render(self.txt, True, ('red'))
        
    
    def run(self):    
            self.parent.blit(self.txt_surface, (500, 540))
    
    def set_text(self,txt):
        self.txt = str(txt)
        self.txt_surface = self.txt_font.render(self.txt, True, ('yellow'))
        


            