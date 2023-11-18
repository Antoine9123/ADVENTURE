import tkinter as tk
from tkinter import ttk

####    Windows     ------------------------------------------------->
window = tk.Tk()
window.title('Character Manager')
window.geometry('200x300')

####    Title       ------------------------------------------------->
title_label = ttk.Label(master=window, text='Adventure Games - Character Manager', font = 'Calibri 24 bold')
title_label.pack()

####    Input Field ------------------------------------------------->
input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master= input_frame)
button = ttk.Button(master = input_frame, text = 'convert')
entry.pack()
button.pack()
input_frame.pack()

####    Run         ------------------------------------------------->
window.mainloop()