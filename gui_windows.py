import tkinter as tk
import tkinter.ttk as ttk
import ast
from PIL import ImageTk, Image
import sys
import os
brokers = []

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

with open(resource_path('config.txt'),'r') as f:
        brokers = ast.literal_eval(f.read())
# print(brokers)
broker_list = [
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
        "count": 1
    },
    {
        "name": "alice",
        "id": 1,
        "params": {
            "username": "",
            "api_key":""
        },
        "active": 0,
        "count": 1
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
    #     "count": 1
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
        "count": 1
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
        "count": 1
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
        "count": 1
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
            "Enc token": ""
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
    },{
        "name": "dhan",
        "id": 0,
        "params": {
            "client_id": "",
        },
        "access_token":"",
        "active": 0,
        "count": 0
    },
]

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
#     "inputs": {},
#     "count": 0
# },
class BrokerWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        icon_img = ImageTk.PhotoImage(file=resource_path("assets/icon.png"))
        self.iconphoto(False,icon_img)
        self.geometry(f'300x200+{int(self.winfo_screenwidth()/2-150)}+{int(self.winfo_screenheight()/2-100)}')
        self.parent = parent
        self.result = None
        self.brokers = [x['name'] for x in broker_list ]
        self.initialize()

    def initialize(self):
        print(self.brokers)
        self.label = tk.ttk.Label(self, text="Select a Broker:",font=("Helvetica, 15"))
        # self.label.grid(row=0,column=0)
        self.label.pack(pady=10)
        self.drop2 = tk.ttk.Combobox(self,state='readonly',values=self.brokers)
        self.drop2.focus()
        self.drop2.set("angel")
        # self.drop2.grid(row=1, column=0)
        self.drop2.pack(pady=5)

        self.button = tk.ttk.Button(self, text="Next", command=self.on_ok)
        # self.button.grid(row=2,column=0)
        self.button.pack(pady=10)

    def on_ok(self):
        self.result = self.drop2.get()
        self.destroy()
        
    # print("Result:", window.result)


class AddKeysWindow(tk.Toplevel):
    def __init__(self, parent,broker):
        tk.Toplevel.__init__(self, parent)
        icon_img = ImageTk.PhotoImage(file=resource_path("assets/icon.png"))
        self.iconphoto(False,icon_img)
        self.geometry(f'500x400+{int(self.winfo_screenwidth()/2-250)}+{int(self.winfo_screenheight()/2-200)}')
        self.parent = parent
        self.result = None
        self.attrs = None
        self.broker = broker
        # with open('config.txt','r') as f:
        #     brokers = ast.literal_eval(f.read())
        brokers = broker_list
        for x in brokers:
            if(x['name']==self.broker):
                self.params = x['params']
        # if len(self.params.keys()) == 0:
        #     self.attrs = {}
        #     self.destroy()
        #     return
        self.initialize()

    def initialize(self):
        print(self.params.keys())
        x_i=1
        if self.broker == "zerodha-enc":
            self.label = tk.ttk.Label(self, text="For Zerodha, use encToken during login process. Click Add to continue.",font=("Helvetica",12))
            self.label.focus()
            self.label.grid(row=0,column=0,pady=10)
        else:
            self.label = tk.ttk.Label(self, text="Enter Details:",font=("Helvetica",15))
            self.label.focus()
            self.label.grid(row=0,column=0,pady=10)

            for x in self.params.keys():
                self.lbl = tk.ttk.Label(self,text=f"{x.capitalize()}:",font=("Helvetica",10),width=15)
                self.lbl.grid(row=x_i,column=0,padx=10,pady=5)
                self.ent = tk.ttk.Entry(self,width=15)
                self.ent.grid(row=x_i,column=1,padx=10,pady=5)
                setattr(self,x,self.ent)
                x_i+=1
                # print(x)
        
        self.button = tk.ttk.Button(self, text="Add", command=self.on_ok)
        self.button.grid(row=x_i,column=0,padx=10,pady=5,sticky='W')


    def on_ok(self):
        self.attrs = {}
        for x in self.params.keys():
            self.attrs[x] = getattr(self, x).get()
            # print(getattr(self, x).get())
        # self.result = self.drop2.get()
        self.destroy()



