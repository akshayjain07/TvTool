import tkinter as tk
from tkinter import ttk

class StrategiesPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#F0F0F0')

        # Configure grid to expand
        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        
        # Add top label
        label = ttk.Label(self, text="Drag a column to group", background='#070707', foreground='white', font=("Helvetica", 12))
        label.pack(padx=10, pady=10)

        # Create a green horizontal bar
        green_bar = tk.Frame(self, bg='#239D60')
        green_bar.place(relx=0, rely=0.1, relwidth=1, height=30)  # Adjust relx, rely, relwidth, height as needed

        # List of buttons with their text, x, and width
        buttons_info = [
            ("Source Symbol   ", 10, 130),
            ("Request ID   ", 150, 110),
            ("Exchange   ", 270, 100),
            ("Exchange Symbol   ", 380, 140),
            ("LTP   ", 530, 60),
            ("P&L   ", 600, 60),
            ("Product   ", 670, 90),
            ("Entry Order Type   ", 770, 140),
            ("Entry Order ID   ", 920, 120),
            ("Entry Order Time   ", 1050, 140),
            ("Source Symbol   ", 1200, 130),
            ("Request ID   ", 1340, 110),
            ("Exchange   ", 1460, 100)
        ]

        # Load the image
        image_file = "filter_logo.png"
        image = tk.PhotoImage(file=image_file)  # Ensure this file exists

        self.buttons = []

        # Set y position for all buttons
        y = 0

        for text, x, width in buttons_info:
            # Create button with image and text
            button = tk.Button(green_bar, text=text, image=image, compound='right', bg="#239D60", fg='white',
                               font=("Helvetica", 10), bd=0, relief=tk.FLAT, cursor='hand2')
            button.place(x=x, y=y, height=30, width=width)
            button.image = image  # Keep a reference to avoid garbage collection
            self.buttons.append(button)
