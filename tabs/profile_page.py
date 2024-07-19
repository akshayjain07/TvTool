import tkinter as tk
from tkinter import ttk

class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#F0F0F0')

        # Configure grid to expand
        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        
        label = ttk.Label(self, text="This is the Profile Page AJ")
        label.pack(padx=10, pady=10)