class UpdateKeysWindow(tk.Toplevel):
    def __init__(self, parent,broker,id):
        tk.Toplevel.__init__(self, parent)
        icon_img = ImageTk.PhotoImage(file=resource_path("assets/icon.png"))
        self.iconphoto(False,icon_img)
        self.geometry(f'500x400+{int(self.winfo_screenwidth()/2-250)}+{int(self.winfo_screenheight()/2-200)}')
        self.parent = parent
        self.result = None
        self.attrs = None
        self.broker = broker
        self.id = id
        with open(resource_path('config.txt'),'r') as f:
            brokers = ast.literal_eval(f.read())
        for x in brokers:
            if(x['name']==self.broker and x['id']==self.id):
                self.params = x['params']
        self.initialize()

    def initialize(self):
        # print(self.params.keys())
        self.label = tk.ttk.Label(self, text="Update Details:",font=("Helvetica",15))
        self.label.focus()
        self.label.grid(row=0,column=0,pady=10)
        x_i=1
        for x in self.params.keys():
            self.lbl = tk.ttk.Label(self,text=f"{x.capitalize()}:",font=("Helvetica",10),width=15)
            self.lbl.grid(row=x_i,column=0,padx=10,pady=5)
            self.ent = tk.ttk.Entry(self,width=15)
            self.ent.insert(0,self.params[x])
            self.ent.grid(row=x_i,column=1,padx=10,pady=5)
            setattr(self,x,self.ent)
            x_i+=1
            # print(x)

        self.button = tk.ttk.Button(self, text="Update", command=self.on_ok)
        self.button.grid(row=x_i,column=0,padx=10,pady=5,sticky='W')


    def on_ok(self):
        self.attrs = {}
        for x in self.params.keys():
            self.attrs[x] = getattr(self, x).get()
            # print(getattr(self, x).get())
        # self.result = self.drop2.get()
        self.destroy()

class ViewKeysWindow(tk.Toplevel):
    def __init__(self, parent,brokername,id):
        tk.Toplevel.__init__(self, parent)

        icon_img = ImageTk.PhotoImage(file=resource_path("assets/icon.png"))
        self.iconphoto(False,icon_img)
        # self.geometry(f'400x400+{int(self.winfo_screenwidth()/2-200)}+{int(self.winfo_screenheight()/2-200)}')
        self.parent = parent
        self.id = id
        self.brokername = brokername
        self.update = 0
        with open(resource_path('config.txt'),'r') as f:
            brokers = ast.literal_eval(f.read())
        # print(brokers)
        for x in brokers:
            if(x['name']==self.brokername and x['id']==self.id):
                self.params = x['params']
                self.broker = x
        self.initialize()

    def initialize(self):
        # print(self.params.keys())
        self.label = tk.ttk.Label(self, text="Broker Details",font=("Helvetica",15))
        self.label.focus()
        self.label.grid(row=0,column=0,pady=10)
        x_i=1
        for x in self.params.keys():
            self.lbl = tk.ttk.Label(self,text=f"{x.capitalize()}:",font=("Helvetica",10),width=15)
            self.lbl.grid(row=x_i,column=0,padx=10,pady=5)
            self.ent = tk.ttk.Label(self,text=self.broker['params'][x])
            self.ent.grid(row=x_i,column=1,padx=10,pady=5)
            x_i+=1
        
        self.button = tk.ttk.Button(self, text="Ok", command=self.on_ok)
        self.button.grid(row=x_i,column=0,padx=10,pady=5,sticky='W')
        self.button = tk.ttk.Button(self, text="Update", command=self.on_update)
        self.button.grid(row=x_i,column=1,padx=10,pady=5,sticky='E')


    def on_ok(self):
        self.destroy()
    def on_update(self):
        self.update = 1
        self.destroy()




class BrokerLoginChildWindow(tk.Toplevel):
    def __init__(self, parent,broker):
        tk.Toplevel.__init__(self, parent)
        icon_img = ImageTk.PhotoImage(file=resource_path("assets/icon.png"))
        self.iconphoto(False,icon_img)
        self.geometry(f'300x200+{int(self.winfo_screenwidth()/2-150)}+{int(self.winfo_screenheight()/2-100)}')
        self.parent = parent
        icon_img = ImageTk.PhotoImage(file=resource_path("assets/icon.png"))
        self.iconphoto(False,icon_img)
        self.result = None
        self.broker = broker
        self.initialize()

    def initialize(self):
        # print(self.broker)
        self.label = tk.ttk.Label(self, text=f"Enter :{self.broker['inputs']}",font=("Helvetica, 15"))
        # self.label.grid(row=0,column=0)
        self.label.pack(pady=10)
        self.ent = tk.ttk.Entry(self,width=20)
        self.ent.focus()
        # self.drop2.grid(row=1, column=0)
        self.ent.pack(pady=5)

        self.button = tk.ttk.Button(self, text="Next", command=self.on_ok)
        self.button.pack(pady=10)
        self.button2 = tk.ttk.Button(self, text="Cancel", command=self.on_cancel)
        self.button2.pack(pady=10)
        # self.button.grid(row=2,column=0)

    def on_ok(self):
        self.result = self.ent.get()
        if self.result != "":
            self.destroy()
        self.messagebox.showerror('Error','Please enter a value!')
    def on_cancel(self):
        self.result = None
        self.destroy()


