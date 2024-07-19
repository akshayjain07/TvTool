import tkinter as tk
from bottom_left import BottomLeft
from bottom_center import BottomCenter
from bottom_right import BottomRight

class BottomComponent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(side="bottom", fill="x")

        sys_width = parent.winfo_screenwidth()

        # Calculate widths
        left_width = sys_width / 6
        center_width = sys_width * 2 / 3
        right_width = sys_width - left_width - center_width

        # Create BottomLeft component
        self.bottom_left = BottomLeft(self, width=left_width)
        self.bottom_left.pack(side="left", fill="both", expand=True)

        # Create BottomCenter component
        self.bottom_center = BottomCenter(self, width=center_width)
        self.bottom_center.pack(side="left", fill="both", expand=True)

        # Create BottomRight component
        self.bottom_right = BottomRight(self, width=right_width)
        self.bottom_right.pack(side="right", fill="both", expand=True)

    def show_bottom_right_page(self, page_name):
        self.bottom_right.show_frame(page_name)

    def show_bottom_left_page(self, page_name):
        self.bottom_left.show_frame(page_name)

    def show_bottom_center_page(self, page_name):
        self.bottom_center.show_frame(page_name)



