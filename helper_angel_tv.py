#DISCLAIMER:
#1) This sample code is for learning purposes only.
#2) Always be very careful when dealing with codes in which you can place orders in your account.
#3) The actual results may or may not be similar to backtested results. The historical results do not guarantee any profits or losses in the future.
#4) You are responsible for any losses/profits that occur in your account in case you plan to take trades in your account.
#5) TFU and Aseem Singhal do not take any responsibility of you running these codes on your account and the corresponding profits and losses that might occur.
#6) The running of the code properly is dependent on a lot of factors such as internet, broker, what changes you have made, etc. So it is always better to keep checking the trades as technology error can come anytime.
#7) This is NOT a tip providing service/code.
#8) This is NOT a software. Its a tool that works as per the inputs given by you.
#9) Slippage is dependent on market conditions.
#10) Option trading and automatic API trading are subject to market risks

# from SmartWebsocketv2 import SmartWebSocketV2

from SmartApi import SmartConnect
import datetime
import time
import requests
from datetime import timedelta
from pytz import timezone
import pandas as pd
import pyotp
import traceback

######PIVOT POINTS##########################
####################__INPUT__#####################

# trading_api_key= '69HcEAl'
# hist_api_key = 'yneyZ6r'
# username = 'P92853'
# password = '1117'   #This is 4 digit MPIN
# otp_token = 'MJOV5A6NTO7HJ4DTN4UOFFOI'

allinst = pd.read_json('https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json')
print(allinst)
# def login_trading():
#     global trading_obj
#     totp=pyotp.TOTP(otp_token).now()
#
#     trading_obj=SmartConnect(api_key=trading_api_key)
#     trading_session=trading_obj.generateSession(username,password,totp)
#     print(trading_session)
#
#     if trading_session['message'] == 'SUCCESS':
#         trading_refreshToken= trading_session['data']['refreshToken']  #till here
#         #trading_authToken = trading_session['data']['jwtToken']
#         #trading_feedToken=trading_obj.getfeedToken()
#         #print(".........................................")
#         #print(trading_feedToken)
#         #print("Connection Successful")
#     else:
#         print(trading_session['message'])
#
#     #SmartWebSocketV2OBJ = SmartWebSocketV2(trading_authToken, trading_api_key, username, trading_feedToken)

# def login_historical():
#     global hist_obj
#     totp=pyotp.TOTP(otp_token).now()
#     hist_obj=SmartConnect(api_key=hist_api_key)
#     hist_session=hist_obj.generateSession(username,password,totp)
#     print(hist_session)
#
#     if hist_session['message'] == 'SUCCESS':
#         hist_refreshToken= hist_session['data']['refreshToken']
#         #hist_authToken = hist_session['data']['jwtToken']
#         #hist_feedToken=hist_obj.getfeedToken()
#         #print(".........................................")
#         #print(hist_feedToken)
#         #print("Connection Successful")
#     else:
#         print(hist_session['message'])



def get_tokens(symbols):
    for i in range(len(allinst)):
        if symbols[4:] == "NIFTY":
            return 99926000
        elif symbols[4:] == "BANKNIFTY":
            return 99926009
        elif symbols[4:] == "FINNIFTY":
            return 99926037
        elif allinst['symbol'][i] == symbols[4:] and allinst['exch_seg'][i] == symbols[:3]:
            if allinst['expiry'][i] == "":
                exch = get_exch_type(symbols, 'NO')
            else:
                exch = get_exch_type(symbols, 'YES')
            # print(exch)
            # symbol_token=allinst['token'][i]
            print(allinst['token'][i])
            return allinst['token'][i]


def get_exch_type(symbol, exp):
    if exp == 'NO':
        if symbol[:3] == 'NSE': return 1
        elif symbol[:3] == 'BSE': return 3
    if exp == 'YES':
        if symbol[:3] == 'NFO': return 2
        elif symbol[:3] == 'BSE': return 4
        elif symbol[:3] == 'MCX': return 5
        elif symbol[:3] == 'NCDEX': return 6
        elif symbol[:3] == 'CDS': return 7


