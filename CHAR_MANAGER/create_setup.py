import tkinter as tk
from tkinter import ttk


class Create(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=10, y=90,relheight=0.7,relwidth=0.8) 
        self.create_widgets()

    def create_widgets(self):
        #### Create Widgets
        general_label = tk.Label(self, text="GENERAL INFORMATION")    
        
        name_label = tk.Label(self, text="Name:")
        name_entry = tk.Entry(self, highlightthickness=0)

        title_label = tk.Label(self, text="Title:")
        title_entry = tk.Entry(self, highlightthickness=0)

        statistics_label = tk.Label(self, text="STATISTICS") 

        strenght_label = tk.Label(self, text="Strenght:")
        strenght_entry = tk.Entry(self, highlightthickness=0)
        
        constitution_label = tk.Label(self, text="Constitution:")
        constitution_entry = tk.Entry(self, highlightthickness=0)
        
        dexterity_label = tk.Label(self, text="Dexterity:")
        dexterity_entry = tk.Entry(self, highlightthickness=0)
        
        witness_label = tk.Label(self, text="Witness:")
        witness_entry = tk.Entry(self, highlightthickness=0)
        
        intelligence_label = tk.Label(self, text="Intelligence:")
        intelligence_entry = tk.Entry(self, highlightthickness=0)
        
        charisma_label = tk.Label(self, text="Charisma:")
        charisma_entry = tk.Entry(self, highlightthickness=0)
        
        #### Create Grid
        self.columnconfigure((0), weight=1, uniform='a')
        self.columnconfigure((1), weight=3, uniform='a')
        self.columnconfigure((2), weight=4, uniform='a')
        self.columnconfigure((3), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1, uniform='a')

        #### Place Widgets
        general_label.grid(row=0, column=0,columnspan=2,sticky="w")

        name_label.grid(row=1, column=1, sticky="w")
        name_entry.grid(row=1, column=2, sticky="w")

        title_label.grid(row=2, column=1, sticky="w")
        title_entry.grid(row=2, column=2, sticky="w")

        statistics_label.grid(row=3, column=0,columnspan=2,sticky="w")

        strenght_label.grid(row=4, column=1, sticky="w")
        strenght_entry.grid(row=4, column=2, sticky="w")

        constitution_label.grid(row=5, column=1, sticky="w")
        constitution_entry.grid(row=5, column=2, sticky="w")

        dexterity_label.grid(row=6, column=1, sticky="w")
        dexterity_entry.grid(row=6, column=2, sticky="w")

        witness_label.grid(row=7, column=1, sticky="w")
        witness_entry.grid(row=7, column=2, sticky="w")

        intelligence_label.grid(row=8, column=1, sticky="w")
        intelligence_entry.grid(row=8, column=2, sticky="w")

        charisma_label.grid(row=9, column=1, sticky="w")
        charisma_entry.grid(row=9, column=2, sticky="w")