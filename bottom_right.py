import tkinter as tk
from bottom_tabs.bottom_orders_page import BottomOrdersPage
from bottom_tabs.bottom_positions_page import BottomPositionsPage
from bottom_tabs.bottom_holdings_page import BottomHoldingsPage
from bottom_tabs.bottom_settings_page import BottomSettingsPage
from bottom_tabs.bottom_strategies_page import BottomStrategiesPage
from bottom_tabs.bottom_brokers_page import BottomBrokersPage
from bottom_tabs.bottom_broker_strategy_mapping_page import BottomBrokerStrategyMappingPage
from bottom_tabs.bottom_profile_page import BottomProfilePage
from bottom_tabs.bottom_signals_page import BottomSignalsPage

class BottomRight(tk.Frame):
    def __init__(self, parent, width=None):
        super().__init__(parent, bg='#070707')

        if width:
            self.config(width=width)  # Set width if provided

        self.frames = {}
        for F in (BottomOrdersPage, BottomPositionsPage, BottomHoldingsPage, BottomSettingsPage, BottomStrategiesPage, BottomBrokersPage, BottomBrokerStrategyMappingPage, BottomProfilePage, BottomSignalsPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("BottomSignalsPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



