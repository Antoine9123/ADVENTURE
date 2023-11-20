import tkinter as tk
from tkinter import ttk
import pickle
from GAME.character.char_sheet import Personnage


class Create(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=10, y=90,relheight=0.7,relwidth=0.8) 
        self.create_widgets()



    def create_widgets(self):
        #### Start Button
        save_char  = ttk.Button(self, text= "Create", command=self.save_new_personnage)
        

        #### Create Widgets
        self.general_label = tk.Label(self, text="GENERAL INFORMATION")    
        
        self.name_label = tk.Label(self, text="Name:")
        self.name_entry = tk.Entry(self, highlightthickness=0)

        self.title_label = tk.Label(self, text="Title:")
        self.title_entry = tk.Entry(self, highlightthickness=0)

        self.statistics_label = tk.Label(self, text="STATISTICS") 

        self.strenght_label = tk.Label(self, text="Strenght:")
        self.strenght_entry = tk.Entry(self, highlightthickness=0)
        
        self.constitution_label = tk.Label(self, text="Constitution:")
        self.constitution_entry = tk.Entry(self, highlightthickness=0)
        
        self.dexterity_label = tk.Label(self, text="Dexterity:")
        self.dexterity_entry = tk.Entry(self, highlightthickness=0)
        
        self.witness_label = tk.Label(self, text="Witness:")
        self.witness_entry = tk.Entry(self, highlightthickness=0)
        
        self.intelligence_label = tk.Label(self, text="Intelligence:")
        self.intelligence_entry = tk.Entry(self, highlightthickness=0)
        
        self.charisma_label = tk.Label(self, text="Charisma:")
        self.charisma_entry = tk.Entry(self, highlightthickness=0)
        
        #### Create Grid
        self.columnconfigure((0), weight=1, uniform='a')
        self.columnconfigure((1), weight=3, uniform='a')
        self.columnconfigure((2), weight=4, uniform='a')
        self.columnconfigure((3), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=2, uniform='a')
        self.rowconfigure((10), weight=1, uniform='a',pad=2)

        #### Place Widgets
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

        self.witness_label.grid(row=7, column=1, sticky="w")
        self.witness_entry.grid(row=7, column=2, sticky="w")

        self.intelligence_label.grid(row=8, column=1, sticky="w")
        self.intelligence_entry.grid(row=8, column=2, sticky="w")

        self.charisma_label.grid(row=9, column=1, sticky="w")
        self.charisma_entry.grid(row=9, column=2, sticky="w")

        save_char.grid(row=10,column=2, sticky='nswe')

    def save_new_personnage(self):
        name = self.name_entry.get()
        title = self.title_entry.get()
        statSTR = int(self.strenght_entry.get())
        statCON = int(self.constitution_entry.get())
        statDEX = int(self.dexterity_entry.get())
        statWIT = int(self.witness_entry.get())
        statINT = int(self.intelligence_entry.get())
        statCHA = int(self.charisma_entry.get())
        new_player = Personnage(name, title, statSTR, statCON, statDEX, statWIT, statINT, statCHA,1)
        
        with open(f"GAME/personnage/{new_player.nom}.data", "wb") as fic:
            record = pickle.Pickler(fic)
            record.dump(new_player)
        