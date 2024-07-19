import tkinter as tk
from tkinter import ttk

class BottomLeft(tk.Frame):
    def __init__(self, parent, width):
        super().__init__(parent, width=width, bg='#F0F0F0')
        self.pack_propagate(False)  # Prevent the frame from resizing to fit its content

        # Create grey border on top and right sides
        self.config(highlightbackground="grey", highlightthickness=1, highlightcolor="grey")

        # Geometry Part 
        sys_width = self.winfo_screenwidth()
        sys_height = self.winfo_screenheight()
        component_width = sys_width/6

        # List of buttons with their text, image file, coordinates, height, and width
        buttons_info = [
            ("   Verify API Login", "api_logo.png", "#4F98CA", sys_width-(sys_width-component_width)- 170 - ((component_width-170)/2) , 20, 35, 170),
            ("   Settings", "setting_logo.png", "#4F98CA", sys_width-(sys_width-component_width)- 110 - ((component_width-110)/2) , 275, 35, 110),
            ("   Start", "start_logo.png", "#6DB193", sys_width-(sys_width-component_width)- component_width/2 - 60 - ((component_width/2-60)/2) , 180, 35, 80),
            ("   Stop", "stop_logo.png", "#C74F50", sys_width-(sys_width-component_width) - 90 - ((component_width/2-90)/2) , 180, 35, 80),
            ("   Option Trading", "stop_logo.png", "#4F98CA", sys_width-(sys_width-component_width)- 150 - ((component_width-150)/2) , 65, 35, 150),
            ("   Trading Tools", "start_logo.png", "#4F98CA", sys_width-(sys_width-component_width)- 150 - ((component_width-150)/2)  , 230, 35, 150)
        ]

        self.buttons = []

        for text, image_file, bg, x, y, height, width in buttons_info:
            # Load the image
            image = tk.PhotoImage(file=image_file)  # Make sure the image files exist
            # image = tk.PhotoImage(file='profile_pic.png')  # Make sure the image files exist

            # Create button with image and text
            button = tk.Button(self, text=text, image=image, compound='left', bg=bg, fg='white',
                               font=("Times New Roman", 12), bd=0, relief=tk.FLAT, cursor='hand2')
            button.place(x=x, y=y, height=height, width=width)
            button.image = image  # Keep a reference to avoid garbage collection
            self.buttons.append(button)

        # Create dropdown for Freak Protection
        self.freak_protection_label = tk.Label(self, text="Freak Protection:", bg='#40474B', fg='white', font=("Times New Roman", 10))
        self.freak_protection_label.place(x=sys_width-(sys_width-component_width)- component_width/2 - 70 - ((component_width/2-70)/2), y=115)

        self.freak_protection_var = tk.StringVar(self)
        self.freak_protection_dropdown = ttk.Combobox(self, textvariable=self.freak_protection_var, state="readonly",
                                                      values=["Light", "Medium", "Strong"], font=("Times New Roman", 10), width=10)
        self.freak_protection_dropdown.place(x=sys_width-(sys_width-component_width)- component_width/2 - 60 - ((component_width/2-60)/2), y=145)
        self.freak_protection_dropdown.current(0)  # Set default value

        # Create dropdown for Trading Mode
        self.trading_mode_label = tk.Label(self, text="Trading Mode:", bg='#40474B', fg='white', font=("Times New Roman", 10))
        self.trading_mode_label.place(x=sys_width-(sys_width-component_width) - 90 - ((component_width/2-90)/2), y=115)

        self.trading_mode_var = tk.StringVar(self)
        self.trading_mode_dropdown = ttk.Combobox(self, textvariable=self.trading_mode_var, state="readonly",
                                                  values=["Live", "Not Live"], font=("Times New Roman", 10), width=10)
        self.trading_mode_dropdown.place(x=sys_width-(sys_width-component_width) - 90 - ((component_width/2-90)/2), y=145)
        self.trading_mode_dropdown.current(0)  # Set default value
