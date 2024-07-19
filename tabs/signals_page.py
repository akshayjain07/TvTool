import tkinter as tk
from tkinter import ttk
import pymongo

class SignalsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#F0F0F0')
        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.create_ui()

    def create_ui(self):
        # Horizontal bar
        bar = tk.Frame(self, bg='#EBEBEB', height=30)
        bar.pack(fill='x', pady=(10, 0))

        # Column headings
        headings = ['TimeStamp', 'Instruments', 'Type', 'Price', 'Strategy', 'Stop Loss', 'Take Profit', 'Duration']
        x_coords = [20, 285, 550, 710, 880, 1050, 1180, 1360]

        font_settings = ("Arial", 10, "bold")

        for i, heading in enumerate(headings):
            tk.Label(bar, text=heading, bg='#EBEBEB', font=font_settings).place(x=x_coords[i], y=5)

        # Frame for the table and scrollbar
        self.table_frame = tk.Frame(self, bg='#F0F0F0')
        self.table_frame.pack(fill='both', expand=True)

        # Create a canvas and scrollbar
        self.canvas = tk.Canvas(self.table_frame, bg='#F0F0F0')
        self.scrollbar = tk.Scrollbar(self.table_frame, orient="vertical", command=self.canvas.yview)

        # Create a frame to contain the table content
        self.scrollable_frame = tk.Frame(self.canvas, bg='#F0F0F0')

        # Add the scrollable frame to the canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Update the canvas scroll region when the scrollable frame is resized
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Add content to the inner frame
        for i in range(250):
            tk.Label(self.scrollable_frame, text=f"........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................", fg="#F0F0F0").pack()

        # Fetch and display data from MongoDB
        # Connect to MongoDB and fetch data
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["trading"]
        collection = db["signals"]
        data = collection.find()

        print("mongodb connected")

        y = 10  # Start position for data rows

        for signal in data:
            fields = ['date_time', 'symbol', 'signal_type', 'price', 'strategy', 'stop_loss', 'take_profit', 'duration']
            x_coords = [20, 220, 550, 710, 870, 1050, 1180, 1360]

            font_settings = ("Arial", 10)

            for i, field in enumerate(fields):
                value = signal.get(field, "")  # Corrected from `data.get` to `signal.get`
                # if field == "signal_type":
                #     if value == "BUY":
                #         color = "green"
                #     elif value == "SELL":
                #         color = "red"
                #     else:
                #         color = "black"
                #     tk.Label(self.scrollable_frame, text=value, bg='#F0F0F0', font=font_settings, fg=color).place(x=x_coords[i], y=y)
                # else:
                #     tk.Label(self.scrollable_frame, text=value, bg='#F0F0F0', font=font_settings).place(x=x_coords[i], y=y)

                tk.Label(self.scrollable_frame, text=value, bg='#F0F0F0', font=font_settings).place(x=x_coords[i], y=y)
            # Horizontal line separator
            tk.Frame(self.scrollable_frame, bg='#000000', height=1).place(x=0, y=y+25, relwidth=1)
            # tk.Frame(self.scrollable_frame, bg='#000000', height=1).pack(fill="x")
            y += 30  # Move to the next row position