mcx_expiries = {
    "GOLD":             {datetime.datetime(2024, 6, 5).date(): "24JUN",
                         datetime.datetime(2024, 8, 5).date(): "24AUG",
                         datetime.datetime(2024, 10, 4).date(): "24OCT",
                         datetime.datetime(2024, 12, 5).date(): "24DEC",
                         datetime.datetime(2025, 2, 5).date(): "25FEB",
                         datetime.datetime(2025, 4, 4).date(): "25APR",},
    "GOLDM":            {datetime.datetime(2024, 6, 5).date(): "24JUN",
                         datetime.datetime(2024, 7, 5).date(): "24JUL",
                         datetime.datetime(2024, 8, 5).date(): "24AUG",
                         datetime.datetime(2024, 9, 5).date(): "24SEP",
                         datetime.datetime(2024, 10, 4).date(): "24OCT",
                         datetime.datetime(2024, 11, 5).date(): "24NOV",
                         datetime.datetime(2024, 12, 5).date(): "24DEC",},
    "GOLDGUINEA":       {datetime.datetime(2024, 5, 31).date(): "24MAY",
                         datetime.datetime(2024, 6, 28).date(): "24JUN",
                         datetime.datetime(2024, 7, 31).date(): "24JUL",
                         datetime.datetime(2024, 8, 30).date(): "24AUG",
                         datetime.datetime(2024, 9, 30).date(): "24SEP",
                         datetime.datetime(2024, 10, 31).date(): "24OCT",
                         datetime.datetime(2024, 11, 29).date(): "24NOV",
                         datetime.datetime(2024, 12, 31).date(): "24DEC"},
    "GOLDPETAL":        {datetime.datetime(2024, 2, 29).date(): "24FEB",
                         datetime.datetime(2024, 3, 29).date(): "24MAR",
                         datetime.datetime(2024, 4, 30).date(): "24APR",
                         datetime.datetime(2024, 5, 31).date(): "24MAY",
                         datetime.datetime(2024, 6, 28).date(): "24JUN",
                         datetime.datetime(2024, 7, 31).date(): "24JUL",
                         datetime.datetime(2024, 8, 30).date(): "24AUG",
                         datetime.datetime(2024, 9, 30).date(): "24SEP",
                         datetime.datetime(2024, 10, 31).date(): "24OCT",
                         datetime.datetime(2024, 11, 29).date(): "24NOV",
                         datetime.datetime(2024, 12, 31).date(): "24DEC"},
    "SILVER":           {datetime.datetime(2024, 5, 3).date(): "24MAY",
                         datetime.datetime(2024, 7, 5).date(): "24JUL",
                         datetime.datetime(2024, 9, 5).date(): "24SEP",
                         datetime.datetime(2024, 12, 5).date(): "24DEC"},
    "SILVERM":          {datetime.datetime(2024, 2, 29).date(): "24FEB",
                         datetime.datetime(2024, 4, 30).date(): "24APR",
                         datetime.datetime(2024, 6, 28).date(): "24JUN",
                         datetime.datetime(2024, 8, 30).date(): "24AUG",
                         datetime.datetime(2024, 11, 29).date(): "24NOV",},
    "SILVERMIC":        {datetime.datetime(2024, 2, 29).date(): "24FEB",
                         datetime.datetime(2024, 4, 30).date(): "24APR",
                         datetime.datetime(2024, 6, 28).date(): "24JUN",
                         datetime.datetime(2024, 8, 30).date(): "24AUG",
                         datetime.datetime(2024, 11, 29).date(): "24NOV",},
    "CRUDEOIL":         {datetime.datetime(2024, 2, 16).date(): "24FEB",
                         datetime.datetime(2024, 3, 19).date(): "24MAR",
                         datetime.datetime(2024, 4, 19).date(): "24APR",
                         datetime.datetime(2024, 5, 20).date(): "24MAY",
                         datetime.datetime(2024, 6, 18).date(): "24JUN",
                         datetime.datetime(2024, 7, 19).date(): "24JUL",
                         datetime.datetime(2024, 8, 19).date(): "24AUG",
                         datetime.datetime(2024, 9, 19).date(): "24SEP",
                         datetime.datetime(2024, 10, 21).date(): "24OCT",
                         datetime.datetime(2024, 11, 19).date(): "24NOV",
                         datetime.datetime(2024, 12, 18).date(): "24DEC"},
    "CRUDEOILM":         {datetime.datetime(2024, 2, 16).date(): "24FEB",
                          datetime.datetime(2024, 3, 19).date(): "24MAR",
                          datetime.datetime(2024, 4, 19).date(): "24APR",
                          datetime.datetime(2024, 5, 20).date(): "24MAY",
                          datetime.datetime(2024, 6, 18).date(): "24JUN",
                          datetime.datetime(2024, 7, 19).date(): "24JUL",
                          datetime.datetime(2024, 8, 19).date(): "24AUG",
                          datetime.datetime(2024, 9, 19).date(): "24SEP",
                          datetime.datetime(2024, 10, 21).date(): "24OCT",
                          datetime.datetime(2024, 11, 19).date(): "24NOV",
                          datetime.datetime(2024, 12, 18).date(): "24DEC"}

}

