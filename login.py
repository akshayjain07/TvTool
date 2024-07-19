# from Login import fyers_login
from fyers_apiv3 import fyersModel
from pya3 import Aliceblue
from SmartApi import SmartConnect    #Use SmartApi instead of smartapi if you get error
import pyotp
from dhanhq import dhanhq
# import breeze_connect
# from breeze_connect import BreezeConnect
from APIConnect.APIConnect import APIConnect
from NorenApi import NorenApi
# import gui_windowsNn
import ast
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import webbrowser
import requests
from pmClient import PMClient
from kiteconnect import KiteConnect
import time
from Connect_iifl import XTSConnect
from neo_api_client import NeoAPI
from kite_trade import *
import sys
import os
def Login(broker):
    getBrokers()
    if(broker['name'] == 'alice'):
        login_alice(broker)
    elif(broker['name'] == 'angel'):
        login_angel(broker)
    elif(broker['name'] == 'fyers'):
        login_fyers(broker)
    # elif(broker['name'] == 'icici'):
    #     login_icici(broker)
    elif(broker['name'] == 'nuvama'):
        login_nuvama(broker)
    elif(broker['name'] == 'paytm'):
        login_paytm(broker)
    elif(broker['name'] == 'shoonya'):
        login_shoonya(broker)
    elif(broker['name'] == 'upstox'):
        login_upstox(broker)
    elif(broker['name'] == 'zerodha'):
        login_zerodha(broker)
    elif(broker['name'] == 'zerodha-enc'):
        login_zerodhaenc(broker)
    elif(broker['name'] == 'iifl'):
        login_iifl(broker)
    elif(broker['name'] == 'kotak'):
        login_kotak(broker)
    elif(broker['name']=='dhan'):
        login_dhan(broker)

brokers = []

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def getBrokers():
    global brokers
    with open(resource_path('config.txt'),'r') as f:
        brokers = ast.literal_eval(f.read())
def updateBrokers():
    global brokers
    with open(resource_path("config.txt"),'w') as f:
        f.write(str(brokers))
    getBrokers()

def login_alice(alice):
    try:
        alicee = Aliceblue(user_id=alice['params']['username'],api_key=alice['params']['api_key'])
        a = (alicee.get_session_id())
        sessionId = a['sessionID']
        print(sessionId)
    except Exception as e:
        # return str(e)
        tk.messagebox.showerror('Error',str(e))
        return None
    else:
        # with open('Alice/alice_session_id.txt', 'w+') as f:
        #     f.write(str(sessionId))
        for x in brokers:
            if x['name'] == alice['name'] and x['id'] == alice['id']:
                # x['isLoggedIn'] = True
                x['timestamp'] = str(datetime.now().date())
                # x['access_token'] = access_token
                x['active'] = 1
                print("Alice Logged In.")
                updateBrokers()
        messagebox.showinfo('Success','Alice Login Successfull')
        print(brokers)
        return 1

def login_angel(angel):
    try:
        print("Logging in Trading Api")
        print(angel['params'])
        totp=pyotp.TOTP(angel['params']['otp_token']).now()
        # print(totp)
        trading_obj=SmartConnect(api_key=angel['params']['trading_api'])
        trading_session=trading_obj.generateSession(angel['params']['username'],angel['params']['password'],totp)
        # print(trading_session)
        if trading_session['message'] == 'SUCCESS':
            # for x in brokers:
            #     if x['name'] == angel['name'] and x['id'] == angel['id']:
            #         x['isLoggedIn'] = True
            #         x['timestamp'] = str(datetime.now())
            #         # x['access_token'] = access_token
            #         x['active'] = 1
            #         print("Angel Trading Api Logged In.")
            #         updateBrokers()
            messagebox.showinfo('Success','Angel Trading Api Login Successfull')
            # print(brokers)

            time.sleep(10)
            hist_obj=SmartConnect(api_key=angel['params']['historical_api'])
            hist_session=hist_obj.generateSession(angel['params']['username'],angel['params']['password'],totp)
            if hist_session['message'] == 'SUCCESS':
                for x in brokers:
                    if x['name'] == angel['name'] and x['id'] == angel['id']:
                        # x['isLoggedIn'] = True
                        x['timestamp'] = str(datetime.now().date())
                        # x['access_token'] = access_token
                        x['active'] = 1
                        print("Angel Historical Api Logged In.")
                        updateBrokers()
                messagebox.showinfo('Success','Angel Historical Api Login Successfull')
            print(brokers)
            return 1

        else:
            print("Angel login Error")
            print(trading_session['message'])
            tk.messagebox.showerror('Error',str(trading_session['message']))
            # tk.messagebox.showerror('Error',str(hist_session['message']))
            return None
    except Exception as e:
        # return str(e)
        tk.messagebox.showerror('Error',str(e))
        return None

