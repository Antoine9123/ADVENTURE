from tkinter import ttk


class Continue(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, background='blue').pack(expand= True, fill= 'both')
        self.place(x=10, y=90,relheight=0.7,relwidth=0.8)
        
        self.create_widgets()
        
    def create_widgets(self):
        menu_create = ttk.Button(self)