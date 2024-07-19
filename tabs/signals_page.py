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








    # def display_data(self):
    #     # Connect to MongoDB and fetch data
    #     client = pymongo.MongoClient("mongodb://localhost:27017/")
    #     db = client["trading"]
    #     collection = db["signals"]
    #     data = collection.find()

    #     y = 45  # Start position for data rows

    #     for signal in data:
    #         self.create_data_row(signal, y)
    #         y += 30  # Move to the next row position

    # def create_data_row(self, data, y):
    #     fields = ['date_time', 'symbol', 'signal_type', 'price', 'strategy', 'stop_loss', 'take_profit', 'duration']
    #     x_coords = [20, 220, 550, 710, 870, 1050, 1180, 1360]

    #     font_settings = ("Arial", 10)

    #     for i, field in enumerate(fields):
    #         value = data.get(field, "")
    #         if field == "signal_type":
    #             if value == "BUY":
    #                 color = "green"
    #             elif value == "SELL":
    #                 color = "red"
    #             else:
    #                 color = "black"
    #             tk.Label(self.scrollable_frame, text=value, bg='#F0F0F0', font=font_settings, fg=color).place(x=x_coords[i], y=y)
    #         else:
    #             tk.Label(self.scrollable_frame, text=value, bg='#F0F0F0', font=font_settings).place(x=x_coords[i], y=y)

    #     # Horizontal line separator
    #     tk.Frame(self.scrollable_frame, bg='#000000', height=1).place(x=0, y=y+25, relwidth=1)






# import tkinter as tk
# from tkinter import ttk
# import pymongo

# class SignalsPage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg='#F0F0F0')
#         self.grid(row=0, column=0, sticky="nsew")
#         parent.grid_rowconfigure(0, weight=1)
#         parent.grid_columnconfigure(0, weight=1)

#         self.create_ui()


#     def create_ui(self):
#         # Horizontal bar
#         bar = tk.Frame(self, bg='#EBEBEB', height=30)
#         bar.pack(fill='x', pady=(10, 0))

#         # Column headings
#         headings = ['TimeStamp', 'Instruments', 'Type', 'Price', 'Strategy', 'Stop Loss', 'Take Profit', 'Duration']
#         x_coords = [20, 285, 550, 710, 880, 1050, 1180, 1360]

#         font_settings = ("Arial", 10, "bold")

#         for i, heading in enumerate(headings):
#             tk.Label(bar, text=heading, bg='#EBEBEB', font=font_settings).place(x=x_coords[i], y=5)

#         # Fetch and display data from MongoDB
#         self.display_data()

#     def display_data(self):
#         # Connect to MongoDB and fetch data
#         client = pymongo.MongoClient("mongodb://localhost:27017/")
#         db = client["trading"]
#         collection = db["signals"]
#         data = collection.find()

#         y = 45  # Start position for data rows

#         for signal in data:
#             self.create_data_row(signal, y)
#             y += 30  # Move to the next row position
            

#     def create_data_row(self, data, y):
#         fields = ['date_time', 'symbol', 'signal_type', 'price', 'strategy', 'stop_loss', 'take_profit', 'duration']
#         x_coords = [20, 220, 550, 710, 870, 1050, 1180, 1360]

#         font_settings = ("Arial", 10)

#         for i, field in enumerate(fields):
#             value = data.get(field, "")
#             if field == "signal_type":
#                 if value == "BUY":
#                     color = "green"
#                 elif value == "SELL":
#                     color = "red"
#                 else:
#                     color = "black"
#                 tk.Label(self, text=value, bg='#F0F0F0', font=font_settings, fg=color).place(x=x_coords[i], y=y)
#             else:
#                 tk.Label(self, text=value, bg='#F0F0F0', font=font_settings).place(x=x_coords[i], y=y)

#         # Horizontal line separator
#         tk.Frame(self, bg='#000000', height=1).place(x=0, y=y+25, relwidth=1)






