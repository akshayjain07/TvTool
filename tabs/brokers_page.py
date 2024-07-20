import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient
from bson.objectid import ObjectId

class BrokersPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#F0F0F0')

        # Configure grid to expand
        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['trading']
        self.collection = self.db['brokers']

        self.brokers = []
        self.auth_codes = []

        self.load_brokers()

        # Horizontal bar with labels
        horizontal_bar1 = tk.Frame(self, bg='#EBEBEB')
        horizontal_bar1.place(x=35, y=20, width=970, height=30)
        
        # Create headings
        headings = ["Broker", "Index", "Executions", "Status", "Keys", "Actions"]
        heading_positions = [50, 200, 350, 500, 650, 800]
        heading_bg = "#EBEBEB"
        heading_font = ("Helvetica", 12)
        for i, heading in enumerate(headings):
            label = tk.Label(self, text=heading, bg=heading_bg, font=heading_font, padx=5, pady=5)
            label.place(x=heading_positions[i], y=20, width=140, height=30)

        self.dot_photo = tk.PhotoImage(file="three_dots.png")

        # Add Brokers heading
        add_brokers_label = tk.Label(self, text="Add Brokers", bg='#F0F0F0', font=("Helvetica", 16))
        add_brokers_label.place(x=1100, y=20, width=200, height=30)

        # Create broker cards on the right
        card_details = [
            {"name": "Alice Blue", "image": "alice_blue.png"},
            {"name": "Angel One", "image": "angel_one.png"},
            {"name": "Dhan", "image": "dhan.png"},
            {"name": "Fyers", "image": "fyers.png"},
            {"name": "ICICI", "image": "icici.png"},
            {"name": "IIFL", "image": "iifl.png"},
            {"name": "Kotak Neo", "image": "kotak_neo.png"},
            {"name": "Nuvama", "image": "nuvama.png"},
            {"name": "Shoonya", "image": "shoonya.png"},
            {"name": "Upstox", "image": "upstox.png"},
            {"name": "Zerodha", "image": "zerodha.png"},
            {"name": "Zerodha-enc", "image": "zerodha_enc.png"}
        ]

        card_positions = [
            {"x": 1050, "y": 60, "width": 130, "height": 110},
            {"x": 1200, "y": 60, "width": 130, "height": 110},
            {"x": 1350, "y": 60, "width": 130, "height": 110},
            {"x": 1050, "y": 180, "width": 130, "height": 110},
            {"x": 1200, "y": 180, "width": 130, "height": 110},
            {"x": 1350, "y": 180, "width": 130, "height": 110},
            {"x": 1050, "y": 300, "width": 130, "height": 110},
            {"x": 1200, "y": 300, "width": 130, "height": 110},
            {"x": 1350, "y": 300, "width": 130, "height": 110},
            {"x": 1050, "y": 420, "width": 130, "height": 110},
            {"x": 1200, "y": 420, "width": 130, "height": 110},
            {"x": 1350, "y": 420, "width": 130, "height": 110}
        ]

        for i, details in enumerate(card_details):
            card_frame = tk.Frame(self, bg='#EBEBEB')
            card_frame.place(x=card_positions[i]["x"], y=card_positions[i]["y"], width=card_positions[i]["width"], height=card_positions[i]["height"])
            
            # Image in the card
            card_image = tk.PhotoImage(file=f"assets/brokers_logo/{details['image']}")
            image_label = tk.Label(card_frame, image=card_image, bg='#EBEBEB')
            image_label.image = card_image  # Keep a reference
            image_label.place(x=10, y=10, width=110, height=50)
            
            # Text in the card
            text_label = tk.Label(card_frame, text=details['name'], font=("Helvetica", 10), bg='#EBEBEB', fg='black')
            text_label.place(x=10, y=60, width=110, height=20)
            
            # Add button in the card
            add_button = tk.Button(card_frame, text="Add", font=("Helvetica", 10), bg='#FDFDFD', fg='black', command=lambda n=details['name'], img=details['image']: self.add_broker(n, img))
            add_button.place(x=25, y=80, width=80, height=20)

    def load_brokers(self):
        self.brokers = list(self.collection.find())
        self.render_brokers()

    def add_broker(self, name, image):
        self.popup_auth_key(name, image)

    def show_keys(self, broker_id):
        broker = self.collection.find_one({"_id": ObjectId(broker_id)})
        if broker:
            messagebox.showinfo("Auth Key", f"The auth key for {broker['name']} is {broker['auth_key']}")

    def update_keys(self, broker_id):
        broker = self.collection.find_one({"_id": ObjectId(broker_id)})
        if broker:
            self.popup_update_key(broker)

    def remove_broker(self, broker_id):
        confirmation = messagebox.askokcancel("Remove Broker", "Do you really want to remove the broker?")
        if confirmation:
            self.collection.delete_one({"_id": ObjectId(broker_id)})
            self.load_brokers()

    def popup_auth_key(self, name, image):
        popup = tk.Toplevel(self)
        popup.title("Authentication Key")
        
        label = tk.Label(popup, text="Enter Auth Key")
        label.pack(side="top", fill="x", pady=10)
        
        entry = tk.Entry(popup)
        entry.pack(pady=5)
        
        def on_ok():
            auth_key = entry.get()
            if auth_key in self.auth_codes:
                messagebox.showerror("Error", "Broker already exists")
            else:
                self.auth_codes.append(auth_key)
                self.add_broker_to_list(name, image, auth_key)
            popup.destroy()

        button_frame = tk.Frame(popup)
        button_frame.pack(pady=5)

        ok_button = tk.Button(button_frame, text="OK", command=on_ok)
        ok_button.pack(side="left", padx=5)

        cancel_button = tk.Button(button_frame, text="Cancel", command=popup.destroy)
        cancel_button.pack(side="left", padx=5)

    def popup_update_key(self, broker):
        popup = tk.Toplevel(self)
        popup.title("Update Authentication Key")
        
        label = tk.Label(popup, text=f"Current Auth Key: {broker['auth_key']}")
        label.pack(side="top", fill="x", pady=10)
        
        new_key_label = tk.Label(popup, text="Enter New Auth Key")
        new_key_label.pack(side="top", fill="x", pady=10)
        
        entry = tk.Entry(popup)
        entry.pack(pady=5)
        
        def on_update():
            new_auth_key = entry.get()
            self.collection.update_one({"_id": broker["_id"]}, {"$set": {"auth_key": new_auth_key}})
            self.load_brokers()
            popup.destroy()

        button_frame = tk.Frame(popup)
        button_frame.pack(pady=5)

        update_button = tk.Button(button_frame, text="Update", command=on_update)
        update_button.pack(side="left", padx=5)

        cancel_button = tk.Button(button_frame, text="Cancel", command=popup.destroy)
        cancel_button.pack(side="left", padx=5)

    def add_broker_to_list(self, name, image, auth_key):
        # Check if the broker already exists
        existing_broker = self.collection.find_one({"name": name})
        if existing_broker:
            existing_broker["index"] += 1
            self.collection.update_one({"_id": existing_broker["_id"]}, {"$set": {"index": existing_broker["index"]}})
        else:
            broker_data = {
                "name": name,
                "image": image,
                "index": 1,
                "execution": "Pending",
                "status": "logged in",
                "auth_key": auth_key
            }
            self.collection.insert_one(broker_data)
        self.load_brokers()

    def render_brokers(self):
        # # Clear previous entries
        # for widget in self.winfo_children():
        #     if isinstance(widget, tk.Frame) and widget.winfo_y() > 60:  # Keep the ones above 60 pixels
        #         widget.destroy()

        for i, broker in enumerate(self.brokers):
            y_position = 60 + i * 40

            # Create frames and labels for each broker data
            broker_frame = tk.Frame(self, bg='#F0F0F0')
            broker_frame.place(x=35, y=y_position, width=970, height=30)

            image = tk.PhotoImage(file=f"assets/brokers_logo/{broker.get('image', 'default_image.png')}")
            image_label = tk.Label(broker_frame, image=image, bg='#F0F0F0')
            image_label.image = image  # Keep a reference
            image_label.place(x=30, y=0, width=30, height=30)

            name_label = tk.Label(broker_frame, text=broker.get('name', 'Unknown'), bg='#F0F0F0', font=("Helvetica", 10))
            name_label.place(x=70, y=0, width=60, height=30)

            index_label = tk.Label(broker_frame, text=str(broker.get('index', 'N/A')), bg='#F0F0F0', font=("Helvetica", 10))
            index_label.place(x=165, y=0, width=140, height=30)

            execution_label = tk.Label(broker_frame, text=broker.get('execution', 'Pending'), bg='#F0F0F0', font=("Helvetica", 10))
            execution_label.place(x=310, y=0, width=140, height=30)

            status = broker.get('status', 'Unknown')
            status_color = 'green' if status == 'logged in' else 'red'
            status_frame = tk.Frame(broker_frame, bg='#F0F0F0')
            status_frame.place(x=490, y=0, width=140, height=30)
            status_label = tk.Label(status_frame, text=status, bg='#F0F0F0', font=("Helvetica", 10))
            status_label.pack(side="left", padx=10)
            status_indicator = tk.Label(status_frame, bg=status_color, width=1, height=1)
            status_indicator.pack(side="left")

            keys_button = tk.Button(broker_frame, text="View Keys", command=lambda b_id=str(broker['_id']): self.show_keys(b_id), font=("Helvetica", 10), bg='#FDFDFD', fg='black')
            keys_button.place(x=635, y=0, width=100, height=30)

            actions_frame = tk.Frame(broker_frame, bg='#F0F0F0')
            actions_frame.place(x=800, y=0, width=140, height=30)

            re_login_button = tk.Button(actions_frame, text="Re-Login", command=lambda b_id=str(broker['_id']): self.update_keys(b_id), font=("Helvetica", 10), bg='#FDFDFD', fg='black')
            re_login_button.pack(side="left", padx=5)

            self.dot_photo = tk.PhotoImage(file="three_dots.png")
            dot_button = tk.Button(actions_frame, image=self.dot_photo, command=lambda b_id=str(broker['_id']): self.show_dot_menu(b_id), bg='#F0F0F0', borderwidth=0)
            dot_button.image = self.dot_photo  # Keep a reference
            dot_button.pack(side="left", padx=5)







