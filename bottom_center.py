# import tkinter as tk
# from tkinter import ttk

# class BottomCenter(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent, bg='#070707')
#         self.pack_propagate(False)  # Prevent the frame from resizing to fit its content

#         # Get the parent dimensions
#         parent_width = parent.winfo_width()
#         parent_height = parent.winfo_height()
#         self.config(width=parent_width, height=parent_height)

#         # Create grey border on top side
#         self.config(highlightbackground="grey", highlightthickness=1, highlightcolor="grey")

#         # List of first row buttons with their text
#         buttons_text = [
#             "All logs", "0 Attention", "1 Errors", "0 Warnings", "6 Messages",
#             "0 Trading", "Clear Logs", "Copy All", "Exports"
#         ]

#         # Adjust button width based on parent width
#         button_width = parent_width // 10  # Width for each button
#         separator_width = button_width // 10  # Width for each separator

#         # Create and place buttons side by side with separators
#         for i, text in enumerate(buttons_text):
#             button = tk.Button(self, text=text, font=("Times New Roman", int(parent_height * 0.02)), bg='#070707', fg='white',
#                                bd=0, relief=tk.FLAT, cursor='hand2')
#             button.place(x=i * (button_width + separator_width), y=0, height=int(parent_height * 0.1), width=button_width)

#             if i < len(buttons_text) - 1:
#                 separator = tk.Label(self, text='|', bg='#070707', fg='white', font=("Times New Roman", int(parent_height * 0.03)))
#                 separator.place(x=(i + 1) * button_width + i * separator_width, y=int(parent_height * 0.02), height=int(parent_height * 0.06))

#         # Array of y coordinates for horizontal lines based on parent height
#         line_height = int(parent_height * 0.01)
#         y_coordinates = [int(parent_height * i) for i in [0.1, 0.2, 0.21, 0.29, 0.37, 0.45, 0.55, 0.63, 0.71, 0.79, 0.87]]

#         # Create horizontal rules (lines)
#         for y in y_coordinates:
#             line = tk.Frame(self, bg='grey', height=line_height, width=parent_width)
#             line.place(x=0, y=y, width=parent_width, height=line_height)

#         # List of second row buttons with their text, image file, and width
#         second_row_buttons = [
#             ("Time Stamp   ", "filter_logo.png", int(parent_width * 0.12), int(parent_width * 0.01)),
#             ("Log Type   ", "filter_logo.png", int(parent_width * 0.15), int(parent_width * 0.13)),
#             ("Message                                                                             ", "filter_logo.png", int(parent_width * 0.55), int(parent_width * 0.28)),
#             ("User   ", "filter_logo.png", int(parent_width * 0.09), int(parent_width * 0.85)),
#             ("Strategy   ", "filter_logo.png", int(parent_width * 0.12), int(parent_width * 0.94)),
#             ("Portfolio   ", "filter_logo.png", int(parent_width * 0.13), int(parent_width * 1.06))
#         ]

#         # Create and place second row buttons with images
#         for i, (text, image_file, button_width, x) in enumerate(second_row_buttons):
#             # Load the image
#             image = tk.PhotoImage(file=image_file)

#             # Create button with image and text
#             button = tk.Button(self, text=text, image=image, compound='right', font=("Times New Roman", int(parent_height * 0.02)),
#                                bg='#070707', fg='white', bd=0, relief=tk.FLAT, cursor='hand2')
#             button.place(x=x, y=int(parent_height * 0.12), height=int(parent_height * 0.1), width=button_width)
#             button.image = image  # Keep a reference to avoid garbage collection

#         # Create an additional space below buttons for any other components
#         self.additional_space = tk.Frame(self, bg='#070707')
#         self.additional_space.place(x=0, y=int(parent_height * 0.25), width=parent_width, height=parent_height - int(parent_height * 0.25))

#         # Example additional content below buttons
#         label = ttk.Label(self.additional_space, text="Bottom Right Component", background='#070707', foreground='white')
#         label.pack(padx=10, pady=10, fill="both", expand=True)




import tkinter as tk
from tkinter import ttk

class BottomCenter(tk.Frame):
    def __init__(self, parent, width):
        super().__init__(parent, width=width, bg='#F0F0F0')
        self.pack_propagate(False)  # Prevent the frame from resizing to fit its content

        # Create grey border on top side
        self.config(highlightbackground="grey", highlightthickness=1, highlightcolor="grey")

        # List of first row buttons with their text
        buttons_text = [
            "All logs", "0 Attention", "1 Errors", "0 Warnings", "6 Messages",
            "0 Trading", "Clear Logs", "Copy All", "Exports"
        ]

        button_width = 100  # Width for each button
        separator_width = 10  # Width for each separator

        # Create and place buttons side by side with separators
        for i, text in enumerate(buttons_text):
            button = tk.Button(self, text=text, font=("Times New Roman", 11), bg='#F0F0F0', fg='#000000', activebackground="#FFFFFF", activeforeground="#000000",
                               bd=0, relief=tk.FLAT, cursor='hand2')
            button.place(x=i*(button_width+separator_width), y=0, height=35, width=button_width)  # Adjust height and width as needed

            if i < len(buttons_text) - 1:
                separator = tk.Label(self, text='|', bg='#F0F0F0', activebackground="#000000", activeforeground="#FFFFFF", fg='#000000', font=("Times New Roman", 14))
                separator.place(x=(i+1)*button_width + i*separator_width, y=5, height=25)  # Adjust y and height as needed

        # # Create horizontal rule (line)
        # line = tk.Frame(self, bg='grey', height=1, width=width)
        # line.place(x=0, y=35, width=width, height=1)

        # Array of y coordinates for horizontal lines
        y_coordinates = [35, 80, 85, 115, 145, 175, 215, 245, 275, 305, 335]

        # Create horizontal rules (lines)
        for y in y_coordinates:
            line = tk.Frame(self, bg='grey', height=1, width=width)
            line.place(x=0, y=y, width=width, height=1)


        # List of second row buttons with their text, image file, and width
        second_row_buttons = [
            ("Time Stamp   ", "filter_logo.png", 110, 10),
            ("Log Type   ", "filter_logo.png", 120, 120),
            ("Message                                                                                                      ", "filter_logo.png", 500, 230),
            ("User   ", "filter_logo.png", 80, 720),
            ("Strategy   ", "filter_logo.png", 100, 800),
            ("Portfolio   ", "filter_logo.png", 115, 900)
        ]

        # Create and place second row buttons with images
        for i, (text, image_file, width, x) in enumerate(second_row_buttons):
            # Load the image
            image = tk.PhotoImage(file=image_file)

            # Create button with image and text
            button = tk.Button(self, text=text, image=image, compound='right', font=("Times New Roman", 12),
                               bg='#F0F0F0', fg='#000000', activebackground="#FFFFFF", activeforeground="#000000", bd=0, relief=tk.FLAT, cursor='hand2')
            button.place(x=x, y=40, height=35, width=width)  # Adjust y, height, and width as needed
            button.image = image  # Keep a reference to avoid garbage collection

        # # Create an additional space below buttons for any other components
        # self.additional_space = tk.Frame(self, bg='#070707')
        # self.additional_space.place(x=0, y=100, width=width, height=self.winfo_reqheight() - 100)  # Adjust y and height as needed

        # # Example additional content below buttons
        # label = ttk.Label(self.additional_space, text="Bottom Right Component", background='#070707', foreground='white')
        # label.pack(padx=10, pady=10, fill="both", expand=True)  # Fill the frame



