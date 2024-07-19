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

from APIConnect.APIConnect import APIConnect
from constants.exchange import ExchangeEnum
from constants.order_type import OrderTypeEnum
from constants.product_code import ProductCodeENum
from constants.duration import DurationEnum
from constants.action import ActionEnum
from constants.asset_type import AssetTypeEnum
from constants.chart_exchange import ChartExchangeEnum
from constants.intraday_interval import IntradayIntervalEnum




#import nuvama_login
import datetime
import time
import requests
from datetime import timedelta
from pytz import timezone
import pandas as pd
import json
import os
import sys
######PIVOT POINTS##########################
####################__INPUT__#####################

#api_connect = nuvama_login.api_connect

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
        datetime.datetime(2023, 11, 30).date(): "23NOV",
        datetime.datetime(2023, 12, 7).date(): "23D07",
        datetime.datetime(2023, 12, 14).date(): "23D14",
        datetime.datetime(2023, 12, 21).date(): "23D21",
        datetime.datetime(2023, 12, 28).date(): "23DEC",
        datetime.datetime(2024, 1, 4).date(): "24104",
        datetime.datetime(2024, 1, 11).date(): "24111",
        datetime.datetime(2024, 1, 18).date(): "24118",
        datetime.datetime(2024, 1, 25).date(): "24JAN",
        datetime.datetime(2024, 2, 1).date(): "24201",
        datetime.datetime(2024, 2, 8).date(): "24208",
        datetime.datetime(2024, 2, 15).date(): "24215",
        datetime.datetime(2024, 2, 22).date(): "24222",
        datetime.datetime(2024, 2, 29).date(): "24FEB",
        datetime.datetime(2024, 3, 7).date(): "24307",
        datetime.datetime(2024, 3, 14).date(): "24314",
        datetime.datetime(2024, 3, 21).date(): "24321",
        datetime.datetime(2024, 3, 28).date(): "24MAR",
        datetime.datetime(2024, 4, 4).date(): "24404",
        datetime.datetime(2024, 4, 10).date(): "24410",
        datetime.datetime(2024, 4, 18).date(): "24418",
        datetime.datetime(2024, 4, 25).date(): "24APR",
        datetime.datetime(2024, 5, 2).date(): "24502",
        datetime.datetime(2024, 5, 9).date(): "24509",
        datetime.datetime(2024, 5, 16).date(): "24516",
        datetime.datetime(2024, 5, 23).date(): "24523",
        datetime.datetime(2024, 5, 30).date(): "24MAY",
        datetime.datetime(2024, 6, 6).date(): "24606",
        datetime.datetime(2024, 6, 13).date(): "24613",
        datetime.datetime(2024, 6, 20).date(): "24620",
        datetime.datetime(2024, 6, 27).date(): "24JUN",
        datetime.datetime(2024, 7, 4).date(): "24704",
        datetime.datetime(2024, 7, 11).date(): "24711",
        datetime.datetime(2024, 7, 18).date(): "24718",
        datetime.datetime(2024, 7, 25).date(): "24JUL",
        datetime.datetime(2024, 8, 1).date(): "24801",
        datetime.datetime(2024, 8, 8).date(): "24808",
        datetime.datetime(2024, 8, 14).date(): "24814",
        datetime.datetime(2024, 8, 22).date(): "24822",
        datetime.datetime(2024, 8, 29).date(): "24AUG",
        datetime.datetime(2024, 9, 5).date(): "24905",
        datetime.datetime(2024, 9, 12).date(): "24912",
        datetime.datetime(2024, 9, 19).date(): "24919",
        datetime.datetime(2024, 9, 26).date(): "24SEP",
        datetime.datetime(2024, 10, 3).date(): "24O03",
        datetime.datetime(2024, 10, 10).date(): "24O10",
        datetime.datetime(2024, 10, 17).date(): "24O17",
        datetime.datetime(2024, 10, 24).date(): "24O24",
        datetime.datetime(2024, 10, 31).date(): "24OCT",
        datetime.datetime(2024, 11, 7).date(): "24N07",
        datetime.datetime(2024, 11, 14).date(): "24N14",
        datetime.datetime(2024, 11, 21).date(): "24N21",
        datetime.datetime(2024, 11, 28).date(): "24NOV",
        datetime.datetime(2024, 12, 5).date(): "24D05",
        datetime.datetime(2024, 12, 12).date(): "24D12",
        datetime.datetime(2024, 12, 19).date(): "24D19",
        datetime.datetime(2024, 12, 26).date(): "24DEC",
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
        datetime.datetime(2023, 11, 30).date(): "23NOV",
        datetime.datetime(2023, 12, 6).date(): "23D06",
        datetime.datetime(2023, 12, 13).date(): "23D13",
        datetime.datetime(2023, 12, 20).date(): "23D20",
        datetime.datetime(2023, 12, 28).date(): "23DEC",
        datetime.datetime(2024, 1, 3).date(): "24103",
        datetime.datetime(2024, 1, 10).date(): "24110",
        datetime.datetime(2024, 1, 17).date(): "24117",
        datetime.datetime(2024, 1, 25).date(): "24JAN",
        datetime.datetime(2024, 1, 31).date(): "24131",
        datetime.datetime(2024, 2, 7).date(): "24207",
        datetime.datetime(2024, 2, 14).date(): "24214",
        datetime.datetime(2024, 2, 21).date(): "24221",
        datetime.datetime(2024, 2, 29).date(): "24FEB",
        datetime.datetime(2024, 3, 6).date(): "24306",
        datetime.datetime(2024, 3, 13).date(): "24313",
        datetime.datetime(2024, 3, 20).date(): "24320",
        datetime.datetime(2024, 3, 27).date(): "24MAR",
        datetime.datetime(2024, 4, 3).date(): "24403",
        datetime.datetime(2024, 4, 10).date(): "24410",
        datetime.datetime(2024, 4, 16).date(): "24416",
        datetime.datetime(2024, 4, 24).date(): "24APR",
        datetime.datetime(2024, 4, 30).date(): "24430",
        datetime.datetime(2024, 5, 8).date(): "24508",
        datetime.datetime(2024, 5, 15).date(): "24515",
        datetime.datetime(2024, 5, 22).date(): "24522",
        datetime.datetime(2024, 5, 29).date(): "24MAY",
        datetime.datetime(2024, 6, 5).date(): "24605",
        datetime.datetime(2024, 6, 12).date(): "24612",
        datetime.datetime(2024, 6, 19).date(): "24619",
        datetime.datetime(2024, 6, 26).date(): "24JUN",
        datetime.datetime(2024, 7, 3).date(): "24703",
        datetime.datetime(2024, 7, 10).date(): "24710",
        datetime.datetime(2024, 7, 16).date(): "24716",
        datetime.datetime(2024, 7, 24).date(): "24724",
        datetime.datetime(2024, 7, 31).date(): "24JUL",
        datetime.datetime(2024, 8, 7).date(): "24807",
        datetime.datetime(2024, 8, 14).date(): "24814",
        datetime.datetime(2024, 8, 21).date(): "24821",
        datetime.datetime(2024, 8, 28).date(): "24AUG",
        datetime.datetime(2024, 9, 4).date(): "24904",
        datetime.datetime(2024, 9, 11).date(): "24911",
        datetime.datetime(2024, 9, 18).date(): "24918",
        datetime.datetime(2024, 9, 25).date(): "24SEP",
        datetime.datetime(2024, 10, 1).date(): "24O01",
        datetime.datetime(2024, 10, 9).date(): "24O09",
        datetime.datetime(2024, 10, 16).date(): "24O16",
        datetime.datetime(2024, 10, 23).date(): "24O23",
        datetime.datetime(2024, 10, 30).date(): "24OCT",
        datetime.datetime(2024, 11, 6).date(): "24N06",
        datetime.datetime(2024, 11, 13).date(): "24N13",
        datetime.datetime(2024, 11, 20).date(): "24N20",
        datetime.datetime(2024, 11, 27).date(): "24NOV",
        datetime.datetime(2024, 12, 4).date(): "24D04",
        datetime.datetime(2024, 12, 11).date(): "24D11",
        datetime.datetime(2024, 12, 18).date(): "24D18",
        datetime.datetime(2024, 12, 24).date(): "24DEC",
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
        datetime.datetime(2024, 2, 27).date(): "24FEB",
        datetime.datetime(2024, 3, 5).date(): "24305",
        datetime.datetime(2024, 3, 12).date(): "24312",
        datetime.datetime(2024, 3, 19).date(): "24319",
        datetime.datetime(2024, 3, 26).date(): "24MAR",
        datetime.datetime(2024, 4, 2).date(): "24402",
        datetime.datetime(2024, 4, 9).date(): "24409",
        datetime.datetime(2024, 4, 16).date(): "24416",
        datetime.datetime(2024, 4, 23).date(): "24423",
        datetime.datetime(2024, 4, 30).date(): "24APR",
        datetime.datetime(2024, 5, 7).date(): "24507",
        datetime.datetime(2024, 5, 14).date(): "24514",
        datetime.datetime(2024, 5, 21).date(): "24521",
        datetime.datetime(2024, 5, 28).date(): "24MAY",
        datetime.datetime(2024, 6, 4).date(): "24604",
        datetime.datetime(2024, 6, 11).date(): "24611",
        datetime.datetime(2024, 6, 18).date(): "24618",
        datetime.datetime(2024, 6, 25).date(): "24JUN",
        datetime.datetime(2024, 7, 2).date(): "24702",
        datetime.datetime(2024, 7, 9).date(): "24709",
        datetime.datetime(2024, 7, 16).date(): "24716",
        datetime.datetime(2024, 7, 23).date(): "24723",
        datetime.datetime(2024, 7, 30).date(): "24JUL",
        datetime.datetime(2024, 8, 6).date(): "24806",
        datetime.datetime(2024, 8, 13).date(): "24813",
        datetime.datetime(2024, 8, 20).date(): "24820",
        datetime.datetime(2024, 8, 27).date(): "24AUG",
        datetime.datetime(2024, 9, 3).date(): "24903",
        datetime.datetime(2024, 9, 10).date(): "24910",
        datetime.datetime(2024, 9, 17).date(): "24917",
        datetime.datetime(2024, 9, 24).date(): "24SEP",
        datetime.datetime(2024, 10, 1).date(): "24O01",
        datetime.datetime(2024, 10, 8).date(): "24O08",
        datetime.datetime(2024, 10, 15).date(): "24O15",
        datetime.datetime(2024, 10, 22).date(): "24O22",
        datetime.datetime(2024, 10, 29).date(): "24OCT",
        datetime.datetime(2024, 11, 5).date(): "24N05",
        datetime.datetime(2024, 11, 12).date(): "24N12",
        datetime.datetime(2024, 11, 19).date(): "24N19",
        datetime.datetime(2024, 11, 26).date(): "24NOV",
        datetime.datetime(2024, 12, 3).date(): "24D03",
        datetime.datetime(2024, 12, 10).date(): "24D10",
        datetime.datetime(2024, 12, 17).date(): "24D17",
        datetime.datetime(2024, 12, 24).date(): "24D24",
        datetime.datetime(2024, 12, 31).date(): "24DEC",
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
        datetime.datetime(2024, 5, 27).date(): "24MAY",
        datetime.datetime(2024, 6, 3).date(): "24603",
        datetime.datetime(2024, 6, 10).date(): "24610",
        datetime.datetime(2024, 6, 17).date(): "24617",
        datetime.datetime(2024, 6, 24).date(): "24JUN",
        datetime.datetime(2024, 7, 1).date(): "24701",
        datetime.datetime(2024, 7, 8).date(): "24708",
        datetime.datetime(2024, 7, 15).date(): "24715",
        datetime.datetime(2024, 7, 22).date(): "24722",
        datetime.datetime(2024, 7, 29).date(): "24JUL",
        datetime.datetime(2024, 8, 5).date(): "24805",
        datetime.datetime(2024, 8, 12).date(): "24812",
        datetime.datetime(2024, 8, 19).date(): "24819",
        datetime.datetime(2024, 8, 26).date(): "24AUG",
        datetime.datetime(2024, 9, 2).date(): "24902",
        datetime.datetime(2024, 9, 9).date(): "24909",
        datetime.datetime(2024, 9, 16).date(): "24916",
        datetime.datetime(2024, 9, 23).date(): "24923",
        datetime.datetime(2024, 9, 30).date(): "24SEP",
        datetime.datetime(2024, 10, 7).date(): "24O07",
        datetime.datetime(2024, 10, 14).date(): "24O14",
        datetime.datetime(2024, 10, 21).date(): "24O21",
        datetime.datetime(2024, 10, 28).date(): "24OCT",
        datetime.datetime(2024, 11, 4).date(): "24N04",
        datetime.datetime(2024, 11, 11).date(): "24N11",
        datetime.datetime(2024, 11, 18).date(): "24N18",
        datetime.datetime(2024, 11, 25).date(): "24NOV",
        datetime.datetime(2024, 12, 2).date(): "24D02",
        datetime.datetime(2024, 12, 9).date(): "24D09",
        datetime.datetime(2024, 12, 16).date(): "24D16",
        datetime.datetime(2024, 12, 23).date(): "24D23",
        datetime.datetime(2024, 12, 30).date(): "24DEC",
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
        datetime.datetime(2024, 3, 28).date(): "24MAR",
        datetime.datetime(2024, 4, 25).date(): "24APR",
        datetime.datetime(2024, 5, 30).date(): "24MAY",
        datetime.datetime(2024, 6, 27).date(): "24JUN",
        datetime.datetime(2024, 7, 25).date(): "24JUL",
        datetime.datetime(2024, 8, 29).date(): "24AUG",
        datetime.datetime(2024, 9, 26).date(): "24SEP",
        datetime.datetime(2024, 10, 31).date(): "24OCT",
        datetime.datetime(2024, 11, 28).date(): "24NOV",
        datetime.datetime(2024, 12, 26).date(): "24DEC",

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
        datetime.datetime(2024, 3, 27).date(): "24MAR",
        datetime.datetime(2024, 4, 30).date(): "24APR",
        datetime.datetime(2024, 5, 29).date(): "24MAY",
        datetime.datetime(2024, 6, 26).date(): "24JUN",
        datetime.datetime(2024, 7, 31).date(): "24JUL",
        datetime.datetime(2024, 8, 28).date(): "24AUG",
        datetime.datetime(2024, 9, 25).date(): "24SEP",
        datetime.datetime(2024, 10, 30).date(): "24OCT",
        datetime.datetime(2024, 11, 27).date(): "24NOV",
        datetime.datetime(2024, 12, 24).date(): "24DEC",

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
    expiry = {datetime.datetime(2024, 2, 20).date(): "24FEB",
              datetime.datetime(2024, 3, 26).date(): "24MAR",
              datetime.datetime(2024, 4, 30).date(): "24APR",
              datetime.datetime(2024, 5, 28).date(): "24MAY",
              datetime.datetime(2024, 6, 25).date(): "24JUN",
              datetime.datetime(2024, 7, 30).date(): "24JUL",
              datetime.datetime(2024, 8, 27).date(): "24AUG",
              datetime.datetime(2024, 9, 24).date(): "24SEP",
              datetime.datetime(2024, 10, 29).date(): "24OCT",
              datetime.datetime(2024, 11, 26).date(): "24NOV",
              datetime.datetime(2024, 12, 31).date(): "24DEC",
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
    expiry = {datetime.datetime(2024, 5, 27).date(): "24MAY",
              datetime.datetime(2024, 6, 24).date(): "24JUN",
              datetime.datetime(2024, 7, 29).date(): "24JUL",
              datetime.datetime(2024, 8, 26).date(): "24AUG",
              datetime.datetime(2024, 9, 30).date(): "24SEP",
              datetime.datetime(2024, 10, 28).date(): "24OCT",
              datetime.datetime(2024, 11, 25).date(): "24NOV",
              datetime.datetime(2024, 12, 30).date(): "24DEC",
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

def getExpiryFormat(year, month, day, monthly):
    if monthly == 0:
        day1 = day
        if month == "JAN":
            month1 = 1
        elif month == "FEB":
            month1 = 2
        elif month == "MAR":
            month1 = 3
        elif month == "APR":
            month1 = 4
        elif month == "MAY":
            month1 = 5
        elif month == "JUN":
            month1 = 6
        elif month == "JUL":
            month1 = 7
        elif month == "AUG":
            month1 = 8
        elif month == "SEP":
            month1 = 9
        elif month == "OCT":
            month1 = "O"
        elif month == "NOV":
            month1 = "N"
        elif month == "DEC":
            month1 = "D"
    elif monthly == 1:
        day1 = ""
        month1 = month

    return str(year)+str(month1)+str(day1)

def getIndexSpot(stock):
    if stock == "BANKNIFTY":
        name = "NSE:Nifty Bank"
    elif stock == "NIFTY":
        name = "NSE:Nifty 50"
    elif stock == "FINNIFTY":
        name = "NSE:Nifty Fin Service"
    elif stock == "MIDCPNIFTY":
        name = "NSE:NSE Midcap 100"
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

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def manualLTP(symbol,object):
    symm, symbolToken = get_tradingSymbol_exchangeToken(symbol)
    response = object.getIntradayChart(ChartExchangeEnum.NSE, AssetTypeEnum.INDEX, symbolToken, IntradayIntervalEnum.M1, TillDate = None, IncludeContinuousFutures = False)
    df = json.loads(response)
    print(df['data'])

    return df['data'][-1]['ltp']

    # getLTP(symbol)


columns_to_select = ['exchangetoken', 'tradingsymbol', 'symbolname', 'description','assettype','exchange']
token = pd.read_csv(resource_path('instruments\instruments.csv'),usecols=columns_to_select, index_col=False)
print(token)

def get_tradingSymbol_exchangeToken(symbolname):
    exch = symbolname[:3]
    name = symbolname[4:]

    #print(token)

    if name == "Nifty 50":
        tradingsymbol = "Nifty 50"
        exchangetoken = "-29"
    elif name == "Nifty Bank":
        tradingsymbol = "Nifty Bank"
        exchangetoken = "-21"
    elif name == "Nifty Fin Service":
        tradingsymbol = "Nifty Fin Service"
        exchangetoken = "-40"
    elif name == "NSE Midcap 100":
        tradingsymbol = "NSE Midcap 100"
        exchangetoken = "-22"
    elif exch == "NSE":
        for j in range(0,len(token)):
            if(token['symbolname'][j] == name) and (token['exchange'][j] == exch):
                tradingsymbol = str(token['tradingsymbol'][j])
                exchangetoken = str(token['exchangetoken'][j])
                break
    elif exch == "NFO" or exch == "MCX":
        for j in range(0,len(token)):
            if(token['tradingsymbol'][j] == name) and (token['exchange'][j] == exch):
                tradingsymbol = str(token['tradingsymbol'][j])
                exchangetoken = str(token['exchangetoken'][j])
                break

    return (tradingsymbol, exchangetoken)

def placeOrder(inst ,t_type,qty,order_type,price,variety, api_connect, papertrading=0):
    exch = inst[:3]
    symb = inst[4:]
    tradingsymbol, exchangetoken = get_tradingSymbol_exchangeToken(inst)
    print(tradingsymbol)
    print(exchangetoken)
    dt = datetime.datetime.now()
    #papertrading = 0 #if this is 1, then actual trades will get placed
    print(dt.hour,":",dt.minute,":",dt.second ," => ",t_type," ",symb," ",qty," ",order_type)

    if(order_type=="MARKET"):
        order_type = OrderTypeEnum.MARKET
    elif(order_type=="LIMIT"):
        order_type = OrderTypeEnum.LIMIT

    if(t_type=="BUY"):
        action = ActionEnum.BUY
    elif(t_type=="SELL"):
        action = ActionEnum.SELL

    if(exch=="NSE"):
        exchange = ExchangeEnum.NSE
    elif(exch=="NFO"):
        exchange = ExchangeEnum.NFO

    try:
        if (papertrading == 1):
            #return tradingsymbol, exchange,action,DurationEnum.DAY,  order_type, qty, exchangetoken, price, "0", "0", ProductCodeENum.MIS

            orderid = api_connect.PlaceTrade(Trading_Symbol = tradingsymbol,
                                             Exchange = exchange,
                                             Action = action,
                                             Duration = DurationEnum.DAY,
                                             Order_Type = order_type,
                                             Quantity = qty,
                                             Streaming_Symbol = exchangetoken,
                                             Limit_Price = price,
                                             Disclosed_Quantity="0",
                                             TriggerPrice="0",
                                             ProductCode = ProductCodeENum.MIS)

            print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , orderid)
            return orderid
        else:
            return 0

    except Exception as e:
        print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , "Failed : {} ".format(e))

