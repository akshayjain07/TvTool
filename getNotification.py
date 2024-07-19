import ast
import imaplib
import email
import time
import json
import csv
import pandas as pd
from bs4 import BeautifulSoup

import os
# from gui_windows import AlertsWindow
# import orderPlacement
import threading
# alerts = []
import tkinter as tk
from tkinter import ttk
import os
import sys
from flask import Flask

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# root = tk.Tk()
def create_side_main_frame(root, height, width,alerts):
    frame = ttk.Frame(root,relief='flat',width=width, height=height, padding=10)
    # print(height)
    # print(width)
    ttk.Label(frame, text='Alerts Generated',font=('Helvetica', 18) ).grid(column=0, row=0, sticky=tk.W)
    # while True:
    # time.sleep(1)
    for i in range(0,len(alerts)):
        iframe = ttk.Frame(frame,relief='solid',height=60,width=root.winfo_screenwidth()/3-70,padding=10)
        iframe.grid(row=i+1,column=0,sticky='w',pady=5)
        iframe.grid_propagate(False)
        ttk.Label(iframe,text="New Alert Detected",font=('Helvetica',12)).grid(row=0,column=0)
        ttk.Label(iframe,text="12:03:23 30-01-2024",font=('Helvetica',8)).grid(row=1,column=0)
        ttk.Label(iframe,text="Nifty",font=('Helvetica',8)).grid(row=1,column=1)
        ttk.Label(iframe,text="Sell",font=('Helvetica',8)).grid(row=1,column=2)
        ttk.Label(iframe,text="22347.00",font=('Helvetica',8)).grid(row=1,column=3)
    # frame.grid(column=2, row=0, padx=10, pady=10,sticky='N')
    frame.grid_propagate(False)
    frame.grid(column=0, row=1, rowspan=4, columnspan=1)