def getNiftyExpiryDate(next=0):
    expiry = {
        datetime.datetime(2023, 11, 16).date(): "16NOV23",
        datetime.datetime(2023, 11, 23).date(): "23NOV23",
        datetime.datetime(2023, 11, 30).date(): "30NOV23",
        datetime.datetime(2023, 12, 7).date(): "07DEC23",
        datetime.datetime(2023, 12, 14).date(): "14DEC23",
        datetime.datetime(2023, 12, 21).date(): "21DEC23",
        datetime.datetime(2023, 12, 28).date(): "28DEC23",
        datetime.datetime(2024, 1, 4).date(): "04JAN24",
        datetime.datetime(2024, 1, 11).date(): "11JAN24",
        datetime.datetime(2024, 1, 18).date(): "18JAN24",
        datetime.datetime(2024, 1, 25).date(): "25JAN24",
        datetime.datetime(2024, 2, 1).date(): "01FEB24",
        datetime.datetime(2024, 2, 8).date(): "08FEB24",
        datetime.datetime(2024, 2, 15).date(): "15FEB24",
        datetime.datetime(2024, 2, 22).date(): "22FEB24",
        datetime.datetime(2024, 2, 29).date(): "29FEB24",
        datetime.datetime(2024, 3, 7).date(): "07MAR24",
        datetime.datetime(2024, 3, 14).date(): "14MAR24",
        datetime.datetime(2024, 3, 21).date(): "21MAR24",
        datetime.datetime(2024, 3, 28).date(): "28MAR24",
        datetime.datetime(2024, 4, 4).date(): "04APR24",
        datetime.datetime(2024, 4, 10).date(): "10APR24",
        datetime.datetime(2024, 4, 18).date(): "18APR24",
        datetime.datetime(2024, 4, 25).date(): "25APR24",
        datetime.datetime(2024, 5, 2).date(): "02MAY24",
        datetime.datetime(2024, 5, 9).date(): "09MAY24",
        datetime.datetime(2024, 5, 16).date(): "16MAY24",
        datetime.datetime(2024, 5, 23).date(): "23MAY24",
        datetime.datetime(2024, 5, 30).date(): "30MAY24",
        datetime.datetime(2024, 6, 6).date(): "06JUN24",
        datetime.datetime(2024, 6, 13).date(): "13JUN24",
        datetime.datetime(2024, 6, 20).date(): "20JUN24",
        datetime.datetime(2024, 6, 27).date(): "27JUN24",
        datetime.datetime(2024, 7, 4).date(): "04JUL24",
        datetime.datetime(2024, 7, 11).date(): "11JUL24",
        datetime.datetime(2024, 7, 18).date(): "18JUL24",
        datetime.datetime(2024, 7, 25).date(): "25JUL24",
        datetime.datetime(2024, 8, 1).date(): "01AUG24",
        datetime.datetime(2024, 8, 8).date(): "08AUG24",
        datetime.datetime(2024, 8, 14).date(): "14AUG24",
        datetime.datetime(2024, 8, 22).date(): "22AUG24",
        datetime.datetime(2024, 8, 29).date(): "29AUG24",
        datetime.datetime(2024, 9, 5).date(): "05SEP24",
        datetime.datetime(2024, 9, 12).date(): "12SEP24",
        datetime.datetime(2024, 9, 19).date(): "19SEP24",
        datetime.datetime(2024, 9, 26).date(): "26SEP24",
        datetime.datetime(2024, 10, 3).date(): "03OCT24",
        datetime.datetime(2024, 10, 10).date(): "10OCT24",
        datetime.datetime(2024, 10, 17).date(): "17OCT24",
        datetime.datetime(2024, 10, 24).date(): "24OCT24",
        datetime.datetime(2024, 10, 31).date(): "31OCT24",
        datetime.datetime(2024, 11, 7).date(): "07NOV24",
        datetime.datetime(2024, 11, 14).date(): "14NOV24",
        datetime.datetime(2024, 11, 21).date(): "21NOV24",
        datetime.datetime(2024, 11, 28).date(): "28NOV24",
        datetime.datetime(2024, 12, 5).date(): "05DEC24",
        datetime.datetime(2024, 12, 12).date(): "12DEC24",
        datetime.datetime(2024, 12, 19).date(): "19DEC24",
        datetime.datetime(2024, 12, 26).date(): "26DEC24",
    }
    today = datetime.datetime.now().date()
    nxt = 0
    for date_key, value in expiry.items():
        if next==1 and nxt==1:
            nxt=0
            print(value)
            return value
        if today <= date_key:
            if next==1 and nxt==0:
                nxt=1
                continue
            print(value)
            return value