class AlertScrollFrame:
    def __init__(self,root,alerts):
        self.AlertFrame = tk.Frame(root, bg="#EBEBEB")
        self.AlertFrame.grid()
        # self.AlertFrame.rowconfigure(0, weight=2)
        # self.AlertFrame.columnconfigure(0, weight=1)
        self.alertCanvas = tk.Canvas(self.AlertFrame, bg="#EBEBEB",height=root.winfo_reqheight()-100, width=root.winfo_reqwidth()-20)
        self.alertCanvas.grid(row=0, column=0, sticky="nsew")

        self.canvasFrame = tk.Frame(self.alertCanvas, bg="#EBEBEB")
        self.alertCanvas.create_window(0, 0, window=self.canvasFrame, anchor='nw')
        for i in range(1,len(alerts)+1):
            alert=alerts[len(alerts)-i]
            # print(alert)
            iframe = ttk.Frame(self.canvasFrame,relief='solid',height=80,width=root.winfo_reqwidth()-30,padding=10)
            iframe.grid(row=i,column=0,sticky='w',pady=5)
            iframe.grid_propagate(False)
            ttk.Label(iframe,text="Time: "+alert['time'],font=('Helvetica',10)).grid(row=0,column=0,columnspan=3,sticky='W',pady=5)
            ttk.Label(iframe,text=alert['alertsubject'],font=('Helvetica',12,'bold')).grid(row=1,column=0,columnspan=4)
            # ttk.Label(iframe,text="Direction: "+alert['direction'],font=('Helvetica',10)).grid(row=1,column=0,padx=5)
            # ttk.Label(iframe,text="Broker: "+alert['broker'],font=('Helvetica',10)).grid(row=1,column=1,padx=5)
            # ttk.Label(iframe,text="Price: "+str(alert['price']),font=('Helvetica',10)).grid(row=1,column=2,padx=5)

        self.photoScroll = tk.Scrollbar(self.AlertFrame, orient=tk.VERTICAL)
        self.photoScroll.config(command=self.alertCanvas.yview)
        self.alertCanvas.config(yscrollcommand=self.photoScroll.set)
        self.photoScroll.grid(row=0, column=1, sticky="ns")

        self.canvasFrame.bind("<Configure>", self.update_scrollregion)

    def update_scrollregion(self,event):
        self.alertCanvas.configure(scrollregion=self.alertCanvas.bbox("all"))


class OrdersScrollFrame:
    def __init__(self,root,orders):
        self.OrderFrame = tk.Frame(root, bg="#EBEBEB")
        self.OrderFrame.grid()
        self.OrderCanvas = tk.Canvas(self.OrderFrame, bg="#EBEBEB",height=root.winfo_reqheight()-100,width=root.winfo_reqwidth()-20)
        self.OrderCanvas.grid(row=0, column=0, sticky="nsew")

        self.canvasFrame = tk.Frame(self.OrderCanvas, bg="#EBEBEB")
        self.OrderCanvas.create_window(0, 0, window=self.canvasFrame, anchor='nw')
        for i in range(1,len(orders)+1):
            order=orders[len(orders)-i]
            # print(order)
            iframe = ttk.Frame(self.canvasFrame,relief='solid',height=120,width=root.winfo_reqwidth()-30,padding=10)
            iframe.grid(row=i,column=0,sticky='w',pady=5)
            iframe.grid_propagate(False)
            # ttk.Label(iframe,text="Symbol: "+order['symbol'],font=('Helvetica',10)).grid(row=0,column=0)
            # ttk.Label(iframe,text=order['time'],font=('Helvetica',10)).grid(row=0,column=1)
            # ttk.Label(iframe,text="Direction: "+order['direction'],font=('Helvetica',10)).grid(row=1,column=0)
            # ttk.Label(iframe,text="Price: "+str(order['price']),font=('Helvetica',10)).grid(row=1,column=2)
            # ttk.Label(iframe,text=order['symbol'],font=('Helvetica',10)).grid(row=0,column=1, sticky='W')
            ttk.Label(iframe,text="Time: "+order['time'],font=('Helvetica',10)).grid(row=0,column=0, sticky='W')
            ttk.Label(iframe,text=order['order_symbol'],font=('Helvetica',12,'bold')).grid(row=1,column=0,columnspan=4,sticky='W')
            ttk.Label(iframe,text=order['direction'],font=('Helvetica',10,'bold')).grid(row=2,column=0, sticky='W')
            ttk.Label(iframe,text="Qty: "+str(order['qty']),font=('Helvetica',10,'bold')).grid(row=2,column=1, sticky='W',padx=5)
            ttk.Label(iframe,text=order['broker'],font=('Helvetica',10)).grid(row=2,column=2)
            if(order['order_type'] == 'M'):
                ttk.Label(iframe,text="Market",font=('Helvetica',10)).grid(row=3,column=0,sticky='W')
            elif(order['order_type'] == 'L'):
                ttk.Label(iframe,text="Limit",font=('Helvetica',10)).grid(row=3,column=0,sticky='W')
                ttk.Label(iframe,text=order['price'],font=('Helvetica',10)).grid(row=3,column=1,sticky='W')
            elif(order['order_type']=='SL'):
                ttk.Label(iframe,text="Stoploss Limit",font=('Helvetica',10)).grid(row=3,column=0,sticky='W')
                ttk.Label(iframe,text=order['trigger_price'],font=('Helvetica',10)).grid(row=3,column=1,sticky='W')
            ttk.Label(iframe,text=order['product'],font=('Helvetica',10)).grid(row=3,column=1,sticky='W',padx=5)
            ttk.Label(iframe,text="Order Id:"+str(order['oid']),font=('Helvetica',10)).grid(row=4,column=0,columnspan=6,sticky='W')

        self.photoScroll = tk.Scrollbar(self.OrderFrame, orient=tk.VERTICAL)
        self.photoScroll.config(command=self.OrderCanvas.yview)
        self.OrderCanvas.config(yscrollcommand=self.photoScroll.set)
        self.photoScroll.grid(row=0, column=1, sticky="ns")

        self.canvasFrame.bind("<Configure>", self.update_scrollregion)

    def update_scrollregion(self,event):
        self.OrderCanvas.configure(scrollregion=self.OrderCanvas.bbox("all"))


