from tkinter import ttk
import os


class Continue(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=10, y=90, relheight=0.7, relwidth=0.8)

        self.create_widgets()

    def create_widgets(self):
        folder_path = "GAME/personnage"
        fichiers = os.listdir(folder_path)

        file_names = [os.path.splitext(f)[0] for f in fichiers]

        self.combobox = ttk.Combobox(self, values=file_names)
        self.combobox.pack(pady=10)
        
        button = ttk.Button(self, text="Print Selection", command=self.print_selection)
        button.pack(pady=10)

    def print_selection(self):
        selected_value = self.combobox.get()
        print("Selected file:", selected_value)