def getBankNiftyExpiryDate(next=0):
    expiry = {
        datetime.datetime(2023, 11, 15).date(): "15NOV23",
        datetime.datetime(2023, 11, 22).date(): "22NOV23",
        datetime.datetime(2023, 11, 30).date(): "30NOV23",
        datetime.datetime(2023, 12, 6).date(): "06DEC23",
        datetime.datetime(2023, 12, 13).date(): "13DEC23",
        datetime.datetime(2023, 12, 20).date(): "20DEC23",
        datetime.datetime(2023, 12, 28).date(): "08DEC23",
        datetime.datetime(2024, 1, 3).date(): "03JAN24",
        datetime.datetime(2024, 1, 10).date(): "10JAN24",
        datetime.datetime(2024, 1, 17).date(): "17JAN24",
        datetime.datetime(2024, 1, 25).date(): "25JAN24",
        datetime.datetime(2024, 1, 31).date(): "31JAN24",
        datetime.datetime(2024, 2, 7).date(): "07FEB24",
        datetime.datetime(2024, 2, 14).date(): "14FEB24",
        datetime.datetime(2024, 2, 21).date(): "21FEB24",
        datetime.datetime(2024, 2, 29).date(): "29FEB24",
        datetime.datetime(2024, 3, 6).date(): "06MAR24",
        datetime.datetime(2024, 3, 13).date(): "13MAR24",
        datetime.datetime(2024, 3, 20).date(): "20MAR24",
        datetime.datetime(2024, 3, 27).date(): "27MAR24",
        datetime.datetime(2024, 4, 3).date(): "03APR24",
        datetime.datetime(2024, 4, 10).date(): "10APR24",
        datetime.datetime(2024, 4, 16).date(): "16APR24",
        datetime.datetime(2024, 4, 24).date(): "24APR24",
        datetime.datetime(2024, 4, 30).date(): "30APR24",
        datetime.datetime(2024, 5, 8).date(): "08MAY24",
        datetime.datetime(2024, 5, 15).date(): "15MAY24",
        datetime.datetime(2024, 5, 22).date(): "22MAY24",
        datetime.datetime(2024, 5, 29).date(): "29MAY24",
        datetime.datetime(2024, 6, 5).date(): "05JUN24",
        datetime.datetime(2024, 6, 12).date(): "12JUN24",
        datetime.datetime(2024, 6, 19).date(): "19JUN24",
        datetime.datetime(2024, 6, 26).date(): "26JUN24",
        datetime.datetime(2024, 7, 3).date(): "03JUL24",
        datetime.datetime(2024, 7, 10).date(): "10JUL24",
        datetime.datetime(2024, 7, 16).date(): "16JUL24",
        datetime.datetime(2024, 7, 24).date(): "24JUL24",
        datetime.datetime(2024, 7, 31).date(): "31JUL24",
        datetime.datetime(2024, 8, 7).date(): "07AUG24",
        datetime.datetime(2024, 8, 14).date(): "14AUG24",
        datetime.datetime(2024, 8, 21).date(): "21AUG24",
        datetime.datetime(2024, 8, 28).date(): "28AUG24",
        datetime.datetime(2024, 9, 4).date(): "04SEP24",
        datetime.datetime(2024, 9, 11).date(): "11SEP24",
        datetime.datetime(2024, 9, 18).date(): "18SEP24",
        datetime.datetime(2024, 9, 25).date(): "25SEP24",
        datetime.datetime(2024, 10, 1).date(): "01OCT24",
        datetime.datetime(2024, 10, 9).date(): "09OCT24",
        datetime.datetime(2024, 10, 16).date(): "16OCT24",
        datetime.datetime(2024, 10, 23).date(): "23OCT24",
        datetime.datetime(2024, 10, 30).date(): "30OCT24",
        datetime.datetime(2024, 11, 6).date(): "06NOV24",
        datetime.datetime(2024, 11, 13).date(): "13NOV24",
        datetime.datetime(2024, 11, 20).date(): "20NOV24",
        datetime.datetime(2024, 11, 27).date(): "27NOV24",
        datetime.datetime(2024, 12, 4).date(): "04DEC24",
        datetime.datetime(2024, 12, 11).date(): "11DEC24",
        datetime.datetime(2024, 12, 18).date(): "18DEC24",
        datetime.datetime(2024, 12, 24).date(): "24DEC24",
    }
    today = datetime.datetime.now().date()
    nxt = 0
    for date_key, value in expiry.items():
        if next==1 and nxt==1:
            nxt=0
            print(value)
            return value
        if today <= date_key:
            if next==1 and nxt==0:
                nxt=1
                continue
            print(value)
            return value

