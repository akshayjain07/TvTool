import tkinter as tk
from tkinter import ttk

class BottomHoldingsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#F0F0F0")

        # Configure grid to expand
        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        # Get screen width
        sys_width = self.winfo_screenwidth()
        
        # Calculate font size relative to screen width
        font_size = int(sys_width * 0.0065)  # Adjust this factor as needed

        # Geometry Part 
        sys_width = self.winfo_screenwidth()
        sys_height = self.winfo_screenheight()
        component_width = sys_width/6


        # Creating a custom style for the checkbox
        style = ttk.Style()
        style.configure("Custom.TCheckbutton",
                        background="#070707",  # Set custom background color
                        foreground="#FFFFFF")  # Set custom foreground color

        # Creating the checkbox with integrated text and applying the custom style
        checkbox_var = tk.BooleanVar()
        checkbox = ttk.Checkbutton(self, text="Add T1 Holdings", variable=checkbox_var, style="Custom.TCheckbutton")
        checkbox.pack(padx=70, pady=(20, 20))



        # List of buttons with their text, image file, coordinates, height, and width
        buttons_info = [
            ("   Export Holdings", "api_logo.png", "#5EA3A3", sys_width-(sys_width-component_width)- 150 - ((component_width-150)/2) , 105, 35, 150),
            ("   Exit", "start_logo.png", "#5EA3A3", sys_width-(sys_width-component_width)- component_width/2 - 70 - ((component_width/2-70)/2) , 60, 35, 80),
            ("   Refresh", "stop_logo.png", "#5EA3A3", sys_width-(sys_width-component_width) - 130 - ((component_width/2-130)/2) , 60, 35, 100)
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

        # Create label with word wrap and background color
        label = ttk.Label(self, text="1. This Grid is a replica of Broker's Holdings.\n2. Holdings are refreshed only once on Start Trading.\n3. You can create groups by Dragging one or more column(s) into Drag a column Area for better viewing.",
                          wraplength=sys_width * 0.14,  # Set wraplength to 80% of screen width
                          background="#070707",
                          foreground="#D9CB50",
                          font=("Helvetica", font_size))
        label.pack(padx=10, pady=(100,0))




