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

# from NorenApi import NorenApi
import datetime
import time
import requests
from datetime import timedelta
from pytz import timezone
import pandas as pd
import ast
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


# with open('user_id.txt','r') as f:
#     user_id = f.read()
######PIVOT POINTS##########################
####################__INPUT__#####################

exchange1 = "NSE"

# def getNiftyExpiryDate():
#     nifty_expiry = {
#         datetime.datetime(2024, 4, 18).date(): "24418",
#         datetime.datetime(2024, 4, 25).date(): "24425",
#         datetime.datetime(2024, 5, 2).date(): "24502",
#         datetime.datetime(2024, 5, 9).date(): "24509",
#         datetime.datetime(2024, 5, 16).date(): "24516",
#         datetime.datetime(2024, 5, 23).date(): "24523",
#         datetime.datetime(2024, 5, 30).date(): "24530",
#         datetime.datetime(2024, 6, 6).date(): "24606",
#         datetime.datetime(2024, 6, 13).date(): "24613",
#         datetime.datetime(2024, 6, 20).date(): "24620",
#         datetime.datetime(2024, 6, 27).date(): "24627",
#     }
#
#     today = datetime.datetime.now().date()
#
#     for date_key, value in nifty_expiry.items():
#         if today <= date_key:
#             print(value)
#             return value
#
# def getNiftyExpiryDate_month():
#     nifty_expiry = {
#         datetime.datetime(2024, 4, 25).date(): "24APR",
#         datetime.datetime(2024, 5, 30).date(): "24MAY",
#         datetime.datetime(2024, 6, 27).date(): "24JUN",
#     }
#
#     today = datetime.datetime.now().date()
#
#     for date_key, value in nifty_expiry.items():
#         if today <= date_key:
#             print(value)
#             return value
#
# def getBankNiftyExpiryDate():
#     banknifty_expiry = {
#         datetime.datetime(2024, 4, 16).date(): "24416",
#         datetime.datetime(2024, 4, 24).date(): "24424",
#         datetime.datetime(2024, 4, 30).date(): "24430",
#         datetime.datetime(2024, 5, 8).date(): "24508",
#         datetime.datetime(2024, 5, 15).date(): "24515",
#         datetime.datetime(2024, 5, 22).date(): "24522",
#         datetime.datetime(2024, 5, 29).date(): "24529",
#         datetime.datetime(2024, 6, 5).date(): "24605",
#         datetime.datetime(2024, 6, 12).date(): "24612",
#         datetime.datetime(2024, 6, 19).date(): "24619",
#         datetime.datetime(2024, 6, 26).date(): "24626",
#     }
#
#     today = datetime.datetime.now().date()
#
#     for date_key, value in banknifty_expiry.items():
#         if today <= date_key:
#             print(value)
#             return value
#
# def getBankNiftyExpiryDate_month():
#     banknifty_expiry = {
#
#         datetime.datetime(2024, 4, 30).date(): "24APR",
#         datetime.datetime(2024, 5, 29).date(): "24MAY",
#         datetime.datetime(2024, 6, 26).date(): "24JUN",
#     }
#
#     today = datetime.datetime.now().date()
#
#     for date_key, value in banknifty_expiry.items():
#         if today <= date_key:
#             print(value)
#             return value
#
#
# def getFinNiftyExpiryDate():
#     finnifty_expiry = {
#         datetime.datetime(2024, 4, 16).date(): "24416",
#         datetime.datetime(2024, 4, 23).date(): "24423",
#         datetime.datetime(2024, 4, 30).date(): "24430",
#         datetime.datetime(2024, 5, 7).date(): "24507",
#         datetime.datetime(2024, 5, 14).date(): "24514",
#         datetime.datetime(2024, 5, 21).date(): "24521",
#         datetime.datetime(2024, 5, 28).date(): "24528",
#         datetime.datetime(2024, 6, 4).date(): "24604",
#         datetime.datetime(2024, 6, 11).date(): "24611",
#         datetime.datetime(2024, 6, 18).date(): "24618",
#         datetime.datetime(2024, 6, 25).date(): "24625",
#     }
#
#     today = datetime.datetime.now().date()
#
#     for date_key, value in finnifty_expiry.items():
#         if today <= date_key:
#             print(value)
#             return value
#
# def getFinNiftyExpiryDate_month():
#     finnifty_expiry = {
#         datetime.datetime(2024, 4, 30).date(): "24APR",
#         datetime.datetime(2024, 5, 28).date(): "24MAY",
#         datetime.datetime(2024, 6, 25).date(): "24JUN",
#     }
#
#     today = datetime.datetime.now().date()
#
#     for date_key, value in finnifty_expiry.items():
#         if today <= date_key:
#             print(value)
#             return value

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
        datetime.datetime(2023, 11, 16).date(): "23N16",
        datetime.datetime(2023, 11, 23).date(): "23N23",
        datetime.datetime(2023, 11, 30).date(): "23N30",
        datetime.datetime(2023, 12, 7).date(): "23D07",
        datetime.datetime(2023, 12, 14).date(): "23D14",
        datetime.datetime(2023, 12, 21).date(): "23D21",
        datetime.datetime(2023, 12, 28).date(): "23D28",
        datetime.datetime(2024, 1, 4).date(): "24104",
        datetime.datetime(2024, 1, 11).date(): "24111",
        datetime.datetime(2024, 1, 18).date(): "24118",
        datetime.datetime(2024, 1, 25).date(): "24125",
        datetime.datetime(2024, 2, 1).date(): "24201",
        datetime.datetime(2024, 2, 8).date(): "24208",
        datetime.datetime(2024, 2, 15).date(): "24215",
        datetime.datetime(2024, 2, 22).date(): "24222",
        datetime.datetime(2024, 2, 29).date(): "24229",
        datetime.datetime(2024, 3, 7).date(): "24307",
        datetime.datetime(2024, 3, 14).date(): "24314",
        datetime.datetime(2024, 3, 21).date(): "24321",
        datetime.datetime(2024, 3, 28).date(): "24328",
        datetime.datetime(2024, 4, 4).date(): "24404",
        datetime.datetime(2024, 4, 10).date(): "24410",
        datetime.datetime(2024, 4, 18).date(): "24418",
        datetime.datetime(2024, 4, 25).date(): "24425",
        datetime.datetime(2024, 5, 2).date(): "24502",
        datetime.datetime(2024, 5, 9).date(): "24509",
        datetime.datetime(2024, 5, 16).date(): "24516",
        datetime.datetime(2024, 5, 23).date(): "24523",
        datetime.datetime(2024, 5, 30).date(): "24530",
        datetime.datetime(2024, 6, 6).date(): "24606",
        datetime.datetime(2024, 6, 13).date(): "24613",
        datetime.datetime(2024, 6, 20).date(): "24620",
        datetime.datetime(2024, 6, 27).date(): "24627",
        datetime.datetime(2024, 7, 4).date(): "24704",
        datetime.datetime(2024, 7, 11).date(): "24711",
        datetime.datetime(2024, 7, 18).date(): "24718",
        datetime.datetime(2024, 7, 25).date(): "24725",
        datetime.datetime(2024, 8, 1).date(): "24801",
        datetime.datetime(2024, 8, 8).date(): "24808",
        datetime.datetime(2024, 8, 14).date(): "24814",
        datetime.datetime(2024, 8, 22).date(): "24822",
        datetime.datetime(2024, 8, 29).date(): "24829",
        datetime.datetime(2024, 9, 5).date(): "24905",
        datetime.datetime(2024, 9, 12).date(): "24912",
        datetime.datetime(2024, 9, 19).date(): "24919",
        datetime.datetime(2024, 9, 26).date(): "24926",
        datetime.datetime(2024, 10, 3).date(): "24O03",
        datetime.datetime(2024, 10, 10).date(): "24O10",
        datetime.datetime(2024, 10, 17).date(): "24O17",
        datetime.datetime(2024, 10, 24).date(): "24O24",
        datetime.datetime(2024, 10, 31).date(): "24O31",
        datetime.datetime(2024, 11, 7).date(): "24N07",
        datetime.datetime(2024, 11, 14).date(): "24N14",
        datetime.datetime(2024, 11, 21).date(): "24N21",
        datetime.datetime(2024, 11, 28).date(): "24N28",
        datetime.datetime(2024, 12, 5).date(): "24D05",
        datetime.datetime(2024, 12, 12).date(): "24D12",
        datetime.datetime(2024, 12, 19).date(): "24D19",
        datetime.datetime(2024, 12, 26).date(): "24D26",
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
        datetime.datetime(2023, 11, 15).date(): "23N15",
        datetime.datetime(2023, 11, 22).date(): "23N22",
        datetime.datetime(2023, 11, 30).date(): "23N30",
        datetime.datetime(2023, 12, 6).date(): "23D06",
        datetime.datetime(2023, 12, 13).date(): "23D13",
        datetime.datetime(2023, 12, 20).date(): "23D20",
        datetime.datetime(2023, 12, 28).date(): "23D28",
        datetime.datetime(2024, 1, 3).date(): "24103",
        datetime.datetime(2024, 1, 10).date(): "24110",
        datetime.datetime(2024, 1, 17).date(): "24117",
        datetime.datetime(2024, 1, 25).date(): "24125",
        datetime.datetime(2024, 1, 31).date(): "24131",
        datetime.datetime(2024, 2, 7).date(): "24207",
        datetime.datetime(2024, 2, 14).date(): "24214",
        datetime.datetime(2024, 2, 21).date(): "24221",
        datetime.datetime(2024, 2, 29).date(): "24229",
        datetime.datetime(2024, 3, 6).date(): "24306",
        datetime.datetime(2024, 3, 13).date(): "24313",
        datetime.datetime(2024, 3, 20).date(): "24320",
        datetime.datetime(2024, 3, 27).date(): "24327",
        datetime.datetime(2024, 4, 3).date(): "24403",
        datetime.datetime(2024, 4, 10).date(): "24410",
        datetime.datetime(2024, 4, 16).date(): "24416",
        datetime.datetime(2024, 4, 24).date(): "24424",
        datetime.datetime(2024, 4, 30).date(): "24430",
        datetime.datetime(2024, 5, 8).date(): "24508",
        datetime.datetime(2024, 5, 15).date(): "24515",
        datetime.datetime(2024, 5, 22).date(): "24522",
        datetime.datetime(2024, 5, 29).date(): "24529",
        datetime.datetime(2024, 6, 5).date(): "24605",
        datetime.datetime(2024, 6, 12).date(): "24612",
        datetime.datetime(2024, 6, 19).date(): "24619",
        datetime.datetime(2024, 6, 26).date(): "24626",
        datetime.datetime(2024, 7, 3).date(): "24703",
        datetime.datetime(2024, 7, 10).date(): "24710",
        datetime.datetime(2024, 7, 16).date(): "24716",
        datetime.datetime(2024, 7, 24).date(): "24724",
        datetime.datetime(2024, 7, 31).date(): "24731",
        datetime.datetime(2024, 8, 7).date(): "24807",
        datetime.datetime(2024, 8, 14).date(): "24814",
        datetime.datetime(2024, 8, 21).date(): "24821",
        datetime.datetime(2024, 8, 28).date(): "24828",
        datetime.datetime(2024, 9, 4).date(): "24904",
        datetime.datetime(2024, 9, 11).date(): "24911",
        datetime.datetime(2024, 9, 18).date(): "24918",
        datetime.datetime(2024, 9, 25).date(): "24925",
        datetime.datetime(2024, 10, 1).date(): "24O01",
        datetime.datetime(2024, 10, 9).date(): "24O09",
        datetime.datetime(2024, 10, 16).date(): "24O16",
        datetime.datetime(2024, 10, 23).date(): "24O23",
        datetime.datetime(2024, 10, 30).date(): "24O30",
        datetime.datetime(2024, 11, 6).date(): "24N06",
        datetime.datetime(2024, 11, 13).date(): "24N13",
        datetime.datetime(2024, 11, 20).date(): "24N20",
        datetime.datetime(2024, 11, 27).date(): "24N27",
        datetime.datetime(2024, 12, 4).date(): "24D04",
        datetime.datetime(2024, 12, 11).date(): "24D11",
        datetime.datetime(2024, 12, 18).date(): "24D18",
        datetime.datetime(2024, 12, 24).date(): "24D24",
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
        datetime.datetime(2024, 2, 20).date(): "24220",
        datetime.datetime(2024, 2, 27).date(): "24227",
        datetime.datetime(2024, 3, 5).date(): "24305",
        datetime.datetime(2024, 3, 12).date(): "24312",
        datetime.datetime(2024, 3, 19).date(): "24319",
        datetime.datetime(2024, 3, 26).date(): "24326",
        datetime.datetime(2024, 4, 2).date(): "24402",
        datetime.datetime(2024, 4, 9).date(): "24409",
        datetime.datetime(2024, 4, 16).date(): "24416",
        datetime.datetime(2024, 4, 23).date(): "24423",
        datetime.datetime(2024, 4, 30).date(): "24430",
        datetime.datetime(2024, 5, 7).date(): "24507",
        datetime.datetime(2024, 5, 14).date(): "24514",
        datetime.datetime(2024, 5, 21).date(): "24521",
        datetime.datetime(2024, 5, 28).date(): "24528",
        datetime.datetime(2024, 6, 4).date(): "24604",
        datetime.datetime(2024, 6, 11).date(): "24611",
        datetime.datetime(2024, 6, 18).date(): "24618",
        datetime.datetime(2024, 6, 25).date(): "24625",
        datetime.datetime(2024, 7, 2).date(): "24702",
        datetime.datetime(2024, 7, 9).date(): "24709",
        datetime.datetime(2024, 7, 16).date(): "24716",
        datetime.datetime(2024, 7, 23).date(): "24723",
        datetime.datetime(2024, 7, 30).date(): "24730",
        datetime.datetime(2024, 8, 6).date(): "24806",
        datetime.datetime(2024, 8, 13).date(): "24813",
        datetime.datetime(2024, 8, 20).date(): "24820",
        datetime.datetime(2024, 8, 27).date(): "24827",
        datetime.datetime(2024, 9, 3).date(): "24903",
        datetime.datetime(2024, 9, 10).date(): "24910",
        datetime.datetime(2024, 9, 17).date(): "24917",
        datetime.datetime(2024, 9, 24).date(): "24924",
        datetime.datetime(2024, 10, 1).date(): "24O01",
        datetime.datetime(2024, 10, 8).date(): "24O08",
        datetime.datetime(2024, 10, 15).date(): "24O15",
        datetime.datetime(2024, 10, 22).date(): "24O22",
        datetime.datetime(2024, 10, 29).date(): "24O29",
        datetime.datetime(2024, 11, 5).date(): "24N05",
        datetime.datetime(2024, 11, 12).date(): "24N12",
        datetime.datetime(2024, 11, 19).date(): "24N19",
        datetime.datetime(2024, 11, 26).date(): "24N26",
        datetime.datetime(2024, 12, 3).date(): "24D03",
        datetime.datetime(2024, 12, 10).date(): "24D10",
        datetime.datetime(2024, 12, 17).date(): "24D17",
        datetime.datetime(2024, 12, 24).date(): "24D24",
        datetime.datetime(2024, 12, 31).date(): "24D31",
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
        datetime.datetime(2024, 5, 13).date(): "24513",
        datetime.datetime(2024, 5, 20).date(): "24520",
        datetime.datetime(2024, 5, 27).date(): "24527",
        datetime.datetime(2024, 6, 3).date(): "24603",
        datetime.datetime(2024, 6, 10).date(): "24610",
        datetime.datetime(2024, 6, 17).date(): "24617",
        datetime.datetime(2024, 6, 24).date(): "24624",
        datetime.datetime(2024, 7, 1).date(): "24701",
        datetime.datetime(2024, 7, 8).date(): "24708",
        datetime.datetime(2024, 7, 15).date(): "24715",
        datetime.datetime(2024, 7, 22).date(): "24722",
        datetime.datetime(2024, 7, 29).date(): "24729",
        datetime.datetime(2024, 8, 5).date(): "24805",
        datetime.datetime(2024, 8, 12).date(): "24812",
        datetime.datetime(2024, 8, 19).date(): "24819",
        datetime.datetime(2024, 8, 26).date(): "24826",
        datetime.datetime(2024, 9, 2).date(): "24902",
        datetime.datetime(2024, 9, 9).date(): "24909",
        datetime.datetime(2024, 9, 16).date(): "24916",
        datetime.datetime(2024, 9, 23).date(): "24923",
        datetime.datetime(2024, 9, 30).date(): "24930",
        datetime.datetime(2024, 10, 7).date(): "24O07",
        datetime.datetime(2024, 10, 14).date(): "24O14",
        datetime.datetime(2024, 10, 21).date(): "24O21",
        datetime.datetime(2024, 10, 28).date(): "24O28",
        datetime.datetime(2024, 11, 4).date(): "24N04",
        datetime.datetime(2024, 11, 11).date(): "24N11",
        datetime.datetime(2024, 11, 18).date(): "24N18",
        datetime.datetime(2024, 11, 25).date(): "24N25",
        datetime.datetime(2024, 12, 2).date(): "24D02",
        datetime.datetime(2024, 12, 9).date(): "24D09",
        datetime.datetime(2024, 12, 16).date(): "24D16",
        datetime.datetime(2024, 12, 23).date(): "24D23",
        datetime.datetime(2024, 12, 30).date(): "24D30",
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
        datetime.datetime(2024, 3, 28).date(): "24328",
        datetime.datetime(2024, 4, 25).date(): "24425",
        datetime.datetime(2024, 5, 30).date(): "24530",
        datetime.datetime(2024, 6, 27).date(): "24627",
        datetime.datetime(2024, 7, 25).date(): "24725",
        datetime.datetime(2024, 8, 29).date(): "24829",
        datetime.datetime(2024, 9, 26).date(): "24926",
        datetime.datetime(2024, 10, 31).date(): "24O31",
        datetime.datetime(2024, 11, 28).date(): "24N28",
        datetime.datetime(2024, 12, 26).date(): "24D26",

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
        datetime.datetime(2024, 3, 27).date(): "24327",
        datetime.datetime(2024, 4, 30).date(): "24430",
        datetime.datetime(2024, 5, 29).date(): "24529",
        datetime.datetime(2024, 6, 26).date(): "24626",
        datetime.datetime(2024, 7, 31).date(): "24731",
        datetime.datetime(2024, 8, 28).date(): "24828",
        datetime.datetime(2024, 9, 25).date(): "24925",
        datetime.datetime(2024, 10, 30).date(): "24O30",
        datetime.datetime(2024, 11, 27).date(): "24N27",
        datetime.datetime(2024, 12, 24).date(): "24D24",

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
    expiry = {datetime.datetime(2024, 2, 20).date(): "24220",
              datetime.datetime(2024, 3, 26).date(): "24326",
              datetime.datetime(2024, 4, 30).date(): "24430",
              datetime.datetime(2024, 5, 28).date(): "24528",
              datetime.datetime(2024, 6, 25).date(): "24625",
              datetime.datetime(2024, 7, 30).date(): "24730",
              datetime.datetime(2024, 8, 27).date(): "24827",
              datetime.datetime(2024, 9, 24).date(): "24924",
              datetime.datetime(2024, 10, 29).date(): "24O29",
              datetime.datetime(2024, 11, 26).date(): "24N26",
              datetime.datetime(2024, 12, 31).date(): "24D31",
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
    expiry = {datetime.datetime(2024, 5, 27).date(): "24527",
              datetime.datetime(2024, 6, 24).date(): "24624",
              datetime.datetime(2024, 7, 29).date(): "24729",
              datetime.datetime(2024, 8, 26).date(): "24826",
              datetime.datetime(2024, 9, 30).date(): "24930",
              datetime.datetime(2024, 10, 28).date(): "24O28",
              datetime.datetime(2024, 11, 25).date(): "24N25",
              datetime.datetime(2024, 12, 30).date(): "24D30",
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
        name = "Nifty Bank"
    elif stock == "NIFTY":
        name = "Nifty 50"
    elif stock == "FINNIFTY":
        name = "Nifty Fin Service"
    elif stock == 'MIDCPNIFTY':
        name = "Nifty Mid Select"
    return name

def getOptionFormat(stock, intExpiry, strike, ce_pe):
    if(ce_pe[0]=='C'):
        return str(stock) + str(intExpiry)+str(strike)+'CE'
    elif(ce_pe[0]=='P'):
        return str(stock) + str(intExpiry)+str(strike)+'PE'

def getFutureFormat(stock, intExpiry):
    if stock in mcx_expiries.keys():
        return str(stock)+str(intExpiry)+str('FUT')
    else:
        return str(stock)+str(intExpiry)+str('FUT')

def getLTP(instrument):
    url = "http://localhost:4000/ltp?instrument=" + instrument
    try:
        resp = requests.get(url)
    except Exception as e:
        print(e)
    data = resp.json()
    return data
# with open('symbol_mapping.txt','r') as f:
#     symbol_to_id_iifl = ast.literal_eval(f.read())[0]

def manualLTP(symbol,api,symbol_to_id):
    # exch = symbol[:3]
    # stockname = symbol[4:]
    symbol_array=[]
    # print(symbol_to_id[symbol])
    print(symbol)
    try:
        symbol = getIndexSpot(symbol)
    except:
        pass
    try:
        sid = symbol_to_id[symbol].split('|')
        symbol_array.append({'exchangeSegment':sid[0],'exchangeInstrumentID':sid[1]})
    except:
        print("Symbol Not found. (Manual LTP)",symbol)
    # print(symbol_array)
    temp = api.get_quote(symbol_array,1512,'JSON')
    if temp['type']!='success':
        print("Manual LTP Error")
    # print(temp)
    if temp['result']['listQuotes'] == []:
        print("LTP not Available.")
        raise f"LTP not available at this time for {symbol}"
    else:
        ltp = ast.literal_eval(temp['result']['listQuotes'][0])['LastTradedPrice']
    print(ltp)
    return ltp

# def placeOrder(inst ,t_type,qty,order_type,price,variety, api,papertrading=0,trigger_price=0):
#     # exch = inst[:3]
#     # symb = inst[4:]
#     try:
#         sid = symbol_to_id[inst].split('|')
#     except:
#         print("Order not placed. Instrument not found")
#         return 0
#     segments_dict = {'1':"NSECM",'2' :"NSEFO", '3':"NSECD", '11':"BSECM", '12':"BSEFO", '51':"MCXFO"}
#     #paperTrading = 0 #if this is 1, then real trades will be placed
#     if( t_type=="BUY"):
#         t_type=api.TRANSACTION_TYPE_BUY
#     else:
#         t_type=api.TRANSACTION_TYPE_SELL
#
#     if(order_type=="MARKET"):
#         order_type=api.ORDER_TYPE_MARKET
#         price = 0
#     elif(order_type=="LIMIT"):
#         order_type=api.ORDER_TYPE_LIMIT
#     elif(order_type=='SL'):
#         order_type=api.ORDER_TYPE_STOPMARKET
#
#     try:
#         if(papertrading == 1):
#             print(t_type)
#             print(inst)
#             # print(symb)
#             print(qty)
#             print(order_type)
#             print(price)
#
#             order_id = api.place_order(
#                 exchangeSegment=segments_dict[sid[0]],
#                 exchangeInstrumentID=int(sid[1]),
#                 productType=api.PRODUCT_MIS,
#                 orderType=order_type,
#                 orderSide=t_type,
#                 timeInForce=api.VALIDITY_DAY,
#                 disclosedQuantity=0,
#                 orderQuantity=qty,
#                 limitPrice=price,
#                 stopPrice=trigger_price,
#                 orderUniqueIdentifier="454845",
#                 clientID=user_id)
#             if order_id['type'] != 'error':
#                 order_id = order_id['result']['AppOrderID']
#             print(" => ", inst , order_id )
#             return order_id
#
#         else:
#             order_id=0
#             return order_id
#
#     except Exception as e:
#         print(" => ", inst , "Failed : {} ".format(e))
#
# def getHistorical(ticker,interval,duration,api):
#     months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#     #token = pd.read_csv(f'https://api.shoonya.com/{exchange1}_symbols.txt.zip')
#     segments_dict = {'1':"NSECM",'2' :"NSEFO", '3':"NSECD", '11':"BSECM", '12':"BSEFO", '51':"MCXFO"}
#     try:
#         sid = symbol_to_id[ticker].split('|')
#     except:
#         print("Historical data not found. Instrument not found")
#         return 0
#     # exch = ticker[:3]
#     # token = pd.read_csv(f'https://api.shoonya.com/{exch}_symbols.txt.zip')
#     stockname = ticker
#     # dt = datetime.datetime.now()
#     # endTime = months[dt.month-1] + " " + str(dt.day) + " " + str(dt.year) + str(dt.hour)
#
#     endtime = time.strftime("%b %d %Y %H%M%S",time.localtime())
#     # startTime =
#     today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
#     no_of_days_before = duration
#     starting_date = today-timedelta(days=no_of_days_before)
#     starting_date = datetime.datetime.strftime(starting_date,"%b %d %Y %H%M%S")
#     print(endtime)
#     print(starting_date)
#     # Compression value
#     # "In1Second:1"
#     # "In1Minute: 60"
#     # "In2Minute : 120"
#     # "In3Minute : 180"
#     # "In5Minute : 300"
#     # "In10Minute : 600"
#     # "In15Minute : 900"
#     # "In30Minute : 1800"
#     # "In60Minute : 3600"
#     hist_data = api.get_ohlc(
#         exchangeSegment=segments_dict[sid[0]],
#         exchangeInstrumentID=int(sid[1]),
#         startTime=starting_date,
#         endTime=endtime,
#         compressionValue=60)
#     # print(starting_date)
#     print(interval)
#
#     # hist_data = api.get_time_price_series(exchange=exch, token=inst, starttime=starting_date, interval=1)
#     # hist_data = pd.DataFrame(hist_data)
#     print(hist_data)
#     if hist_data['type'] != 'success':
#         print("Error Getting historical data.")
#         return 0
#     hist_data = hist_data['result']['dataReponse'].split(',')
#     hist_list = []
#     for i in range(len(hist_data)):
#         single_row = hist_data[i].split('|')
#         hist_list.append(single_row)
#     hist_data = pd.DataFrame(hist_list,columns=['timeframe','open','high','low','close','volume','oi','blank'])
#     hist_data.drop(['blank'],axis=1)
#     hist_data['timeframe'] = [datetime.datetime.utcfromtimestamp(int(x)) for x in hist_data['timeframe']]
#     hist_data['timeframe'] = pd.to_datetime(hist_data['timeframe'])
#     # hist_data =
#     print(hist_data)
#
#     #hist_data = hist_data.sort_values(by='time', ascending=True)
#     hist_data = hist_data.reset_index(drop=True)
#
#     # hist_data.columns = ['status','Date','Interval open','Interval high','Interval low','Interval close','Interval vwap','Interval volume','volume','Interval io change','oi']
#     # for i in range(0,hist_data['Current epoch time'].size):
#     #   hist_data['Current epoch time'][i] = datetime.fromtimestamp(int(hist_data['Current epoch time'][i]))
#     reversed_df = hist_data
#     # reversed_df = hist_data.iloc[::-1]
#
#     reversed_df = reversed_df.reset_index(drop=True)
#     # new_column_names = {'into': 'open', 'inth': 'high', 'intl': 'low', 'intc': 'close', 'intv': 'volume', 'intoi': 'openinterest'}
#     # reversed_df.rename(columns=new_column_names, inplace=True)
#
#     reversed_df['open'] = pd.to_numeric(reversed_df['open'])
#     reversed_df['high'] = pd.to_numeric(reversed_df['high'])
#     reversed_df['low'] = pd.to_numeric(reversed_df['low'])
#     reversed_df['close'] = pd.to_numeric(reversed_df['close'])
#     reversed_df['volume'] = pd.to_numeric(reversed_df['volume'])
#     reversed_df['openinterest'] = pd.to_numeric(reversed_df['oi'])
#     reversed_df['datetime2'] = reversed_df['timeframe'].copy()
#     reversed_df['time'] = pd.to_datetime(reversed_df['timeframe'])
#     reversed_df = reversed_df[reversed_df['time'].dt.time >= pd.to_datetime("09:15:00").time()]
#     reversed_df = reversed_df.reset_index(drop=True)
#
#     # Set 'datetime' as the index
#     reversed_df.set_index('time', inplace=True)
#     # Update the format of the datetime index and add 5 hours and 30 minutes for IST
#     #reversed_df.index = reversed_df.index.floor('min')  # Floor to minutes
#     #print(hist_data)
#
#     finaltimeframe = str(interval)  + "min"
#
#     # Resample to a specific time frame, for example, 30 minutes
#     resampled_df = reversed_df.resample(finaltimeframe).agg({
#         'open': 'first',
#         'high': 'max',
#         'low': 'min',
#         'close': 'last',
#         'volume': 'sum',
#         'datetime2': 'first',
#         'openinterest': 'last'
#     })
#
#     # If you want to fill any missing values with a specific method, you can use fillna
#     #resampled_df = resampled_df.fillna(method='ffill')  # Forward fill
#
#     #print(resampled_df)
#     resampled_df = resampled_df.dropna(subset=['open'])
#     return resampled_df

# def getHistorical_old(ticker,interval,duration,api):
#     token = pd.read_csv(f'https://api.shoonya.com/{exchange1}_symbols.txt.zip')
#     exch = ticker[:3]
#     stockname = ticker[4:]
#     today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
#     no_of_days_before = duration
#     starting_date = today-timedelta(days=no_of_days_before)
#     starting_date = starting_date.timestamp()
#
#     if stockname == "Nifty 50":
#         inst = "26000"
#     elif stockname == "Nifty Bank":
#         inst = "26009"
#     else:
#         inst = token[token.TradingSymbol==stockname].Token.values[0]
#         inst = str(inst)
#         #for j in range(0,len(token)):
#         #    if(token['TradingSymbol'][j] == stockname):
#         #        inst = str(token['Token'][j])
#         #        time.sleep(1)
#         #        break
#     #print(inst)
#
#     print(starting_date)
#     print(interval)
#     hist_data = api.get_time_price_series(exchange=exch, token=inst, starttime=starting_date, interval=interval)
#     hist_data = pd.DataFrame(hist_data)
#     print(hist_data)
#
#     #hist_data = hist_data.sort_values(by='time', ascending=True)
#     hist_data = hist_data.reset_index(drop=True)
#
#     # hist_data.columns = ['status','Date','Interval open','Interval high','Interval low','Interval close','Interval vwap','Interval volume','volume','Interval io change','oi']
#     # for i in range(0,hist_data['Current epoch time'].size):
#     #   hist_data['Current epoch time'][i] = datetime.fromtimestamp(int(hist_data['Current epoch time'][i]))
#
#     reversed_df = hist_data.iloc[::-1]
#     reversed_df = reversed_df.reset_index(drop=True)
#     new_column_names = {'into': 'open', 'inth': 'high', 'intl': 'low', 'intc': 'close', 'intv': 'volume', 'intoi': 'oi'}
#     reversed_df.rename(columns=new_column_names, inplace=True)
#     print(reversed_df)
#     return reversed_df