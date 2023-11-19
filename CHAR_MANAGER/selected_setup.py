from tkinter import ttk


class Selected(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(x=(350), y=(20),height=324,width=200)

        self.create_widgets()
    
    def create_widgets(self):
        start_label = ttk.Label(self, text= "Character :")
        start_name = ttk.Label(self, text= "Char Name")

        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0), weight=1, uniform='a')

        start_label.grid(row=0,column=0, sticky='nswe')
        start_name.grid(row=0,column=1, sticky='nswe')