# import tkinter as tk
# from tkinter import ttk, messagebox
# import pymongo
# import bson
# import base64

# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["trading"]
# brokers_collection = db["brokers"]

# class BrokersPage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg='#F0F0F0')

#         # Configure grid to expand
#         self.grid(row=0, column=0, sticky="nsew")
#         parent.grid_rowconfigure(0, weight=1)
#         parent.grid_columnconfigure(0, weight=1)

#         self.brokers = []
#         self.auth_codes = []

#         # Horizontal bar with labels
#         horizontal_bar1 = tk.Frame(self, bg='#EBEBEB')
#         horizontal_bar1.place(x=35, y=20, width=970, height=30)
        
#         # Create headings
#         headings = ["Broker", "Index", "Executions", "Status", "Keys", "Actions"]
#         heading_bg = "#EBEBEB"
#         heading_font = ("Helvetica", 12)
#         self.column_positions = [20, 160, 300, 440, 580, 720, 860]
#         for i, heading in enumerate(headings):
#             label = tk.Label(self, text=heading, bg=heading_bg, font=heading_font, padx=5, pady=5)
#             label.place(x=self.column_positions[i], y=20, width=140, height=30)

#         self.dot_photo = tk.PhotoImage(file="three_dots.png")

#         # Add Brokers heading
#         add_brokers_label = tk.Label(self, text="Add Brokers", bg='#F0F0F0', font=("Helvetica", 16))
#         add_brokers_label.place(x=1100, y=20, width=200, height=30)

