import tkinter as tk
from tkinter import ttk

class Navbar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#EBEBEB', relief=tk.SUNKEN)
        self.parent = parent
        self.middle_component = None
        self.bottom_component = None  # Add reference to BottomComponent

        # Get screen dimensions
        self.sys_width = self.parent.winfo_screenwidth()
        self.sys_height = self.parent.winfo_screenheight()

        # Set initial dimensions
        width = int(self.sys_width * 0.8)
        height = int(self.sys_height * 0.1)
        self.config(width=width, height=height)

        tabs = [
            ('SignalsPage', 'SIGNALS', 'button1', 'BottomSignalsPage'),
            ('OrdersPage', 'ORDERS', 'button2', 'BottomOrdersPage'),
            ('PositionsPage', 'POSITIONS', 'button3', 'BottomPositionsPage'),
            ('HoldingsPage', 'HOLDINGS', 'button4', 'BottomHoldingsPage'),
            ('SettingsPage', 'SETTINGS', 'button5', 'BottomSettingsPage'),
            ('StrategiesPage', 'STRATEGIES', 'button6', 'BottomStrategiesPage'),
            ('BrokersPage', 'BROKERS', 'button7', 'BottomBrokersPage'),
            ('BrokerStrategyMappingPage', 'BROKER STRATEGY MAPPING', 'button8', 'BottomBrokerStrategyMappingPage')
        ]

        self.tab_buttons = {}

        # Create buttons on the left side
        for tab in tabs:
            button = tk.Button(self, text=tab[1], padx=10, pady=15, bd=0, font=("Times New Roman", int(self.sys_height * 0.02)),
                               bg='#EBEBEB', fg='#000000', activebackground='#FFFFFF', activeforeground='#000000',
                               relief=tk.FLAT, cursor='hand2', command=lambda t=tab: self.show_page(t))
            button.pack(side='left', padx=10, pady=1)
            self.tab_buttons[tab[2]] = button

        # Load the image using PhotoImage
        profile_pic = tk.PhotoImage(file='profile_pic.png')  # Assuming 'profile_pic.png' is your converted file
        # Resize the image as needed
        profile_pic = profile_pic.subsample(1, 1)  # Example resizing

        # Create the image-based button on the right side
        right_tabs = [('ProfilePage', profile_pic, 'button9', 'BottomProfilePage')]  # Use the loaded profile_pic
        for tab in right_tabs:
            button = tk.Button(self, image=profile_pic, bg='#EBEBEB', activebackground="#FFFFFF", bd=0, relief=tk.FLAT, cursor='hand2',
                               command=lambda t=tab: self.show_page(t))
            button.pack(side='right', padx=30)
            self.tab_buttons[tab[2]] = button
            button.image = profile_pic  # Keep a reference to avoid garbage collection

        self.bind("<Configure>", self.on_resize)

    def set_middle_component(self, middle_component):
        self.middle_component = middle_component

    def set_bottom_component(self, bottom_component):
        self.bottom_component = bottom_component

    def show_page(self, tab):
        middle_page, bottom_page = tab[0], tab[3]
        if self.middle_component:
            self.middle_component.show_frame(middle_page)
        if self.bottom_component:
            self.bottom_component.show_bottom_right_page(bottom_page)

    def on_resize(self, event):
        # Adjust button sizes based on the new size
        new_width = event.width
        new_height = event.height

        font_size = int(new_height * 0.2)
        for button in self.tab_buttons.values():
            button.config(font=("Times New Roman", font_size), padx=10, pady=15)


