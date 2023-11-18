import tkinter as tk
from tkinter import font
from tkinter import ttk
from classes import *

WIDHT, HEIGHT = 900, 550

def create_character(event):
    # Function to handle the "Create Character" button click
    # You can modify the content of the main_frame here
    main_frame.config(bg="lightblue")
    main_frame_label.config(text="Creating Character!")

def select_character(event):
    # Function to handle the "Select Character" button click
    # You can modify the content of the main_frame here
    main_frame.config(bg="lightgreen")
    main_frame_label.config(text="Selecting Character!")

def on_enter(event):
    # Function to handle mouse entering the button
    event.widget.config(bg="lightcoral")

def on_leave(event):
    # Function to handle mouse leaving the button
    event.widget.config(bg="lightblue")

# Main Window                 --------------------------------------------------------->
window = tk.Tk()
window.title('Character Manager')
center_window(window, WIDHT, HEIGHT)
window.overrideredirect(False)

padding = 30
button_font = font.Font(family="Arial", size=16, weight="bold")

# Background Image            --------------------------------------------------------->
bg_image = tk.PhotoImage(file="ADVENTURE_SETUP/background.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Make grid frame            --------------------------------------------------------->
 # Create the menu frame
menu_frame = tk.Frame(window, bg="lightblue", height=300)
menu_frame.grid(row=0, column=0, sticky="nsew", padx=padding, pady=padding)

# Create the main frame
main_frame = tk.Frame(window, bg="lightgreen")
main_frame.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=padding, pady=padding)

# Create a label in the main_frame to display content
main_frame_label = tk.Label(main_frame, text="Main Frame Content", font=button_font)
main_frame_label.pack()


window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)  # Left column
window.grid_columnconfigure(1, weight=4)  # Middle column
window.grid_columnconfigure(2, weight=4)  # Right column

# Create buttons using Labels


create_button = tk.Label(menu_frame, text="Create Character", bg="lightblue", padx=10, pady=10, font=button_font)
create_button.grid(row=0, column=0, sticky="ew")
create_button.bind("<Button-1>", create_character)
create_button.bind("<Enter>", on_enter)
create_button.bind("<Leave>", on_leave)

select_button = tk.Label(menu_frame, text="Select Character", bg="lightblue", padx=10, pady=10, font=button_font)
select_button.grid(row=1, column=0, sticky="ew")
select_button.bind("<Button-1>", select_character)
select_button.bind("<Enter>", on_enter)
select_button.bind("<Leave>", on_leave)




# Explicitly set columnspan for the Quit button


# run Loop                      ------------------------------------------------------->
window.mainloop()
