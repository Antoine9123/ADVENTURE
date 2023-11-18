import tkinter as tk
from tkinter import ttk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

####    Windows     ------------------------------------------------->
WIDHT, HEIGHT = 900,550
window = tk.Tk()
window.title('Character Manager')
center_window(window, WIDHT, HEIGHT)
window.overrideredirect(False)

bg_image = tk.PhotoImage(file = "ADVENTURE_SETUP/background.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1) 

####    Title       ------------------------------------------------->
title_label = ttk.Label(master=window, text='Adventure Games\n Characters Manager', font = 'Calibri 24 bold')
title_label.pack()

####    Menu Create ------------------------------------------------->
class FrameCreate:
    def __init__(self, info, main_frame):
        self.main_frame = main_frame
        self.frame = ttk.Frame(master=self.main_frame)
        self.info = info
        
        self.label_name = ttk.Label(master=self.frame, text=self.info, font = 'Calibri 12 bold')
        self.name = ttk.Entry(master= self.frame)
    
    def create_frame(self):
        self.label_name.pack(side='left')
        self.name.pack()

main_frame = ttk.Frame(master=window)

name = FrameCreate('name', main_frame)







button = ttk.Button(master = main_frame, text = 'Create Character')

####    Packing     ------------------------------------------------->

button.pack()
name.create_frame()
main_frame.pack()

####    Run         ------------------------------------------------->
window.mainloop()