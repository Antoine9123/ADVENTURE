import tkinter as tk
from tkinter import ttk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

class FrameCreate:
    def __init__(self, info, main_frame):
        self.main_frame = main_frame
        self.info = info
        

    
    def create_frame(self):
        self.frame = ttk.Frame(master=self.main_frame)
        self.label_name = ttk.Label(master=self.frame, text=self.info, font = 'Calibri 12 bold')
        self.name = ttk.Entry(master= self.frame)

    
    def pack_frame(self):
        self.label_name.pack(side='left')
        self.name.pack()