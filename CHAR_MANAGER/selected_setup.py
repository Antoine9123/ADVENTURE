import tkinter as tk
from tkinter import ttk


class Selected(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(x=(350), y=(20),height=324,width=200)
        self.create_widgets()
    
    def create_widgets(self):
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

  