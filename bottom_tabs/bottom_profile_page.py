import tkinter as tk
from tkinter import ttk

class BottomProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#F0F0F0")

        # Configure grid to expand
        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        # Get screen width
        sys_width = self.winfo_screenwidth()
        
        # Calculate font size relative to screen width
        font_size = int(sys_width * 0.0055)  # Adjust this factor as needed
        
        # Create label with word wrap and background color
        label = ttk.Label(self, text="This is Bottom Profile Page",
                          wraplength=sys_width * 0.15,  # Set wraplength to 14% of screen width
                          background="#070707",
                          foreground="#D9CB50",
                          font=("Helvetica", font_size))
        label.pack(padx=5, pady=(135, 0))

       