#         # Create broker cards on the right
#         card_details = [
#             {"name": "Alice Blue", "image": "alice_blue.png"},
#             {"name": "Angel One", "image": "angel_one.png"},
#             {"name": "Dhan", "image": "dhan.png"},
#             {"name": "Fyers", "image": "fyers.png"},
#             {"name": "ICICI", "image": "icici.png"},
#             {"name": "IIFL", "image": "iifl.png"},
#             {"name": "Kotak Neo", "image": "kotak_neo.png"},
#             {"name": "Nuvama", "image": "nuvama.png"},
#             {"name": "Shoonya", "image": "shoonya.png"},
#             {"name": "Upstox", "image": "upstox.png"},
#             {"name": "Zerodha", "image": "zerodha.png"},
#             {"name": "Zerodha-enc", "image": "zerodha_enc.png"}
#         ]

#         card_positions = [
#             {"x": 1050, "y": 60, "width": 130, "height": 110},
#             {"x": 1200, "y": 60, "width": 130, "height": 110},
#             {"x": 1350, "y": 60, "width": 130, "height": 110},
#             {"x": 1050, "y": 180, "width": 130, "height": 110},
#             {"x": 1200, "y": 180, "width": 130, "height": 110},
#             {"x": 1350, "y": 180, "width": 130, "height": 110},
#             {"x": 1050, "y": 300, "width": 130, "height": 110},
#             {"x": 1200, "y": 300, "width": 130, "height": 110},
#             {"x": 1350, "y": 300, "width": 130, "height": 110},
#             {"x": 1050, "y": 420, "width": 130, "height": 110},
#             {"x": 1200, "y": 420, "width": 130, "height": 110},
#             {"x": 1350, "y": 420, "width": 130, "height": 110}
#         ]

#         for i, details in enumerate(card_details):
#             card_frame = tk.Frame(self, bg='#EBEBEB')
#             card_frame.place(x=card_positions[i]["x"], y=card_positions[i]["y"], width=card_positions[i]["width"], height=card_positions[i]["height"])
            
#             # Image in the card
#             card_image = tk.PhotoImage(file=f"assets/brokers_logo/{details['image']}")
#             image_label = tk.Label(card_frame, image=card_image, bg='#EBEBEB')
#             image_label.image = card_image  # Keep a reference
#             image_label.place(x=10, y=10, width=110, height=50)
            
#             # Text in the card
#             text_label = tk.Label(card_frame, text=details['name'], font=("Helvetica", 10), bg='#EBEBEB', fg='black')
#             text_label.place(x=10, y=60, width=110, height=20)
            
#             # Add button in the card
#             add_button = tk.Button(card_frame, text="Add", font=("Helvetica", 10), bg='#FDFDFD', fg='black', command=lambda n=details['name'], img=details['image']: self.add_broker(n, img))
#             add_button.place(x=25, y=80, width=80, height=20)

#         self.load_brokers()

#     def add_broker(self, name, image):
#         self.popup_auth_key(name, image)

#     def show_keys(self):
#         self.popup_keys()

#     def show_message(self):
#         print("Menu item selected")

#     def remove_broker(self, row_index):
#         confirmation = messagebox.askokcancel("Remove Broker", "Do you really want to remove the broker?")
#         if confirmation:
#             broker_to_remove = self.brokers[row_index]
#             brokers_collection.delete_one({"_id": broker_to_remove["_id"]})
#             del self.brokers[row_index]
#             self.render_brokers()

#     def popup_auth_key(self, name, image):
#         popup = tk.Toplevel(self)
#         popup.title("Authentication Key")
        
#         label = tk.Label(popup, text="Enter Auth Key")
#         label.pack(side="top", fill="x", pady=10)
        
#         entry = tk.Entry(popup)
#         entry.pack(pady=5)
        
#         def on_ok():
#             auth_key = entry.get()
#             if auth_key in self.auth_codes:
#                 messagebox.showerror("Error", "Broker already exists")
#             else:
#                 self.auth_codes.append(auth_key)
#                 self.add_broker_to_list(name, image, auth_key)
#             popup.destroy()

#         button_frame = tk.Frame(popup)
#         button_frame.pack(pady=5)

#         ok_button = tk.Button(button_frame, text="OK", command=on_ok)
#         ok_button.pack(side="left", padx=5)

#         cancel_button = tk.Button(button_frame, text="Cancel", command=popup.destroy)
#         cancel_button.pack(side="left", padx=5)

#     def add_broker_to_list(self, name, image, auth_key):
#         existing_broker = next((b for b in self.brokers if b["name"] == name), None)
#         if existing_broker:
#             existing_broker["index"] += 1
#             brokers_collection.update_one(
#                 {"_id": existing_broker["_id"]},
#                 {"$set": {"index": existing_broker["index"]}}
#             )
#         else:
#             broker_data = {
#                 "name": name,
#                 "image": image,
#                 "index": 1,
#                 "executions": "Pending",
#                 "status": "logged in",
#                 "status_color": "green",
#                 "keys": base64.b64encode(auth_key.encode()).decode(),
#                 "actions": "Re-Login"
#             }
#             result = brokers_collection.insert_one(broker_data)
#             broker_data["_id"] = result.inserted_id
#             self.brokers.append(broker_data)
#         self.render_brokers()

#     def render_brokers(self):
#         for widget in self.grid_slaves():  # Clear existing rows
#             if int(widget.grid_info()["row"]) > 1:
#                 widget.destroy()