def getFinNiftyExpiryDate(next=0):
    expiry = {
        datetime.datetime(2024, 2, 20).date(): "20FEB24",
        datetime.datetime(2024, 2, 27).date(): "27FEB24",
        datetime.datetime(2024, 3, 5).date(): "05MAR24",
        datetime.datetime(2024, 3, 12).date(): "12MAR24",
        datetime.datetime(2024, 3, 19).date(): "19MAR24",
        datetime.datetime(2024, 3, 26).date(): "26MAR24",
        datetime.datetime(2024, 4, 2).date(): "02APR24",
        datetime.datetime(2024, 4, 9).date(): "09APR24",
        datetime.datetime(2024, 4, 16).date(): "16APR24",
        datetime.datetime(2024, 4, 23).date(): "23APR24",
        datetime.datetime(2024, 4, 30).date(): "30APR24",
        datetime.datetime(2024, 5, 7).date(): "07MAY24",
        datetime.datetime(2024, 5, 14).date(): "14MAY24",
        datetime.datetime(2024, 5, 21).date(): "21MAY24",
        datetime.datetime(2024, 5, 28).date(): "28MAY24",
        datetime.datetime(2024, 6, 4).date(): "04JUN24",
        datetime.datetime(2024, 6, 11).date(): "11JUN24",
        datetime.datetime(2024, 6, 18).date(): "18JUN24",
        datetime.datetime(2024, 6, 25).date(): "25JUN24",
        datetime.datetime(2024, 7, 2).date(): "02JUL24",
        datetime.datetime(2024, 7, 9).date(): "09JUL24",
        datetime.datetime(2024, 7, 16).date(): "16JUL24",
        datetime.datetime(2024, 7, 23).date(): "23JUL24",
        datetime.datetime(2024, 7, 30).date(): "30JUL24",
        datetime.datetime(2024, 8, 6).date(): "06AUG24",
        datetime.datetime(2024, 8, 13).date(): "13AUG24",
        datetime.datetime(2024, 8, 20).date(): "20AUG24",
        datetime.datetime(2024, 8, 27).date(): "27AUG24",
        datetime.datetime(2024, 9, 3).date(): "03SEP24",
        datetime.datetime(2024, 9, 10).date(): "10SEP24",
        datetime.datetime(2024, 9, 17).date(): "17SEP24",
        datetime.datetime(2024, 9, 24).date(): "24SEP24",
        datetime.datetime(2024, 10, 1).date(): "01OCT24",
        datetime.datetime(2024, 10, 8).date(): "08OCT24",
        datetime.datetime(2024, 10, 15).date(): "15OCT24",
        datetime.datetime(2024, 10, 22).date(): "22OCT24",
        datetime.datetime(2024, 10, 29).date(): "29OCT24",
        datetime.datetime(2024, 11, 5).date(): "05NOV24",
        datetime.datetime(2024, 11, 12).date(): "12NOV24",
        datetime.datetime(2024, 11, 19).date(): "19NOV24",
        datetime.datetime(2024, 11, 26).date(): "26NOV24",
        datetime.datetime(2024, 12, 3).date(): "03DEC24",
        datetime.datetime(2024, 12, 10).date(): "10DEC24",
        datetime.datetime(2024, 12, 17).date(): "17DEC24",
        datetime.datetime(2024, 12, 24).date(): "24DEC24",
        datetime.datetime(2024, 12, 31).date(): "31DEC24",
    }

    today = datetime.datetime.now().date()

    nxt = 0
    for date_key, value in expiry.items():
        if next==1 and nxt==1:
            nxt=0
            print(value)
            return value
        if today <= date_key:
            if next==1 and nxt==0:
                nxt=1
                continue
            print(value)
            return value

