import tkinter as tk
from tkinter import ttk
from classes import center_window

WIDHT, HEIGHT = 900, 550

# Main Window                 --------------------------------------------------------->
window = tk.Tk()
window.title('Character Manager')
center_window(window, WIDHT, HEIGHT)
window.overrideredirect(False)

padding = 30

# Background Image            --------------------------------------------------------->
bg_image = tk.PhotoImage(file="ADVENTURE_SETUP/background.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Make grid frame            --------------------------------------------------------->
menu_frame = tk.Frame(window, bg="lightblue", height=300)
menu_frame.grid(row=0, column=0, sticky="nsew", padx=padding, pady=padding)

main_frame = tk.Frame(window, bg="lightgreen")
main_frame.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=padding, pady=padding)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)


# run Loop                      ------------------------------------------------------->
window.mainloop()