class BrokersScrollFrame:
    def __init__(self,root,orders):
        self.OrderFrame = tk.Frame(root, bg="#EBEBEB")
        self.OrderFrame.grid()
        self.OrderCanvas = tk.Canvas(self.OrderFrame, bg="#EBEBEB",height=root.winfo_screenheight()-200,width=root.winfo_screenwidth()/3-70)
        self.OrderCanvas.grid(row=0, column=0, sticky="nsew")

        self.canvasFrame = tk.Frame(self.OrderCanvas, bg="#EBEBEB")
        self.OrderCanvas.create_window(0, 0, window=self.canvasFrame, anchor='nw')
        for i in range(1,len(orders)+1):
            order=orders[len(orders)-i]
            print(order)
            iframe = ttk.Frame(self.canvasFrame,relief='solid',height=100,width=root.winfo_screenwidth()/3-80,padding=10)
            iframe.grid(row=i,column=0,sticky='w',pady=5)
            iframe.grid_propagate(False)
            # ttk.Label(iframe,text="Symbol: "+order['symbol'],font=('Helvetica',10)).grid(row=0,column=0)
            # ttk.Label(iframe,text=order['time'],font=('Helvetica',10)).grid(row=0,column=1)
            # ttk.Label(iframe,text="Direction: "+order['direction'],font=('Helvetica',10)).grid(row=1,column=0)
            # ttk.Label(iframe,text="Broker: "+order['broker'],font=('Helvetica',10)).grid(row=1,column=1)
            # ttk.Label(iframe,text="Price: "+str(order['price']),font=('Helvetica',10)).grid(row=1,column=2)
            ttk.Label(iframe,text=order['symbol'],font=('Helvetica',10)).grid(row=0,column=0, sticky='W')
            ttk.Label(iframe,text=order['direction'],font=('Helvetica',10)).grid(row=0,column=1, sticky='W')
            ttk.Label(iframe,text="Qty: "+str(order['qty']),font=('Helvetica',10)).grid(row=0,column=2, sticky='W')
            ttk.Label(iframe,text=order['time'],font=('Helvetica',10)).grid(row=0,column=3, sticky='W')
            ttk.Label(iframe,text=order['order_type'],font=('Helvetica',10)).grid(row=1,column=0,sticky='W')
            ttk.Label(iframe,text=order['product'],font=('Helvetica',10)).grid(row=1,column=1,sticky='W')
            ttk.Label(iframe,text=order['inst'],font=('Helvetica',10)).grid(row=2,column=0,columnspan=3,sticky='W')
            ttk.Label(iframe,text=order['oid'],font=('Helvetica',8)).grid(row=3,column=0,columnspan=4)

        self.photoScroll = tk.Scrollbar(self.OrderFrame, orient=tk.VERTICAL)
        self.photoScroll.config(command=self.OrderCanvas.yview)
        self.OrderCanvas.config(yscrollcommand=self.photoScroll.set)
        self.photoScroll.grid(row=0, column=1, sticky="ns")

        self.canvasFrame.bind("<Configure>", self.update_scrollregion)

    def update_scrollregion(self,event):
        self.OrderCanvas.configure(scrollregion=self.OrderCanvas.bbox("all"))