# def login_icici(icici):
#     try:
#         breeze = breeze_connect.BreezeConnect(api_key=icici['params']['api_key'])
#         auth_code = simpledialog.askstring("Input","Enter Session Code: ")
#         if not auth_code:  # User cancelled out of the dialog box
#             print("Login cancelled")
#             return None
#         else:
#             breeze.generate_session(api_secret=icici['params']['secret_key'], session_token=auth_code)
#             for x in brokers:
#                 if x['name'] == icici['name'] and x['id'] == icici['id']:
#                     # x['isLoggedIn'] = True
#                     x['timestamp'] = str(datetime.now().date())
#                     x['session_key'] = auth_code
#                     # x['access_token'] = access_token
#                     x['active'] = 1
#                     updateBrokers()
#             print(brokers)
#             messagebox.showinfo('Success','ICICI Login Successfull')
#             print("ICICI Logged in.")
#     except Exception as e:
#         tk.messagebox.showerror('Error',f'Error Logging In. {str(e)}')
#         return None

def login_iifl(iifl):
    try:
        # api = NorenApi()
        api_key    = iifl['params']['Interactive_api_key']
        secret_key     = iifl['params']['Interactive_api_secret']
        m_api_key = iifl['params']['Market_api_key']
        m_secret_key = iifl['params']['Market_api_secret']
        source = "WEBAPI"

        # Initialise
        xtm = XTSConnect(m_api_key,m_secret_key,source)
        xt = XTSConnect(api_key, secret_key, source)
        # Login for authorization token
        mresponse = xtm.marketdata_login()
        response = xt.interactive_login()

        # Store the token and userid
        # print(response)
        if(response['type']=='success' and mresponse['type']=='success'):
            resmaster = xtm.get_master( ["NSECM","NSECD","NSEFO","BSECM","BSEFO","MCXFO"])
            symbol_to_id_dict = {}
            segments_dict = {"NSECM": 1, "NSEFO": 2, "NSECD": 3, "BSECM": 11, "BSEFO": 12, "MCXFO": 51}
            master_data = resmaster['result'].split('\n')
            for i in range(0,len(master_data)):
                single_row = master_data[i].split('|')
                symbol_to_id_dict[single_row[4]] = str(segments_dict[single_row[0]])+"|"+str(single_row[1])
            symbol_to_id_dict['Nifty 50'] = '1|26000'
            symbol_to_id_dict['Nifty Bank'] = '1|26001'
            symbol_to_id_dict['Nifty Fin Service'] = '1|26034'
            symbol_to_id_dict['Nifty Mid Select'] = '1|26121'
            with open(resource_path('symbol_mapping.txt'),'w') as f:
                f.write(str([symbol_to_id_dict]))

            Token = response['result']['token']
            user_token = response['result']['userID']
            # print(ret['susertoken'])
            for x in brokers:
                if x['name'] == iifl['name'] and x['id'] == iifl['id']:
                    # x['isLoggedIn'] = True
                    x['timestamp'] = str(datetime.now().date())
                    x['userId'] = user_token
                    x['token'] = Token
                    x['active'] = 1
                    updateBrokers()
            print(brokers)
            messagebox.showinfo('Success','IIFL Login Successfull')
            print("IIFL Logged in.")
        else:
            print("Error Loggin in")
            raise "Error Loggin in"
    except Exception as e:
        tk.messagebox.showerror('Error',f'Error Logging In. {str(e)}')
        return None