# import tkinter as tk
# from tkinter import ttk
# import pymongo

# class SignalsPage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg='#F0F0F0')
#         self.grid(row=0, column=0, sticky="nsew")
#         parent.grid_rowconfigure(0, weight=1)
#         parent.grid_columnconfigure(0, weight=1)

#         self.create_ui()

#     def create_ui(self):
#         # Horizontal bar
#         bar = tk.Frame(self, bg='#EBEBEB', height=30)
#         bar.pack(fill='x', pady=(10, 0))

#         # Column headings
#         headings = ['TimeStamp', 'Instruments', 'Type', 'Price', 'Strategy', 'Stop Loss', 'Take Profit', 'Duration']
#         x_coords = [20, 285, 550, 710, 880, 1050, 1180, 1360]

#         font_settings = ("Arial", 10, "bold")

#         for i, heading in enumerate(headings):
#             tk.Label(bar, text=heading, bg='#EBEBEB', font=font_settings).place(x=x_coords[i], y=3)

#         # Frame for the table
#         table_frame = tk.Frame(self, bg='#F0F0F0')
#         table_frame.pack(fill='both', expand=True)

#         # Canvas and scrollbar for the table
#         canvas = tk.Canvas(table_frame, bg='#F0F0F0')
#         scrollbar = tk.Scrollbar(table_frame, orient="vertical", command=canvas.yview)
#         scrollable_frame = tk.Frame(canvas, bg='#F0F0F0')

#         scrollable_frame.bind(
#             "<Configure>",
#             lambda e: canvas.configure(
#                 scrollregion=canvas.bbox("all")
#             )
#         )

#         canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
#         canvas.configure(yscrollcommand=scrollbar.set)

#         scrollbar.pack(side="right", fill="y")
#         canvas.pack(side="left", fill="both", expand=True)

#         # Fetch and display data from MongoDB
#         self.display_data(scrollable_frame)

#     def display_data(self, parent):
#         # Connect to MongoDB and fetch data
#         client = pymongo.MongoClient("mongodb://localhost:27017/")
#         db = client["trading"]
#         collection = db["signals"]
#         data = collection.find()

#         print("mongodb")

#         y = 10  # Start position for data rows

#         for signal in data:
#             self.create_data_row(parent, signal, y)
#             y += 30  # Move to the next row position

#     def create_data_row(self, parent, data, y):
#         fields = ['date_time', 'symbol', 'signal_type', 'price', 'strategy', 'stop_loss', 'take_profit', 'duration']
#         x_coords = [20, 220, 550, 710, 870, 1050, 1180, 1360]

#         font_settings = ("Arial", 10)

#         for i, field in enumerate(fields):
#             value = data.get(field, "")
#             if field == "signal_type":
#                 if value == "BUY":
#                     color = "green"
#                 elif value == "SELL":
#                     color = "red"
#                 else:
#                     color = "black"
#                 tk.Label(parent, text=value, bg='#F0F0F0', font=font_settings, fg=color).place(x=x_coords[i], y=y)
#             else:
#                 tk.Label(parent, text=value, bg='#F0F0F0', font=font_settings).place(x=x_coords[i], y=y)

#         # Horizontal line separator
#         tk.Frame(parent, bg='#000000', height=1).place(x=0, y=y+25, relwidth=1)

















# import tkinter as tk
# from tkinter import ttk
# import pymongo

# class SignalsPage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg='#F0F0F0')
#         self.grid(row=0, column=0, sticky="nsew")
#         parent.grid_rowconfigure(0, weight=1)
#         parent.grid_columnconfigure(0, weight=1)

#         self.create_ui()

#     def create_ui(self):
#         # Horizontal bar
#         bar = tk.Frame(self, bg='#EBEBEB', height=30)
#         bar.pack(fill='x', pady=(10, 0))

