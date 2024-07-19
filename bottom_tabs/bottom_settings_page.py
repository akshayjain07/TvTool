import tkinter as tk
from tkinter import ttk

class BottomSettingsPage(tk.Frame):
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
        label = ttk.Label(self, text="PRESS ENTER TO SAVE THE ROW.\nPRESS ESC TO CANCEL SAVING.\nUSE TAB FOR BETTER EXPERIENCE WHILE FILLING DATA\n1. Bridge never collects user id or related details. Any provided ID, Password or any other sensitive information will be saved only in user's computer with encryption.\n2. Password and Pin is only required if you have selected for Auto Login. Auto login internally fills user details in browser for easy login. It is totally optional feature.\n3. If you are facing Login issue with Zerodha, AliceBlue, Upstox.",
                          wraplength=sys_width * 0.15,  # Set wraplength to 14% of screen width
                          background="#070707",
                          foreground="#D9CB50",
                          font=("Helvetica", font_size))
        label.pack(padx=5, pady=(135, 0))

        # List of buttons with their text, image file, coordinates, height, and width
        buttons_info = [
            ("Refresh", "refresh_logo.png", 20, 20, 60, 60),
            ("Import", "import_logo.png", 90, 20, 60, 60),
            ("Export", "export_logo.png", 160, 20, 60, 60),
        ]

        self.buttons = []

        for text, image_file, x, y, height, width in buttons_info:
            # Load the image
            image = tk.PhotoImage(file=image_file)  # Make sure the image files exist

            # Create button with image and text
            button = tk.Button(self, text=text, image=image, compound='top', bg="#5EA3A3", fg='white',
                               font=("Times New Roman", 12), bd=0, relief=tk.FLAT, cursor='hand2')
            button.place(x=x, y=y, height=height, width=width)
            button.image = image  # Keep a reference to avoid garbage collection
            self.buttons.append(button)
            
        # Geometry Part 
        sys_width = self.winfo_screenwidth()
        sys_height = self.winfo_screenheight()
        component_width = sys_width/6

        # List of buttons with their text, image file, coordinates, height, and width
        buttons_info = [
               ("   Help", "setting_logo.png", "#5EA3A3", sys_width-(sys_width-component_width)- 110 - ((component_width-110)/2) , 90, 35, 100)
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

