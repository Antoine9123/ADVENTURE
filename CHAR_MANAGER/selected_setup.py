import tkinter as tk
from tkinter import ttk
import pickle
import subprocess


class Selected(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(x=(350), y=(20),height=324,width=200)

        self.player = self.open_last()
        self.create_widgets(self.player)
    
    def create_widgets(self, player):
        start_frame = ttk.Frame(self)
        character_selected_frame = ttk.LabelFrame(start_frame, text="  Character Selected  ")
        selected_main = ttk.Frame(character_selected_frame)

        start_frame.pack()
        character_selected_frame.pack(side=tk.TOP, pady=10, padx=10) 
        selected_main.pack()

        name_label = tk.Label(selected_main, text="NAME :")
        title_label = tk.Label(selected_main, text="TITLE :")

        strenght_label = tk.Label(selected_main, text="STR :")
        constitution_label = tk.Label(selected_main, text="CON :")
        dexterity_label = tk.Label(selected_main, text="DEX :")
        witness_label = tk.Label(selected_main, text="WIT:")
        intelligence_label = tk.Label(selected_main, text="INT:")
        charisma_label = tk.Label(selected_main, text="CHA :")

        name = tk.Label(selected_main, text=player.nom)
        title = tk.Label(selected_main, text=player.titre)

        strenght = tk.Label(selected_main, text= player.force)
        constitution = tk.Label(selected_main, text= player.constitution)
        dexterity = tk.Label(selected_main, text= player.dexterite)
        witness = tk.Label(selected_main, text=player.sagesse)
        intelligence = tk.Label(selected_main, text=player.intelligence)
        charisma = tk.Label(selected_main, text=player.charisme)
   
        
        #### Create Grid
        selected_main.columnconfigure((0), weight=1, uniform='a')
        selected_main.columnconfigure((1), weight=5, uniform='a')
        selected_main.columnconfigure((2), weight=5, uniform='a')
        selected_main.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1, uniform='a')

        #### Place Widgets

        name_label.grid(row=1, column=1, sticky="w")
        title_label.grid(row=2, column=1, sticky="w")
 
        strenght_label.grid(row=4, column=1, sticky="w")
        constitution_label.grid(row=5, column=1, sticky="w")
        dexterity_label.grid(row=6, column=1, sticky="w")
        witness_label.grid(row=7, column=1, sticky="w")
        intelligence_label.grid(row=8, column=1, sticky="w")
        charisma_label.grid(row=9, column=1, sticky="w")

        name.grid(row=1, column=2, sticky="w")
        title.grid(row=2, column=2, sticky="w")
 
        strenght.grid(row=4, column=2, sticky="w")
        constitution.grid(row=5, column=2, sticky="w")
        dexterity.grid(row=6, column=2, sticky="w")
        witness.grid(row=7, column=2, sticky="w")
        intelligence.grid(row=8, column=2, sticky="w")
        charisma.grid(row=9, column=2, sticky="w")

    
    def open_last(self):
        with open(f"GAME/last_char.data", "rb") as fic:
            get_record = pickle.Unpickler(fic)
            last_player = get_record.load()
            return last_player
    



  