# create_side_main_frame(root,300,400,[1])
# root.mainloop()
# with open('tv_credentials.json') as creds:
#     data = json.load(creds)
#     username = data['email']
#     password = data['password']
# app = Flask(__name__)
# bridgeStatus = 0
# @app.route("/bridgestatus", methods=["GET"])
# def alertstatus():
#     return str(bridgeStatus)
#
# def startServer():
#     app.run(host='0.0.0.0', port=7000)
#     # global app
# th = threading.Thread(target=startServer)
# th.start()
# th.join()
#     print("Inside startServer()")
def login_and_get_tv_alerts(username,password,alerts,orders,papertrading=True):
    global bridgeStatus
    print(papertrading)
    trades_df = pd.DataFrame(columns=['paper/live','symbol','time','qty',])
    import orderPlacement
    # alerts = []

    currenttime = time.localtime()
    print(currenttime)
    crnttimesec = currenttime.tm_hour*60*60+currenttime.tm_min*60+currenttime.tm_sec
    mail_server = "imap.gmail.com"
    # username = "sahildhillon.8278@gmail.com"

    mail = imaplib.IMAP4_SSL(mail_server,993)
    try:
        mail.login(username, password)
        bridgeStatus = 1
    except:
        # roott = tk.Toplevel()
        # roott.title("TV login error")
        # roott.state('zoomed')
        print("Trading View Login Error.")
        bridgeStatus = 0
        return 0
    index=0
    while True:
        try:
            # login imap
            index = 1

            while True:
                mail.select("inbox")
                date = time.strftime("%d-%b-%Y",currenttime)
                status, response = mail.search(None, "UNSEEN","(FROM 'noreply@tradingview.com')",f"(SINCE {date})")
                if status == "OK":
                    emails = response[0].split()
                    if len(emails) > 0:
                        # print(emails[-1])
                        for num in emails[::-1]:
                            status, data = mail.fetch(num, "(RFC822)")
                            if status == "OK":
                                msg = email.message_from_bytes(data[0][1])
                                # print(msg.get_payload())


                                # quit()
                                emailDate = msg["Date"]
                                msgtime = None
                                try:
                                    msgtime = time.strptime(emailDate, "%a, %d %b %Y %H:%M:%S %z")
                                except ValueError:
                                    emailDate = emailDate.rstrip()
                                    msgtime = time.strptime(emailDate, "%a, %d %b %Y %H:%M:%S %z")
                                # print(msgtime)
                                # print(currenttime)
                                msgtimesec = msgtime.tm_hour*60*60+msgtime.tm_min*60+msgtime.tm_sec
                                if (crnttimesec <= msgtimesec + (5*60*60+30*60) and currenttime.tm_yday == msgtime.tm_yday):
                                    # print(msgtimesec)
                                    # print(msgtimesec + (5*60*60+30*60))
                                    # print(crnttimesec)
                                    print(f"\n\nNew Alert Detected\nDate: {msg['Date']}")
                                    alert_time = time.strftime("%H:%M:%S %d %b %Y",time.localtime())
                                    if(msg['Subject'][0:5] != 'Alert'):
                                        continue
                                    # alertsubject = msg['Subject'].lstrip('Alert: ')
                                    htmlcontent = msg.get_payload(decode=True)
                                    soup = BeautifulSoup(htmlcontent, 'html.parser')
                                    specific_p_tags = soup.find_all('p', style=lambda value: 'font-family: -apple-system, BlinkMacSystemFont, \'Trebuchet MS\', Roboto, Ubuntu, sans-serif;font-size: 18px;line-height: 28px;margin: 0;padding: 0;text-align: center !important;white-space: pre-line;color: #131722;' in value)
                                    for p in specific_p_tags:
                                        print(p.text)
                                        alertsubject = p.text.strip()
                                    alertitems = alertsubject.split()
                                    item_desc = {}
                                    item_desc['alertsubject'] = alertsubject
                                    item_desc['index'] = index
                                    item_desc['Time'] = msg['Date']
                                    if(len(alertitems)<5):
                                        print("Minimum required Alert Parameters missing.")
                                        continue
                                    else:
                                        # Type
                                        if(alertitems[0].upper() in ['E','F','O']):
                                            item_desc['type']=alertitems[0].upper()
                                        else:
                                            print("Invalid Type. Enter E/F/O only.")
                                            continue

                                        # Qty.
                                        try:
                                            item_desc['qty'] = int(alertitems[1])
                                        except ValueError as e:
                                            print("Enter quantity only in integer format.")
                                            continue

                                        # Direction
                                        if(alertitems[2].upper() in ['BUY','SELL']):
                                            item_desc['direction']=alertitems[2].upper()
                                        else:
                                            print("Invalid Direction. Enter Buy/Sell only.")
                                            continue

                                        # Symbol
                                        item_desc['symbol'] = alertitems[3].upper()

                                        # Broker
                                        item_desc['broker'] = alertitems[4].upper().split("_")[0]
                                        try:
                                            item_desc['broker_id'] = alertitems[4].upper().split("_")[1]
                                        except:
                                            item_desc['broker_id'] = "1"
                                        item_desc['order_type'] = 'M'
                                        item_desc['price'] = 0
                                        item_desc['trigger_price'] = 0
                                        item_desc['product'] = 'MIS'
                                        if(len(alertitems)==6):
                                            optionals = alertitems[5].strip('(').strip(')')
                                            optionalItems = optionals.split(',')
                                            if(len(optionalItems)<1):
                                                print("Invalid optional params")
                                                continue
                                            else:

                                                # Order Type
                                                if(optionalItems[0].upper() in ['M','L','SL']):
                                                    item_desc['order_type']=optionalItems[0].upper()
                                                elif(optionalItems[0] == ''):
                                                    item_desc['order_type']='M'
                                                else:
                                                    print("Invalid Order Type. Enter only M/L/SL")
                                                    continue

                                                # Price
                                                if(len(optionalItems)>1):
                                                    try:
                                                        if(optionalItems[1] == ''):
                                                            item_desc['price'] = 0.0
                                                        else:
                                                            item_desc['price'] = float(optionalItems[1])
                                                    except ValueError as e:
                                                        print("Enter price only in integer or float format.")
                                                        continue

                                                # Trigger Price
                                                if(len(optionalItems)>2):
                                                    try:
                                                        if(optionalItems[2] == ''):
                                                            item_desc['trigger_price'] = 0.0
                                                        else:
                                                            item_desc['trigger_price'] = float(optionalItems[2])
                                                    except ValueError as e:
                                                        print("Enter price only in integer or float format.")
                                                        continue

                                                # Product
                                                if(len(optionalItems)>3):
                                                    if(optionalItems[3].upper() in ['MIS','NRML','CNC']):
                                                        item_desc['product']=optionalItems[3].upper()
                                                    elif(optionalItems[3] == ''):
                                                        item_desc['product']='MIS'
                                                    else:
                                                        print("Invalid Product. Enter only MIS/NRML")
                                                        continue

                                        # # Testing
                                        # item_desc['inst'] = 'NSE:NIFTY50-INDEX'
                                        # item_desc['inst'] = 'SILVERMIC24T'


                                        #         item_desc['placed'] = 0
                                        # item_desc['inst'] = 'MCX:SILVERmmmmMI'
                                        item_desc['placed'] = 0
                                        item_desc['time'] = alert_time
                                        print("Alert Details: \n",item_desc)
                                        with open(resource_path('orders.txt'),'r') as f:
                                            orders = ast.literal_eval(f.read())
                                        orderThread = threading.Thread(target=orderPlacement.main,args=(item_desc,orders,papertrading))
                                        orderThread.start()
                                        orderThread.join()
                                        print("Updated orders")
                                        # print(orders)
                                        with open(resource_path('alerts.txt'),'r') as f:
                                            alerts = ast.literal_eval(f.read())
                                        alerts.append(item_desc)
                                        with open(resource_path('alerts.txt'),'w') as f:
                                            f.write(str(alerts))

                                        with open(resource_path('orders.txt'),'w') as f:
                                            f.write(str(orders))
                                        # with open('alerts.csv','+a') as f:
                                        #     f.write(item_desc)
                                        # create_side_main_frame(root,300,400,alerts)
                                        # writer.writerow(list(item_desc.values()))
                                        index += 1
                                        # df = pd.DataFrame(item_desc)
                                        # print(df)
                                        # with open('received_alerts.text', 'a') as f:
                                        #     item_desc['index'] = index
                                        #     json.dump(item_desc, f)
                                        #     f.write('\n')
                                        #     index += 1





                    # else:
                    #     print("None")
                time.sleep(0.5)
        except Exception as e:
            print("Error")
            print(e)
            # mail.close()
            # mail.logout()
            print("Logging in again...")
            time.sleep(2)
            mail = imaplib.IMAP4_SSL(mail_server,993)
            mail.login(username,password)
            print("Login Success")

# login_and_get_tv_alerts("sa","sa",[],[],False)
'''	        			                            Remarks				                    Default
            Type	        E/F/O		            E Equity, F Future, O Option				
            Qty	            50		                Quantity (not lots)				
            Direction	    BUY		                BUY, SELL				
            Symbol	        NIFTY		            Equity, Future				
            Symbol_option	NIFTY_ATM+100_W_CE		Name	ATM+100	    W (Weekly)	    CE	      
                            NIFTY_Prem+100_W_CE			    Prem+50	    	PE	        
                            NIFTY_21000_M_PE  			    21000	    M (Monthly)		          
            Broker          Fyers
Optional	Order Type	    M/L/SL		            Market, Limit, Stoploss Limit				    Market
Optional	Price	        0						                                                0
Optional	Trigger Price	0						                                                0
Optional	Product	        MIS		                MIS, NRML		                                MIS



								
	FINAL	Type Qty Direction Symbol Broker OrderType Price TriggerPrice Product				
	
	F 50 BUY nifty angel
	F 50 BUY nifty_NM angel		
'''
# login_and_get_tv_alerts(username,password,alerts)
