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


# import time
# import requests
# import datetime 
from datetime import timedelta, datetime
# from pytz import timezone
# import pandas as pd
from pya3 import *


######PIVOT POINTS##########################
####################__INPUT__#####################



def getNiftyExpiryDate(next=0):
    expiry = {
        datetime(2023, 11, 16).date(): "16NOV23",
        datetime(2023, 11, 23).date(): "23NOV23",
        datetime(2023, 11, 30).date(): "30NOV23",
        datetime(2023, 12, 7).date(): "07DEC23",
        datetime(2023, 12, 14).date(): "14DEC23",
        datetime(2023, 12, 21).date(): "21DEC23",
        datetime(2023, 12, 28).date(): "28DEC23",
        datetime(2024, 1, 4).date(): "04JAN24",
        datetime(2024, 1, 11).date(): "11JAN24",
        datetime(2024, 1, 18).date(): "18JAN24",
        datetime(2024, 1, 25).date(): "25JAN24",
        datetime(2024, 2, 1).date(): "01FEB24",
        datetime(2024, 2, 8).date(): "08FEB24",
        datetime(2024, 2, 15).date(): "15FEB24",
        datetime(2024, 2, 22).date(): "22FEB24",
        datetime(2024, 2, 29).date(): "29FEB24",
        datetime(2024, 3, 7).date(): "07MAR24",
        datetime(2024, 3, 14).date(): "14MAR24",
        datetime(2024, 3, 21).date(): "21MAR24",
        datetime(2024, 3, 28).date(): "28MAR24",
        datetime(2024, 4, 4).date(): "04APR24",
        datetime(2024, 4, 10).date(): "10APR24",
        datetime(2024, 4, 18).date(): "18APR24",
        datetime(2024, 4, 25).date(): "25APR24",
        datetime(2024, 5, 2).date(): "02MAY24",
        datetime(2024, 5, 9).date(): "09MAY24",
        datetime(2024, 5, 16).date(): "16MAY24",
        datetime(2024, 5, 23).date(): "23MAY24",
        datetime(2024, 5, 30).date(): "30MAY24",
        datetime(2024, 6, 6).date(): "06JUN24",
        datetime(2024, 6, 13).date(): "13JUN24",
        datetime(2024, 6, 20).date(): "20JUN24",
        datetime(2024, 6, 27).date(): "27JUN24",
        datetime(2024, 7, 4).date(): "04JUL24",
        datetime(2024, 7, 11).date(): "11JUL24",
        datetime(2024, 7, 18).date(): "18JUL24",
        datetime(2024, 7, 25).date(): "25JUL24",
        datetime(2024, 8, 1).date(): "01AUG24",
        datetime(2024, 8, 8).date(): "08AUG24",
        datetime(2024, 8, 14).date(): "14AUG24",
        datetime(2024, 8, 22).date(): "22AUG24",
        datetime(2024, 8, 29).date(): "29AUG24",
        datetime(2024, 9, 5).date(): "05SEP24",
        datetime(2024, 9, 12).date(): "12SEP24",
        datetime(2024, 9, 19).date(): "19SEP24",
        datetime(2024, 9, 26).date(): "26SEP24",
        datetime(2024, 10, 3).date(): "03OCT24",
        datetime(2024, 10, 10).date(): "10OCT24",
        datetime(2024, 10, 17).date(): "17OCT24",
        datetime(2024, 10, 24).date(): "24OCT24",
        datetime(2024, 10, 31).date(): "31OCT24",
        datetime(2024, 11, 7).date(): "07NOV24",
        datetime(2024, 11, 14).date(): "14NOV24",
        datetime(2024, 11, 21).date(): "21NOV24",
        datetime(2024, 11, 28).date(): "28NOV24",
        datetime(2024, 12, 5).date(): "05DEC24",
        datetime(2024, 12, 12).date(): "12DEC24",
        datetime(2024, 12, 19).date(): "19DEC24",
        datetime(2024, 12, 26).date(): "26DEC24",

    }
    today = datetime.now().date()
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
        datetime(2023, 11, 15).date(): "15NOV23",
        datetime(2023, 11, 22).date(): "22NOV23",
        datetime(2023, 11, 30).date(): "30NOV23",
        datetime(2023, 12, 6).date(): "06DEC23",
        datetime(2023, 12, 13).date(): "13DEC23",
        datetime(2023, 12, 20).date(): "20DEC23",
        datetime(2023, 12, 28).date(): "08DEC23",
        datetime(2024, 1, 3).date(): "03JAN24",
        datetime(2024, 1, 10).date(): "10JAN24",
        datetime(2024, 1, 17).date(): "17JAN24",
        datetime(2024, 1, 25).date(): "25JAN24",
        datetime(2024, 1, 31).date(): "31JAN24",
        datetime(2024, 2, 7).date(): "07FEB24",
        datetime(2024, 2, 14).date(): "14FEB24",
        datetime(2024, 2, 21).date(): "21FEB24",
        datetime(2024, 2, 29).date(): "29FEB24",
        datetime(2024, 3, 6).date(): "06MAR24",
        datetime(2024, 3, 13).date(): "13MAR24",
        datetime(2024, 3, 20).date(): "20MAR24",
        datetime(2024, 3, 27).date(): "27MAR24",
        datetime(2024, 4, 3).date(): "03APR24",
        datetime(2024, 4, 10).date(): "10APR24",
        datetime(2024, 4, 16).date(): "16APR24",
        datetime(2024, 4, 24).date(): "24APR24",
        datetime(2024, 4, 30).date(): "30APR24",
        datetime(2024, 5, 8).date(): "08MAY24",
        datetime(2024, 5, 15).date(): "15MAY24",
        datetime(2024, 5, 22).date(): "22MAY24",
        datetime(2024, 5, 29).date(): "29MAY24",
        datetime(2024, 6, 5).date(): "05JUN24",
        datetime(2024, 6, 12).date(): "12JUN24",
        datetime(2024, 6, 19).date(): "19JUN24",
        datetime(2024, 6, 26).date(): "26JUN24",
        datetime(2024, 7, 3).date(): "03JUL24",
        datetime(2024, 7, 10).date(): "10JUL24",
        datetime(2024, 7, 16).date(): "16JUL24",
        datetime(2024, 7, 24).date(): "24JUL24",
        datetime(2024, 7, 31).date(): "31JUL24",
        datetime(2024, 8, 7).date(): "07AUG24",
        datetime(2024, 8, 14).date(): "14AUG24",
        datetime(2024, 8, 21).date(): "21AUG24",
        datetime(2024, 8, 28).date(): "28AUG24",
        datetime(2024, 9, 4).date(): "04SEP24",
        datetime(2024, 9, 11).date(): "11SEP24",
        datetime(2024, 9, 18).date(): "18SEP24",
        datetime(2024, 9, 25).date(): "25SEP24",
        datetime(2024, 10, 1).date(): "01OCT24",
        datetime(2024, 10, 9).date(): "09OCT24",
        datetime(2024, 10, 16).date(): "16OCT24",
        datetime(2024, 10, 23).date(): "23OCT24",
        datetime(2024, 10, 30).date(): "30OCT24",
        datetime(2024, 11, 6).date(): "06NOV24",
        datetime(2024, 11, 13).date(): "13NOV24",
        datetime(2024, 11, 20).date(): "20NOV24",
        datetime(2024, 11, 27).date(): "27NOV24",
        datetime(2024, 12, 4).date(): "04DEC24",
        datetime(2024, 12, 11).date(): "11DEC24",
        datetime(2024, 12, 18).date(): "18DEC24",
        datetime(2024, 12, 24).date(): "24DEC24",
    }
    today = datetime.now().date()
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
        datetime(2024, 2, 20).date(): "20FEB24",
        datetime(2024, 2, 27).date(): "27FEB24",
        datetime(2024, 3, 5).date(): "05MAR24",
        datetime(2024, 3, 12).date(): "12MAR24",
        datetime(2024, 3, 19).date(): "19MAR24",
        datetime(2024, 3, 26).date(): "26MAR24",
        datetime(2024, 4, 2).date(): "02APR24",
        datetime(2024, 4, 9).date(): "09APR24",
        datetime(2024, 4, 16).date(): "16APR24",
        datetime(2024, 4, 23).date(): "23APR24",
        datetime(2024, 4, 30).date(): "30APR24",
        datetime(2024, 5, 7).date(): "07MAY24",
        datetime(2024, 5, 14).date(): "14MAY24",
        datetime(2024, 5, 21).date(): "21MAY24",
        datetime(2024, 5, 28).date(): "28MAY24",
        datetime(2024, 6, 4).date(): "04JUN24",
        datetime(2024, 6, 11).date(): "11JUN24",
        datetime(2024, 6, 18).date(): "18JUN24",
        datetime(2024, 6, 25).date(): "25JUN24",
        datetime(2024, 7, 2).date(): "02JUL24",
        datetime(2024, 7, 9).date(): "09JUL24",
        datetime(2024, 7, 16).date(): "16JUL24",
        datetime(2024, 7, 23).date(): "23JUL24",
        datetime(2024, 7, 30).date(): "30JUL24",
        datetime(2024, 8, 6).date(): "06AUG24",
        datetime(2024, 8, 13).date(): "13AUG24",
        datetime(2024, 8, 20).date(): "20AUG24",
        datetime(2024, 8, 27).date(): "27AUG24",
        datetime(2024, 9, 3).date(): "03SEP24",
        datetime(2024, 9, 10).date(): "10SEP24",
        datetime(2024, 9, 17).date(): "17SEP24",
        datetime(2024, 9, 24).date(): "24SEP24",
        datetime(2024, 10, 1).date(): "01OCT24",
        datetime(2024, 10, 8).date(): "08OCT24",
        datetime(2024, 10, 15).date(): "15OCT24",
        datetime(2024, 10, 22).date(): "22OCT24",
        datetime(2024, 10, 29).date(): "29OCT24",
        datetime(2024, 11, 5).date(): "05NOV24",
        datetime(2024, 11, 12).date(): "12NOV24",
        datetime(2024, 11, 19).date(): "19NOV24",
        datetime(2024, 11, 26).date(): "26NOV24",
        datetime(2024, 12, 3).date(): "03DEC24",
        datetime(2024, 12, 10).date(): "10DEC24",
        datetime(2024, 12, 17).date(): "17DEC24",
        datetime(2024, 12, 24).date(): "24DEC24",
        datetime(2024, 12, 31).date(): "31DEC24",
    }

    today = datetime.now().date()

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
        datetime(2024, 5, 13).date(): "13MAY24",
        datetime(2024, 5, 20).date(): "20MAY24",
        datetime(2024, 5, 27).date(): "27MAY24",
        datetime(2024, 6, 3).date(): "03JUN24",
        datetime(2024, 6, 10).date(): "10JUN24",
        datetime(2024, 6, 17).date(): "17JUN24",
        datetime(2024, 6, 24).date(): "24JUN24",
        datetime(2024, 7, 1).date(): "01JUL24",
        datetime(2024, 7, 8).date(): "08JUL24",
        datetime(2024, 7, 15).date(): "15JUL24",
        datetime(2024, 7, 22).date(): "22JUL24",
        datetime(2024, 7, 29).date(): "29JUL24",
        datetime(2024, 8, 5).date(): "05AUG24",
        datetime(2024, 8, 12).date(): "12AUG24",
        datetime(2024, 8, 19).date(): "19AUG24",
        datetime(2024, 8, 26).date(): "26AUG24",
        datetime(2024, 9, 2).date(): "02SEP24",
        datetime(2024, 9, 9).date(): "09SEP24",
        datetime(2024, 9, 16).date(): "16SEP24",
        datetime(2024, 9, 23).date(): "23SEP24",
        datetime(2024, 9, 30).date(): "30SEP24",
        datetime(2024, 10, 7).date(): "07OCT24",
        datetime(2024, 10, 14).date(): "14OCT24",
        datetime(2024, 10, 21).date(): "21OCT24",
        datetime(2024, 10, 28).date(): "28OCT24",
        datetime(2024, 11, 4).date(): "04NOV24",
        datetime(2024, 11, 11).date(): "11NOV24",
        datetime(2024, 11, 18).date(): "18NOV24",
        datetime(2024, 11, 25).date(): "25NOV24",
        datetime(2024, 12, 2).date(): "02DEC24",
        datetime(2024, 12, 9).date(): "09DEC24",
        datetime(2024, 12, 16).date(): "16DEC24",
        datetime(2024, 12, 23).date(): "23DEC24",
        datetime(2024, 12, 30).date(): "30DEC24",
    }

    today = datetime.now().date()

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
        datetime(2024, 3, 28).date(): "28MAR24",
        datetime(2024, 4, 25).date(): "25APR24",
        datetime(2024, 5, 30).date(): "30MAY24",
        datetime(2024, 6, 27).date(): "27JUN24",
        datetime(2024, 7, 25).date(): "25JUL24",
        datetime(2024, 8, 29).date(): "29AUG24",
        datetime(2024, 9, 26).date(): "26SEP24",
        datetime(2024, 10, 31).date(): "31OCT24",
        datetime(2024, 11, 28).date(): "28NOV24",
        datetime(2024, 12, 26).date(): "26DEC24",

    }
    today = datetime.now().date()
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
        datetime(2024, 3, 27).date(): "27MAR24",
        datetime(2024, 4, 30).date(): "30APR24",
        datetime(2024, 5, 29).date(): "29MAY24",
        datetime(2024, 6, 26).date(): "26JUN24",
        datetime(2024, 7, 31).date(): "31JUL24",
        datetime(2024, 8, 28).date(): "28AUG24",
        datetime(2024, 9, 25).date(): "25SEP24",
        datetime(2024, 10, 30).date(): "30OCT24",
        datetime(2024, 11, 27).date(): "27NOV24",
        datetime(2024, 12, 24).date(): "24DEC24",

    }

    today = datetime.now().date()
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
    expiry = {datetime(2024, 2, 20).date(): "20FEB24",
              datetime(2024, 3, 26).date(): "26MAR24",
              datetime(2024, 4, 30).date(): "30APR24",
              datetime(2024, 5, 28).date(): "28MAY24",
              datetime(2024, 6, 25).date(): "25JUN24",
              datetime(2024, 7, 30).date(): "30JUL24",
              datetime(2024, 8, 27).date(): "27AUG24",
              datetime(2024, 9, 24).date(): "24SEP24",
              datetime(2024, 10, 29).date(): "29OCT24",
              datetime(2024, 11, 26).date(): "26NOV24",
              datetime(2024, 12, 31).date(): "31DEC24",
              }
    today = datetime.now().date()
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
    expiry = {datetime(2024, 5, 27).date(): "27MAY24",
              datetime(2024, 6, 24).date(): "24JUN24",
              datetime(2024, 7, 29).date(): "29JUL24",
              datetime(2024, 8, 26).date(): "26AUG24",
              datetime(2024, 9, 30).date(): "30SEP24",
              datetime(2024, 10, 28).date(): "28OCT24",
              datetime(2024, 11, 25).date(): "25NOV24",
              datetime(2024, 12, 30).date(): "30DEC24",
              }
    today = datetime.now().date()
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
    today = datetime.now().date()
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


