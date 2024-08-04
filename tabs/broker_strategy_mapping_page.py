import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymongo
from datetime import datetime
from PIL import Image, ImageTk

class BrokerStrategyMappingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#F0F0F0')
        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        self.create_ui()

    def create_ui(self):
        # Horizontal bar1
        bar1 = tk.Frame(self, bg='#EBEBEB', height=100)
        bar1.pack(fill='x', pady=10)

        # Headings
        headings = ['Select Broker', 'Index', 'Select Strategy', 'Lots']
        x_coords_headings = [100, 350, 600, 850]
        font_settings_heading = ("Arial", 10, "bold")

        for i, heading in enumerate(headings):
            tk.Label(bar1, text=heading, bg='#EBEBEB', font=font_settings_heading).place(x=x_coords_headings[i], y=15)

        # Dropdown for Select Broker
        broker_options = [
            "Alice Blue", "Angel One", "Dhan", "Fyers", "ICICI", "IIFL", 
            "Kotak Neo", "Nuvama", "Shoonya", "Upstox", "Zerodha", "Zerodha-enc"
        ]
        self.selected_broker = tk.StringVar()
        broker_dropdown = ttk.Combobox(bar1, textvariable=self.selected_broker, values=broker_options)
        broker_dropdown.place(x=100, y=40, width=150)

        # Textbox for Index
        self.index_entry = tk.Entry(bar1)
        self.index_entry.place(x=350, y=40, width=100)
        self.index_entry.config(validate="key", validatecommand=(self.register(self.validate_positive_number), '%P'))

        # Dropdown for Select Strategy
        strategy_options = ["MACD Crossover", "EMI Crossover", "Strategy-3", "Strategy-4", "Strategy-5"]
        self.selected_strategy = tk.StringVar()
        strategy_dropdown = ttk.Combobox(bar1, textvariable=self.selected_strategy, values=strategy_options)
        strategy_dropdown.place(x=600, y=40, width=150)

        # Textbox for Lots
        self.lots_entry = tk.Entry(bar1)
        self.lots_entry.place(x=850, y=40, width=100)
        self.lots_entry.config(validate="key", validatecommand=(self.register(self.validate_positive_number), '%P'))
        
        # Button to Add Strategy
        add_button = tk.Button(bar1, text="ADD Strategy", command=self.add_strategy)
        add_button.place(x=1050, y=30)

        # Create table headers for the strategy list
        bar2 = tk.Frame(self, bg='#EBEBEB', height=30)
        bar2.pack(fill='x', pady=10)

        headers = ['Brokers', 'Index', 'Strategy', 'Lots', 'Status', 'Last Updated']
        x_coords_headers = [40, 300, 500, 700, 900, 1100]
        font_settings_heading = ("Arial", 10, "bold")

        for i, header in enumerate(headers):
            tk.Label(bar2, text=header, bg='#EBEBEB', font=font_settings_heading).place(x=x_coords_headers[i], y=5)

        # Frame for the strategy table
        self.strategy_frame = tk.Frame(self, bg='#F0F0F0')
        self.strategy_frame.place(x=40, y=180, relwidth=0.9, relheight=0.6)

        self.update_strategy_table()

    def validate_positive_number(self, value):
        if value.isdigit() and int(value) >= 0:
            return True
        elif value == "":
            return True
        else:
            return False

    def add_strategy(self):
        # Function to add strategy to the table and MongoDB
        broker = self.selected_broker.get()
        index = self.index_entry.get()
        strategy = self.selected_strategy.get()
        lots = self.lots_entry.get()
        status = "Active"
        last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Add to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["trading"]
        collection = db["broker_strategy_mapping"]
        new_strategy = {
            "broker": broker,
            "index": index,
            "strategy": strategy,
            "lots": lots,
            "status": status,
            "last_updated": last_updated
        }
        collection.insert_one(new_strategy)
        
        # Clear the entry fields
        self.selected_broker.set('')
        self.index_entry.delete(0, tk.END)
        self.selected_strategy.set('')
        self.lots_entry.delete(0, tk.END)
        
        # Update the strategy table
        self.update_strategy_table()

    def update_strategy_table(self):
        # Clear previous strategy rows
        for widget in self.strategy_frame.winfo_children():
            widget.destroy()

        # Fetch and display data from MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["trading"]
        collection = db["broker_strategy_mapping"]
        data = collection.find()

        y = 0  # Start position for data rows
        font_settings = ("Arial", 10)
        
        # Load images for edit and delete icons
        edit_image = Image.open("edit_icon.png")
        edit_icon = ImageTk.PhotoImage(edit_image)
        delete_image = Image.open("delete_icon.png")
        delete_icon = ImageTk.PhotoImage(delete_image)

        # Broker images mapping
        broker_images = {
            "Alice Blue": "alice_blue.png",
            "Angel One": "angel_one.png",
            "Dhan": "dhan.png",
            "Fyers": "fyers.png",
            "ICICI": "icici.png",
            "IIFL": "iifl.png",
            "Kotak Neo": "kotak_neo.png",
            "Nuvama": "nuvama.png",
            "Shoonya": "shoonya.png",
            "Upstox": "upstox.png",
            "Zerodha": "zerodha.png",
            "Zerodha-enc": "zerodha_enc.png"
        }

        for strategy in data:
            broker_frame = tk.Frame(self.strategy_frame, bg='#F0F0F0')
            # broker_frame.place(x=0, y=y, width=970, height=30)
            broker_frame.place(x=0, y=y, width=1400, height=30)

            # Broker image
            broker_image_path = broker_images.get(strategy["broker"], "default_image.png")
            broker_image = Image.open(f"assets/brokers_logo_xs/{broker_image_path}")
            broker_photo = ImageTk.PhotoImage(broker_image)
            image_label = tk.Label(broker_frame, image=broker_photo, bg='#F0F0F0')
            image_label.image = broker_photo  # Keep a reference
            image_label.place(x=0, y=0, width=30, height=30)

            # Broker name
            broker_label = tk.Label(broker_frame, text=strategy["broker"], bg='#F0F0F0', font=font_settings)
            broker_label.place(x=40, y=4)
            index_label = tk.Label(broker_frame, text=strategy["index"], bg='#F0F0F0', font=font_settings)
            index_label.place(x=260, y=4)
            strategy_label = tk.Label(broker_frame, text=strategy["strategy"], bg='#F0F0F0', font=font_settings)
            strategy_label.place(x=460, y=4)
            lots_label = tk.Label(broker_frame, text=strategy["lots"], bg='#F0F0F0', font=font_settings)
            lots_label.place(x=660, y=4)
            status_label = tk.Label(broker_frame, text=strategy["status"], bg='#F0F0F0', font=font_settings)
            status_label.place(x=860, y=4)
            last_updated_label = tk.Label(broker_frame, text=strategy["last_updated"], bg='#F0F0F0', font=font_settings)
            last_updated_label.place(x=1040, y=4)

            # Edit and delete buttons with icons
            edit_button = tk.Button(broker_frame, image=edit_icon, command=lambda s=strategy: self.edit_strategy(s))
            edit_button.image = edit_icon  # Keep a reference to avoid garbage collection
            edit_button.place(x=1210, y=0)
            delete_button = tk.Button(broker_frame, image=delete_icon, command=lambda s=strategy: self.delete_strategy(s))
            delete_button.image = delete_icon  # Keep a reference to avoid garbage collection
            delete_button.place(x=1260, y=0)

            y += 30  # Move to the next row position

    def delete_strategy(self, strategy):
        # Confirm before deleting
        if messagebox.askokcancel("Delete", "Are you sure you want to delete this strategy?"):
            # Delete from MongoDB
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client["trading"]
            collection = db["broker_strategy_mapping"]
            collection.delete_one({"_id": strategy["_id"]})
            
            # Update the strategy table
            self.update_strategy_table()

    def edit_strategy(self, strategy):
        # Edit window
        edit_window = tk.Toplevel(self)
        edit_window.title("Edit Strategy")
        edit_window.geometry("300x250")

        # Dropdown for Select Broker
        tk.Label(edit_window, text="Select Broker").place(x=10, y=10)
        selected_broker = tk.StringVar(value=strategy["broker"])
        broker_dropdown = ttk.Combobox(edit_window, textvariable=selected_broker, values=[
            "Alice Blue", "Angel One", "Dhan", "Fyers", "ICICI", "IIFL", 
            "Kotak Neo", "Nuvama", "Shoonya", "Upstox", "Zerodha", "Zerodha-enc"
        ])
        broker_dropdown.place(x=120, y=10, width=150)

        # Textbox for Index
        tk.Label(edit_window, text="Index").place(x=10, y=50)
        index_entry = tk.Entry(edit_window)
        index_entry.insert(0, strategy["index"])
        index_entry.place(x=120, y=50, width=150)
        index_entry.config(validate="key", validatecommand=(self.register(self.validate_positive_number), '%P'))

        # Dropdown for Select Strategy
        tk.Label(edit_window, text="Select Strategy").place(x=10, y=90)
        selected_strategy = tk.StringVar(value=strategy["strategy"])
        strategy_dropdown = ttk.Combobox(edit_window, textvariable=selected_strategy, values=[
            "MACD Crossover", "EMI Crossover", "Strategy-3", "Strategy-4", "Strategy-5"
        ])
        strategy_dropdown.place(x=120, y=90, width=150)

        # Textbox for Lots
        tk.Label(edit_window, text="Lots").place(x=10, y=130)
        lots_entry = tk.Entry(edit_window)
        lots_entry.insert(0, strategy["lots"])
        lots_entry.place(x=120, y=130, width=150)
        lots_entry.config(validate="key", validatecommand=(self.register(self.validate_positive_number), '%P'))

        # Buttons
        update_button = tk.Button(edit_window, text="Update", command=lambda: self.update_strategy(
            strategy["_id"], selected_broker.get(), index_entry.get(), selected_strategy.get(), lots_entry.get(), edit_window
        ))
        update_button.place(x=80, y=170)
        cancel_button = tk.Button(edit_window, text="Cancel", command=edit_window.destroy)
        cancel_button.place(x=160, y=170)
        cancel_button.place(x=160, y=170)

    def update_strategy(self, strategy_id, broker, index, strategy_name, lots, edit_window):
        # Update in MongoDB
        last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["trading"]
        collection = db["broker_strategy_mapping"]
        collection.update_one(
            {"_id": strategy_id},
            {"$set": {"broker": broker, "index": index, "strategy": strategy_name, "lots": lots, "last_updated": last_updated}}
        )
        # Close the edit window
        edit_window.destroy()
        # Update the strategy table
        self.update_strategy_table()