def getMidCapNiftyExpiryDate(next=0):
    expiry = {
        datetime.datetime(2024, 5, 13).date(): "13MAY24",
        datetime.datetime(2024, 5, 20).date(): "20MAY24",
        datetime.datetime(2024, 5, 27).date(): "27MAY24",
        datetime.datetime(2024, 6, 3).date(): "03JUN24",
        datetime.datetime(2024, 6, 10).date(): "10JUN24",
        datetime.datetime(2024, 6, 17).date(): "17JUN24",
        datetime.datetime(2024, 6, 24).date(): "24JUN24",
        datetime.datetime(2024, 7, 1).date(): "01JUL24",
        datetime.datetime(2024, 7, 8).date(): "08JUL24",
        datetime.datetime(2024, 7, 15).date(): "15JUL24",
        datetime.datetime(2024, 7, 22).date(): "22JUL24",
        datetime.datetime(2024, 7, 29).date(): "29JUL24",
        datetime.datetime(2024, 8, 5).date(): "05AUG24",
        datetime.datetime(2024, 8, 12).date(): "12AUG24",
        datetime.datetime(2024, 8, 19).date(): "19AUG24",
        datetime.datetime(2024, 8, 26).date(): "26AUG24",
        datetime.datetime(2024, 9, 2).date(): "02SEP24",
        datetime.datetime(2024, 9, 9).date(): "09SEP24",
        datetime.datetime(2024, 9, 16).date(): "16SEP24",
        datetime.datetime(2024, 9, 23).date(): "23SEP24",
        datetime.datetime(2024, 9, 30).date(): "30SEP24",
        datetime.datetime(2024, 10, 7).date(): "07OCT24",
        datetime.datetime(2024, 10, 14).date(): "14OCT24",
        datetime.datetime(2024, 10, 21).date(): "21OCT24",
        datetime.datetime(2024, 10, 28).date(): "28OCT24",
        datetime.datetime(2024, 11, 4).date(): "04NOV24",
        datetime.datetime(2024, 11, 11).date(): "11NOV24",
        datetime.datetime(2024, 11, 18).date(): "18NOV24",
        datetime.datetime(2024, 11, 25).date(): "25NOV24",
        datetime.datetime(2024, 12, 2).date(): "02DEC24",
        datetime.datetime(2024, 12, 9).date(): "09DEC24",
        datetime.datetime(2024, 12, 16).date(): "16DEC24",
        datetime.datetime(2024, 12, 23).date(): "23DEC24",
        datetime.datetime(2024, 12, 30).date(): "30DEC24",
    }

    today = datetime.datetime.now().date()

    nxt = 0
    for date_key, value in expiry.items():
        if next==1 and nxt==1:
            nxt=0
            print(value)
            return value
        if today <= date_key:
            if next==1 and nxt==0:
                nxt=1
                continue
            print(value)
            return value

def getNiftyExpiryDate_month(next=0):
    expiry = {
        datetime.datetime(2024, 3, 28).date(): "28MAR24",
        datetime.datetime(2024, 4, 25).date(): "25APR24",
        datetime.datetime(2024, 5, 30).date(): "30MAY24",
        datetime.datetime(2024, 6, 27).date(): "27JUN24",
        datetime.datetime(2024, 7, 25).date(): "25JUL24",
        datetime.datetime(2024, 8, 29).date(): "29AUG24",
        datetime.datetime(2024, 9, 26).date(): "26SEP24",
        datetime.datetime(2024, 10, 31).date(): "31OCT24",
        datetime.datetime(2024, 11, 28).date(): "28NOV24",
        datetime.datetime(2024, 12, 26).date(): "26DEC24",

    }
    today = datetime.datetime.now().date()
    nxt = 0
    for date_key, value in expiry.items():
        if next==1 and nxt==1:
            nxt=0
            print(value)
            return value
        if today <= date_key:
            if next==1 and nxt==0:
                nxt=1
                continue
            print(value)
            return value

def getBankNiftyExpiryDate_month(next=0):
    expiry = {
        datetime.datetime(2024, 3, 27).date(): "27MAR24",
        datetime.datetime(2024, 4, 30).date(): "30APR24",
        datetime.datetime(2024, 5, 29).date(): "29MAY24",
        datetime.datetime(2024, 6, 26).date(): "26JUN24",
        datetime.datetime(2024, 7, 31).date(): "31JUL24",
        datetime.datetime(2024, 8, 28).date(): "28AUG24",
        datetime.datetime(2024, 9, 25).date(): "25SEP24",
        datetime.datetime(2024, 10, 30).date(): "30OCT24",
        datetime.datetime(2024, 11, 27).date(): "27NOV24",
        datetime.datetime(2024, 12, 24).date(): "24DEC24",

    }

    today = datetime.datetime.now().date()
    nxt = 0
    for date_key, value in expiry.items():
        if next==1 and nxt==1:
            nxt=0
            print(value)
            return value
        if today <= date_key:
            if next==1 and nxt==0:
                nxt=1
                continue
            print(value)
            return value