mcx_expiries = {
    "GOLD":             {datetime(2024, 6, 5).date(): "05JUN24",
                         datetime(2024, 8, 5).date(): "05AUG24",
                         datetime(2024, 10, 4).date(): "04OCT24",
                         datetime(2024, 12, 5).date(): "05DEC24",
                         datetime(2025, 2, 5).date(): "05FEB24",
                         datetime(2025, 4, 4).date(): "05APR24",},
    "GOLDM":            {datetime(2024, 6, 5).date(): "05JUN24",
                         datetime(2024, 7, 5).date(): "05JUL24",
                         datetime(2024, 8, 5).date(): "05AUG24",
                         datetime(2024, 9, 5).date(): "05SEP24",
                         datetime(2024, 10, 4).date(): "04OCT24",
                         datetime(2024, 11, 5).date(): "05NOV24",
                         datetime(2024, 12, 5).date(): "05DEC24",},
    "GOLDGUINEA":       {datetime(2024, 5, 31).date(): "31MAY24",
                         datetime(2024, 6, 28).date(): "28JUN24",
                         datetime(2024, 7, 31).date(): "31JUL24",
                         datetime(2024, 8, 30).date(): "30AUG24",
                         datetime(2024, 9, 30).date(): "30SEP24",
                         datetime(2024, 10, 31).date(): "31OCT24",
                         datetime(2024, 11, 29).date(): "29NOV24",
                         datetime(2024, 12, 31).date(): "31DEC24"},
    "GOLDPETAL":        {datetime(2024, 2, 29).date(): "29FEB24",
                         datetime(2024, 3, 29).date(): "29MAR24",
                         datetime(2024, 4, 30).date(): "30APR24",
                         datetime(2024, 5, 31).date(): "31MAY24",
                         datetime(2024, 6, 28).date(): "28JUN24",
                         datetime(2024, 7, 31).date(): "31JUL24",
                         datetime(2024, 8, 30).date(): "30AUG24",
                         datetime(2024, 9, 30).date(): "30SEP24",
                         datetime(2024, 10, 31).date(): "31OCT24",
                         datetime(2024, 11, 29).date(): "29NOV24",
                         datetime(2024, 12, 31).date(): "31DEC24"},
    "SILVER":           {datetime(2024, 5, 3).date(): "03MAY24",
                         datetime(2024, 7, 5).date(): "05JUL24",
                         datetime(2024, 9, 5).date(): "05SEP24",
                         datetime(2024, 12, 5).date(): "05DEC24"},
    "SILVERM":          {datetime(2024, 2, 29).date(): "29FEB24",
                         datetime(2024, 4, 30).date(): "30APR24",
                         datetime(2024, 6, 28).date(): "28JUN24",
                         datetime(2024, 8, 30).date(): "30AUG24",
                         datetime(2024, 11, 29).date(): "29NOV24",},
    "SILVERMIC":        {datetime(2024, 2, 29).date(): "29FEB24",
                         datetime(2024, 4, 30).date(): "30APR24",
                         datetime(2024, 6, 28).date(): "28JUN24",
                         datetime(2024, 8, 30).date(): "30AUG24",
                         datetime(2024, 11, 29).date(): "29NOV24",},
    "CRUDEOIL":         {datetime(2024, 2, 16).date(): "16FEB24",
                         datetime(2024, 3, 19).date(): "19MAR24",
                         datetime(2024, 4, 19).date(): "19APR24",
                         datetime(2024, 5, 20).date(): "20MAY24",
                         datetime(2024, 6, 18).date(): "18JUN24",
                         datetime(2024, 7, 19).date(): "19JUL24",
                         datetime(2024, 8, 19).date(): "19AUG24",
                         datetime(2024, 9, 19).date(): "19SEP24",
                         datetime(2024, 10, 21).date(): "21OCT24",
                         datetime(2024, 11, 19).date(): "19NOV24",
                         datetime(2024, 12, 18).date(): "18DEC24"},
    "CRUDEOILM":         {datetime(2024, 2, 16).date(): "16FEB24",
                          datetime(2024, 3, 19).date(): "19MAR24",
                          datetime(2024, 4, 19).date(): "19APR24",
                          datetime(2024, 5, 20).date(): "20MAY24",
                          datetime(2024, 6, 18).date(): "18JUN24",
                          datetime(2024, 7, 19).date(): "19JUL24",
                          datetime(2024, 8, 19).date(): "19AUG24",
                          datetime(2024, 9, 19).date(): "19SEP24",
                          datetime(2024, 10, 21).date(): "21OCT24",
                          datetime(2024, 11, 19).date(): "19NOV24",
                          datetime(2024, 12, 18).date(): "18DEC24"}

}

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
        name = "NSE:NIFTY BANK"
    elif stock == "NIFTY":
        name = "NSE:NIFTY 50"
    elif stock == "FINNIFTY":
        name = "NSE:NIFTY FIN SERVICE"
    elif stock == "MIDCPNIFTY":
        name = "NSE:NIFTY MIDCAP SELECT"
    return name