#         for row_index, broker in enumerate(self.brokers):
#             y = 50 + row_index * 40
#             broker_photo = tk.PhotoImage(file=f"assets/brokers_logo/{broker['image']}")
#             for col_index, (key, cell_data) in enumerate(broker.items()):
#                 if key == "name":
#                     label = tk.Label(self, image=broker_photo, bg='#F0F0F0')
#                     label.image = broker_photo  # Keep a reference
#                     label.place(x=self.column_positions[col_index] - 20, y=y, width=140, height=40)
#                     label = tk.Label(self, text=cell_data, font=("Helvetica", 10), bg='#F0F0F0')
#                     label.place(x=self.column_positions[col_index], y=y, width=140, height=40)
#                 elif key == "index":
#                     label = tk.Label(self, text=cell_data, font=("Helvetica", 10), bg='#F0F0F0')
#                     label.place(x=self.column_positions[col_index], y=y, width=140, height=40)
#                 elif key == "executions":
#                     label = tk.Label(self, text=cell_data, font=("Helvetica", 10), bg='#F0F0F0')
#                     label.place(x=self.column_positions[col_index], y=y, width=140, height=40)
#                 elif key == "status":
#                     label = tk.Label(self, text=cell_data, font=("Helvetica", 10), bg=broker['status_color'])
#                     label.place(x=self.column_positions[col_index], y=y, width=140, height=40)
#                 elif key == "keys":
#                     label = tk.Label(self, text=cell_data, font=("Helvetica", 10), bg='#F0F0F0')
#                     label.place(x=self.column_positions[col_index], y=y, width=140, height=40)
#                 elif key == "actions":
#                     dot_button = tk.Button(self, image=self.dot_photo, command=self.show_message)
#                     dot_button.place(x=self.column_positions[col_index], y=y, width=40, height=40)
#                     remove_button = tk.Button(self, text="Remove", font=("Helvetica", 10), bg='#EBEBEB', command=lambda ri=row_index: self.remove_broker(ri))
#                     remove_button.place(x=self.column_positions[col_index] + 50, y=y, width=80, height=30)

#     def load_brokers(self):
#         self.brokers = list(brokers_collection.find())
#         self.render_brokers()








# import tkinter as tk
# from tkinter import ttk, messagebox

# class BrokersPage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg='#F0F0F0')

#         # Configure grid to expand
#         self.grid(row=0, column=0, sticky="nsew")
#         parent.grid_rowconfigure(0, weight=1)
#         parent.grid_columnconfigure(0, weight=1)

#         self.brokers = []
#         self.auth_codes = []

#         # Horizontal bar with labels
#         horizontal_bar1 = tk.Frame(self, bg='#EBEBEB')
#         horizontal_bar1.place(x=35, y=20, width=910, height=30)
        
#         # Create headings
#         headings = ["Broker", "Index", "Executions", "Status", "Keys", "Actions"]
#         heading_bg = "#EBEBEB"
#         heading_font = ("Helvetica", 12)
#         for i, heading in enumerate(headings):
#             label = tk.Label(self, text=heading, bg=heading_bg, font=heading_font, padx=5, pady=5)
#             label.place(x=10 + i*150, y=20, width=140, height=30)

#         self.dot_photo = tk.PhotoImage(file="three_dots.png")

#         # Add Brokers heading
#         add_brokers_label = tk.Label(self, text="Add Brokers", bg='#F0F0F0', font=("Helvetica", 16))
#         add_brokers_label.place(x=1100, y=20, width=200, height=30)

#         # Create broker cards on the right
#         card_photos = ["kotak_logo.png", "kotak_logo.png", "kotak_logo.png"]
#         card_names = ["Kotak Neo", "kotak Broker", "kotak Broker"]

#         for i in range(4):  # 4 rows
#             for j in range(3):  # 3 columns
#                 x = 950 + j * 150
#                 y = 50 + i * 110
#                 card_frame = tk.Frame(self, bg='#EBEBEB')
#                 card_frame.place(x=x, y=y, width=130, height=110)
                
#                 # Image in the card
#                 card_image = tk.PhotoImage(file=card_photos[(i * 3 + j) % len(card_photos)])
#                 image_label = tk.Label(card_frame, image=card_image, bg='#EBEBEB')
#                 image_label.image = card_image  # Keep a reference
#                 image_label.place(x=10, y=10, width=110, height=50)
                
#                 # Text in the card
#                 text_label = tk.Label(card_frame, text=card_names[(i * 3 + j) % len(card_names)], font=("Helvetica", 10), bg='#EBEBEB', fg='black')
#                 text_label.place(x=10, y=70, width=110, height=20)
                
#                 # Add button in the card
#                 add_button = tk.Button(card_frame, text="Add", font=("Helvetica", 10), bg='green', fg='white', command=lambda n=card_names[(i * 3 + j) % len(card_names)], img=card_photos[(i * 3 + j) % len(card_photos)]: self.add_broker(n, img))
#                 add_button.place(x=10, y=90, width=110, height=20)

#     def add_broker(self, name, image):
#         self.popup_auth_key(name, image)

#     def show_keys(self):
#         self.popup_keys()

#     def show_message(self):
#         print("Menu item selected")

#     def remove_broker(self, row_index):
#         confirmation = messagebox.askokcancel("Remove Broker", "Do you really want to remove the broker?")
#         if confirmation:
#             del self.brokers[row_index]
#             self.render_brokers()

#     def popup_auth_key(self, name, image):
#         popup = tk.Toplevel(self)
#         popup.title("Authentication Key")
        
#         label = tk.Label(popup, text="Enter Auth Key")
#         label.pack(side="top", fill="x", pady=10)
        
#         entry = tk.Entry(popup)
#         entry.pack(pady=5)
        
#         def on_ok():
#             auth_key = entry.get()
#             if auth_key in self.auth_codes:
#                 messagebox.showerror("Error", "Broker already exists")
#             else:
#                 self.auth_codes.append(auth_key)
#                 self.add_broker_to_list(name, image)
#             popup.destroy()

#         button_frame = tk.Frame(popup)
#         button_frame.pack(pady=5)