def getHistorical(ticker,interval,duration,assetType, api_connect):
    exch = ticker[:3]
    sym = ticker[4:]

    if exch == "NSE":
        chart_exch = ChartExchangeEnum.NSE
    elif exch == "NFO":
        chart_exch = ChartExchangeEnum.NFO

    if assetType == "INDEX":
        asset_type = AssetTypeEnum.INDEX
    elif assetType == "EQUITY":
        asset_type = AssetTypeEnum.EQUITY
    elif assetType == "FUTUREINDEX":
        asset_type = AssetTypeEnum.FUTIDX
    elif assetType == "FUTURESTOCK":
        asset_type = AssetTypeEnum.FUTSTK
    elif assetType == "OPTIONINDEX":
        asset_type = AssetTypeEnum.OPTIDX
    elif assetType == "OPTIONSTOCK":
        asset_type = AssetTypeEnum.OPTSTK

    if interval == 1:
        internal_nuvama = IntradayIntervalEnum.M1
    elif interval == 3:
        internal_nuvama = IntradayIntervalEnum.M3
    elif interval == 5:
        internal_nuvama = IntradayIntervalEnum.M5
    elif interval == 15:
        internal_nuvama = IntradayIntervalEnum.M15
    elif interval == 30:
        internal_nuvama = IntradayIntervalEnum.M30
    elif interval == 60:
        internal_nuvama = IntradayIntervalEnum.H1
    internal_nuvama = IntradayIntervalEnum.M1

    symm, symbolToken = get_tradingSymbol_exchangeToken(ticker)

    #return chart_exch, asset_type, symbolToken, internal_nuvama

    response = api_connect.getIntradayChart(chart_exch,
                                            asset_type,
                                            symbolToken,
                                            internal_nuvama,
                                            TillDate = None)
    #print(response)
    data_dict = json.loads(response)
    #print(data_dict['data'])
    df = pd.DataFrame(data_dict['data'], columns=["Timestamp", "open", "high", "low", "close", "volume"])
    print(df)

    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Timestamp'] = df['Timestamp'] - pd.Timedelta(minutes=1)
    filtered_df = df[(df['Timestamp'].dt.time >= pd.to_datetime("09:15:00").time()) & (df['Timestamp'].dt.time <= pd.to_datetime("15:29:00").time())]
    filtered_df = filtered_df.reset_index(drop=True)

    filtered_df['datetime2'] = filtered_df['Timestamp'].copy()
    # Set 'datetime' as the index
    filtered_df.set_index('Timestamp', inplace=True)
    # Update the format of the datetime index and add 5 hours and 30 minutes for IST
    #df.index = df.index.floor('min')  # Floor to minutes
    #print(hist_data)
    finaltimeframe = str(interval)  + "min"

    # Resample to a specific time frame, for example, 30 minutes
    resampled_df = filtered_df.resample(finaltimeframe).agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum',
        'datetime2': 'first'
    })
    resampled_df = resampled_df.dropna(subset=['open'])

    # If you want to fill any missing values with a specific method, you can use fillna
    #resampled_df = resampled_df.fillna(method='ffill')  # Forward fill

    #print(resampled_df)

    return resampled_df

