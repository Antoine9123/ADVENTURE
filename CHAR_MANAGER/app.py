import tkinter as tk
from tkinter import font
from tkinter import ttk


WIDHT, HEIGHT = 900, 550
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_coordinate = (screen_width - width) // 2
    y_coordinate = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

def create_character(event):
    main_frame.config(bg="lightgreen")
    main_frame_label.config(text="Creating Character!")

    # Destroy previous widgets in the main_frame, excluding the button frame
    for widget in main_frame.winfo_children():
        if widget.winfo_class() != 'TButton':
            widget.destroy()

    # Create label for general information
    general_label = tk.Label(main_frame, text="GENERAL INFORMATION", font=button_font)
    general_label.grid(row=0, column=0, columnspan=2, sticky="w")

    # Create labels and entry widgets for general information
    name_label = tk.Label(main_frame, text="Name:", font=button_font)
    name_label.grid(row=1, column=0, sticky="w")

    name_entry = tk.Entry(main_frame, font=button_font, highlightthickness=0)
    name_entry.grid(row=1, column=1, sticky="w")

    title_label = tk.Label(main_frame, text="Title:", font=button_font)
    title_label.grid(row=2, column=0, sticky="w")

    title_entry = tk.Entry(main_frame, font=button_font, highlightthickness=0)
    title_entry.grid(row=2, column=1, sticky="w")

    # Create labels and entry widgets for statistics
    stats_label = tk.Label(main_frame, text="STATISTICS", font=button_font)
    stats_label.grid(row=3, column=0, columnspan=2, sticky="w")

    statistics = ["Strength", "Constitution", "Dexterity", "Witness", "Intelligence", "Charisma"]

    for i, stat in enumerate(statistics, start=4):
        label = tk.Label(main_frame, text=f"{stat}:", font=button_font)
        label.grid(row=i, column=0, sticky="w")

        entry = tk.Entry(main_frame, font=button_font, highlightthickness=0)
        entry.grid(row=i, column=1, sticky="w")

    # Create a frame for the buttons within main_frame
    button_frame = tk.Frame(main_frame)
    button_frame.grid(row=i + 1, column=0, columnspan=2, sticky="e")

    # Create "Create Character" button
    button_style = ttk.Style()
    button_style.configure("Rounded.TButton", borderwidth=2, relief="solid", borderradius=5, font=button_font)

    create_button = ttk.Button(button_frame, text="Create Character", command=submit_character, style="Rounded.TButton", padding=(5, 5))
    create_button.grid(row=0, column=0, sticky="e")

def submit_character():
    print("character created")
    pass

def select_character(event):

    main_frame.config(bg="lightgreen")
    main_frame_label.config(text="Selecting Character!")

def on_enter(event):
    event.widget.config(bg="lightcoral")

def on_leave(event):
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
main_frame = tk.Frame(window, bg="lightcoral")
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



# run Loop                      ------------------------------------------------------->
window.mainloop()