#         ok_button = tk.Button(button_frame, text="OK", command=on_ok)
#         ok_button.pack(side="left", padx=5)

#         cancel_button = tk.Button(button_frame, text="Cancel", command=popup.destroy)
#         cancel_button.pack(side="left", padx=5)

#     def add_broker_to_list(self, name, image):
#         # Check if the broker already exists
#         existing_broker = next((b for b in self.brokers if b["name"] == name), None)
#         if existing_broker:
#             existing_broker["index"] += 1
#         else:
#             self.brokers.append({
#                 "name": name,
#                 "image": image,
#                 "index": 1,
#                 "executions": "Pending",
#                 "status": "logged in",
#                 "status_color": "green",
#                 "keys": "View Keys",
#                 "actions": "Re-Login"
#             })
#         self.render_brokers()

#     def render_brokers(self):
#         for widget in self.grid_slaves():  # Clear existing rows
#             if int(widget.grid_info()["row"]) > 1:
#                 widget.destroy()

#         for row_index, broker in enumerate(self.brokers):
#             y = 50 + row_index * 40
#             broker_photo = tk.PhotoImage(file=broker["image"])
#             for col_index, (key, cell_data) in enumerate(broker.items()):
#                 if col_index == 0:
#                     label = tk.Label(self, image=broker_photo, bg='#F0F0F0')
#                     label.image = broker_photo  # Keep a reference
#                     label.place(x=10 + col_index * 150, y=y, width=140, height=30)
#                 elif key == "index":
#                     label = tk.Label(self, text=cell_data, font=("Helvetica", 10), bg='#F0F0F0')
#                     label.place(x=10 + col_index * 150, y=y, width=140, height=30)
#                 elif key == "executions":
#                     label = tk.Label(self, text=cell_data, font=("Helvetica", 10), bg='#F0F0F0')
#                     label.place(x=10 + col_index * 150, y=y, width=140, height=30)
#                 elif key == "status":
#                     label = tk.Label(self, text=cell_data, font=("Helvetica", 10), fg='black', bg='#F0F0F0')
#                     label.place(x=10 + col_index * 150, y=y, width=120, height=30)
#                     circle = tk.Canvas(self, width=8, height=8, bg='#F0F0F0', highlightthickness=0)
#                     circle.create_oval(0, 0, 8, 8, fill=broker["status_color"])
#                     circle.place(x=130 + col_index * 150, y=y+11)
#                 elif key == "keys":
#                     button = tk.Button(self, text=cell_data, font=("Helvetica", 10), command=self.show_keys)
#                     button.place(x=10 + col_index * 150, y=y, width=140, height=30)
#                 elif key == "actions":
#                     button = tk.Button(self, text=cell_data, font=("Helvetica", 10))
#                     button.place(x=10 + col_index * 150, y=y, width=140, height=30)
#             # Dot button with dropdown menu
#             dot_button = tk.Menubutton(self, image=self.dot_photo, bg='#F0F0F0')
#             dot_button.image = self.dot_photo  # Keep a reference
#             menu = tk.Menu(dot_button, tearoff=0)
#             menu.add_command(label="Delete Keys", command=self.show_message)
#             menu.add_command(label="Update Keys", command=self.show_message)
#             menu.add_command(label="Remove Broker", command=lambda r=row_index: self.remove_broker(r))
#             dot_button["menu"] = menu
#             dot_button.place(x=10 + 6 * 150, y=y, width=30, height=30)

#     def popup_keys(self):
#         popup = tk.Toplevel(self)
#         popup.title("Keys")

#         label = tk.Label(popup, text="Here are your keys.")
#         label.pack(side="top", fill="x", pady=10)
        
#         button_frame = tk.Frame(popup)
#         button_frame.pack(pady=5)

#         def update_keys():
#             print("Keys Updated")
        
#         ok_button = tk.Button(button_frame, text="OK", command=popup.destroy)
#         ok_button.pack(side="left", padx=5)
        
#         update_button = tk.Button(button_frame, text="Update Keys", command=update_keys)
#         update_button.pack(side="left", padx=5)











# import tkinter as tk
# from tkinter import ttk, messagebox
# from pymongo import MongoClient
# from bson.objectid import ObjectId

# class SignalsPage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg='#F0F0F0')

#         # MongoDB setup
#         self.client = MongoClient('mongodb://localhost:27017/')
#         self.db = self.client['trading']
#         self.collection = self.db['brokers']

#         # Configure grid to expand
#         self.grid(row=0, column=0, sticky="nsew")
#         parent.grid_rowconfigure(0, weight=1)
#         parent.grid_columnconfigure(0, weight=1)

#         self.brokers = []
#         self.auth_codes = []

#         # Horizontal bar with labels
#         horizontal_bar1 = tk.Frame(self, bg='#EBEBEB')
#         horizontal_bar1.place(x=35, y=20, width=970, height=30)
        
#         # Create headings
#         self.headings = ["Broker", "Index", "Executions", "Status", "Keys", "Actions"]
#         self.heading_positions = [20, 160, 300, 440, 580, 720, 860]
#         heading_bg = "#EBEBEB"
#         heading_font = ("Helvetica", 12)
#         for i, heading in enumerate(self.headings):
#             label = tk.Label(self, text=heading, bg=heading_bg, font=heading_font, padx=5, pady=5)
#             label.place(x=self.heading_positions[i], y=20, width=140, height=30)

#         self.dot_photo = tk.PhotoImage(file="three_dots.png")

#         # Add Brokers heading
#         add_brokers_label = tk.Label(self, text="Add Brokers", bg='#F0F0F0', font=("Helvetica", 16))
#         add_brokers_label.place(x=1100, y=20, width=200, height=30)

