import tkinter as tk
from tkinter import ttk

from globals_setup import *

####    Menu Frame               ---------------------------------------------------------------------------------------->
class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.place(x=10, y=10,relheight=0.1,relwidth=0.8)

        self.create_widgets()
    
    def create_widgets(self):
        menu_create = ttk.Button(self, text= "Create")
        menu_select = ttk.Button(self, text= "Select")
        menu_quit  = ttk.Button(self, text= "Quit")

        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0), weight=1, uniform='a')

        menu_create.grid(row=0,column=0, sticky='nswe')
        menu_select.grid(row=0,column=1, sticky='nswe')
        menu_quit.grid(row=0,column=2, sticky='nswe')
    


####    Main Frame               ---------------------------------------------------------------------------------------->
class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, background='blue').pack(expand= True, fill= 'both')
        self.place(x=10, y=90,relheight=0.7,relwidth=0.8)
        
        self.create_widgets()
    
    def create_widgets(self):
        menu_create = ttk.Button(self)

####    Main Frame               ---------------------------------------------------------------------------------------->
class Start(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(x=(WIDHT-280), y=(HEIGHT- 60),relheight=0.1,relwidth=0.3)

        self.create_widgets()
    
    def create_widgets(self):
        start_label = ttk.Label(self, text= "Character :")
        start_name = ttk.Label(self, text= "Char Name")
        start_play  = ttk.Button(self, text= "Play")

        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0), weight=1, uniform='a')

        start_label.grid(row=0,column=0, sticky='nswe')
        start_name.grid(row=0,column=1, sticky='nswe')
        start_play.grid(row=0,column=2, sticky='nswe')


    