def getFinNiftyExpiryDate_month(next=0):
    expiry = {datetime.datetime(2024, 2, 20).date(): "20FEB24",
              datetime.datetime(2024, 3, 26).date(): "26MAR24",
              datetime.datetime(2024, 4, 30).date(): "30APR24",
              datetime.datetime(2024, 5, 28).date(): "28MAY24",
              datetime.datetime(2024, 6, 25).date(): "25JUN24",
              datetime.datetime(2024, 7, 30).date(): "30JUL24",
              datetime.datetime(2024, 8, 27).date(): "27AUG24",
              datetime.datetime(2024, 9, 24).date(): "24SEP24",
              datetime.datetime(2024, 10, 29).date(): "29OCT24",
              datetime.datetime(2024, 11, 26).date(): "26NOV24",
              datetime.datetime(2024, 12, 31).date(): "31DEC24",
              }
    today = datetime.datetime.now().date()
    nxt = 0
    for date_key, value in expiry.items():
        if next==1 and nxt==1:
            nxt=0
            print(value)
            return value
        if today <= date_key:
            if next==1 and nxt==0:
                nxt=1
                continue
            print(value)
            return value

def getMidCapNiftyExpiryDate_month(next=0):
    expiry = {datetime.datetime(2024, 5, 27).date(): "27MAY24",
              datetime.datetime(2024, 6, 24).date(): "24JUN24",
              datetime.datetime(2024, 7, 29).date(): "29JUL24",
              datetime.datetime(2024, 8, 26).date(): "26AUG24",
              datetime.datetime(2024, 9, 30).date(): "30SEP24",
              datetime.datetime(2024, 10, 28).date(): "28OCT24",
              datetime.datetime(2024, 11, 25).date(): "25NOV24",
              datetime.datetime(2024, 12, 30).date(): "30DEC24",
              }
    today = datetime.datetime.now().date()
    nxt = 0
    for date_key, value in expiry.items():
        if next==1 and nxt==1:
            nxt=0
            print(value)
            return value
        if today <= date_key:
            if next==1 and nxt==0:
                nxt=1
                continue
            print(value)
            return value


def getExpiryDate(expiry,next=0):
    today = datetime.datetime.now().date()
    nxt = 0
    for date_key, value in expiry.items():
        if next==1 and nxt==1:
            nxt=0
            print(value)
            return value
        if today <= date_key:
            if next==1 and nxt==0:
                nxt=1
                continue
            print(value)
            return value

def getCurrentExpiry_month(stock,next_exp=0):
    if stock == "BANKNIFTY":
        return getBankNiftyExpiryDate_month(next_exp)
    elif stock == "NIFTY":
        return getNiftyExpiryDate_month(next_exp)
    elif stock == "FINNIFTY":
        return getFinNiftyExpiryDate_month(next_exp)
    elif stock == "MIDCPNIFTY":
        return getMidCapNiftyExpiryDate_month(next_exp)
    elif stock == "GOLD":
        return getExpiryDate(mcx_expiries['GOLD'],next_exp)
    elif stock == "GOLDM":
        return getExpiryDate(mcx_expiries['GOLDM'],next_exp)
    elif stock == "GOLDGUINEA":
        return getExpiryDate(mcx_expiries['GOLDGUINEA'],next_exp)
    elif stock == "GOLDPETAL":
        return getExpiryDate(mcx_expiries['GOLDPETAL'],next_exp)
    elif stock == "SILVER":
        return getExpiryDate(mcx_expiries['SILVER'],next_exp)
    elif stock == "SILVERM":
        return getExpiryDate(mcx_expiries['SILVERM'],next_exp)
    elif stock == "SILVERMIC":
        return getExpiryDate(mcx_expiries['SILVERMIC'],next_exp)
    elif stock == "CRUDEOIL":
        return getExpiryDate(mcx_expiries['CRUDEOIL'],next_exp)
    elif stock == "CRUDEOILM":
        return getExpiryDate(mcx_expiries['CRUDEOILM'],next_exp)
    else:
        return getNiftyExpiryDate_month(next_exp)

def getIndexSpot(stock):
    if stock == "BANKNIFTY":
        name = "NSE:BANKNIFTY"
    elif stock == "NIFTY":
        name = "NSE:NIFTY"
    elif stock == "FINNIFTY":
        name = "NSE:FINNIFTY"
    elif stock == "MIDCPNIFTY":
        name = "NSE:NIFTY MID SELECT"

    return name

def getOptionFormat(stock, intExpiry, strike, ce_pe):
    return "NFO:" + str(stock) + str(intExpiry)+str(strike)+str(ce_pe)

def getFutureFormat(stock, intExpiry):
    if stock in mcx_expiries.keys():
        return "MCX:"+str(stock)+str(intExpiry)+str('FUT')
    else:
        return "NFO:"+str(stock)+str(intExpiry)+str('FUT')

def getLTP(instrument):
    url = "http://localhost:4000/ltp?instrument=" + instrument
    try:
        resp = requests.get(url)
    except Exception as e:
        print(e)
    data = resp.json()
    return data