#         # Create broker cards on the right
#         card_details = [
#             {"name": "Alice Blue", "image": "alice_blue.png"},
#             {"name": "Angel One", "image": "angel_one.png"},
#             {"name": "Dhan", "image": "dhan.png"},
#             {"name": "Fyers", "image": "fyers.png"},
#             {"name": "ICICI", "image": "icici.png"},
#             {"name": "IIFL", "image": "iifl.png"},
#             {"name": "Kotak Neo", "image": "kotak_neo.png"},
#             {"name": "Nuvama", "image": "nuvama.png"},
#             {"name": "Shoonya", "image": "shoonya.png"},
#             {"name": "Upstox", "image": "upstox.png"},
#             {"name": "Zerodha", "image": "zerodha.png"},
#             {"name": "Zerodha-enc", "image": "zerodha_enc.png"}
#         ]

#         card_positions = [
#             {"x": 1050, "y": 60, "width": 130, "height": 110},
#             {"x": 1200, "y": 60, "width": 130, "height": 110},
#             {"x": 1350, "y": 60, "width": 130, "height": 110},
#             {"x": 1050, "y": 180, "width": 130, "height": 110},
#             {"x": 1200, "y": 180, "width": 130, "height": 110},
#             {"x": 1350, "y": 180, "width": 130, "height": 110},
#             {"x": 1050, "y": 300, "width": 130, "height": 110},
#             {"x": 1200, "y": 300, "width": 130, "height": 110},
#             {"x": 1350, "y": 300, "width": 130, "height": 110},
#             {"x": 1050, "y": 420, "width": 130, "height": 110},
#             {"x": 1200, "y": 420, "width": 130, "height": 110},
#             {"x": 1350, "y": 420, "width": 130, "height": 110}
#         ]

#         for i, details in enumerate(card_details):
#             card_frame = tk.Frame(self, bg='#EBEBEB')
#             card_frame.place(x=card_positions[i]["x"], y=card_positions[i]["y"], width=card_positions[i]["width"], height=card_positions[i]["height"])
            
#             # Image in the card
#             card_image = tk.PhotoImage(file=f"assets/brokers_logo/{details['image']}")
#             image_label = tk.Label(card_frame, image=card_image, bg='#EBEBEB')
#             image_label.image = card_image  # Keep a reference
#             image_label.place(x=10, y=10, width=110, height=50)
            
#             # Text in the card
#             text_label = tk.Label(card_frame, text=details['name'], font=("Helvetica", 10), bg='#EBEBEB', fg='black')
#             text_label.place(x=10, y=60, width=110, height=20)
            
#             # Add button in the card
#             add_button = tk.Button(card_frame, text="Add", font=("Helvetica", 10), bg='#FDFDFD', fg='black', command=lambda n=details['name'], img=details['image']: self.add_broker(n, img))
#             add_button.place(x=25, y=80, width=80, height=20)

#         # Load brokers from MongoDB
#         self.load_brokers_from_db()

#     def add_broker(self, name, image):
#         self.popup_auth_key(name, image)

#     def show_keys(self, broker_id):
#         self.popup_keys(broker_id)

#     def show_message(self):
#         print("Menu item selected")

#     def remove_broker(self, row_index):
#         confirmation = messagebox.askokcancel("Remove Broker", "Do you really want to remove the broker?")
#         if confirmation:
#             broker_id = self.brokers[row_index]["_id"]
#             self.collection.delete_one({"_id": ObjectId(broker_id)})
#             del self.brokers[row_index]
#             self.render_brokers()

#     def popup_auth_key(self, name, image):
#         popup = tk.Toplevel(self)
#         popup.title("Authentication Key")
        
#         label = tk.Label(popup, text="Enter Auth Key")
#         label.pack(side="top", fill="x", pady=10)
        
#         entry = tk.Entry(popup)
#         entry.pack(pady=5)
        
#         def on_ok():
#             auth_key = entry.get()
#             if auth_key in self.auth_codes:
#                 messagebox.showerror("Error", "Broker already exists")
#             else:
#                 self.auth_codes.append(auth_key)
#                 self.add_broker_to_list(name, image, auth_key)
#             popup.destroy()

#         button_frame = tk.Frame(popup)
#         button_frame.pack(pady=5)

#         ok_button = tk.Button(button_frame, text="OK", command=on_ok)
#         ok_button.pack(side="left", padx=5)

#         cancel_button = tk.Button(button_frame, text="Cancel", command=popup.destroy)
#         cancel_button.pack(side="left", padx=5)

#     def add_broker_to_list(self, name, image, auth_key):
#         # Check if the broker already exists
#         existing_broker = next((b for b in self.brokers if b["name"] == name), None)
#         if existing_broker:
#             existing_broker["index"] += 1
#         else:
#             broker_data = {
#                 "name": name,
#                 "image": image,
#                 "index": 1,
#                 "executions": "Pending",
#                 "status": "logged in",
#                 "status_color": "green",
#                 "keys": auth_key  # Storing auth_key in MongoDB
#             }
#             result = self.collection.insert_one(broker_data)
#             broker_data["_id"] = result.inserted_id
#             self.brokers.append(broker_data)
#         self.render_brokers()

#     def render_brokers(self):
#         for widget in self.grid_slaves():  # Clear existing rows
#             if int(widget.grid_info()["row"]) > 1:
#                 widget.grid_forget()

#         for row_index, broker in enumerate(self.brokers):
#             row_y_position = 60 + (row_index * 40)
#             broker_name = tk.Label(self, text=broker["name"], font=("Helvetica", 12), bg='#F0F0F0', fg='black')
#             broker_name.place(x=20, y=row_y_position, width=140, height=30)

#             index_label = tk.Label(self, text=str(broker["index"]), font=("Helvetica", 12), bg='#F0F0F0', fg='black')
#             index_label.place(x=160, y=row_y_position, width=140, height=30)

#             executions_label = tk.Label(self, text=broker["executions"], font=("Helvetica", 12), bg='#F0F0F0', fg='black')
#             executions_label.place(x=300, y=row_y_position, width=140, height=30)

