import ssl

import requests

ssl._create_default_context = ssl._create_unverified_context()
# ssl._create_default_https_context = ssl._create_unverified_context()
import tkinter as tk
import webbrowser
from tkinter import TclError, ttk
# import login_gui
import pandas as pd
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
from PIL import ImageTk, Image
import ast
from gui_windows import *
# from ttkbootstrap import Style
import login
import threading
import getNotification
# import orderPlacement
import multiprocessing
import multiprocessing.popen_spawn_win32 as forking
# import multiprocessing
from datetime import datetime, timedelta
# from ttkbootstrap import Style
from pymongo import MongoClient
import configparser
import os
import sys
import socket
import uuid
import platform
from tkinter import scrolledtext
import time
dirs = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1,dirs)

import tkinter as tk
from tkinter import ttk
from navbar import Navbar
from middle_component import MiddleComponent
from bottom_component import BottomComponent

class _Popen(forking.Popen):
    def __init__(self, *args, **kw):
        if hasattr(sys, 'frozen'):
            # We have to set original _MEIPASS2 value from sys._MEIPASS
            # to get --onefile mode working.
            os.putenv('_MEIPASS2', sys._MEIPASS)
        try:
            super(_Popen, self).__init__(*args, **kw)
        finally:
            if hasattr(sys, 'frozen'):
                # On some platforms (e.g. AIX) 'os.unsetenv()' is not
                # available. In those cases we cannot delete the variable
                # but only set it to the empty string. The bootloader
                # can handle this case.
                if hasattr(os, 'unsetenv'):
                    os.unsetenv('_MEIPASS2')
                else:
                    os.putenv('_MEIPASS2', '')

class Process(multiprocessing.Process):
    _Popen = _Popen


def get_system_id():
    # Try to get MAC address (may not work on all systems)
    # try:
    #     mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)])
    # except Exception as e:
    #     mac_address = "Unknown"
    # Get hostname
    hostname = socket.gethostname()
    system_platform = platform.system()
    # Combine all information to create a unique system identifier
    system_id = f"{hostname}-{system_platform}"
    return system_id


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # self.title(" | Alignz Exports - AlgoTrading Platform")
        # self.iconbitmap('unfluke.ico')
        #
        # Geometry Part
        sys_width = self.winfo_screenwidth()
        sys_height = self.winfo_screenheight()
        # self.geometry(f'{sys_width}x{sys_height-180}+0+0')
        # self.resizable(False, False)

        # Initialize components
        self.top = Navbar(self)
        self.middle = MiddleComponent(self)
        self.bottom = BottomComponent(self)
        #
        # # Set heights for each component based on proportions
        # navbar_height = int(sys_height * 0.06)
        # middle_height = int(sys_height * 0.45)
        # bottom_height = int(sys_height * 0.45-43)
        #
        # # Layout Navbar using place
        # self.top.place(x=0, y=0, width=sys_width, height=navbar_height)
        #
        # # Layout MiddleComponent using place
        # self.middle.place(x=0, y=navbar_height, width=sys_width, height=middle_height)
        #
        # # Layout BottomComponent using place
        # self.bottom.place(x=0, y=navbar_height + middle_height, width=sys_width, height=bottom_height)
        #
        # # Pass the reference of middle and bottom components to top for navigation
        # self.top.set_middle_component(self.middle)
        # self.top.set_bottom_component(self.bottom)  # Added this line


        # import time
# import ttkbootstrap
# import tkinter as tk

def get_system_id():
    # Try to get MAC address (may not work on all systems)
    # try:
    #     mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)])
    # except Exception as e:
    #     mac_address = "Unknown"
    # Get hostname
    hostname = socket.gethostname()
    system_platform = platform.system()
    # Combine all information to create a unique system identifier
    system_id = f"{hostname}-{system_platform}"
    return system_id


tradingViewCreds = [{
    'email': '',
    'password': ''
}]
# API Keys
exchangess = [
    {
        "name": "angel",
        "id":1,
        "params": {
            "username": "",
            "password": "",
            "market_api":"",
            "trading_api":"",
            "historical_api":"",
            "otp_token":""
        },
        "active": 0,
        "count": 0
    },
    {
        "name": "alice",
        "id": 1,
        "params": {
            "username": "",
            "api_key":""
        },
        "active": 0,
        "count": 0
    },
    {
        "name": "dhan",
        "id": 1,
        "params": {
            "client_id": "",

        },
        "access_token":"",
        "active": 0,
        "count": 0
    },
    # {
    #     "name": "paytm",
    #     "id": 1,
    #     "params": {
    #         "api_key": "",
    #         "api_secret": "",
    #     },
    #     "active": 0,
    #     "inputs": {
    #         "request_token": ""
    #     },
    #     "count": 0
    # },
    {
        "name": "fyers",
        "id": 1,
        "params": {
            "client_id": "",
            "secret_key": "",
            "redirect_url":""
        },
        "active": 0,
        "inputs": {
            "Auth_Token": ""
        },
        "count": 0
    },
    # {
    #     "name": "icici",
    #     "id": 0,
    #     "params": {
    #         "api_key": "",
    #         "secret_key": "",
    #         "session_key":""
    #     },
    #     "active": 0,
    #     "inputs": {},
    #     "count": 0
    # },
    # {
    #     "name": "kotak",
    #     "id": 0,
    #     "params": {
    #         "consumer_key": "",
    #         "consumer_secret": "",
    #         "mobile_number":"",
    #         "password":""
    #     },
    #     "active": 0,
    #     "inputs": {
    #         "OTP":""
    #     },
    #     "count": 0
    # },
    {
        "name": "nuvama",
        "id": 1,
        "params": {
            "api_key": "",
            "api_secret": "",
        },
        "active": 0,
        "inputs": {
            "Request Id": ""
        },
        "count": 0
    },
    {
        "name": "shoonya",
        "id": 1,
        "params": {
            "username": "",
            "password": "",
            "app_key": "",
            "otp_token":"",
            "imei": "",
            # "totp":"",

        },
        "active": 0,
        "inputs": {},
        "count": 0
    },
    {
        "name": "upstox",
        "id": 0,
        "params": {
            "client_id": "",
            "client_secret": "",
            "redirect_url": ""
        },
        "active": 0,
        "inputs": {
            "auth_code":""
        },
        "count": 0
    },
    {
        "name": "zerodha-enc",
        "id": 0,
        "params": {
        },
        "active": 0,
        "inputs": {
            "Enc Token": ""
        },
        "count": 0
    },
    {
        "name": "zerodha",
        "id": 0,
        "params": {
            "api_key": "",
            "api_secret": ""
        },
        "active": 0,
        "inputs": {
            "Token": ""
        },
        "count": 0
    },
    {
        "name": "iifl",
        "id": 0,
        "params": {
            "Interactive_api_key": "",
            "Interactive_api_secret": "",
            "Market_api_key":"",
            "Market_api_secret":""
        },
        "active": 0,
        "count": 0
    }
]

loggedin = []
# with open("config.txt",'w') as f:
#         f.write(str(exchangess))

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def display_terms_and_conditions():
    # Create a new window for displaying terms and conditions
    popup = tk.Toplevel()
    popup.title("Terms and Conditions")
    popup.iconphoto(False,icon_img)
    # Add a scrolled text widget to display the terms
    text_area = scrolledtext.ScrolledText(popup, width=80, height=30, wrap=tk.WORD)
    text_area.pack(expand=True, fill=tk.BOTH)

    # Insert your terms and conditions text into the scrolled text widget
    terms_and_conditions = """
    Terms and Conditions
    ---------------------
    This agreement ("Agreement") is entered into between [Aseem Singhal] ("Instructor" or "We") and yourself ("Student" or "You") in connection to your usage of this tool (TVTool). By using this tool, you acknowledge and agree to be bound by the terms and conditions of this Agreement.

    • Use of Trading View Tool (TVTool): The TVTool is not intended as a recommendation or endorsement of any specific trading strategies or techniques. You agree to use the TVTool solely for educational purposes and understand that the Instructor does not provide a tip-providing service.

    • Responsibility: You acknowledge and agree that all decisions made and actions taken regarding your trading activities are solely your responsibility. We do not assume any responsibility for any profits or losses generated through the use of our trading tools (TVTool).

    • Tool Usage: You agree not to attempt to reverse engineer, modify, or share the code provided with others. The trading tool is for your personal use only and should not be distributed or repurposed without our explicit consent.

    • Functionality: You understand that the trading tool's (TVTool’s) performance may be affected by various factors, including but not limited to internet connectivity, hardware limitations (such as a slow laptop), errors within trading platforms (e.g., TradingView), issues with brokers, API malfunctions, and other technical glitches. We do not guarantee uninterrupted or error-free operation of the trading tool and are not liable for any issues arising from such factors.

    • Indemnification: By using this tool, you acknowledge and agree to indemnify and hold the Instructor harmless against any and all claims, damages, losses, liabilities, costs, and expenses (including attorney's fees) incurred by the Instructor arising out of or in connection with:
        - Any losses incurred by you in trading activities, whether or not influenced by this TVTool;
        - Any losses resulting from technology errors, including but not limited to technical glitches, system failures, failure of Python codes, failure of TVTool, or other technical issues;
        - The non-refundable nature of the TVTool fee and the understanding that no refunds will be provided after the usage of the tool commencement; and
        - The understanding that any backtested strategy results presented during the Course do not guarantee future profits or outcomes.

    • No Financial Guarantee: The Instructor makes no representations or warranties regarding the profitability or success of any trading strategies or techniques discussed. You understand and acknowledge that trading activities involve inherent risks, and any decisions or actions taken based on the Course content are at your own discretion and risk.

    • Market Risks: You understand and acknowledge that option trading and automatic API trading are subject to market risks. The Instructor shall not be held liable for any losses incurred due to market volatility, fluctuations, or any other market-related factors.

    • Intellectual Property: All Course materials, including but not limited to text, graphics, videos, and code, are the intellectual property of the Instructor and protected by applicable copyright laws. You agree not to reproduce, distribute, or share any Course materials without prior written permission from the Instructor.

    • Governing Law and Jurisdiction: This Agreement shall be governed by and construed in accordance with the laws of India. Any disputes arising out of or in connection with this Agreement shall be subject to the exclusive jurisdiction of the courts located in New Delhi, India.

    • Disclosure: I am not a SEBI registered Advisor, and I do not possess any Research Analyst or Investment Advisor license. By enrolling in this course, you acknowledge and agree that you are undertaking the course at your own responsibility. You understand that any information or guidance provided during the course is for educational purposes only and should not be construed as financial advice or recommendations for investment decisions. You are solely responsible for any actions you take based on the knowledge and skills acquired through the course.

    By using this TVTool, you acknowledge that you have read and understood the terms and conditions of this Agreement. You agree to comply with all the obligations and responsibilities outlined herein.

    IF YOU DO NOT AGREE TO ABOVE, YOU SHOULD NOT LOGIN TO THE TOOL.
    """

    text_area.insert(tk.END, terms_and_conditions)

    # Disable editing in the text widget
    text_area.configure(state='disabled')

    # Run the popup window
    popup.mainloop()


