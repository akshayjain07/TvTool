import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Ensure you have Pillow installed: pip install pillow


# Assuming your brokers array
brokers = [("Kotak Neo", "Add_Kotak_Neo_Broker"), 
           ("Broker 2", "Add_Broker_2"),
           ("Broker 3", "Add_Broker_3"),
           ("Broker 4", "Add_Broker_4"),
           ("Broker 5", "Add_Broker_5"),
           ("Broker 6", "Add_Broker_6"),
           ("Broker 7", "Add_Broker_7"),
           ("Broker 8", "Add_Broker_8"),
           ("Broker 3", "Add_Broker_3"),
           ("Broker 4", "Add_Broker_4"),
           ("Broker 5", "Add_Broker_5"),
           ("Broker 6", "Add_Broker_6"),
           ("Broker 7", "Add_Broker_7"),
           ("Broker 8", "Add_Broker_8"),
           ("Broker 3", "Add_Broker_3"),
           ("Broker 4", "Add_Broker_4"),
           ("Broker 5", "Add_Broker_5"),
           ("Broker 6", "Add_Broker_6"),
           ("Broker 7", "Add_Broker_7"),
           ("Broker 8", "Add_Broker_8"),
           ("Broker 9", "Add_Broker_9")]



class BrokersPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#F0F0F0')  # Set the background color for the entire frame

        heading = tk.Label(self, text="Setup Brokers", foreground="#FFFFFF", background="#070707", anchor='w')
        heading.pack(side="top", fill="x", padx=20, pady=10)  # Fill the x-axis

        # Horizontal bar with labels
        horizontal_bar1 = tk.Frame(self, bg='#50727B')
        horizontal_bar1.pack(side="top", fill="x", expand=True, padx=20, pady=(0, 10))

        labels = [
            ("Broker", "left", (10, 59)),
            ("Index", "left", 170),
            ("Execution", "left", 130),
            ("Status", "left", 170),
            ("Actions", "right", (110, 150))
        ]

        for text, side, padx in labels:
            label = tk.Label(horizontal_bar1, text=text, background='#50727B', foreground="white")
            label.pack(side=side, padx=padx)



       # Broker information
        brokers = [
            ("Kotak Neo", "1", "Pending", "Logged In", "Logged Out", "Login"),
            ("Another Broker", "2", "Active", "Logged In", "Logged Out", "Logout"),
            # Add more brokers here
        ]

        for i, broker_info in enumerate(brokers):
            bg_color = '#395B64'
            horizontal_bar = tk.Frame(self, bg=bg_color)
            horizontal_bar.pack(fill="x", padx=20, pady=(0, 10), ipady=10)

            labels_info = [
                (broker_info[0], "left", (59, 40)),
                (broker_info[1], "left", 59),
                (broker_info[2], "left", 59),
                (broker_info[3], "left", (59, 3)),
                (broker_info[4], "left", (3, 59)),
                (broker_info[5], "right", (100, 80))
            ]

            for text, side, padx in labels_info:
                label = tk.Label(horizontal_bar, text=text, background='#395B64', foreground="white")
                label.pack(side=side, padx=padx)
        

        # Setup Brokers heading
        horizontal_bar = tk.Frame(self)
        # horizontal_bar = tk.Frame(self, bg="#F0F0F0")
        horizontal_bar.pack(fill="x")

        heading = tk.Label(horizontal_bar, text="Not Connected Brokers", foreground="#146C94", background="#F0F0F0")
        heading.pack(side="left", padx=10, pady=10)

       
        for broker in brokers:
            horizontal_bar2 = tk.Frame(self, bg='white')
            horizontal_bar2.pack(fill="x", padx=10, pady=(0, 10))

            broker_name = tk.Label(horizontal_bar2, text=broker[0], background='orange', foreground="white")
            broker_name.pack(side="left", padx=(59,40))

            # Create the button
            action_button = tk.Button(horizontal_bar2, text="Not Setup", background='orange', foreground="white", command=lambda b=broker: self.on_broker_click(b[1]))
            action_button.pack(side="right", padx=(100, 80))

    def on_broker_click(self, command):
        # Here you can handle the button click event
        print(f"Button clicked: {command}")
        # You can call the actual command function here, for example:
        # if command == "Add_Kotak_Neo_Broker":
        #     self.Add_Kotak_Neo_Broker()