#             status_label = tk.Label(self, text=broker["status"], font=("Helvetica", 12), bg='#F0F0F0', fg=broker["status_color"])
#             status_label.place(x=440, y=row_y_position, width=140, height=30)

#             keys_button = tk.Button(self, text="View Keys", font=("Helvetica", 12), bg='#F0F0F0', fg='black', command=lambda row_index=row_index: self.show_keys(row_index))
#             keys_button.place(x=580, y=row_y_position, width=140, height=30)

#             menu_button = tk.Button(self, image=self.dot_photo, bg='#F0F0F0', command=self.show_message)
#             menu_button.place(x=720, y=row_y_position, width=140, height=30)

#             remove_button = tk.Button(self, text="Remove", font=("Helvetica", 12), bg='#F0F0F0', fg='black', command=lambda row_index=row_index: self.remove_broker(row_index))
#             remove_button.place(x=860, y=row_y_position, width=140, height=30)

#     def popup_keys(self, broker_index):
#         broker = self.brokers[broker_index]
#         popup = tk.Toplevel(self)
#         popup.title(f"{broker['name']} - Authentication Key")
        
#         label = tk.Label(popup, text=f"Auth Key for {broker['name']}")
#         label.pack(side="top", fill="x", pady=10)
        
#         entry = tk.Entry(popup)
#         entry.pack(pady=5)
#         entry.insert(0, broker["keys"])
        
#         def update_key():
#             new_key = entry.get()
#             broker["keys"] = new_key
#             self.collection.update_one({"_id": broker["_id"]}, {"$set": {"keys": new_key}})
#             popup.destroy()
        
#         button_frame = tk.Frame(popup)
#         button_frame.pack(pady=5)

#         update_button = tk.Button(button_frame, text="Update", command=update_key)
#         update_button.pack(side="left", padx=5)

#         close_button = tk.Button(button_frame, text="Close", command=popup.destroy)
#         close_button.pack(side="left", padx=5)

#     def load_brokers_from_db(self):
#         brokers_cursor = self.collection.find()
#         self.brokers = list(brokers_cursor)
#         self.render_brokers()






# import tkinter as tk
# from tkinter import ttk, messagebox

# class SignalsPage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg='#F0F0F0')

#         # Configure grid to expand
#         self.grid(row=0, column=0, sticky="nsew")
#         parent.grid_rowconfigure(0, weight=1)
#         parent.grid_columnconfigure(0, weight=1)

#         self.brokers = []
#         self.auth_codes = []

#         # Horizontal bar with labels
#         horizontal_bar1 = tk.Frame(self, bg='#EBEBEB')
#         horizontal_bar1.place(x=35, y=20, width=970, height=30)
        
#         # Create headings
#         headings = ["Broker", "Index", "Executions", "Status", "Keys", "Actions"]
#         heading_bg = "#EBEBEB"
#         heading_font = ("Helvetica", 12)
#         for i, heading in enumerate(headings):
#             label = tk.Label(self, text=heading, bg=heading_bg, font=heading_font, padx=5, pady=5)
#             label.place(x=20 + i*160, y=20, width=140, height=30)

#         self.dot_photo = tk.PhotoImage(file="three_dots.png")

#         # Add Brokers heading
#         add_brokers_label = tk.Label(self, text="Add Brokers", bg='#F0F0F0', font=("Helvetica", 16))
#         add_brokers_label.place(x=1100, y=20, width=200, height=30)

#         # Create broker cards on the right
#         card_details = [
#             {"name": "Alice Blue", "image": "alice_blue.png"},
#             {"name": "Angel One", "image": "angel_one.png"},
#             {"name": "Dhan", "image": "dhan.png"},
#             {"name": "Fyers", "image": "fyers.png"},
#             {"name": "ICICI", "image": "icici.png"},
#             {"name": "IIFL", "image": "iifl.png"},
#             {"name": "Kotak Neo", "image": "kotak_neo.png"},
#             {"name": "Nuvama", "image": "nuvama.png"},
#             {"name": "Shoonya", "image": "shoonya.png"},
#             {"name": "Upstox", "image": "upstox.png"},
#             {"name": "Zerodha", "image": "zerodha.png"},
#             {"name": "Zerodha-enc", "image": "zerodha_enc.png"}
#         ]

#         card_positions = [
#             {"x": 1050, "y": 60, "width": 130, "height": 110},
#             {"x": 1200, "y": 60, "width": 130, "height": 110},
#             {"x": 1350, "y": 60, "width": 130, "height": 110},
#             {"x": 1050, "y": 180, "width": 130, "height": 110},
#             {"x": 1200, "y": 180, "width": 130, "height": 110},
#             {"x": 1350, "y": 180, "width": 130, "height": 110},
#             {"x": 1050, "y": 300, "width": 130, "height": 110},
#             {"x": 1200, "y": 300, "width": 130, "height": 110},
#             {"x": 1350, "y": 300, "width": 130, "height": 110},
#             {"x": 1050, "y": 420, "width": 130, "height": 110},
#             {"x": 1200, "y": 420, "width": 130, "height": 110},
#             {"x": 1350, "y": 420, "width": 130, "height": 110}
#         ]

#         for i, details in enumerate(card_details):
#             card_frame = tk.Frame(self, bg='#EBEBEB')
#             card_frame.place(x=card_positions[i]["x"], y=card_positions[i]["y"], width=card_positions[i]["width"], height=card_positions[i]["height"])
            
#             # Image in the card
#             card_image = tk.PhotoImage(file=f"assets/brokers_logo/{details['image']}")
#             image_label = tk.Label(card_frame, image=card_image, bg='#EBEBEB')
#             image_label.image = card_image  # Keep a reference
#             image_label.place(x=10, y=10, width=110, height=50)
            
