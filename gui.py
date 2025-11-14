from tkinter import Tk, ttk

class TemplateWindow(Tk):
    def __init__(self):
        super().__init__()
        
        self.create_frame()

        self.my_credit = ttk.Frame(self)
        self.my_credit.pack(side='bottom', pady=10)

        self.credit_label = ttk.Label(self.my_credit, font=('Segoe UI', 8), text='\nApp developed by\nRitesh (1AM22CI079)\nand\nPannaga JA (1AM22CI064)', justify='center')
        self.credit_label.pack()

    def create_frame(self):
        pass