#         # Column headings
#         headings = ['TimeStamp', 'Instruments', 'Type', 'Price', 'Strategy', 'Stop Loss', 'Take Profit', 'Duration']
#         x_coords = [20, 285, 550, 710, 880, 1050, 1180, 1360]

#         font_settings = ("Arial", 10, "bold")

#         for i, heading in enumerate(headings):
#             tk.Label(bar, text=heading, bg='#EBEBEB', font=font_settings).place(x=x_coords[i], y=5)

#         # Fetch and display data from MongoDB
#         self.display_data()

#     def display_data(self):
#         # Connect to MongoDB and fetch data
#         client = pymongo.MongoClient("mongodb://localhost:27017/")
#         db = client["trading"]
#         collection = db["signals"]
#         data = collection.find()

#         y = 45  # Start position for data rows

#         for signal in data:
#             self.create_data_row(signal, y)
#             y += 30  # Move to the next row position

#     def create_data_row(self, data, y):
#         fields = ['date_time', 'symbol', 'signal_type', 'price', 'strategy', 'stop_loss', 'take_profit', 'duration']
#         x_coords = [20, 220, 550, 710, 870, 1050, 1180, 1360]

#         font_settings = ("Arial", 10)

#         for i, field in enumerate(fields):
#             value = data.get(field, "")
#             if field == "signal_type":
#                 if value == "BUY":
#                     color = "green"
#                 elif value == "SELL":
#                     color = "red"
#                 else:
#                     color = "black"
#                 tk.Label(self, text=value, bg='#F0F0F0', font=font_settings, fg=color).place(x=x_coords[i], y=y)
#             else:
#                 tk.Label(self, text=value, bg='#F0F0F0', font=font_settings).place(x=x_coords[i], y=y)

#         # Horizontal line separator
#         tk.Frame(self, bg='#000000', height=1).place(x=0, y=y+25, relwidth=1)













# import tkinter as tk
# from tkinter import ttk

# class SignalsPage(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, bg='#F0F0F0')

#         # Configure grid to expand
#         self.grid(row=0, column=0, sticky="nsew")
#         parent.grid_rowconfigure(0, weight=1)
#         parent.grid_columnconfigure(0, weight=1)
        
#         # Add top label
#         label = ttk.Label(self, text="Drag a column to group", background='#F0F0F0', foreground='#000000', font=("Helvetica", 12))
#         label.pack(padx=10, pady=10)

#         # Create a green horizontal bar
#         green_bar = tk.Frame(self, bg='#EBEBEB')
#         green_bar.place(relx=0, rely=0.1, relwidth=1, height=30)  # Adjust relx, rely, relwidth, height as needed

#         # List of buttons with their text, x, and width
#         buttons_info = [
#             ("Source Symbol   ", 10, 130),
#             ("Request ID   ", 150, 110),
#             ("Exchange   ", 270, 100),
#             ("Exchange Symbol   ", 380, 140),
#             ("LTP   ", 530, 60),
#             ("P&L   ", 600, 60),
#             ("Product   ", 670, 90),
#             ("Entry Order Type   ", 770, 140),
#             ("Entry Order ID   ", 920, 120),
#             ("Entry Order Time   ", 1050, 140),
#             ("Source Symbol   ", 1200, 130),
#             ("Request ID   ", 1340, 110),
#             ("Exchange   ", 1460, 100)
#         ]

#         # Load the image
#         image_file = "filter_logo.png"
#         image = tk.PhotoImage(file=image_file)  # Ensure this file exists

#         self.buttons = []

#         # Set y position for all buttons
#         y = 0

#         for text, x, width in buttons_info:
#             # Create button with image and text
#             button = tk.Button(green_bar, text=text, image=image, compound='right', bg="#EBEBEB", fg='#000000',
#                                font=("Helvetica", 10), bd=0, relief=tk.FLAT, cursor='hand2')
#             button.place(x=x, y=y, height=30, width=width)
#             button.image = image  # Keep a reference to avoid garbage collection
#             self.buttons.append(button)
