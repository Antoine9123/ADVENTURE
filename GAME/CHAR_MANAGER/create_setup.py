import os
import json
import subprocess

import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox

from GAME.CHAR_MANAGER.globals_setup import MAX_POINT


class Create(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=10, y=90,relheight=0.7,relwidth=0.8) # Place into the frame
        self.create_widgets()
        self.parent = parent

    def create_widgets(self):
        #### Create Button
        save_char  = ttk.Button(self, text= "Create", command=self.save_new_personnage)
        #meter_stat = ttk.Progressbar(self)
        #meter_stat.configure(maximum=MAX_POINT)
        #meter_stat['value'] = int(self.strenght_entry.get()) + int(self.constitution_entry.get())+ int(self.dexterity_entry.get())+int(self.wisdom_entry.get())+ int(self.intelligence_entry.get())+ int(self.charisma_entry.get())
        
        #### Create Widgets
        self.general_label = tk.Label(self, text="GENERAL INFORMATION")    
        
        self.name_label = tk.Label(self, text="Name:")
        self.name_entry = tk.Entry(self)

        self.title_label = tk.Label(self, text="Title:")
        self.title_entry = tk.Entry(self)

        self.statistics_label = tk.Label(self, text="STATISTICS") 

        self.strenght_label = tk.Label(self, text="Strenght:")
        self.strenght_entry = tk.Spinbox(self, from_=1, to=20)
        
        self.constitution_label = tk.Label(self, text="Constitution:")
        self.constitution_entry = tk.Spinbox(self, from_=1, to=20)
        
        self.dexterity_label = tk.Label(self, text="Dexterity:")
        self.dexterity_entry = tk.Spinbox(self, from_=1, to=20)
        
        self.wisdom_label = tk.Label(self, text="Wisdom:")
        self.wisdom_entry = tk.Spinbox(self, from_=1, to=20)
        
        self.intelligence_label = tk.Label(self, text="Intelligence:")
        self.intelligence_entry = tk.Spinbox(self, from_=1, to=20)
        
        self.charisma_label = tk.Label(self, text="Charisma:")
        self.charisma_entry = tk.Spinbox(self, from_=1, to=20)
        
        #### Create Grid
        self.columnconfigure((0), weight=1, uniform='a')
        self.columnconfigure((1), weight=3, uniform='a')
        self.columnconfigure((2), weight=4, uniform='a')
        self.columnconfigure((3), weight=2, uniform='a')
        self.columnconfigure((4), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=2, uniform='a')
        self.rowconfigure((10), weight=1, uniform='a',pad=2)

        #### Place Widgets
        save_char.grid(row=8,rowspan=9, column=3,  sticky='we')
        #meter_stat.grid(row=6,rowspan=7, column=3,  sticky='we')

        self.general_label.grid(row=0, column=0,columnspan=2,sticky="w")

        self.name_label.grid(row=1, column=1, sticky="w")
        self.name_entry.grid(row=1, column=2, sticky="w")

        self.title_label.grid(row=2, column=1, sticky="w")
        self.title_entry.grid(row=2, column=2, sticky="w")

        self.statistics_label.grid(row=3, column=0,columnspan=2,sticky="w")

        self.strenght_label.grid(row=4, column=1, sticky="w")
        self.strenght_entry.grid(row=4, column=2, sticky="w")

        self.constitution_label.grid(row=5, column=1, sticky="w")
        self.constitution_entry.grid(row=5, column=2, sticky="w")

        self.dexterity_label.grid(row=6, column=1, sticky="w")
        self.dexterity_entry.grid(row=6, column=2, sticky="w")

        self.wisdom_label.grid(row=7, column=1, sticky="w")
        self.wisdom_entry.grid(row=7, column=2, sticky="w")

        self.intelligence_label.grid(row=8, column=1, sticky="w")
        self.intelligence_entry.grid(row=8, column=2, sticky="w")

        self.charisma_label.grid(row=9, column=1, sticky="w")
        self.charisma_entry.grid(row=9, column=2, sticky="w")

        

    def save_new_personnage(self):
        #### Imposition des conditions
        checked_stat = True
        checked_stat = self.check_create()

        # Encodage des stats
        if checked_stat == True:
            name = self.name_entry.get()
            title = self.title_entry.get()
            statSTR = int(self.strenght_entry.get())
            statCON = int(self.constitution_entry.get())
            statDEX = int(self.dexterity_entry.get())
            statWIS = int(self.wisdom_entry.get())
            statINT = int(self.intelligence_entry.get())
            statCHA = int(self.charisma_entry.get())
            level = 1

            new_player = {
                'name': name,
                'title': title,
                'statSTR': statSTR,
                'statCON': statCON,
                'statDEX': statDEX,
                'statWIS': statWIS,
                'statINT': statINT,
                'statCHA': statCHA,
                'level': level
                }

            file_path = f"GAME/personnage/{name}.json" 
            os.makedirs(os.path.dirname(file_path), exist_ok=True) # Check if repertory exist. If not, create it !

            player_json = json.dumps(new_player, indent=4)
            with open(f"GAME/personnage/{name}.json", "w") as fic:
                fic.write(player_json)
            
            with open(f"GAME/last_char.json", "w") as fic:
                fic.write(player_json)
            
            self.parent.destroy()
            subprocess.run(["python", "LAUNCHER.py"])

    def show_error(self, message):
        Messagebox.show_info(message, "Error Creation - Read Downside")
        return False

    def check_create(self):
        attributes = {
            "Strength": int(self.strenght_entry.get()),
            "Constitution": int(self.constitution_entry.get()),
            "Dexterity": int(self.dexterity_entry.get()),
            "Wisdom": int(self.wisdom_entry.get()),
            "Intelligence": int(self.intelligence_entry.get()),
            "Charisma": int(self.charisma_entry.get()),
        }

        name_length = len(self.name_entry.get())
        title_length = len(self.title_entry.get())
        total_point = sum(attributes.values())

        if name_length > 12 or title_length > 12:
            return self.show_error("Name or Title should be < 12")

        for attribute, value in attributes.items():
            if value <= 0 or value > 20:
                return self.show_error(f"{attribute} should be between 1 and 20")
            

        if total_point != MAX_POINT:
            return self.show_error(f"You didn't reach {MAX_POINT} points. Exceeded points = {MAX_POINT - total_point}")

        return True
    