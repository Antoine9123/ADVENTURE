import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import json
import subprocess

from GAME.classes.char_sheet import Personnage


class Continue(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=10, y=90, relheight=0.7, relwidth=0.8)
        self.parent = parent
        self.player = self.open_last()
        self.create_widgets_selected(self.player)
        self.create_widgets()
        

        
    def open_last(self):
        with open(f"GAME/last_char.json", "r") as f:
            load_player = json.load(f)
            name = load_player['name']
            title = load_player['title']
            strenght = load_player['statSTR']
            constitution = load_player['statCON']
            dexterity = load_player['statDEX']
            wisdom = load_player['statWIS']
            intelligence = load_player['statINT']
            charisma = load_player['statCHA']
            level = load_player['level']
         
        return Personnage(name, title, strenght, constitution,dexterity, wisdom, intelligence, charisma, level) 
        
    def select_action(self):
        selected_value = self.combobox.get()
        with open(f"GAME/characters/{selected_value}.json", "r") as f:
            load_player = json.load(f)
        with open(f"GAME/last_char.json", "w") as fic:
            json.dump(load_player, fic, indent=4)
        self.parent.destroy()
        subprocess.run(["python", "LAUNCHER.py"])


    def delete_action(self):
        selected_value = self.combobox.get()
        try:
            os.remove(f"GAME/characters/{selected_value}.json")
            self.parent.destroy()
            subprocess.run(["python", "LAUNCHER.py"])
        except:
            messagebox.showinfo("Alerte", "Ceci est un message d'alerte !")

    def create_widgets(self):
        folder_path = "GAME/characters"
        fichiers = os.listdir(folder_path)
        file_names = [os.path.splitext(f)[0] for f in fichiers]

        self.combobox = ttk.Combobox(self, values=file_names)
        select_button = ttk.Button(self, text="Select", command=self.select_action)
        delete_button = ttk.Button(self, text="Delete", command=self.delete_action)

        self.combobox.place(x=60, y=30, width=100, anchor="center")
        select_button.place(x=160, y=30, width=60, anchor="center")
        delete_button.place(x=230, y=30, width=60, anchor="center")

    def create_widgets_selected(self, player):
        #### Installation du cadre
        start_frame = ttk.Frame(self)
        start_frame.place(x=10, y=30, height=150, width=500)

        character_selected_frame = ttk.LabelFrame(start_frame, text="  Character Selected  ")
        selected_main = ttk.Frame(character_selected_frame)

        character_selected_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, pady=10)
        selected_main.pack(fill="both", expand=True)

        start_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20, padx= 20)  # Pack the start_frame only once

        #### Installation des labels
        name_label = tk.Label(selected_main, text="NAME :")
        title_label = tk.Label(selected_main, text="lvl :")
        strenght_label = tk.Label(selected_main, text="Strenght :")
        constitution_label = tk.Label(selected_main, text="Constitution :")
        dexterity_label = tk.Label(selected_main, text="Dexterity :")
        witness_label = tk.Label(selected_main, text="Witness :")
        intelligence_label = tk.Label(selected_main, text="Intelligence :")
        charisma_label = tk.Label(selected_main, text="Charisma :")

        name = tk.Label(selected_main, text=player.name) # -------------------------->>>>> TODO
        title = tk.Label(selected_main, text='player.titre')
        strenght = tk.Label(selected_main, text= 'player.force')
        constitution = tk.Label(selected_main, text= 'player.constitution')
        dexterity = tk.Label(selected_main, text= 'player.dexterite')
        witness = tk.Label(selected_main, text='player.sagesse')
        intelligence = tk.Label(selected_main, text='player.intelligence')
        charisma = tk.Label(selected_main, text='player.charisme')
   
        #### Create Grid
        selected_main.columnconfigure(0, weight=1)
        selected_main.columnconfigure(1, weight=5)
        selected_main.columnconfigure(2, weight=4)
        selected_main.columnconfigure(3, weight=4)
        selected_main.columnconfigure(4, weight=4)
        selected_main.columnconfigure(5, weight=1)
        selected_main.rowconfigure(0, weight=2) 
        selected_main.rowconfigure(1, weight=1)
        selected_main.rowconfigure(2, weight=1)
        selected_main.rowconfigure(3, weight=1)
        selected_main.rowconfigure(4, weight=1)
        selected_main.rowconfigure(5, weight=2)


        #### Place Widgets
        name_label.grid(row=0, column=0, sticky="e", padx=(5, 0), pady=(5, 0))
        title_label.grid(row=0, column=1, sticky="e", padx=(5, 0), pady=(5, 0))

        strenght_label.grid(row=2, column=2, sticky="e", padx=(5, 0), pady=(5, 0))
        constitution_label.grid(row=3, column=2, sticky="e", padx=(5, 0), pady=(5, 0))
        dexterity_label.grid(row=4, column=2, sticky="e", padx=(5, 0), pady=(5, 0))
        witness_label.grid(row=2, column=3, sticky="e", padx=(5, 0), pady=(5, 0))
        intelligence_label.grid(row=3, column=3, sticky="e", padx=(5, 0), pady=(5, 0))
        charisma_label.grid(row=4, column=3, sticky="e", padx=(5, 0), pady=(5, 0))

        name.grid(row=0, column=1, sticky="w", padx=(0, 5), pady=(5, 0))
        title.grid(row=0, column=2, sticky="w", padx=(0, 5), pady=(5, 0))

        strenght.grid(row=2, column=3, sticky="w", padx=(0, 5), pady=(5, 0))
        constitution.grid(row=3, column=3, sticky="w", padx=(0, 5), pady=(5, 0))
        dexterity.grid(row=4, column=3, sticky="w", padx=(0, 5), pady=(5, 0))
        witness.grid(row=2, column=4, sticky="w", padx=(0, 5), pady=(5, 0))
        intelligence.grid(row=3, column=4, sticky="w", padx=(0, 5), pady=(5, 0))
        charisma.grid(row=4, column=4, sticky="w", padx=(0, 5), pady=(5, 0))


