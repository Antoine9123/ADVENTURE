from tkinter import ttk
import subprocess

from CHAR_MANAGER.create_setup import Create
from CHAR_MANAGER.continue_setup import Continue
from CHAR_MANAGER.globals_setup import *


####    Main Frame               ---------------------------------------------------------------------------------------->
class Main(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=20, y=20, height=485, width=300)
        self.add(Continue(self), text= "Continue")
        self.add(Create(self), text= "New Player")

####    Start Frame               ---------------------------------------------------------------------------------------->
class Start(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=(350), y=(360),height=50,width=200)
        self.create_widgets()
    
    def create_widgets(self):
        start_play  = ttk.Button(self, text= "Play", command=self.switch_to_game)
        self.columnconfigure((0), weight=1, uniform='a')
        self.rowconfigure((0), weight=1, uniform='a')
        start_play.grid(row=0,column=0, sticky='nswe')
    
    def switch_to_game(self):
        self.master.destroy()
        subprocess.run(["python", "GAME/main.py"])

####    Quit Frame               ---------------------------------------------------------------------------------------->
class Quit(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=(WIDHT-30), y=(0),height=30,width=30)
        self.create_widgets()
    
    def create_widgets(self):
        quit_play  = ttk.Button(self, text= "X", command=self.quit_application)
        self.columnconfigure((0), weight=1, uniform='a')
        self.rowconfigure((0), weight=1, uniform='a')
        quit_play.grid(row=0,column=0, sticky='nswe')
    
    def quit_application(self):
        self.master.destroy()
        
        









    