def login_kotak(kotak):
    pass
    # grant_type = 'password'
    # username = ''
    # password = ''
    # url = "https://example.com/api/endpoint"
    # # Headers containing any necessary authentication tokens or other metadata
    # headers = {
    # "Content-Type": "application/json",  # Specify the content type as JSON
    # "Authorization": "Basic Z0N0WjFVNWZmbGhPMG03Nk5VMU5waHZ0Zko0YTpjZlhDMXVHS1dYcFZnSkJtUFZNRkRJV05MUm9h"
    # }
    #
    # # Data to be sent in the request body (in this case, a JSON payload)
    # data = {
    # "key1": "value1",
    # "key2": "value2",
    # "nested": {
    #     "nested_key": "nested_value"
    # }
    # }
    # Authorization = Basic Z0N0WjFVNWZmbGhPMG03Nk5VMU5waHZ0Zko0YTpjZlhDMXVHS1dYcFZnSkJtUFZNRkRJV05MUm9h
    # client = NeoAPI(consumer_key=kotak['params']['consumer_key'], consumer_secret=kotak['params']['consumer_secret'], environment="prod", on_message=on_message, on_error=on_error, on_open=on_open, on_close=on_close)
    # client.login(mobilenumber=kotak['params']['mobilenumber'], password=kotak['params']['loginpassword'])
    # otp = input("otp: ")
    # otp = str(otp)
    # client.session_2fa(otp)

def login_dhan(dhan):
    try:
        auth_code = simpledialog.askstring("Input","Enter Access Token: ")
        dhan_obj = dhanhq(dhan['params']["client_id"],auth_code)
        print(dhan_obj)
        for x in brokers:
            if x['name'] == dhan['name'] and x['id'] == dhan['id']:
                x['timestamp'] = str(datetime.now().date())
                x['access_token'] = auth_code
                x['active'] = 1
                updateBrokers()
        print(brokers)
        messagebox.showinfo('Success','Dhan Login Successfull')
        print("Dhan Logged in.")
    except Exception as e:
        tk.messagebox.showerror('Error',f'Error Logging In. {str(e)}')
        print(e)
        return None
def login_shoonya(shoonya):
    try:
        api = NorenApi()
        user    = shoonya['params']['username']
        pwd     = shoonya['params']['password']
        vc      = user+'_U'
        otp_token = shoonya['params']['otp_token']
        factor2=pyotp.TOTP(otp_token).now()
        app_key = shoonya['params']['app_key']
        imei    = shoonya['params']['imei']
        user_token = ''
        # print(user)
        # print(pwd)
        # print(vc)
        # print(otp_token)
        # print(factor2)
        # print(app_key)
        # print(imei)
        #make the api call
        ret = api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
        print(ret)
        user_token = ret['susertoken']
        # print(ret['susertoken'])
        for x in brokers:
            if x['name'] == shoonya['name'] and x['id'] == shoonya['id']:
                # x['isLoggedIn'] = True
                x['timestamp'] = str(datetime.now().date())
                x['user_token'] = user_token
                x['active'] = 1
                updateBrokers()
        # print(brokers)
        messagebox.showinfo('Success','Shoonya Login Successfull')
        print("Shoonya Logged in.")
    except Exception as e:
        tk.messagebox.showerror('Error',f'Error Logging In. {str(e)}')
        return None

