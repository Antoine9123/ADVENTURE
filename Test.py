class First:
    def __init__(self):
        self.bonjour = "bonjour"
        self.aurevoir = "aurevoir"
        
class Second:
    def __init__(self):
        self.nothing = "nothing"
    
    def dire_bjr(self,objet):
        print(objet.bonjour)
        
Second().dire_bjr(First())