#             # Text in the card
#             text_label = tk.Label(card_frame, text=details['name'], font=("Helvetica", 10), bg='#EBEBEB', fg='black')
#             text_label.place(x=10, y=60, width=110, height=20)
            
#             # Add button in the card
#             add_button = tk.Button(card_frame, text="Add", font=("Helvetica", 10), bg='#FDFDFD', fg='black', command=lambda n=details['name'], img=details['image']: self.add_broker(n, img))
#             add_button.place(x=25, y=80, width=80, height=20)

#     def add_broker(self, name, image):
#         self.popup_auth_key(name, image)

#     def show_keys(self):
#         self.popup_keys()

#     def show_message(self):
#         print("Menu item selected")

#     def remove_broker(self, row_index):
#         confirmation = messagebox.askokcancel("Remove Broker", "Do you really want to remove the broker?")
#         if confirmation:
#             del self.brokers[row_index]
#             self.render_brokers()

#     def popup_auth_key(self, name, image):
#         popup = tk.Toplevel(self)
#         popup.title("Authentication Key")
        
#         label = tk.Label(popup, text="Enter Auth Key")
#         label.pack(side="top", fill="x", pady=10)
        
#         entry = tk.Entry(popup)
#         entry.pack(pady=5)
        
#         def on_ok():
#             auth_key = entry.get()
#             if auth_key in self.auth_codes:
#                 messagebox.showerror("Error", "Broker already exists")
#             else:
#                 self.auth_codes.append(auth_key)
#                 self.add_broker_to_list(name, image)
#             popup.destroy()

#         button_frame = tk.Frame(popup)
#         button_frame.pack(pady=5)

#         ok_button = tk.Button(button_frame, text="OK", command=on_ok)
#         ok_button.pack(side="left", padx=5)

#         cancel_button = tk.Button(button_frame, text="Cancel", command=popup.destroy)
#         cancel_button.pack(side="left", padx=5)

#     def add_broker_to_list(self, name, image):
#         # Check if the broker already exists
#         existing_broker = next((b for b in self.brokers if b["name"] == name), None)
#         if existing_broker:
#             existing_broker["index"] += 1
#         else:
#             self.brokers.append({
#                 "name": name,
#                 "image": image,
#                 "index": 1,
#                 "executions": "Pending",
#                 "status": "logged in",
#                 "status_color": "green",
#                 "keys": "View Keys",
#                 "actions": "Re-Login"
#             })
#         self.render_brokers()

#     def render_brokers(self):
#         for widget in self.grid_slaves():  # Clear existing rows
#             if int(widget.grid_info()["row"]) > 1:
#                 widget.destroy()

#         for row_index, broker in enumerate(self.brokers):
#             y = 50 + row_index * 40
#             broker_photo = tk.PhotoImage(file=f"assets/brokers_logo/{broker['image']}")
#             for col_index, (key, cell_data) in enumerate(broker.items()):
#                 if col_index == 0:
#                     label = tk.Label(self, image=broker_photo, bg='#F0F0F0')
#                     label.image = broker_photo  # Keep a reference
#                     label.place(x=10 + col_index * 150, y=y, width=140, height=30)
#                     label = tk.Label(self, text=cell_data, font=("Helvetica", 10), bg='#F0F0F0')
#                     label.place(x=20 + col_index * 150, y=y, width=140, height=30)
#                 elif key == "index":
#                     label = tk.Label(self, text=cell_data, font=("Helvetica", 10), bg='#F0F0F0')
#                     label.place(x=10 + col_index * 150, y=y, width=140, height=30)
#                 elif key == "executions":
#                     label = tk.Label(self, text=cell_data, font=("Helvetica", 10), bg='#F0F0F0')
#                     label.place(x=10 + col_index * 150, y=y, width=140, height=30)
#                 elif key == "status":
#                     label = tk.Label(self, text=cell_data, font=("Helvetica", 10), fg='black', bg='#F0F0F0')
#                     label.place(x=10 + col_index * 150, y=y, width=120, height=30)
#                     circle = tk.Canvas(self, width=8, height=8, bg='#F0F0F0', highlightthickness=0)
#                     circle.create_oval(0, 0, 8, 8, fill=broker["status_color"])
#                     circle.place(x=130 + col_index * 150, y=y+11)
#                 elif key == "keys":
#                     button = tk.Button(self, text=cell_data, font=("Helvetica", 10), command=self.show_keys)
#                     button.place(x=10 + col_index * 150, y=y, width=140, height=30)
#                 elif key == "actions":
#                     button = tk.Button(self, text=cell_data, font=("Helvetica", 10))
#                     button.place(x=10 + col_index * 150, y=y, width=140, height=30)
#             # Dot button with dropdown menu
#             dot_button = tk.Menubutton(self, image=self.dot_photo, bg='#F0F0F0')
#             dot_button.image = self.dot_photo  # Keep a reference
#             menu = tk.Menu(dot_button, tearoff=0)
#             menu.add_command(label="Delete Keys", command=self.show_message)
#             menu.add_command(label="Update Keys", command=self.show_message)
#             menu.add_command(label="Remove Broker", command=lambda r=row_index: self.remove_broker(r))
#             dot_button["menu"] = menu
#             dot_button.place(x=10 + 6 * 150, y=y, width=30, height=30)

#     def popup_keys(self):
#         popup = tk.Toplevel(self)
#         popup.title("Keys")

#         label = tk.Label(popup, text="Here are your keys.")
#         label.pack(side="top", fill="x", pady=10)
        
#         button_frame = tk.Frame(popup)
#         button_frame.pack(pady=5)

#         def update_keys():
#             print("Keys Updated")
        
#         ok_button = tk.Button(button_frame, text="OK", command=popup.destroy)
#         ok_button.pack(side="left", padx=5)
        
#         update_button = tk.Button(button_frame, text="Update Keys", command=update_keys)
#         update_button.pack(side="left", padx=5)
