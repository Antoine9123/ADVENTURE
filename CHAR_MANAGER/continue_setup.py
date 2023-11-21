from tkinter import ttk
import os
import pickle
import subprocess


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
        
        select_button = ttk.Button(self, text="Select", command=self.select_action)
        select_button.pack(side='left', padx=5)

        delete_button = ttk.Button(self, text="Delete", command=self.delete_action)
        delete_button.pack(side='left', padx=5)

        refresh_button = ttk.Button(self, text="Refresh", command=self.refresh_action)
        refresh_button.pack(side='right', padx=5)

    def select_action(self):
        try:
            selected_value = self.combobox.get()
            with open(f"GAME/personnage/{selected_value}.data", "rb") as fic:
                get_record = pickle.Unpickler(fic)
                selected_player = get_record.load()
            with open("GAME/last_char.data", "wb") as fic:
                record = pickle.Pickler(fic)
                record.dump(selected_player)
            self.master.destroy()
            subprocess.run(["python", "LAUNCHER.py"])
        except:
            pass

    def delete_action(self):
        selected_value = self.combobox.get()
        print("Deleted file:", selected_value)

    def refresh_action(self):
        print("Screen Refreshed")
