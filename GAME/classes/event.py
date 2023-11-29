from time import time
  

class EventManager:
    def __init__(self, ennemy, font, life_player) :
        self.events_queue = []
        self.ennemy = ennemy
        self.font = font
        self.life_player = life_player
    
    def events_check(self):
        i = 0
        while i < len(self.events_queue):
            current_time = time()
            if current_time >= self.events_queue[i]['time_to_trigger']:
                print(self.events_queue[i]['name'])
                self.life_ennemy = self.font.render(f'{self.ennemy.name} - HP :{self.ennemy.healthPoint}', True, (250, 250, 210))
                del self.events_queue[i]
            else:
                i += 1
             
    def add_event(self, name: str, delay: float):
        active_time = time() + (delay/1000)
        new_dict = {'name': name, 'time_to_trigger': active_time}
        self.events_queue.append(new_dict)







    
        
        
            
    
