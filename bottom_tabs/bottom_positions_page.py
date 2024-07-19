import tkinter as tk
from tkinter import ttk

class BottomPositionsPage(tk.Frame):
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
        
        # Create label with word wrap and background color
        label = ttk.Label(self, text="1. This Grid is a replica of Broker's Positions. It Includes manual and other positions taken outside of Bridge./n2. Positions refreshed only if Trading is Started in the Bridge and are not Squared Off.\n3. LTP will not be updated for Zero Net Positions.\n4. You can create groups by Dragging one or more column(s) into Drag a column Area for better viewing.",
                          wraplength=sys_width * 0.14,  # Set wraplength to 80% of screen width
                          background="#070707",
                          foreground="#D9CB50",
                          font=("Helvetica", font_size))
        label.pack(padx=10, pady=(140,0))


        # Geometry Part 
        sys_width = self.winfo_screenwidth()
        sys_height = self.winfo_screenheight()
        component_width = sys_width/6

        # List of buttons with their text, image file, coordinates, height, and width
        buttons_info = [
            ("   Refresh", "api_logo.png", "#5EA3A3", sys_width-(sys_width-component_width)- 115 - ((component_width-115)/2) , 10, 35, 110),
            ("   Convert Positions", "api_logo.png", "#5EA3A3", sys_width-(sys_width-component_width)- 180 - ((component_width-180)/2) , 55, 35, 170),
            ("   Exit", "start_logo.png", "#5EA3A3", sys_width-(sys_width-component_width)- component_width/2 - 70 - ((component_width/2-70)/2) , 100, 35, 80),
            ("   Export", "stop_logo.png", "#5EA3A3", sys_width-(sys_width-component_width) - 110 - ((component_width/2-110)/2) , 100, 35, 80)
            # ("   Export", "api_logo.png", "#5EA3A3", sys_width-(sys_width-component_width)- 210 - ((component_width-210)/2) , 90, 35, 100),
            # ("   Exit", "api_logo.png", "#5EA3A3", sys_width-(sys_width-component_width)- 210 - ((component_width-210)/2) , 130, 35, 100)
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
