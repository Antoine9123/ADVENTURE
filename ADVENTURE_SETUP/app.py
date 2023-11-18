import tkinter as tk
from tkinter import ttk

####    Windows     ------------------------------------------------->
window = tk.Tk()
window.title('Character Manager')
window.geometry('500x700')

background_path = ""

####    Title       ------------------------------------------------->
title_label = ttk.Label(master=window, text='Adventure Games\n Characters Manager', font = 'Calibri 24 bold')
title_label.pack()

####    Menu Create ------------------------------------------------->
create_frame = ttk.Frame(master=window)
name_label = ttk.Label(master=create_frame, text='Name', font = 'Calibri 12 bold')
name = ttk.Entry(master= create_frame)
statFOR_label = ttk.Label(master=create_frame, text='Strength', font = 'Calibri 12 bold')
statFOR = ttk.Entry(master= create_frame)

statCON_label = ttk.Label(master=create_frame, text='Constitution', font = 'Calibri 12 bold')
statCON = ttk.Entry(master= create_frame)

statDEX_label = ttk.Label(master=create_frame, text='Dexterity', font = 'Calibri 12 bold')
statDEX = ttk.Entry(master= create_frame)

statWIS_label = ttk.Label(master=create_frame, text='Wisdom', font = 'Calibri 12 bold')
statWIS = ttk.Entry(master= create_frame)

statINT_label = ttk.Label(master=create_frame, text='Intelligence', font = 'Calibri 12 bold')
statINT = ttk.Entry(master= create_frame)

statCHA_label = ttk.Label(master=create_frame, text='Charisma', font = 'Calibri 12 bold')
statCHA = ttk.Entry(master= create_frame)


button = ttk.Button(master = create_frame, text = 'Create Character')

####    Packing     ------------------------------------------------->
name_label.pack()
name.pack()
statFOR_label.pack()
statFOR.pack()

statCON_label.pack()
statCON.pack()

statDEX_label.pack()
statDEX.pack()

statWIS_label.pack()
statWIS.pack()

statINT_label.pack()
statINT.pack()

statCHA_label.pack()
statCHA.pack()

button.pack()
create_frame.pack()

####    Run         ------------------------------------------------->
window.mainloop()