def login_fyers(fyers):
    grant_type = "authorization_code"                  ## The grant_type always has to be "authorization_code"
    response_type = "code"                             ## The response_type always has to be "code"
    state = "sample"
    appSession = fyersModel.SessionModel(client_id = fyers['params']['client_id'], redirect_uri = fyers['params']['redirect_url'],response_type=response_type,state=state,secret_key=fyers['params']['secret_key'],grant_type=grant_type)
    generateTokenUrl = appSession.generate_authcode()
    webbrowser.open(generateTokenUrl,new=1)

    auth_code = simpledialog.askstring("Input","Enter Auth Code: ")
    if not auth_code:  # User cancelled out of the dialog box
        print("Login cancelled")
        return None
    else:
        try:
            appSession.set_token(auth_code)
            response = appSession.generate_token()
            access_token = response["access_token"]
            print("token: ",access_token)
            if(access_token != ''):
                messagebox.showinfo('Success','Fyers Login Successfull')
                print("Fyers Logged in.")
                for x in brokers:
                    if x['name'] == fyers['name'] and x['id'] == fyers['id']:
                        # x['isLoggedIn'] = True
                        x['timestamp'] = str(datetime.now().date())
                        x['access_token'] = access_token
                        x['active'] = 1
                        updateBrokers()
                print(brokers)
                return access_token
                # loggedin.append('Fyers')
        except:
            tk.messagebox.showerror('Error','Invalid Authentication code')
            return None

def login_nuvama(nuvama):
    url = "https://nuvamawealth.com/api-connect/login?api_key=" + nuvama['params']['api_key']
    webbrowser.open(url,new=1)
    auth_code = simpledialog.askstring("Input","Enter Request Id: ")
    if not auth_code:  # User cancelled out of the dialog box
        print("Login cancelled")
        return None
    else:
        try:
            api_connect = APIConnect(nuvama['params']['api_key'], nuvama['params']['api_secret'], auth_code, True)
            print(api_connect.GetLoginData())
            messagebox.showinfo('Success','Nuvama Login Successfull')
            print("Nuvama Logged in.")
            for x in brokers:
                if x['name'] == nuvama['name'] and x['id'] == nuvama['id']:
                    # x['isLoggedIn'] = True
                    x['request_token'] = auth_code
                    x['timestamp'] = str(datetime.now().date())
                    x['active'] = 1
                    updateBrokers()
            print(brokers)
            return 1
            # loggedin.append('Fyers')
        except Exception as e:
            tk.messagebox.showerror('Error',e)
            return None

def login_paytm(paytm):
    url = "https://login.paytmmoney.com/merchant-login?apiKey="+ paytm['params']['api_key']
    webbrowser.open(url=url,new=1)

    auth_code = simpledialog.askstring("Input","Enter Request Id: ")
    if not auth_code:  # User cancelled out of the dialog box
        print("Login cancelled")
        return None
    else:
        try:
            pm = PMClient(api_secret=paytm['params']['secret_key'], api_key=paytm['params']['api_key'])
            sess = pm.generate_session(request_token=auth_code)
            print(sess)
            messagebox.showinfo('Success','Paytm Login Successfull')
            access_token = sess['access_token']
            public_access_token = sess['public_access_token']
            read_access_token = sess['read_access_token']
            for x in brokers:
                if x['name'] == paytm['name'] and x['id'] == paytm['id']:
                    # x['isLoggedIn'] = True
                    x['access_token'] = access_token
                    x['public_access_token'] = public_access_token
                    x['read_access_token'] = read_access_token
                    x['timestamp'] = str(datetime.now().date())
                    x['active'] = 1
                    updateBrokers()
            # print(brokers)
            print("Paytm Logged in.")
            return 1
        except Exception as e:
            tk.messagebox.showerror('Error',f'{e}')
            return None

def login_zerodha(zerodha):
    login_url = "https://kite.trade/connect/login?api_key=" + zerodha['params']['api_key']
    webbrowser.open(login_url,new=1)

    auth_code = simpledialog.askstring("Input","Enter Token: ")
    if not auth_code:  # User cancelled out of the dialog box
        print("Login cancelled")
        return None
    else:
        try:
            kite = KiteConnect(api_key=zerodha['params']['api_key'])
            data = kite.generate_session(auth_code, api_secret=zerodha['params']['api_secret'])
            # kc = KiteApp(enctoken=zerodha['enctoken'])
            # kc = KiteApp(enctoken=auth_code)

            # res = kc.login().json()
            # print(res)
            # if(res['status'] == 'error'):
            #     raise
            kite.set_access_token(data["access_token"])
            accessToken = data["access_token"]

            messagebox.showinfo('Success','Zerodha Login Successfull')

            for x in brokers:
                if x['name'] == zerodha['name'] and x['id'] == zerodha['id']:
                    # x['isLoggedIn'] = True
                    x['access_token'] = accessToken
                    x['timestamp'] = str(datetime.now().date())
                    x['active'] = 1
                    updateBrokers()
            # print(brokers)
            print("Zerodha Logged in.")
            return 1
        except Exception as e:
            tk.messagebox.showerror('Error',f'Zerodha Login Error.')
            return None

