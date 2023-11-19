import tkinter as tk
from tkinter import ttk
import subprocess


from CHAR_MANAGER.globals_setup import *
#### STRUCTURE ####
#### Menu Frame
#### Start Frame
#### Main Frame
# Create Frame
# Select Frame


####    Menu Frame               ---------------------------------------------------------------------------------------->
class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.place(x=10, y=10,relheight=0.1,relwidth=0.8)

        self.create_widgets()
    
    def create_widgets(self):
        menu_create = ttk.Button(self, text= "Create")
        menu_select = ttk.Button(self, text= "Select")

        self.columnconfigure((0,1), weight=1, uniform='a')
        self.rowconfigure((0), weight=1, uniform='a')

        menu_create.grid(row=0,column=0, sticky='nswe')
        menu_select.grid(row=0,column=1, sticky='nswe')

####    Start Frame               ---------------------------------------------------------------------------------------->
class Start(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(x=(WIDHT-280), y=(HEIGHT- 60),relheight=0.1,relwidth=0.3)

        self.create_widgets()
    
    def create_widgets(self):
        start_label = ttk.Label(self, text= "Character :")
        start_name = ttk.Label(self, text= "Char Name")
        start_play  = ttk.Button(self, text= "Play", command=self.switch_to_game)

        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0), weight=1, uniform='a')

        start_label.grid(row=0,column=0, sticky='nswe')
        start_name.grid(row=0,column=1, sticky='nswe')
        start_play.grid(row=0,column=2, sticky='nswe')
    
    def switch_to_game(self):
        self.master.destroy()
        subprocess.run(["python", "GAME/main.py"])

####    Quit Frame               ---------------------------------------------------------------------------------------->
class Quit(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(x=(WIDHT-80), y=(10),relheight=0.1,relwidth=0.1)

        self.create_widgets()
    
    def create_widgets(self):
        quit_play  = ttk.Button(self, text= "QUIT GAME", command=self.quit_application)

        self.columnconfigure((0), weight=1, uniform='a')
        self.rowconfigure((0), weight=1, uniform='a')

        quit_play.grid(row=0,column=0, sticky='nswe')
    
    def quit_application(self):
        self.master.destroy()

    
####    Main Frame               ---------------------------------------------------------------------------------------->
class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, background='blue').pack(expand= True, fill= 'both')
        self.place(x=10, y=90,relheight=0.7,relwidth=0.8)
        
        self.create_widgets()
    
    def create_widgets(self):
        menu_create = ttk.Button(self)

####    Create Frame               ---------------------------------------------------------------------------------------->
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
        self.columnconfigure((1), weight=2, uniform='a')
        self.columnconfigure((2), weight=2, uniform='a')
        self.columnconfigure((3), weight=8, uniform='a')
        self.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1, uniform='a')

        #### Place Widgets
        general_label.grid(row=0, column=1,columnspan=2,sticky="w")

        name_label.grid(row=1, column=1, sticky="w")
        name_entry.grid(row=1, column=2, sticky="w")

        title_label.grid(row=2, column=1, sticky="w")
        title_entry.grid(row=2, column=2, sticky="w")

        statistics_label.grid(row=3, column=1,sticky="w")

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







    