def getHistorical_old(ticker,interval,duration,assetType, api_connect):
    exch = ticker[:3]
    sym = ticker[4:]

    if exch == "NSE":
        chart_exch = ChartExchangeEnum.NSE
    elif exch == "NFO":
        chart_exch = ChartExchangeEnum.NFO

    if assetType == "INDEX":
        asset_type = AssetTypeEnum.INDEX
    elif assetType == "EQUITY":
        asset_type = AssetTypeEnum.EQUITY
    elif assetType == "FUTUREINDEX":
        asset_type = AssetTypeEnum.FUTIDX
    elif assetType == "FUTURESTOCK":
        asset_type = AssetTypeEnum.FUTSTK
    elif assetType == "OPTIONINDEX":
        asset_type = AssetTypeEnum.OPTIDX
    elif assetType == "OPTIONSTOCK":
        asset_type = AssetTypeEnum.OPTSTK

    if interval == 1:
        internal_nuvama = IntradayIntervalEnum.M1
    elif interval == 3:
        internal_nuvama = IntradayIntervalEnum.M3
    elif interval == 5:
        internal_nuvama = IntradayIntervalEnum.M5
    elif interval == 15:
        internal_nuvama = IntradayIntervalEnum.M15
    elif interval == 30:
        internal_nuvama = IntradayIntervalEnum.M30
    elif interval == 60:
        internal_nuvama = IntradayIntervalEnum.H1

    symm, symbolToken = get_tradingSymbol_exchangeToken(ticker)

    #return chart_exch, asset_type, symbolToken, internal_nuvama

    response = api_connect.getIntradayChart(chart_exch,
                                            asset_type,
                                            symbolToken,
                                            internal_nuvama,
                                            TillDate = None)
    #print(response)
    data_dict = json.loads(response)
    #print(data_dict['data'])
    df = pd.DataFrame(data_dict['data'], columns=["Timestamp", "open", "high", "low", "close", "volume"])
    #print(df)
    return df