def getOptionFormat(stock, intExpiry, strike, ce_pe):
    return "NFO:" + str(stock) + str(intExpiry)+str(ce_pe[0])+str(strike)

def getFutureFormat(stock, intExpiry):
    if stock in mcx_expiries.keys():
        return "MCX:"+str(stock)+str(intExpiry)
    else:
        return "NFO:"+str(stock)+str(intExpiry)+str('F')

def getLTP(instrument):
    url = "http://localhost:4000/ltp?instrument=" + instrument
    try:
        resp = requests.get(url)
    except Exception as e:
        print(e)
    data = resp.json()
    return data

def manualLTP(symbol,alice):
    exch = symbol[:3]
    symb = symbol[4:]
    nifty_ltp = alice.get_scrip_info(alice.get_instrument_by_symbol(exch, symb))
    print(nifty_ltp)
    a = float(nifty_ltp['LTP'])
    return a

def placeOrder(inst ,t_type,qty,order_type,price,variety, alice, papertrading=0):
    exch = inst[:3]
    symb = inst[4:]
    #paperTrading = 0 #if this is 1, then real trades will be placed
    if( t_type=="BUY"):
        t_type=TransactionType.Buy
    else:
        t_type=TransactionType.Sell

    #OrderType.Market, OrderType.Limit, OrderType.StopLossMarket, OrderType.StopLossLimit
    #ProductType.Delivery, ProductType.Intraday

    if(order_type=="MARKET"):
        order_type=OrderType.Market
    elif(order_type=="LIMIT"):
        order_type=OrderType.Limit

    if variety == "regular":
        is_amo = False
    else:
        is_amo = True

    try:
        if(papertrading == 1):
            order_id = alice.place_order(transaction_type = t_type,
                                         instrument = alice.get_instrument_by_symbol(exch, symb),
                                         quantity = qty,
                                         order_type = order_type,
                                         product_type = ProductType.Intraday,
                                         price = float(price),
                                         trigger_price = float(price),
                                         stop_loss = None,
                                         square_off = None,
                                         trailing_sl = None,
                                         is_amo = is_amo,
                                         order_tag='order1')
            print(order_id)
            return order_id

        else:
            order_id=0
            return order_id

    except Exception as e:
        print(" => ", symb , "Failed : {} ".format(e))

