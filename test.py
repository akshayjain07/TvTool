import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Canvas with Vertical Scrollbar")

# Create a frame to contain the canvas and scrollbar
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create the canvas
canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a vertical scrollbar to the frame
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas to work with the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Create an inner frame to hold the content
inner_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Function to update the canvas scroll region
def configure_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Bind the configure event of the inner frame to the function
inner_frame.bind("<Configure>", configure_canvas)

# Add content to the inner frame
for i in range(50):
    tk.Label(inner_frame, text=f"Item {i+1}").pack()

# Start the Tkinter event loop
root.mainloop()






# from tkinter import *
# root = Tk()
# root.geometry("500x500")
# root.title("scrollbar tutorial")
# # For connecting scrollbar to a widget 
# scrollbar = Scrollbar(root)
# scrollbar.pack(side=RIGHT, fill=Y)
# listbox = Listbox(root, yscrollcommand=scrollbar.set)
# for i in range(344):
#     listbox.insert(END, f"item {i}")
# listbox.pack(fill=Y, padx=22)
# scrollbar.config(command=listbox.yview)
# root.mainloop()




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

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Signals Page Test")
#     root.geometry("1400x800")

#     # Assuming there's a controller to pass, for simplicity, we pass None here
#     page = SignalsPage(root, None)
    
#     root.mainloop()
