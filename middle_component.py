# import tkinter as tk
# from tkinter import ttk

# class MiddleComponent(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)
        
#         self.frames = {}
#         for F in (Dashboard, Orders, Positions, Strategy_Mapping, Brokers, Profile):
#             page_name = F.__name__
#             frame = F(parent=self, controller=self)
#             self.frames[page_name] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
        
#         self.show_frame("Dashboard")

#     def show_frame(self, page_name):
#         frame = self.frames[page_name]
#         frame.tkraise()

# class Dashboard(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         label = ttk.Label(self, text="This is DashBoard Page")
#         label.pack(padx=10, pady=10)

# class Orders(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         label = ttk.Label(self, text="This is Orders Page")
#         label.pack(padx=10, pady=10)

# class Positions(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         label = ttk.Label(self, text="This is Positions Page")
#         label.pack(padx=10, pady=10)

# class Strategy_Mapping(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         label = ttk.Label(self, text="This is Strategy Mapping Page")
#         label.pack(padx=10, pady=10)

# class Brokers(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         label = ttk.Label(self, text="This is Brokers Page")
#         label.pack(padx=10, pady=10)

# class Profile(tk.Frame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         label = ttk.Label(self, text="This is Profile Page")
#         label.pack(padx=10, pady=10)


# import tkinter as tk
# from tabs.dashboard_page import DashboardPage
# from tabs.orders_page import OrdersPage
# from tabs.positions_page import PositionsPage
# from tabs.strategy_mapping_page import StrategyMappingPage
# from tabs.brokers_page import BrokersPage
# from tabs.profile_page import ProfilePage

# class MiddleComponent(tk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)
        
#         self.frames = {}
#         for F in (DashboardPage, OrdersPage, PositionsPage, StrategyMappingPage, BrokersPage, ProfilePage):
#             page_name = F.__name__
#             frame = F(parent=self, controller=self)
#             self.frames[page_name] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
        
#         self.show_frame("DashboardPage")

#     def show_frame(self, page_name):
#         frame = self.frames[page_name]
#         frame.tkraise()



import tkinter as tk
from tabs.orders_page import OrdersPage
from tabs.positions_page import PositionsPage
from tabs.holdings_page import HoldingsPage
from tabs.settings_page import SettingsPage
from tabs.strategies_page import StrategiesPage
from tabs.brokers_page import BrokersPage
from tabs.broker_strategy_mapping_page import BrokerStrategyMappingPage
from tabs.profile_page import ProfilePage
from tabs.signals_page import SignalsPage

class MiddleComponent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#070707')
        
        self.frames = {}
        for F in (OrdersPage, PositionsPage, HoldingsPage, SettingsPage, StrategiesPage, BrokersPage, BrokerStrategyMappingPage, ProfilePage, SignalsPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            # frame.configure(bd=2, relief="solid")
        
        self.show_frame("SignalsPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

