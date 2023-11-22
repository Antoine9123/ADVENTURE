import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from CHAR_MANAGER.globals_setup import WIDHT, HEIGHT
from CHAR_MANAGER.quit_start_setup import Main, Quit, Start



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        tb.Style(theme="superhero")
        self.title('Character Manager')
        self.overrideredirect(True)

        # Positionning screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width - WIDHT) // 2
        y_coordinate = (screen_height - HEIGHT) // 2
        self.geometry(f"{WIDHT}x{HEIGHT}+{x_coordinate}+{y_coordinate}")

        # Background
        bg_image = tk.PhotoImage(file="CHAR_MANAGER/background.png")
        bg_label = tk.Label(self, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        # Widgets
        self.main = Main(self)
        self.start = Start(self)
        self.quit = Quit(self)
        
        # Running
        self.mainloop()
    