def create_side_frame(root):



    # Geometry Part
    sys_width = root.winfo_screenwidth()
    sys_height = root.winfo_screenheight()
    # root.geometry(f'{sys_width}x{sys_height-180}+0+0')
    # root.resizable(False, False)

    # Initialize components
    root.top = Navbar(root)
    root.middle = MiddleComponent(root)
    root.bottom = BottomComponent(root)

    # Set heights for each component based on proportions
    navbar_height = int(sys_height * 0.06)
    middle_height = int(sys_height * 0.64)
    bottom_height = int(sys_height * 0.26-43)

    # Layout Navbar using place
    root.top.place(x=0, y=0, width=sys_width, height=navbar_height)

    # Layout MiddleComponent using place
    root.middle.place(x=0, y=navbar_height, width=sys_width, height=middle_height)

    # Layout BottomComponent using place
    root.bottom.place(x=0, y=navbar_height + middle_height, width=sys_width, height=bottom_height)

    # Pass the reference of middle and bottom components to top for navigation
    root.top.set_middle_component(root.middle)
    root.top.set_bottom_component(root.bottom)  # Added this line
    # getExchanges()
    # global tradingViewCreds
    # try:
    #     with open(resource_path("trading_view_creds.txt"),'r') as f:
    #         tradingViewCreds = ast.literal_eval(f.read())
    # except:
    #     print("Enter trading view Credentials creds.")
    # frame = ttk.Frame(root,height=root.winfo_screenheight()-100,width=root.winfo_screenwidth()/3-30)
    #
    # side_top_frame = create_side_top_frame(frame,(root.winfo_screenheight()-100)*0.30, root.winfo_screenwidth()/3-30-20)
    # side_top_frame.grid(column=0, row=0, rowspan=1, columnspan=1)
    # # create_side_main_frame(frame,(root.winfo_screenheight()-100)*0.75, root.winfo_screenwidth()/3-30-20)
    # create_broker_frame(frame,(root.winfo_screenheight()-100)*0.75, root.winfo_screenwidth()/3-30-20)
    # for widget in frame.winfo_children():
    #     widget.grid(padx=5, pady=5)
    # frame.grid_propagate(False)
    # frame.grid(column=0, row=0,padx=10,pady=10, sticky='N')
    # return frame

# def toggle_button():
# Toggle the state of the button
# if paper_trading:
#     paper_trading_btn.config(text="Toggle Off")
# else:
#     paper_trading_btn.config(text="Toggle On")
# paper_trading.set(not paper_trading.get())
def create_side_top_frame(root,height,width):
    global paper_trading_btn
    global paper_trading
    frame = ttk.Frame(root,height=height,width=width,padding=10)

    ttk.Label(frame, text='Trading View Details',font=('Helvetica', 18) ).grid(column=0, row=0, sticky=tk.W, columnspan=2,rowspan=1)
    # keyword = ttk.Entry(frame, width=30)
    # keyword.focus()
    # keyword.grid(column=1, row=0, sticky=tk.W)

    # Replace with:

    # paper_trading = True
    ttk.Label(frame, text='Gmail Id: ').grid(column=0, row=1, sticky=tk.W)
    gmailid = ttk.Entry(frame)
    gmailid.insert(0,tradingViewCreds[0]['email'])
    gmailid.grid(column=1, row=1, sticky=tk.W)
    ttk.Label(frame, text='Password: ').grid(column=0, row=2, sticky=tk.W)
    password = ttk.Entry(frame, show='*')
    password.insert(0,tradingViewCreds[0]['password'])
    password.grid(column=1, row=2, sticky=tk.W)
    paper_trading_btn = ttk.Checkbutton(frame, text="Paper trading ?", variable=paper_trading)
    paper_trading_btn.grid(row=3,column= 0)
    start_alerts_btn = ttk.Button(frame, text='Start Bridge',command=lambda: start_tv_alerts(root,gmailid.get(),password.get()))
    start_alerts_btn.grid(column=2, row=1)
    stop_alerts_btn = ttk.Button(frame, text='Stop Bridge',state='disabled',command=stop_alerts)
    if(alerts_status):
        stop_alerts_btn['state'] = 'normal'
        start_alerts_btn['state'] = 'disabled'
        paper_trading_btn['state'] = 'disabled'
    stop_alerts_btn.grid(column=2, row=2)
    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)
    frame.grid_propagate(False)
    return frame

alerts=[]
with open(resource_path('alerts.txt'),'r') as f:
    alerts = ast.literal_eval(f.read())
orders=[]
with open(resource_path('orders.txt'),'r') as f:
    orders = ast.literal_eval(f.read())
alertProcess  = None
alerts_status = 0

def stop_alerts():
    global alerts_status
    try:
        if alertProcess.is_alive() :
            alertProcess.terminate()
            print("Stopping alerts...")
            alerts_status=0
            create_side_frame(root)
            messagebox.showinfo("TVTool Bridge","Bridge stopped successfully")
            print("Alerts Stopped !")
        else:
            print("Stopping alerts...")
            alerts_status=0
            create_side_frame(root)
            print("Alerts Stopped !")

    except:
        alerts_status=0
        create_side_frame(root)
def start_tv_alerts(root,username,password):
    print(username)
    global alertProcess,alerts_status
    global orders
    global alerts
    tradingViewCreds[0]['email'] = username
    tradingViewCreds[0]['password'] = password
    with open(resource_path("trading_view_creds.txt"),'w') as f:
        f.write(str(tradingViewCreds))
    try:
        alertProcess = Process(target=getNotification.login_and_get_tv_alerts,args=(username,password,alerts,orders,paper_trading.get()))
        alertProcess.start()

        alerts_status=1
        create_side_frame(root)
    except:
        print("Error starting Trading view alerts. Use correct credentials.")
    messagebox.showinfo("Starting Bridge", "Please wait for 20 secs after pressing OK.")
    time.sleep(20)
    if not alertProcess.is_alive():
        messagebox.showerror("Login Error","Trading view Login Error")
    else:
        messagebox.showinfo("Success", "Bridge Started successfully.")
    print(alertProcess)


def create_broker_frame(root,height,width):
    getExchanges()
    frame = ttk.Frame(root,height=height,width=width)

    ttk.Label(frame, text='Brokers',font=('Helvetica', 18)).grid(column=0, row=0, sticky='w')
    row_index=1
    for exchange in exchanges:
        if exchange['id'] > 0:
            exc_frame = ttk.Frame(frame,height=40,width=width,padding='5 0')
            exc_frame.grid_propagate(False)
            exc_frame.grid(row=row_index,column=0,sticky='w',ipadx=5)

            row_index += 1
            if exchange['id'] == 1:
                ttk.Label(exc_frame,text=exchange['name'].capitalize(),font=('Helvetica', 12),width=10).grid(row=0,column=0)
            else:
                ttk.Label(exc_frame,text=exchange['name'].capitalize()+" "+str(exchange['id']),width=10,font=('Helvetica', 12)).grid(row=0,column=0)
            keys_missing = False
            # print(warning_img)
            # ttk.Photo
            for x in exchange['params']:
                # print(exchange['params'][x])
                if exchange['params'][x] == "":
                    # print('True')
                    keys_missing = True
            if(keys_missing):
                ttk.Button(exc_frame,text='View Keys', image=warning_img, compound="right",command=lambda ex=exchange['name'], id=exchange['id']: view_keys_window(ex,id)).grid(row=0,column=1)
                # ttk.Button(exc_frame,text='Update Keys',command=lambda ex=exchange['name'], id=exchange['id']: update_broker_window(ex,id)).grid(row=0,column=2,padx=5)
                ttk.Button(exc_frame,text='Login',state='disabled').grid(row=0,column=2,padx=5)

                # ttk.Checkbutton(exc_frame, text='Use', command=lambda broker=exchange['name'], id=exchange['id']: toggle_broker(broker,id)).grid(row=0,column=4)
            else:
                ttk.Button(exc_frame,text='View Keys',command=lambda ex=exchange['name'], id=exchange['id']: view_keys_window(ex,id)).grid(row=0,column=1)
                # ttk.Button(exc_frame,text='Update Keys',command=lambda ex=exchange['name'], id=exchange['id']: update_broker_window(ex,id)).grid(row=0,column=2,padx=5)
                ttk.Button(exc_frame,text='Login', command=lambda root = root,broker=exchange: broker_login(broker)).grid(row=0,column=3,padx=5)
                # tk.PhotoImage(file='assets/light-png-42433.png')
                # ttk.Checkbutton(exc_frame, text='Use', command=lambda broker=exchange['name'], id=exchange['id']: toggle_broker(broker,id)).grid(row=0,column=4)
                try:
                    if exchange['timestamp'] == str(datetime.now().date()):
                        ttk.Label(exc_frame,image=green_indicator_img).grid(row=0,column=4,padx=5)
                    else:
                        ttk.Label(exc_frame,image=red_indicator_img).grid(row=0,column=4,padx=5)
                except:
                    ttk.Label(exc_frame,image=red_indicator_img).grid(row=0,column=4,padx=5)
            # for widget in exc_frame.winfo_children():
            #     widget.grid( pady=1)
    add_frame = ttk.Frame(frame)
    add_frame.grid(row=row_index,column=0,sticky='w',ipadx=5)
    for widget in frame.winfo_children():
        widget.grid(padx=10, pady=0)
    ttk.Button(add_frame,text="Add Broker",width=15,command=add_broker_window).grid(row=0,column=0)
    frame.grid(column=2, row=0, padx=10,sticky='N')
    frame.grid_propagate(False)
    frame.grid(column=0, row=1, rowspan=4, columnspan=1)

    # return frame

