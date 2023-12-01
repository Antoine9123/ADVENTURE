from time import time
  

class EventManager:
    def __init__(self, fight) :
        self.events_queue = []
        self.fight = fight
        
    
    def events_check(self):
        i = 0
        while i < len(self.events_queue):
            current_time = time()
            if current_time >= self.events_queue[i]['time_to_trigger']:
                if self.events_queue[i]['mode'] == True:
                    self.fight.load_players_screen()
                self.fight.txtFight.set_text(f"{self.events_queue[i]['txt']}")
                del self.events_queue[i]
            else:
                i += 1
             
    def add_event(self, txt: str, delay: float, mode: bool):
        active_time = time() + (delay/1000)
        new_dict = {'txt': txt, 'time_to_trigger': active_time, 'mode':mode}
        self.events_queue.append(new_dict)







    
        
        
            
    