def getHistorical(ticker,interval,duration, alice, index):
    exch = ticker[:3]
    stockname = ticker[4:]
    instrument = alice.get_instrument_by_symbol(exch, stockname)

    to_datetime = datetime.now()
    from_datetime = datetime.now() - timedelta(days=duration)     # From last & days

    ## ["1", "D"]
    if index == "INDEX":
        indices = True
    else:
        indices = False

    hist_data = alice.get_historical(instrument, from_datetime, to_datetime, 1, indices)
    hist_data = pd.DataFrame(hist_data)
    print(hist_data)

    # Convert string columns to float
    hist_data['open'] = pd.to_numeric(hist_data['open'])
    hist_data['high'] = pd.to_numeric(hist_data['high'])
    hist_data['low'] = pd.to_numeric(hist_data['low'])
    hist_data['close'] = pd.to_numeric(hist_data['close'])
    hist_data['volume'] = pd.to_numeric(hist_data['volume'])
    hist_data['datetime2'] = hist_data['datetime'].copy()
    hist_data['datetime'] = pd.to_datetime(hist_data['datetime'])
    # Set 'datetime' as the index
    hist_data.set_index('datetime', inplace=True)
    # Update the format of the datetime index and add 5 hours and 30 minutes for IST
    hist_data.index = hist_data.index.floor('min')  # Floor to minutes
    #print(hist_data)

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

    #print(resampled_df)
    resampled_df = resampled_df.dropna(subset=['open'])
    return resampled_df


