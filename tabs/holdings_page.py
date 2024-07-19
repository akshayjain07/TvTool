import tkinter as tk
from tkinter import ttk
import pymongo
import random
from datetime import datetime

class HoldingsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#F0F0F0')
        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        self.create_ui()

    def create_ui(self):
        # Horizontal bar
        bar1 = tk.Frame(self, bg='#EBEBEB', height=100)
        bar1.pack(fill='x', pady=10)

        summary_headings = ['Orders', 'Positions', 'Profit/Loss', 'Realised P/L', 'Unrealised P/L', 'Net Traded Value']
        summary_values = ['12', '11', '+7,780', '+7,780', '+7,780', '+7,780']  # Replace with dynamic values as needed
        x_coords_summary = [90, 290, 500, 710, 920, 1130]

        font_settings_heading = ("Arial", 10, "bold")
        font_settings_value = ("Arial", 12, "bold")

        for i, heading in enumerate(summary_headings):
            value = summary_values[i]
            color = "green" if value.startswith('+') else "black"
            tk.Label(bar1, text=heading, bg='#EBEBEB', font=font_settings_heading).place(x=x_coords_summary[i], y=15)
            tk.Label(bar1, text=value, bg='#EBEBEB', font=font_settings_value, fg=color).place(x=x_coords_summary[i]+10, y=40)

        def show_mtm_graph():
            new_window = tk.Toplevel(self)
            new_window.title("MTM Graph")
            new_window.geometry("600x400")
            # Add your MTM graph display code here

        tk.Button(bar1, text="Show MTM Graph", bg='#FFFFFF', font=font_settings_heading, command=show_mtm_graph).place(x=1300, y=30)

        bar2 = tk.Frame(self, bg='#EBEBEB', height=30)
        bar2.pack(fill='x')

        # Column headings
        headings = ['Instruments', 'Qty.', 'Avg.', 'LTP', 'P&L']
        x_coords = [40, 550, 800, 1030, 1240]

        font_settings = ("Arial", 10, "bold")

        for i, heading in enumerate(headings):
            tk.Label(bar2, text=heading, bg='#EBEBEB', font=font_settings).place(x=x_coords[i], y=5)

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
        self.fetch_and_display_data()

    def fetch_and_display_data(self):
        # Connect to MongoDB and fetch data
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["trading"]
        collection = db["positions"]
        data = collection.find()

        y = 10  # Start position for data rows

        for position in data:
            fields = ['instrument', 'quantity', 'average_price', 'ltp', 'pnl']
            x_coords = [40, 550, 800, 1030, 1230]

            font_settings = ("Arial", 10)

            for i, field in enumerate(fields):
                value = position.get(field, "")  # Corrected from `data.get` to `position.get`
                if field == "pnl":
                    color = "green" if float(value) > 0 else "red"
                    tk.Label(self.scrollable_frame, text=value, bg='#F0F0F0', font=font_settings, fg=color).place(x=x_coords[i], y=y)
                else:
                    tk.Label(self.scrollable_frame, text=value, bg='#F0F0F0', font=font_settings).place(x=x_coords[i], y=y)

            # Horizontal line separator
            tk.Frame(self.scrollable_frame, bg='#000000', height=1).place(x=0, y=y+25, relwidth=1)
            y += 30  # Move to the next row position
