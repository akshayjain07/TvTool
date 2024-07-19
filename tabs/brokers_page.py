import tkinter as tk
from tkinter import ttk, messagebox

class BrokersPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#F0F0F0')

        # Configure grid to expand
        self.grid(row=0, column=0, sticky="nsew")
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.brokers = []
        self.auth_codes = []

        # Horizontal bar with labels
        horizontal_bar1 = tk.Frame(self, bg='#EBEBEB')
        horizontal_bar1.place(x=35, y=20, width=910, height=30)
        
        # Create headings
        headings = ["Broker", "Index", "Executions", "Status", "Keys", "Actions"]
        heading_bg = "#EBEBEB"
        heading_font = ("Helvetica", 12)
        for i, heading in enumerate(headings):
            label = tk.Label(self, text=heading, bg=heading_bg, font=heading_font, padx=5, pady=5)
            label.place(x=10 + i*150, y=20, width=140, height=30)

        self.dot_photo = tk.PhotoImage(file="three_dots.png")

        # Add Brokers heading
        add_brokers_label = tk.Label(self, text="Add Brokers", bg='#F0F0F0', font=("Helvetica", 16))
        add_brokers_label.place(x=1100, y=20, width=200, height=30)

        # Create broker cards on the right
        card_photos = ["kotak_logo.png", "kotak_logo.png", "kotak_logo.png"]
        card_names = ["Kotak Neo", "kotak Broker", "kotak Broker"]

        for i in range(4):  # 4 rows
            for j in range(3):  # 3 columns
                x = 950 + j * 150
                y = 50 + i * 110
                card_frame = tk.Frame(self, bg='#EBEBEB')
                card_frame.place(x=x, y=y, width=130, height=110)
                
                # Image in the card
                card_image = tk.PhotoImage(file=card_photos[(i * 3 + j) % len(card_photos)])
                image_label = tk.Label(card_frame, image=card_image, bg='#EBEBEB')
                image_label.image = card_image  # Keep a reference
                image_label.place(x=10, y=10, width=110, height=50)
                
                # Text in the card
                text_label = tk.Label(card_frame, text=card_names[(i * 3 + j) % len(card_names)], font=("Helvetica", 10), bg='#EBEBEB', fg='black')
                text_label.place(x=10, y=70, width=110, height=20)
                
                # Add button in the card
                add_button = tk.Button(card_frame, text="Add", font=("Helvetica", 10), bg='green', fg='white', command=lambda n=card_names[(i * 3 + j) % len(card_names)], img=card_photos[(i * 3 + j) % len(card_photos)]: self.add_broker(n, img))
                add_button.place(x=10, y=90, width=110, height=20)

    def add_broker(self, name, image):
        self.popup_auth_key(name, image)

    def show_keys(self):
        self.popup_keys()

    def show_message(self):
        print("Menu item selected")

    def remove_broker(self, row_index):
        confirmation = messagebox.askokcancel("Remove Broker", "Do you really want to remove the broker?")
        if confirmation:
            del self.brokers[row_index]
            self.render_brokers()

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
                self.add_broker_to_list(name, image)
            popup.destroy()

        button_frame = tk.Frame(popup)
        button_frame.pack(pady=5)

        ok_button = tk.Button(button_frame, text="OK", command=on_ok)
        ok_button.pack(side="left", padx=5)

        cancel_button = tk.Button(button_frame, text="Cancel", command=popup.destroy)
        cancel_button.pack(side="left", padx=5)

    def add_broker_to_list(self, name, image):
        # Check if the broker already exists
        existing_broker = next((b for b in self.brokers if b["name"] == name), None)
        if existing_broker:
            existing_broker["index"] += 1
        else:
            self.brokers.append({
                "name": name,
                "image": image,
                "index": 1,
                "executions": "Pending",
                "status": "logged in",
                "status_color": "green",
                "keys": "View Keys",
                "actions": "Re-Login"
            })
        self.render_brokers()

    def render_brokers(self):
        for widget in self.grid_slaves():  # Clear existing rows
            if int(widget.grid_info()["row"]) > 1:
                widget.destroy()

        for row_index, broker in enumerate(self.brokers):
            y = 50 + row_index * 40
            broker_photo = tk.PhotoImage(file=broker["image"])
            for col_index, (key, cell_data) in enumerate(broker.items()):
                if col_index == 0:
                    label = tk.Label(self, image=broker_photo, bg='#F0F0F0')
                    label.image = broker_photo  # Keep a reference
                    label.place(x=10 + col_index * 150, y=y, width=140, height=30)
                elif key == "index":
                    label = tk.Label(self, text=cell_data, font=("Helvetica", 10), bg='#F0F0F0')
                    label.place(x=10 + col_index * 150, y=y, width=140, height=30)
                elif key == "executions":
                    label = tk.Label(self, text=cell_data, font=("Helvetica", 10), bg='#F0F0F0')
                    label.place(x=10 + col_index * 150, y=y, width=140, height=30)
                elif key == "status":
                    label = tk.Label(self, text=cell_data, font=("Helvetica", 10), fg='black', bg='#F0F0F0')
                    label.place(x=10 + col_index * 150, y=y, width=120, height=30)
                    circle = tk.Canvas(self, width=8, height=8, bg='#F0F0F0', highlightthickness=0)
                    circle.create_oval(0, 0, 8, 8, fill=broker["status_color"])
                    circle.place(x=130 + col_index * 150, y=y+11)
                elif key == "keys":
                    button = tk.Button(self, text=cell_data, font=("Helvetica", 10), command=self.show_keys)
                    button.place(x=10 + col_index * 150, y=y, width=140, height=30)
                elif key == "actions":
                    button = tk.Button(self, text=cell_data, font=("Helvetica", 10))
                    button.place(x=10 + col_index * 150, y=y, width=140, height=30)
            # Dot button with dropdown menu
            dot_button = tk.Menubutton(self, image=self.dot_photo, bg='#F0F0F0')
            dot_button.image = self.dot_photo  # Keep a reference
            menu = tk.Menu(dot_button, tearoff=0)
            menu.add_command(label="Delete Keys", command=self.show_message)
            menu.add_command(label="Update Keys", command=self.show_message)
            menu.add_command(label="Remove Broker", command=lambda r=row_index: self.remove_broker(r))
            dot_button["menu"] = menu
            dot_button.place(x=10 + 6 * 150, y=y, width=30, height=30)

    def popup_keys(self):
        popup = tk.Toplevel(self)
        popup.title("Keys")

        label = tk.Label(popup, text="Here are your keys.")
        label.pack(side="top", fill="x", pady=10)
        
        button_frame = tk.Frame(popup)
        button_frame.pack(pady=5)

        def update_keys():
            print("Keys Updated")
        
        ok_button = tk.Button(button_frame, text="OK", command=popup.destroy)
        ok_button.pack(side="left", padx=5)
        
        update_button = tk.Button(button_frame, text="Update Keys", command=update_keys)
        update_button.pack(side="left", padx=5)