def manualLTP(symbol,hist_obj):
    # global hist_obj
    exch = symbol[:3]
    sym = symbol[4:]
    tok = get_tokens(symbol)
    ltp = hist_obj.ltpData(exch, symbol, tok)
    return (ltp['data']['ltp'])
def placeOrder(inst ,t_type,qty,order_type,price,variety, papertrading=0):
    global trading_obj
    variety = 'NORMAL'
    exch = inst[:3]
    symbol_name = inst[4:]
    if(order_type=="MARKET"):
        price = 0
    #papertrading = 0 #if this is 1, then real trades will be placed
    token = get_tokens(inst)

    try:
        if (papertrading == 1):
            Targetorderparams = {
                "variety": "NORMAL",
                "tradingsymbol": symbol_name,
                "symboltoken": token,
                "transactiontype": t_type,
                "exchange": exch,
                "ordertype": order_type,
                "producttype": "INTRADAY",
                "duration": "DAY",
                "price": price,
                "squareoff": 0,
                "stoploss": 0,
                "triggerprice": 0,
                "trailingStopLoss": 0,
                "quantity": qty
            }

            print(Targetorderparams)
            orderId = trading_obj.placeOrder(Targetorderparams)
            print("The order id is: {}".format(orderId))
            return orderId
        else:
            return 0
    except Exception as e:
        traceback.print_exc()
        print("Order placement failed: {}".format(e.message))

def getHistorical(ticker,interval,duration):
    exch = ticker[:3]
    sym = ticker[4:]
    tok = get_tokens(ticker)

    time_intervals = {
        1: "ONE_MINUTE",
        3: "THREE_MINUTE",
        5: "FIVE_MINUTE",
        10: "TEN_MINUTE",
        15: "FIFTEEN_MINUTE",
        30: "THIRTY_MINUTE",
        60: "ONE_HOUR"
    }

    interval_str = time_intervals.get(interval, "Key not found")
    interval_str = "ONE_MINUTE"

    #find todate
    current_time = datetime.datetime.now()
    previous_minute_time = current_time - timedelta(minutes=1)
    start_date = previous_minute_time - timedelta(days=duration)
    to_date_string = previous_minute_time.strftime("%Y-%m-%d %H:%M")
    start_date_string = start_date.strftime("%Y-%m-%d %H:%M")

    historyparams = {
        "exchange": str(exch),
        #  "tradingsymbol":str(sym),
        "symboltoken": str(tok),
        "interval": interval_str,
        "fromdate": start_date_string,
        "todate": to_date_string
    }
    hist_data = hist_obj.getCandleData(historicDataParams= historyparams)
    hist_data = pd.DataFrame(hist_data['data'])
    hist_data.columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    hist_data['datetime2'] = hist_data['timestamp'].copy()
    hist_data['timestamp'] = pd.to_datetime(hist_data['timestamp'])
    hist_data.set_index('timestamp', inplace=True)
    finaltimeframe = str(interval)  + "min"

    # Resample to a specific time frame, for example, 30 minutes
    resampled_df = hist_data.resample(finaltimeframe).agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum',
        'datetime2': 'first'
    })

    # If you want to fill any missing values with a specific method, you can use fillna
    #resampled_df = resampled_df.fillna(method='ffill')  # Forward fill

    resampled_df = resampled_df.dropna(subset=['open'])
    return (resampled_df)

def getHistorical_old(ticker,interval,duration):
    exch = ticker[:3]
    sym = ticker[4:]
    tok = get_tokens(ticker)

    time_intervals = {
        1: "ONE_MINUTE",
        3: "THREE_MINUTE",
        5: "FIVE_MINUTE",
        10: "TEN_MINUTE",
        15: "FIFTEEN_MINUTE",
        30: "THIRTY_MINUTE",
        60: "ONE_HOUR"
    }

    interval_str = time_intervals.get(interval, "Key not found")

    #find todate
    current_time = datetime.datetime.now()
    previous_minute_time = current_time - timedelta(minutes=1)
    start_date = previous_minute_time - timedelta(days=duration)
    to_date_string = previous_minute_time.strftime("%Y-%m-%d %H:%M")
    start_date_string = start_date.strftime("%Y-%m-%d %H:%M")

    historyparams = {
        "exchange": str(exch),
        #  "tradingsymbol":str(sym),
        "symboltoken": str(tok),
        "interval": interval_str,
        "fromdate": start_date_string,
        "todate": to_date_string
    }
    hist_data = hist_obj.getCandleData(historicDataParams= historyparams)
    hist_data = pd.DataFrame(hist_data['data'])
    hist_data.columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    return (hist_data)