# def toggle_broker(broker,id):
#     global exchanges
#     # print(use_var.get())
#     for i in range(len(exchanges)):
#         if exchanges[i]['name'] == broker and exchanges[i]['id'] == id:
#             if exchanges[i]['active'] ==1:
#                 exchanges[i]['active'] = 0
#             else:
#                 exchanges[i]['active'] = 1
#             # exchanges[i]['active'] = int(use_var.get())
#             print(exchanges[i])
#
#     updateExchanges()
#     return
def broker_login(broker):
    login.Login(broker)
    create_side_frame(root)

def update_broker_window(broker,id):
    global exchanges
    new_keys = UpdateKeysWindow(root,broker,id)
    new_keys.wait_window(new_keys)
    print(new_keys.attrs)
    if(new_keys.attrs == None):
        return
    for i in range(len(exchanges)):
        if exchanges[i]['name'] == broker and exchanges[i]['id'] == id:
            exchanges[i]['params'] = new_keys.attrs
    # print(exchanges)
    print("---")
    with open(resource_path("config.txt"),'w') as f:
        f.write(str(exchanges))
    getExchanges()
    updateExchanges()
    create_side_frame(root)
    return
    # create_broker_frame(root,(root.winfo_screenheight()-100)*0.75, root.winfo_screenwidth()/3-30-20)
def add_broker_window():
    global exchanges
    getExchanges()
    broker_window = BrokerWindow(root)
    broker_window.wait_window(broker_window)
    print("Result:", broker_window.result)
    if(broker_window.result != None):
        keys_window = AddKeysWindow(root,broker_window.result)
        keys_window.wait_window(keys_window)
        if(keys_window.attrs == None):
            return
        # else:
        print(keys_window.attrs)
        for x in exchanges:
            if x['name'] == broker_window.result:
                c = x['count'] +1
                new_x = {
                    'id': x['count']+1,
                    'name' : x['name'],
                    "params": keys_window.attrs,
                    "active": 0,
                    "count" : c
                }
                print(c)
                for rem_x in exchanges:
                    if rem_x['name'] == broker_window.result:
                        rem_x['count'] = c

                if('inputs' in x.keys()):
                    new_x['inputs'] = x['inputs']
                exchanges.append(new_x)
                print("Added")
                # print(exchanges)
                updateExchanges()
                # print(exchanges)
                # create_broker_frame(root,(root.winfo_screenheight()-100)*0.75, root.winfo_screenwidth()/3-30-20)
                create_side_frame(root)
                return
        for x in exchangess:
            if x['name'] == broker_window.result:
                print(x)
                if x['count'] == 0:
                    x['id'] = 1
                    x['count'] = 1
                    x['params'] = keys_window.attrs
                    exchanges.append(x)
                    # break
                # else:

                break
        # print(exchanges)
        updateExchanges()
        # print(exchanges)
        # create_broker_frame(root,(root.winfo_screenheight()-100)*0.75, root.winfo_screenwidth()/3-30-20)
        create_side_frame(root)
        return

def view_keys_window(broker,id):
    view_key_window = ViewKeysWindow(root,broker,id)
    view_key_window.wait_window(view_key_window)
    if(view_key_window.update == 1):
        # print("update kro")
        update_broker_window(broker,id)
    return

# def create_main_frame(root):
#     frame = ttk.Frame(root)
#     broker_frame = create_broker_frame(frame)
#     broker_frame.grid(row=0,column=0)
#
#     for widget in frame.winfo_children():
#         widget.grid(padx=5, pady=5)
#     return frame


def get_orders_list():
    create_orders_frame(root)

# def get_alerts_list():
#     create_alert_frame(root)

# def clear_alerts_list():
#     global alerts
#     alerts=[]
#     with open(resource_path('alerts.txt'),'w') as f:
#         f.write(str(alerts))
#     create_alert_frame(root)

def clear_orders_list():
    global orders
    orders=[]
    with open(resource_path('orders.txt'),'w') as f:
        f.write(str(orders))
    create_orders_frame(root)

def save_alerts_list():
    global alerts
    with open(resource_path('alerts.txt'),'r') as f:
        alerts = ast.literal_eval(f.read())
    alerts_df = pd.DataFrame(alerts)
    dt = datetime.now()
    _file_name = f'Alerts_{str(dt.day)+"_"+str(dt.month)+"_"+str(dt.year)+"_"+str(dt.hour)+"_"+str(dt.minute)+"_"+str(dt.second)}.csv'
    _path = asksaveasfile(confirmoverwrite=True,defaultextension='.csv',filetypes=[("Comma Seperated Values", "*.csv")],title="Choose File Path",initialfile=_file_name)

    alerts_df.to_csv(_path)

def save_orders_list():
    global orders
    with open(resource_path('orders.txt'),'r') as f:
        orders = ast.literal_eval(f.read())
    orders_df = pd.DataFrame(orders)
    dt = datetime.now()
    _file_name = f'Orders_{str(dt.day)+"_"+str(dt.month)+"_"+str(dt.year)+"_"+str(dt.hour)+"_"+str(dt.minute)+"_"+str(dt.second)}.csv'
    _path = asksaveasfile(confirmoverwrite=True,defaultextension='.csv',filetypes=[("CSV", "*.csv")],title="Choose File Path",initialfile=_file_name)
    orders_df.to_csv(_path)

# def create_alert_frame(root_):
#     global alerts
#     with open(resource_path('alerts.txt'),'r') as f:
#         alerts = ast.literal_eval(f.read())
#
#     frame = ttk.Frame(root_,height=root_.winfo_screenheight()-100,width=root_.winfo_screenwidth()/3-30)
#     ttk.Label(frame, text='Alerts',font=('Helvetica', 18)).grid(column=0, row=0, sticky='w')
#
#     add_frame = ttk.Frame(frame)
#     add_frame.grid(row=1,column=0,sticky='w',ipadx=5)
#     for widget in frame.winfo_children():
#         widget.grid(padx=10, pady=5)
#     ttk.Button(add_frame,text="Refresh",command=lambda:get_alerts_list()).grid(row=0,column=0)
#     ttk.Button(add_frame,text="Clear All",command=lambda:clear_alerts_list()).grid(row=0,column=1,padx=5)
#     ttk.Button(add_frame,text="Export to CSV",command=lambda:save_alerts_list()).grid(row=0,column=2)
#     AlertScrollFrame(frame,alerts)
#
#     frame.grid(column=1, row=0, padx=10, pady=10, sticky='N')
#     frame.grid_propagate(False)
#     # root.after(1000,lambda root = root_:create_alert_frame(root))
# def create_orders_frame(root):
#     # frame = ttk.Frame(root,height=root.winfo_screenheight()-100,width=root.winfo_screenwidth()/3-30,padding=10)
#     global orders
#     with open(resource_path('orders.txt'),'r') as f:
#         orders = ast.literal_eval(f.read())
#     frame = ttk.Frame(root,height=root.winfo_screenheight()-100,width=root.winfo_screenwidth()/3-30)
#     ttk.Label(frame, text='Orders',font=('Helvetica', 18)).grid(column=0, row=0, sticky='w')
#     add_frame = ttk.Frame(frame)
#     add_frame.grid(row=1,column=0,sticky='w',ipadx=5)
#     for widget in frame.winfo_children():
#         widget.grid(padx=10, pady=5)
#     ttk.Button(add_frame,text="Refresh",command=lambda:get_orders_list()).grid(row=0,column=0)
#     ttk.Button(add_frame,text="Clear All",command=lambda:clear_orders_list()).grid(row=0,column=1,padx=5)
#     ttk.Button(add_frame,text="Export to CSV",command=lambda:save_orders_list()).grid(row=0,column=2)
#     OrdersScrollFrame(frame,orders)
#
#     frame.grid(column=2, row=0, padx=10, pady=10, sticky='N')
#     frame.grid_propagate(False)
#     return frame
# # warningimg = Image.open('assets/warning.png')
# # print(warningimg)

def updateExchanges():
    global exchanges
    with open(resource_path("config.txt"),'w') as f:
        f.write(str(exchanges))
    getExchanges()

# def updateAlerts():
#     global alerts

def getExchanges():
    global exchanges
    with open(resource_path('config.txt'),'r') as f:
        exchanges = ast.literal_eval(f.read())

def seedExchanges():
    with open(resource_path("config.txt"),'w') as f:
        f.write(str(exchangess))

