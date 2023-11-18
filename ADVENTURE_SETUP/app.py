import tkinter as tk
from tkinter import ttk
from classes import center_window

WIDHT, HEIGHT = 900, 550

# Main Window                 --------------------------------------------------------->
window = tk.Tk()
window.title('Character Manager')
center_window(window, WIDHT, HEIGHT)
window.overrideredirect(False)

# Background Image            --------------------------------------------------------->
bg_image = tk.PhotoImage(file="ADVENTURE_SETUP/background.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Make grid frame            --------------------------------------------------------->



# run Loop                      ------------------------------------------------------->
window.mainloop()
