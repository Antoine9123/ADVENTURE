from time import time
  

class EventManager:
    def __init__(self, fight, txt) :
        self.events_queue = []
        self.fight = fight
        self.txt = txt
    
    def events_check(self):
        i = 0
        while i < len(self.events_queue):
            current_time = time()
            if current_time >= self.events_queue[i]['time_to_trigger']:
                print(self.events_queue[i]['name'])
                self.fight.life_ennemy = self.fight.font.render(f'{self.fight.ennemy.name} - HP :{self.fight.ennemy.healthPoint}', True, (250, 250, 210))
                self.txt.set_text(f"{self.events_queue[i]['name']}")
                self.fight.menuFight.display()
                del self.events_queue[i]
            else:
                i += 1
             
    def add_event(self, name: str, delay: float):
        active_time = time() + (delay/1000)
        new_dict = {'name': name, 'time_to_trigger': active_time}
        self.events_queue.append(new_dict)







    
        
        
            
    