def logout():
    global _id
    active_session_fetch_url = api+"/"+database_name+'/'+sessions_collection_name+'/?query={"username":"'+username+'"}'
    userdetails  = requests.get(active_session_fetch_url)
    if userdetails.status_code == 200:
        print(userdetails.json())
        _id = userdetails.json()[0]['_id']
    else:
        print('Failed to fetch data. Status code:', userdetails.status_code)
    if len(userdetails.json())>0:
        # sessions_collection.delete_one({"username": username})
        session_del = requests.delete(api+"/"+database_name+'/'+sessions_collection_name+'/'+_id)
        print(api+"/"+database_name+'/'+sessions_collection_name+'/'+_id)
        print(session_del.status_code)
        if session_del.status_code == 200 and  len(session_del.json())>0:
            print(session_del.json())
            login_doc = {
                "username": username,
                "time": str(datetime.now()),
                "system_id": get_system_id(),
                "login/logout": "Logout"
            }
            # Insert session document into MongoDB
            logs_res = requests.post(str(api+'/'+database_name+'/'+login_logs_collection_name),json={"data":login_doc})
            # login_logs_collection.insert_one(login_doc)
            return True, "Logout successful"
        else:
            return False, "User not logged out. Network error."
    else:
        return False, "User not logged in"
def on_closing():
    # global username
    if messagebox.askokcancel("Quit", "Do you want to logout and exit?"):
        stop_alerts()
        success, message = logout()
        if success:

            messagebox.showinfo("Logout", message)
            root.destroy()
            sys.exit()
        else:
            messagebox.showerror("Logout Error", message)

def on_closing_login():
    # global username
    if messagebox.askokcancel("Quit", "Do you want to exit?"):
        root1.destroy()
        # sys.quit()
        sys.exit()

# def main():
#     global warning_img
#     global red_indicator_img
#     global green_indicator_img
#     global exchanges
#     global root
#     # root.configure(bg='#000')
#

def tnc_tvauto():
    webbrowser.open("https://drive.google.com/file/d/1JwjcQztRJVzIAMoGi0-XoMx3ojSDVzA8/view?usp=sharing")

def login_tvauto():
    # print("test")
    # return
    global sessions_collection
    global login_logs_collection
    global username
    print(tnc_var.get())
    if not tnc_var.get():
        messagebox.showerror("Login Error", f"Please agree terms and conditions to continue login.")
        return
    username = username_entry.get()
    password = password_entry.get()
    print(username,password)
    # if(username.split('_')[0] == 'INSERTNEWUSER'):
    #     new_user = {
    #         "username": username.split('_')[1],
    #         "password":
    #     }

    # config = configparser.ConfigParser()
    # config.read(resource_path('mongo_config.ini'))
    # Get MongoDB credentials from config file
    # mongodb_uri = 'mongodb+srv://admin:3RTFzhRSz989070u@tvtool.k8yv10o.mongodb.net/'



    # Connect to MongoDB
    # client = MongoClient(mongodb_uri)
    # db = client[database_name]
    # collection = db[users_collection_name]
    # sessions_collection = db[sessions_collection_name]
    # login_logs_collection = db[login_logs_collection_name]
    # roundoff_collection = db[roundoff_collection_name]
    # roundoff_data = roundoff_collection.find({}, {"_id": 0})
    # # print(roundoff_data)
    # roundoffdf = pd.DataFrame(list(roundoff_data))
    # roundoffdf.to_csv('optionstrike_data.csv')
    active_session_fetch_url = api+"/"+database_name+'/'+sessions_collection_name+'/?query={"username":"'+username+'"}'
    # print(user_fetch_url)

    userdetails  = requests.get(active_session_fetch_url)
    if userdetails.status_code == 200:
        # print('GET request was successful!')
        # print('Response JSON:')
        print(userdetails.json())
    else:
        print('Failed to fetch data. Status code:', userdetails.status_code)
    if len(userdetails.json())>0:
        active_id_session_fetch_url = api+"/"+database_name+'/'+sessions_collection_name+'/?query={"username":"'+username+'","system_id":"'+get_system_id()+'"}'
        session_res = requests.get(active_id_session_fetch_url)
        if session_res.status_code == 200:
            session = session_res.json()[0]
            _id = session['_id']
            print(_id)
        else:
            session = False
        # if sessions_collection.find_one({"user_id":username,"system_id":get_system_id()}) and tnc_var.get():
        if session and tnc_var.get():
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            root.deiconify()
            root.state('zoomed')
            root1.destroy()
            return
        else:
            messagebox.showerror("Login Error", f"User, {username} already logged in another system!")
            return False
        # return False, "User already logged in from another location"
    # Check if username and password are correct
    dt = datetime.now()
    # collection.insert_one({"username": username, "password": password,"valid_till":datetime(2024, 5, 30, 12, 30, 0)})
    # user = collection.find_one({"username": username, "password": password,"valid_till":{'$gte':dt}})
    user_auth = api+"/"+database_name+'/'+users_collection_name+'/?query='+'{"username":"'+username+'","password":"'+password+'"}'
    print(user_auth)
    auth_res = requests.get(user_auth)
    if auth_res.status_code == 200:
        # print('GET request was successful!')
        # print('Response JSON:')
        print(auth_res.json())
        user = auth_res.json()
        if len(user)>0:
            valid_date = datetime.fromisoformat(user[0]['valid_till'])
            print(valid_date)
        if len(user)>0 and tnc_var.get() and valid_date >= dt:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            session_doc = {
                "username": username,
                "start_time": str(datetime.now()),
                "system_id": get_system_id()
            }
            login_doc = {
                "username": username,
                "time": str(datetime.now()),
                "system_id": get_system_id(),
                "login/logout": "Login"
            }
            # Insert session document into MongoDB
            logs_res = requests.post(str(api+'/'+database_name+'/'+login_logs_collection_name),json={"data":login_doc})
            session_res = requests.post(str(api+'/'+database_name+'/'+sessions_collection_name),json={"data":session_doc})

            if session_res.status_code == 200:

                print(session_res.json())
                _id = session_res.json()[0]['_id']
                print(_id)
            else:
                print('Failed to post session data. Status code:', session_res.status_code)
            # login_logs_collection.insert_one(login_doc)
            # sessions_collection.insert_one(session_doc)
            root.deiconify()
            root.state('zoomed')
            root1.destroy()
            # main()
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password")
    else:
        messagebox.showerror("Network Error", "Failed to Fetch Data")
        print('Failed to fetch data. Status code:', auth_res.status_code)



if __name__ == "__main__":
    multiprocessing.freeze_support()
    # login_gui.main()
    # main()
    api = 'http://ec2-65-0-85-93.ap-south-1.compute.amazonaws.com'
    database_name = 'TVTool'
    users_collection_name = 'users'
    sessions_collection_name = 'Active_Sessions'
    roundoff_collection_name = 'Roundoff_data'
    login_logs_collection_name = 'User_Login_Logs'
    _id='0'
    root = tk.Tk()
    root.title("TVTool by Unfluke")
    # root.state('zoomed')
    root.geometry("")
    # root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()-180}+0+0')
    root.protocol("WM_DELETE_WINDOW", on_closing)

    warning_img = ImageTk.PhotoImage(Image.open(resource_path('assets/warning_18.png')))
    red_indicator_img = ImageTk.PhotoImage(Image.open(resource_path('assets/light-png-42433-small.png')))
    green_indicator_img = ImageTk.PhotoImage(file=resource_path('assets/light-png-42432-small.png'))
    icon_img = ImageTk.PhotoImage(file=resource_path("assets/icon.png"))
    exchanges=[]
    # use_var = tk.StringVar(value='0')
    getExchanges()
    paper_trading = tk.BooleanVar(value=False)
    tnc_var = tk.BooleanVar(value=False)
    create_side_frame(root)
    # create_alert_frame(root)
    # create_orders_frame(root)
    # for widget in root.winfo_children():
    #     widget.configure()

    # def login_guii():
    #     global username
    #     global password
    root1 = tk.Toplevel()
    root1.title("TVTool by Unfluke")
    root1.state('zoomed')
    root1.protocol("WM_DELETE_WINDOW", on_closing_login)
    frame = tk.Frame(root1)
    frame.pack(expand=True)
    ttk.Label(frame,text="TVTool",font=("Helvetica",32)).pack(pady=5)
    ttk.Label(frame,text="by",font=("Helvetica",13)).pack(pady=0)
    logo_img = ImageTk.PhotoImage(file=resource_path("assets/UNFLUKE (Custom) (Custom).png"))
    # Create username label and entry
    ttk.Label(frame,image=logo_img).pack(pady=0)
    username_label = ttk.Label(frame, text="Username",font=("Helvetica",13))
    username_label.pack(pady=5)
    username_entry = ttk.Entry(frame,width=30)
    username_entry.pack(pady=10)
    # Create password label and entry
    password_label = ttk.Label(frame, text="Password",font=("Helvetica",13))
    password_label.pack(pady=10)
    password_entry = ttk.Entry(frame, show="*",width=30)
    password_entry.pack(pady=5)
    frametnc = tk.Frame(frame)
    frametnc.pack(pady=20)
    tnc_button = ttk.Button(frametnc, text="Terms & Conditions", command=display_terms_and_conditions).pack(side=tk.RIGHT)
    tnc_cbx = ttk.Checkbutton(frametnc, text="I agree to all the terms and conditions mentioned here and continue.", variable=tnc_var).pack(padx=10,side=tk.LEFT)
    # Create login button
    login_button = ttk.Button(frame, text="Login", command= login_tvauto ,width=15)
    login_button.pack(pady=0)

    vertical_center = (root1.winfo_screenheight() - root1.winfo_reqheight()) // 2
    # Place the frame at the vertical center
    frame.place(relx=0.5, rely=0.5, anchor="center")

    root1.iconphoto(False,icon_img)
    root.iconphoto(False,icon_img)
    # Run the Tkinter event loop
    # root1.mainloop()
    # return root1
    root.withdraw()
    root.mainloop()
    app = MainApp()
    app.mainloop()