def login_zerodhaenc(zerodha):
    # login_url = "https://kite.trade/connect/login?api_key=" + zerodha['params']['api_key']
    # webbrowser.open(login_url,new=1)

    auth_code = simpledialog.askstring("Input","Enter Enc Token: ")
    if not auth_code:  # User cancelled out of the dialog box
        print("Login cancelled")
        return None
    else:
        try:
            # kite = KiteConnect(api_key=zerodha['params']['api_key'])
            # data = kite.generate_session(auth_code, api_secret=zerodha['params']['api_secret'])
            # kc = KiteApp(enctoken=zerodha['enctoken'])
            kc = KiteApp(enctoken=auth_code)

            # res = kc.login().json()
            # print(res)
            # if(res['status'] == 'error'):
            #     raise
            # kite.set_access_token(data["access_token"])
            # accessToken = data["access_token"]

            messagebox.showinfo('Success','Zerodha Login Successfull')

            for x in brokers:
                if x['name'] == zerodha['name'] and x['id'] == zerodha['id']:
                    # x['isLoggedIn'] = True
                    x['enc_token'] = auth_code
                    x['timestamp'] = str(datetime.now().date())
                    x['active'] = 1
                    updateBrokers()
            # print(brokers)
            print("Zerodha Logged in.")
            return 1
        except Exception as e:
            tk.messagebox.showerror('Error',f'Zerodha Login Error. Enter latest enc and keep zerodha logged in on browser.')
            return None


def login_upstox(upstox):
    client_id = upstox['params']['client_id']
    redirect_url = upstox['params']['redirect_url']
    client_secret = upstox['params']['client_secret']
    uri = f'https://api-v2.upstox.com/login/authorization/dialog?response_type=code&client_id={client_id}&redirect_uri={redirect_url}'
    webbrowser.open(uri,new=1)

    auth_code = simpledialog.askstring("Input","Enter Auth Code: ")
    if not auth_code:  # User cancelled out of the dialog box
        print("Login cancelled")
        return None
    else:
        try:
            api_version = '2.0' # str | API Version Header
            grant_type = 'authorization_code'
            token_url = "https://api-v2.upstox.com/login/authorization/token"
            headers = {
                'accept': 'application/json',
                'Api-Version': api_version,
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            data = {
                'code': auth_code,
                'client_id': client_id,
                'client_secret': client_secret,
                'redirect_uri': redirect_url,
                'grant_type': grant_type
            }

            response = requests.post(token_url, headers=headers, data=data)
            json_response = response.json()
            accessToken = json_response['access_token']

            messagebox.showinfo('Success','Upstox Login Successfull')

            for x in brokers:
                if x['name'] == upstox['name'] and x['id'] == upstox['id']:
                    # x['isLoggedIn'] = True
                    x['access_token'] = accessToken
                    x['timestamp'] = str(datetime.now().date())
                    x['active'] = 1
                    updateBrokers()
            print(brokers)
            print("Upstox Logged in.")
            return 1
        except Exception as e:
            tk.messagebox.showerror('Error',f'{e}')
            return None




def logout(broker):
    for x in brokers:
        if x['name'] == broker['name'] and x['id'] == broker['id']:
            # x['timestamp'] = str(datetime.now())
            x['active'] = 0
            updateBrokers()

def logout_all():
    for x in brokers:
        x['active'] = 0