# if __name__ == "__main__":
#     app = MainApp()
#     app.mainloop()


# class _Popen(forking.Popen):
#     def __init__(self, *args, **kw):
#         if hasattr(sys, 'frozen'):
#             # We have to set original _MEIPASS2 value from sys._MEIPASS
#             # to get --onefile mode working.
#             os.putenv('_MEIPASS2', sys._MEIPASS)
#         try:
#             super(_Popen, self).__init__(*args, **kw)
#         finally:
#             if hasattr(sys, 'frozen'):
#                 # On some platforms (e.g. AIX) 'os.unsetenv()' is not
#                 # available. In those cases we cannot delete the variable
#                 # but only set it to the empty string. The bootloader
#                 # can handle this case.
#                 if hasattr(os, 'unsetenv'):
#                     os.unsetenv('_MEIPASS2')
#                 else:
#                     os.putenv('_MEIPASS2', '')
#
# class Process(multiprocessing.Process):
#     _Popen = _Popen
#
#
# def get_system_id():
#     # Try to get MAC address (may not work on all systems)
#     # try:
#     #     mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)])
#     # except Exception as e:
#     #     mac_address = "Unknown"
#     # Get hostname
#     hostname = socket.gethostname()
#     system_platform = platform.system()
#     # Combine all information to create a unique system identifier
#     system_id = f"{hostname}-{system_platform}"
#     return system_id
#
# # import time
# # import ttkbootstrap
# # import tkinter as tk
# tradingViewCreds = [{
#     'email': '',
#     'password': ''
# }]
# # API Keys
# exchangess = [
#     {
#         "name": "angel",
#         "id":1,
#         "params": {
#             "username": "",
#             "password": "",
#             "market_api":"",
#             "trading_api":"",
#             "historical_api":"",
#             "otp_token":""
#         },
#         "active": 0,
#         "count": 0
#     },
#     {
#         "name": "alice",
#         "id": 1,
#         "params": {
#             "username": "",
#             "api_key":""
#         },
#         "active": 0,
#         "count": 0
#     },
#     {
#         "name": "dhan",
#         "id": 1,
#         "params": {
#             "client_id": "",
#
#         },
#         "access_token":"",
#         "active": 0,
#         "count": 0
#     },
#     # {
#     #     "name": "paytm",
#     #     "id": 1,
#     #     "params": {
#     #         "api_key": "",
#     #         "api_secret": "",
#     #     },
#     #     "active": 0,
#     #     "inputs": {
#     #         "request_token": ""
#     #     },
#     #     "count": 0
#     # },
#     {
#         "name": "fyers",
#         "id": 1,
#         "params": {
#             "client_id": "",
#             "secret_key": "",
#             "redirect_url":""
#         },
#         "active": 0,
#         "inputs": {
#             "Auth_Token": ""
#         },
#         "count": 0
#     },
#     # {
#     #     "name": "icici",
#     #     "id": 0,
#     #     "params": {
#     #         "api_key": "",
#     #         "secret_key": "",
#     #         "session_key":""
#     #     },
#     #     "active": 0,
#     #     "inputs": {},
#     #     "count": 0
#     # },
#     # {
#     #     "name": "kotak",
#     #     "id": 0,
#     #     "params": {
#     #         "consumer_key": "",
#     #         "consumer_secret": "",
#     #         "mobile_number":"",
#     #         "password":""
#     #     },
#     #     "active": 0,
#     #     "inputs": {
#     #         "OTP":""
#     #     },
#     #     "count": 0
#     # },
#     {
#         "name": "nuvama",
#         "id": 1,
#         "params": {
#             "api_key": "",
#             "api_secret": "",
#         },
#         "active": 0,
#         "inputs": {
#             "Request Id": ""
#         },
#         "count": 0
#     },
#     {
#         "name": "shoonya",
#         "id": 1,
#         "params": {
#             "username": "",
#             "password": "",
#             "app_key": "",
#             "otp_token":"",
#             "imei": "",
#             # "totp":"",
#
#         },
#         "active": 0,
#         "inputs": {},
#         "count": 0
#     },
#     {
#         "name": "upstox",
#         "id": 0,
#         "params": {
#             "client_id": "",
#             "client_secret": "",
#             "redirect_url": ""
#         },
#         "active": 0,
#         "inputs": {
#             "auth_code":""
#         },
#         "count": 0
#     },
#     {
#         "name": "zerodha-enc",
#         "id": 0,
#         "params": {
#         },
#         "active": 0,
#         "inputs": {
#             "Enc Token": ""
#         },
#         "count": 0
#     },
#     {
#         "name": "zerodha",
#         "id": 0,
#         "params": {
#             "api_key": "",
#             "api_secret": ""
#         },
#         "active": 0,
#         "inputs": {
#             "Token": ""
#         },
#         "count": 0
#     },
#     {
#         "name": "iifl",
#         "id": 0,
#         "params": {
#             "Interactive_api_key": "",
#             "Interactive_api_secret": "",
#             "Market_api_key":"",
#             "Market_api_secret":""
#         },
#         "active": 0,
#         "count": 0
#     }
# ]
#
# loggedin = []
# # with open("config.txt",'w') as f:
# #         f.write(str(exchangess))
#
# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS2
#     except Exception:
#         base_path = os.path.abspath(".")
#
#     return os.path.join(base_path, relative_path)
#
# def display_terms_and_conditions():
#     # Create a new window for displaying terms and conditions
#     popup = tk.Toplevel()
#     popup.title("Terms and Conditions")
#     popup.iconphoto(False,icon_img)
#     # Add a scrolled text widget to display the terms
#     text_area = scrolledtext.ScrolledText(popup, width=80, height=30, wrap=tk.WORD)
#     text_area.pack(expand=True, fill=tk.BOTH)
#
#     # Insert your terms and conditions text into the scrolled text widget
#     terms_and_conditions = """
#     Terms and Conditions
#     ---------------------
#     This agreement ("Agreement") is entered into between [Aseem Singhal] ("Instructor" or "We") and yourself ("Student" or "You") in connection to your usage of this tool (TVTool). By using this tool, you acknowledge and agree to be bound by the terms and conditions of this Agreement.
#
#     • Use of Trading View Tool (TVTool): The TVTool is not intended as a recommendation or endorsement of any specific trading strategies or techniques. You agree to use the TVTool solely for educational purposes and understand that the Instructor does not provide a tip-providing service.
#
#     • Responsibility: You acknowledge and agree that all decisions made and actions taken regarding your trading activities are solely your responsibility. We do not assume any responsibility for any profits or losses generated through the use of our trading tools (TVTool).
#
#     • Tool Usage: You agree not to attempt to reverse engineer, modify, or share the code provided with others. The trading tool is for your personal use only and should not be distributed or repurposed without our explicit consent.
#
#     • Functionality: You understand that the trading tool's (TVTool’s) performance may be affected by various factors, including but not limited to internet connectivity, hardware limitations (such as a slow laptop), errors within trading platforms (e.g., TradingView), issues with brokers, API malfunctions, and other technical glitches. We do not guarantee uninterrupted or error-free operation of the trading tool and are not liable for any issues arising from such factors.
#
#     • Indemnification: By using this tool, you acknowledge and agree to indemnify and hold the Instructor harmless against any and all claims, damages, losses, liabilities, costs, and expenses (including attorney's fees) incurred by the Instructor arising out of or in connection with:
#         - Any losses incurred by you in trading activities, whether or not influenced by this TVTool;
#         - Any losses resulting from technology errors, including but not limited to technical glitches, system failures, failure of Python codes, failure of TVTool, or other technical issues;
#         - The non-refundable nature of the TVTool fee and the understanding that no refunds will be provided after the usage of the tool commencement; and
#         - The understanding that any backtested strategy results presented during the Course do not guarantee future profits or outcomes.
#
#     • No Financial Guarantee: The Instructor makes no representations or warranties regarding the profitability or success of any trading strategies or techniques discussed. You understand and acknowledge that trading activities involve inherent risks, and any decisions or actions taken based on the Course content are at your own discretion and risk.
#
#     • Market Risks: You understand and acknowledge that option trading and automatic API trading are subject to market risks. The Instructor shall not be held liable for any losses incurred due to market volatility, fluctuations, or any other market-related factors.
#
#     • Intellectual Property: All Course materials, including but not limited to text, graphics, videos, and code, are the intellectual property of the Instructor and protected by applicable copyright laws. You agree not to reproduce, distribute, or share any Course materials without prior written permission from the Instructor.
#
#     • Governing Law and Jurisdiction: This Agreement shall be governed by and construed in accordance with the laws of India. Any disputes arising out of or in connection with this Agreement shall be subject to the exclusive jurisdiction of the courts located in New Delhi, India.
#
#     • Disclosure: I am not a SEBI registered Advisor, and I do not possess any Research Analyst or Investment Advisor license. By enrolling in this course, you acknowledge and agree that you are undertaking the course at your own responsibility. You understand that any information or guidance provided during the course is for educational purposes only and should not be construed as financial advice or recommendations for investment decisions. You are solely responsible for any actions you take based on the knowledge and skills acquired through the course.
#
#     By using this TVTool, you acknowledge that you have read and understood the terms and conditions of this Agreement. You agree to comply with all the obligations and responsibilities outlined herein.
#
#     IF YOU DO NOT AGREE TO ABOVE, YOU SHOULD NOT LOGIN TO THE TOOL.
#     """
#
#     text_area.insert(tk.END, terms_and_conditions)
#
#     # Disable editing in the text widget
#     text_area.configure(state='disabled')
#
#     # Run the popup window
#     popup.mainloop()
#
#
# def create_side_frame(root):
#     getExchanges()
#     global tradingViewCreds
#     try:
#         with open(resource_path("trading_view_creds.txt"),'r') as f:
#             tradingViewCreds = ast.literal_eval(f.read())
#     except:
#         print("Enter trading view Credentials creds.")
#     frame = ttk.Frame(root,height=root.winfo_screenheight()-100,width=root.winfo_screenwidth()/3-30)
#
#     side_top_frame = create_side_top_frame(frame,(root.winfo_screenheight()-100)*0.30, root.winfo_screenwidth()/3-30-20)
#     side_top_frame.grid(column=0, row=0, rowspan=1, columnspan=1)
#     # create_side_main_frame(frame,(root.winfo_screenheight()-100)*0.75, root.winfo_screenwidth()/3-30-20)
#     create_broker_frame(frame,(root.winfo_screenheight()-100)*0.75, root.winfo_screenwidth()/3-30-20)
#     for widget in frame.winfo_children():
#         widget.grid(padx=5, pady=5)
#     frame.grid_propagate(False)
#     frame.grid(column=0, row=0,padx=10,pady=10, sticky='N')
#     # return frame
#
# # def toggle_button():
#     # Toggle the state of the button
#     # if paper_trading:
#     #     paper_trading_btn.config(text="Toggle Off")
#     # else:
#     #     paper_trading_btn.config(text="Toggle On")
#     # paper_trading.set(not paper_trading.get())
# def create_side_top_frame(root,height,width):
#     global paper_trading_btn
#     global paper_trading
#     frame = ttk.Frame(root,height=height,width=width,padding=10)
#
#     ttk.Label(frame, text='Trading View Details',font=('Helvetica', 18) ).grid(column=0, row=0, sticky=tk.W, columnspan=2,rowspan=1)
#     # keyword = ttk.Entry(frame, width=30)
#     # keyword.focus()
#     # keyword.grid(column=1, row=0, sticky=tk.W)
#
#     # Replace with:
#
#     # paper_trading = True
#     ttk.Label(frame, text='Gmail Id: ').grid(column=0, row=1, sticky=tk.W)
#     gmailid = ttk.Entry(frame)
#     gmailid.insert(0,tradingViewCreds[0]['email'])
#     gmailid.grid(column=1, row=1, sticky=tk.W)
#     ttk.Label(frame, text='Password: ').grid(column=0, row=2, sticky=tk.W)
#     password = ttk.Entry(frame, show='*')
#     password.insert(0,tradingViewCreds[0]['password'])
#     password.grid(column=1, row=2, sticky=tk.W)
#     paper_trading_btn = ttk.Checkbutton(frame, text="Paper trading ?", variable=paper_trading)
#     paper_trading_btn.grid(row=3,column= 0)
#     start_alerts_btn = ttk.Button(frame, text='Start Bridge',command=lambda: start_tv_alerts(root,gmailid.get(),password.get()))
#     start_alerts_btn.grid(column=2, row=1)
#     stop_alerts_btn = ttk.Button(frame, text='Stop Bridge',state='disabled',command=stop_alerts)
#     if(alerts_status):
#         stop_alerts_btn['state'] = 'normal'
#         start_alerts_btn['state'] = 'disabled'
#         paper_trading_btn['state'] = 'disabled'
#     stop_alerts_btn.grid(column=2, row=2)
#     for widget in frame.winfo_children():
#         widget.grid(padx=5, pady=5)
#     frame.grid_propagate(False)
#     return frame
#
# alerts=[]
# with open(resource_path('alerts.txt'),'r') as f:
#     alerts = ast.literal_eval(f.read())
# orders=[]
# with open(resource_path('orders.txt'),'r') as f:
#     orders = ast.literal_eval(f.read())
# alertProcess  = None
# alerts_status = 0
#
# def stop_alerts():
#     global alerts_status
#     try:
#         if alertProcess.is_alive() :
#             alertProcess.terminate()
#             print("Stopping alerts...")
#             alerts_status=0
#             create_side_frame(root)
#             messagebox.showinfo("TVTool Bridge","Bridge stopped successfully")
#             print("Alerts Stopped !")
#         else:
#             print("Stopping alerts...")
#             alerts_status=0
#             create_side_frame(root)
#             print("Alerts Stopped !")
#
#     except:
#         alerts_status=0
#         create_side_frame(root)
# def start_tv_alerts(root,username,password):
#     print(username)
#     global alertProcess,alerts_status
#     global orders
#     global alerts
#     tradingViewCreds[0]['email'] = username
#     tradingViewCreds[0]['password'] = password
#     with open(resource_path("trading_view_creds.txt"),'w') as f:
#         f.write(str(tradingViewCreds))
#     try:
#         alertProcess = Process(target=getNotification.login_and_get_tv_alerts,args=(username,password,alerts,orders,paper_trading.get()))
#         alertProcess.start()
#
#         alerts_status=1
#         create_side_frame(root)
#     except:
#         print("Error starting Trading view alerts. Use correct credentials.")
#     messagebox.showinfo("Starting Bridge", "Please wait for 20 secs after pressing OK.")
#     time.sleep(20)
#     if not alertProcess.is_alive():
#         messagebox.showerror("Login Error","Trading view Login Error")
#     else:
#         messagebox.showinfo("Success", "Bridge Started successfully.")
#     print(alertProcess)
#
#
# def create_broker_frame(root,height,width):
#     getExchanges()
#     frame = ttk.Frame(root,height=height,width=width)
#
#     ttk.Label(frame, text='Brokers',font=('Helvetica', 18)).grid(column=0, row=0, sticky='w')
#     row_index=1
#     for exchange in exchanges:
#         if exchange['id'] > 0:
#             exc_frame = ttk.Frame(frame,height=40,width=width,padding='5 0')
#             exc_frame.grid_propagate(False)
#             exc_frame.grid(row=row_index,column=0,sticky='w',ipadx=5)
#
#             row_index += 1
#             if exchange['id'] == 1:
#                 ttk.Label(exc_frame,text=exchange['name'].capitalize(),font=('Helvetica', 12),width=10).grid(row=0,column=0)
#             else:
#                 ttk.Label(exc_frame,text=exchange['name'].capitalize()+" "+str(exchange['id']),width=10,font=('Helvetica', 12)).grid(row=0,column=0)
#             keys_missing = False
#             # print(warning_img)
#             # ttk.Photo
#             for x in exchange['params']:
#                 # print(exchange['params'][x])
#                 if exchange['params'][x] == "":
#                     # print('True')
#                     keys_missing = True
#             if(keys_missing):
#                 ttk.Button(exc_frame,text='View Keys', image=warning_img, compound="right",command=lambda ex=exchange['name'], id=exchange['id']: view_keys_window(ex,id)).grid(row=0,column=1)
#                 # ttk.Button(exc_frame,text='Update Keys',command=lambda ex=exchange['name'], id=exchange['id']: update_broker_window(ex,id)).grid(row=0,column=2,padx=5)
#                 ttk.Button(exc_frame,text='Login',state='disabled').grid(row=0,column=2,padx=5)
#
#                 # ttk.Checkbutton(exc_frame, text='Use', command=lambda broker=exchange['name'], id=exchange['id']: toggle_broker(broker,id)).grid(row=0,column=4)
#             else:
#                 ttk.Button(exc_frame,text='View Keys',command=lambda ex=exchange['name'], id=exchange['id']: view_keys_window(ex,id)).grid(row=0,column=1)
#                 # ttk.Button(exc_frame,text='Update Keys',command=lambda ex=exchange['name'], id=exchange['id']: update_broker_window(ex,id)).grid(row=0,column=2,padx=5)
#                 ttk.Button(exc_frame,text='Login', command=lambda root = root,broker=exchange: broker_login(broker)).grid(row=0,column=3,padx=5)
#                 # tk.PhotoImage(file='assets/light-png-42433.png')
#                 # ttk.Checkbutton(exc_frame, text='Use', command=lambda broker=exchange['name'], id=exchange['id']: toggle_broker(broker,id)).grid(row=0,column=4)
#                 try:
#                     if exchange['timestamp'] == str(datetime.now().date()):
#                         ttk.Label(exc_frame,image=green_indicator_img).grid(row=0,column=4,padx=5)
#                     else:
#                         ttk.Label(exc_frame,image=red_indicator_img).grid(row=0,column=4,padx=5)
#                 except:
#                     ttk.Label(exc_frame,image=red_indicator_img).grid(row=0,column=4,padx=5)
#             # for widget in exc_frame.winfo_children():
#             #     widget.grid( pady=1)
#     add_frame = ttk.Frame(frame)
#     add_frame.grid(row=row_index,column=0,sticky='w',ipadx=5)
#     for widget in frame.winfo_children():
#         widget.grid(padx=10, pady=0)
#     ttk.Button(add_frame,text="Add Broker",width=15,command=add_broker_window).grid(row=0,column=0)
#     frame.grid(column=2, row=0, padx=10,sticky='N')
#     frame.grid_propagate(False)
#     frame.grid(column=0, row=1, rowspan=4, columnspan=1)
#
#     # return frame
#
# # def toggle_broker(broker,id):
# #     global exchanges
# #     # print(use_var.get())
# #     for i in range(len(exchanges)):
# #         if exchanges[i]['name'] == broker and exchanges[i]['id'] == id:
# #             if exchanges[i]['active'] ==1:
# #                 exchanges[i]['active'] = 0
# #             else:
# #                 exchanges[i]['active'] = 1
# #             # exchanges[i]['active'] = int(use_var.get())
# #             print(exchanges[i])
# #
# #     updateExchanges()
# #     return
# def broker_login(broker):
#     login.Login(broker)
#     create_side_frame(root)
#
# def update_broker_window(broker,id):
#     global exchanges
#     new_keys = UpdateKeysWindow(root,broker,id)
#     new_keys.wait_window(new_keys)
#     print(new_keys.attrs)
#     if(new_keys.attrs == None):
#         return
#     for i in range(len(exchanges)):
#         if exchanges[i]['name'] == broker and exchanges[i]['id'] == id:
#             exchanges[i]['params'] = new_keys.attrs
#     # print(exchanges)
#     print("---")
#     with open(resource_path("config.txt"),'w') as f:
#         f.write(str(exchanges))
#     getExchanges()
#     updateExchanges()
#     create_side_frame(root)
#     return
#     # create_broker_frame(root,(root.winfo_screenheight()-100)*0.75, root.winfo_screenwidth()/3-30-20)
# def add_broker_window():
#     global exchanges
#     getExchanges()
#     broker_window = BrokerWindow(root)
#     broker_window.wait_window(broker_window)
#     print("Result:", broker_window.result)
#     if(broker_window.result != None):
#         keys_window = AddKeysWindow(root,broker_window.result)
#         keys_window.wait_window(keys_window)
#         if(keys_window.attrs == None):
#             return
#         # else:
#         print(keys_window.attrs)
#         for x in exchanges:
#             if x['name'] == broker_window.result:
#                 c = x['count'] +1
#                 new_x = {
#                     'id': x['count']+1,
#                     'name' : x['name'],
#                     "params": keys_window.attrs,
#                     "active": 0,
#                     "count" : c
#                 }
#                 print(c)
#                 for rem_x in exchanges:
#                     if rem_x['name'] == broker_window.result:
#                         rem_x['count'] = c
#
#                 if('inputs' in x.keys()):
#                     new_x['inputs'] = x['inputs']
#                 exchanges.append(new_x)
#                 print("Added")
#                 # print(exchanges)
#                 updateExchanges()
#                 # print(exchanges)
#                 # create_broker_frame(root,(root.winfo_screenheight()-100)*0.75, root.winfo_screenwidth()/3-30-20)
#                 create_side_frame(root)
#                 return
#         for x in exchangess:
#             if x['name'] == broker_window.result:
#                 print(x)
#                 if x['count'] == 0:
#                     x['id'] = 1
#                     x['count'] = 1
#                     x['params'] = keys_window.attrs
#                     exchanges.append(x)
#                     # break
#                 # else:
#
#                 break
#         # print(exchanges)
#         updateExchanges()
#         # print(exchanges)
#         # create_broker_frame(root,(root.winfo_screenheight()-100)*0.75, root.winfo_screenwidth()/3-30-20)
#         create_side_frame(root)
#         return
#
# def view_keys_window(broker,id):
#     view_key_window = ViewKeysWindow(root,broker,id)
#     view_key_window.wait_window(view_key_window)
#     if(view_key_window.update == 1):
#         # print("update kro")
#         update_broker_window(broker,id)
#     return
#
# # def create_main_frame(root):
# #     frame = ttk.Frame(root)
# #     broker_frame = create_broker_frame(frame)
# #     broker_frame.grid(row=0,column=0)
# #
# #     for widget in frame.winfo_children():
# #         widget.grid(padx=5, pady=5)
# #     return frame
#
#
# def get_orders_list():
#     create_orders_frame(root)
#
# # def get_alerts_list():
# #     create_alert_frame(root)
#
# # def clear_alerts_list():
# #     global alerts
# #     alerts=[]
# #     with open(resource_path('alerts.txt'),'w') as f:
# #         f.write(str(alerts))
# #     create_alert_frame(root)
#
# def clear_orders_list():
#     global orders
#     orders=[]
#     with open(resource_path('orders.txt'),'w') as f:
#         f.write(str(orders))
#     create_orders_frame(root)
#
# def save_alerts_list():
#     global alerts
#     with open(resource_path('alerts.txt'),'r') as f:
#         alerts = ast.literal_eval(f.read())
#     alerts_df = pd.DataFrame(alerts)
#     dt = datetime.now()
#     _file_name = f'Alerts_{str(dt.day)+"_"+str(dt.month)+"_"+str(dt.year)+"_"+str(dt.hour)+"_"+str(dt.minute)+"_"+str(dt.second)}.csv'
#     _path = asksaveasfile(confirmoverwrite=True,defaultextension='.csv',filetypes=[("Comma Seperated Values", "*.csv")],title="Choose File Path",initialfile=_file_name)
#
#     alerts_df.to_csv(_path)
#
# def save_orders_list():
#     global orders
#     with open(resource_path('orders.txt'),'r') as f:
#         orders = ast.literal_eval(f.read())
#     orders_df = pd.DataFrame(orders)
#     dt = datetime.now()
#     _file_name = f'Orders_{str(dt.day)+"_"+str(dt.month)+"_"+str(dt.year)+"_"+str(dt.hour)+"_"+str(dt.minute)+"_"+str(dt.second)}.csv'
#     _path = asksaveasfile(confirmoverwrite=True,defaultextension='.csv',filetypes=[("CSV", "*.csv")],title="Choose File Path",initialfile=_file_name)
#     orders_df.to_csv(_path)
#
# # def create_alert_frame(root_):
# #     global alerts
# #     with open(resource_path('alerts.txt'),'r') as f:
# #         alerts = ast.literal_eval(f.read())
# #
# #     frame = ttk.Frame(root_,height=root_.winfo_screenheight()-100,width=root_.winfo_screenwidth()/3-30)
# #     ttk.Label(frame, text='Alerts',font=('Helvetica', 18)).grid(column=0, row=0, sticky='w')
# #
# #     add_frame = ttk.Frame(frame)
# #     add_frame.grid(row=1,column=0,sticky='w',ipadx=5)
# #     for widget in frame.winfo_children():
# #         widget.grid(padx=10, pady=5)
# #     ttk.Button(add_frame,text="Refresh",command=lambda:get_alerts_list()).grid(row=0,column=0)
# #     ttk.Button(add_frame,text="Clear All",command=lambda:clear_alerts_list()).grid(row=0,column=1,padx=5)
# #     ttk.Button(add_frame,text="Export to CSV",command=lambda:save_alerts_list()).grid(row=0,column=2)
# #     AlertScrollFrame(frame,alerts)
# #
# #     frame.grid(column=1, row=0, padx=10, pady=10, sticky='N')
# #     frame.grid_propagate(False)
# #     # root.after(1000,lambda root = root_:create_alert_frame(root))
# # def create_orders_frame(root):
# #     # frame = ttk.Frame(root,height=root.winfo_screenheight()-100,width=root.winfo_screenwidth()/3-30,padding=10)
# #     global orders
# #     with open(resource_path('orders.txt'),'r') as f:
# #         orders = ast.literal_eval(f.read())
# #     frame = ttk.Frame(root,height=root.winfo_screenheight()-100,width=root.winfo_screenwidth()/3-30)
# #     ttk.Label(frame, text='Orders',font=('Helvetica', 18)).grid(column=0, row=0, sticky='w')
# #     add_frame = ttk.Frame(frame)
# #     add_frame.grid(row=1,column=0,sticky='w',ipadx=5)
# #     for widget in frame.winfo_children():
# #         widget.grid(padx=10, pady=5)
# #     ttk.Button(add_frame,text="Refresh",command=lambda:get_orders_list()).grid(row=0,column=0)
# #     ttk.Button(add_frame,text="Clear All",command=lambda:clear_orders_list()).grid(row=0,column=1,padx=5)
# #     ttk.Button(add_frame,text="Export to CSV",command=lambda:save_orders_list()).grid(row=0,column=2)
# #     OrdersScrollFrame(frame,orders)
# #
# #     frame.grid(column=2, row=0, padx=10, pady=10, sticky='N')
# #     frame.grid_propagate(False)
# #     return frame
# # # warningimg = Image.open('assets/warning.png')
# # # print(warningimg)
#
# def updateExchanges():
#     global exchanges
#     with open(resource_path("config.txt"),'w') as f:
#         f.write(str(exchanges))
#     getExchanges()
#
# # def updateAlerts():
# #     global alerts
#
# def getExchanges():
#     global exchanges
#     with open(resource_path('config.txt'),'r') as f:
#         exchanges = ast.literal_eval(f.read())
#
# def seedExchanges():
#     with open(resource_path("config.txt"),'w') as f:
#         f.write(str(exchangess))
#
# def logout():
#     global _id
#     active_session_fetch_url = api+"/"+database_name+'/'+sessions_collection_name+'/?query={"username":"'+username+'"}'
#     userdetails  = requests.get(active_session_fetch_url)
#     if userdetails.status_code == 200:
#         print(userdetails.json())
#         _id = userdetails.json()[0]['_id']
#     else:
#         print('Failed to fetch data. Status code:', userdetails.status_code)
#     if len(userdetails.json())>0:
#         # sessions_collection.delete_one({"username": username})
#         session_del = requests.delete(api+"/"+database_name+'/'+sessions_collection_name+'/'+_id)
#         print(api+"/"+database_name+'/'+sessions_collection_name+'/'+_id)
#         print(session_del.status_code)
#         if session_del.status_code == 200 and  len(session_del.json())>0:
#             print(session_del.json())
#             login_doc = {
#                 "username": username,
#                 "time": str(datetime.now()),
#                 "system_id": get_system_id(),
#                 "login/logout": "Logout"
#             }
#             # Insert session document into MongoDB
#             logs_res = requests.post(str(api+'/'+database_name+'/'+login_logs_collection_name),json={"data":login_doc})
#             # login_logs_collection.insert_one(login_doc)
#             return True, "Logout successful"
#         else:
#             return False, "User not logged out. Network error."
#     else:
#         return False, "User not logged in"
# def on_closing():
#     # global username
#     if messagebox.askokcancel("Quit", "Do you want to logout and exit?"):
#         stop_alerts()
#         success, message = logout()
#         if success:
#
#             messagebox.showinfo("Logout", message)
#             root.destroy()
#             sys.exit()
#         else:
#             messagebox.showerror("Logout Error", message)
#
# def on_closing_login():
#     # global username
#     if messagebox.askokcancel("Quit", "Do you want to exit?"):
#         root1.destroy()
#         # sys.quit()
#         sys.exit()
#
# # def main():
# #     global warning_img
# #     global red_indicator_img
# #     global green_indicator_img
# #     global exchanges
# #     global root
# #     # root.configure(bg='#000')
# #
#
# def tnc_tvauto():
#     webbrowser.open("https://drive.google.com/file/d/1JwjcQztRJVzIAMoGi0-XoMx3ojSDVzA8/view?usp=sharing")
#
# def login_tvauto():
#     # print("test")
#     # return
#     global sessions_collection
#     global login_logs_collection
#     global username
#     print(tnc_var.get())
#     if not tnc_var.get():
#         messagebox.showerror("Login Error", f"Please agree terms and conditions to continue login.")
#         return
#     username = username_entry.get()
#     password = password_entry.get()
#     print(username,password)
#     # if(username.split('_')[0] == 'INSERTNEWUSER'):
#     #     new_user = {
#     #         "username": username.split('_')[1],
#     #         "password":
#     #     }
#
#     # config = configparser.ConfigParser()
#     # config.read(resource_path('mongo_config.ini'))
#     # Get MongoDB credentials from config file
#     # mongodb_uri = 'mongodb+srv://admin:3RTFzhRSz989070u@tvtool.k8yv10o.mongodb.net/'
#
#
#
#     # Connect to MongoDB
#     # client = MongoClient(mongodb_uri)
#     # db = client[database_name]
#     # collection = db[users_collection_name]
#     # sessions_collection = db[sessions_collection_name]
#     # login_logs_collection = db[login_logs_collection_name]
#     # roundoff_collection = db[roundoff_collection_name]
#     # roundoff_data = roundoff_collection.find({}, {"_id": 0})
#     # # print(roundoff_data)
#     # roundoffdf = pd.DataFrame(list(roundoff_data))
#     # roundoffdf.to_csv('optionstrike_data.csv')
#     active_session_fetch_url = api+"/"+database_name+'/'+sessions_collection_name+'/?query={"username":"'+username+'"}'
#     # print(user_fetch_url)
#
#     userdetails  = requests.get(active_session_fetch_url)
#     if userdetails.status_code == 200:
#         # print('GET request was successful!')
#         # print('Response JSON:')
#         print(userdetails.json())
#     else:
#         print('Failed to fetch data. Status code:', userdetails.status_code)
#     if len(userdetails.json())>0:
#         active_id_session_fetch_url = api+"/"+database_name+'/'+sessions_collection_name+'/?query={"username":"'+username+'","system_id":"'+get_system_id()+'"}'
#         session_res = requests.get(active_id_session_fetch_url)
#         if session_res.status_code == 200:
#             session = session_res.json()[0]
#             _id = session['_id']
#             print(_id)
#         else:
#             session = False
#         # if sessions_collection.find_one({"user_id":username,"system_id":get_system_id()}) and tnc_var.get():
#         if session and tnc_var.get():
#             messagebox.showinfo("Login Successful", f"Welcome, {username}!")
#             root.deiconify()
#             root.state('zoomed')
#             root1.destroy()
#             return
#         else:
#             messagebox.showerror("Login Error", f"User, {username} already logged in another system!")
#             return False
#         # return False, "User already logged in from another location"
#     # Check if username and password are correct
#     dt = datetime.now()
#     # collection.insert_one({"username": username, "password": password,"valid_till":datetime(2024, 5, 30, 12, 30, 0)})
#     # user = collection.find_one({"username": username, "password": password,"valid_till":{'$gte':dt}})
#     user_auth = api+"/"+database_name+'/'+users_collection_name+'/?query='+'{"username":"'+username+'","password":"'+password+'"}'
#     print(user_auth)
#     auth_res = requests.get(user_auth)
#     if auth_res.status_code == 200:
#         # print('GET request was successful!')
#         # print('Response JSON:')
#         print(auth_res.json())
#         user = auth_res.json()
#         if len(user)>0:
#             valid_date = datetime.fromisoformat(user[0]['valid_till'])
#             print(valid_date)
#         if len(user)>0 and tnc_var.get() and valid_date >= dt:
#             messagebox.showinfo("Login Successful", f"Welcome, {username}!")
#             session_doc = {
#                 "username": username,
#                 "start_time": str(datetime.now()),
#                 "system_id": get_system_id()
#             }
#             login_doc = {
#                 "username": username,
#                 "time": str(datetime.now()),
#                 "system_id": get_system_id(),
#                 "login/logout": "Login"
#             }
#             # Insert session document into MongoDB
#             logs_res = requests.post(str(api+'/'+database_name+'/'+login_logs_collection_name),json={"data":login_doc})
#             session_res = requests.post(str(api+'/'+database_name+'/'+sessions_collection_name),json={"data":session_doc})
#
#             if session_res.status_code == 200:
#
#                 print(session_res.json())
#                 _id = session_res.json()[0]['_id']
#                 print(_id)
#             else:
#                 print('Failed to post session data. Status code:', session_res.status_code)
#             # login_logs_collection.insert_one(login_doc)
#             # sessions_collection.insert_one(session_doc)
#             root.deiconify()
#             root.state('zoomed')
#             root1.destroy()
#             # main()
#         else:
#             messagebox.showerror("Login Failed", "Invalid Username or Password")
#     else:
#         messagebox.showerror("Network Error", "Failed to Fetch Data")
#         print('Failed to fetch data. Status code:', auth_res.status_code)
#
#
#
# if __name__ == "__main__":
#     multiprocessing.freeze_support()
#     # login_gui.main()
#     # main()
#     api = 'http://ec2-65-0-85-93.ap-south-1.compute.amazonaws.com'
#     database_name = 'TVTool'
#     users_collection_name = 'users'
#     sessions_collection_name = 'Active_Sessions'
#     roundoff_collection_name = 'Roundoff_data'
#     login_logs_collection_name = 'User_Login_Logs'
#     _id='0'
#     root = tk.Tk()
#     root.title("TVTool by Unfluke")
#     root.state('zoomed')
#     root.geometry("")
#     root.protocol("WM_DELETE_WINDOW", on_closing)
#
#     warning_img = ImageTk.PhotoImage(Image.open(resource_path('assets/warning_18.png')))
#     red_indicator_img = ImageTk.PhotoImage(Image.open(resource_path('assets/light-png-42433-small.png')))
#     green_indicator_img = ImageTk.PhotoImage(file=resource_path('assets/light-png-42432-small.png'))
#     icon_img = ImageTk.PhotoImage(file=resource_path("assets/icon.png"))
#     exchanges=[]
#     # use_var = tk.StringVar(value='0')
#     getExchanges()
#     paper_trading = tk.BooleanVar(value=False)
#     tnc_var = tk.BooleanVar(value=False)
#     create_side_frame(root)
#     # create_alert_frame(root)
#     # create_orders_frame(root)
#     # for widget in root.winfo_children():
#     #     widget.configure()
#
#     # def login_guii():
#     #     global username
#     #     global password
#     root1 = tk.Toplevel()
#     root1.title("TVTool by Unfluke")
#     root1.state('zoomed')
#     root1.protocol("WM_DELETE_WINDOW", on_closing_login)
#     frame = tk.Frame(root1)
#     frame.pack(expand=True)
#     ttk.Label(frame,text="TVTool",font=("Helvetica",32)).pack(pady=5)
#     ttk.Label(frame,text="by",font=("Helvetica",13)).pack(pady=0)
#     logo_img = ImageTk.PhotoImage(file=resource_path("assets/UNFLUKE (Custom) (Custom).png"))
#     # Create username label and entry
#     ttk.Label(frame,image=logo_img).pack(pady=0)
#     username_label = ttk.Label(frame, text="Username",font=("Helvetica",13))
#     username_label.pack(pady=5)
#     username_entry = ttk.Entry(frame,width=30)
#     username_entry.pack(pady=10)
#     # Create password label and entry
#     password_label = ttk.Label(frame, text="Password",font=("Helvetica",13))
#     password_label.pack(pady=10)
#     password_entry = ttk.Entry(frame, show="*",width=30)
#     password_entry.pack(pady=5)
#     frametnc = tk.Frame(frame)
#     frametnc.pack(pady=20)
#     tnc_button = ttk.Button(frametnc, text="Terms & Conditions", command=display_terms_and_conditions).pack(side=tk.RIGHT)
#     tnc_cbx = ttk.Checkbutton(frametnc, text="I agree to all the terms and conditions mentioned here and continue.", variable=tnc_var).pack(padx=10,side=tk.LEFT)
#     # Create login button
#     login_button = ttk.Button(frame, text="Login", command= login_tvauto ,width=15)
#     login_button.pack(pady=0)
#
#     vertical_center = (root1.winfo_screenheight() - root1.winfo_reqheight()) // 2
#     # Place the frame at the vertical center
#     frame.place(relx=0.5, rely=0.5, anchor="center")
#
#     root1.iconphoto(False,icon_img)
#     root.iconphoto(False,icon_img)
#     # Run the Tkinter event loop
#     # root1.mainloop()
#     # return root1
#     root.withdraw()
#     root.mainloop()

