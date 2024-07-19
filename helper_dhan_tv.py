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

from dhanhq import dhanhq
import datetime
import time
import requests
from datetime import timedelta
from pytz import timezone
import pandas as pd
import pytz

######PIVOT POINTS##########################
####################__INPUT__#####################
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
def makeMasterList():
    global masterList
    scrip_master = "https://images.dhan.co/api-data/api-scrip-master.csv"
    masterList = pd.read_csv(scrip_master,usecols=['SEM_SMST_SECURITY_ID','SEM_INSTRUMENT_NAME','SEM_TRADING_SYMBOL','SEM_CUSTOM_SYMBOL','SEM_EXM_EXCH_ID','SEM_EXCH_INSTRUMENT_TYPE'],low_memory=False)
    #print(masterList)

def getSecurityId(inst):
    makeMasterList()
    position = inst.find(':')
    exch = inst[:position]
    symb = inst[position+1:]

    try:
        if exch == "EQ":
            filtered_df = masterList[
                (masterList['SEM_INSTRUMENT_NAME'] == "EQUITY") &
                (masterList['SEM_TRADING_SYMBOL'] == symb) &
                (masterList['SEM_EXM_EXCH_ID'] == 'NSE')
                ]
            result = filtered_df['SEM_SMST_SECURITY_ID'].values
            result = result[0]
            segment = 1
            inst_type = 'EQUITY'
        elif exch == "IN":
            if symb == "NIFTY":
                result = 13
            elif symb == "BANKNIFTY":
                result = 25
            elif symb == "FINNIFTY":
                result = 27
            elif symb == "MIDCPNIFTY":
                result = 442
            segment = 0
            inst_type = "INDEX"
        else:
            filtered_df = masterList[
                (masterList['SEM_EXCH_INSTRUMENT_TYPE'] == exch) &
                (masterList['SEM_CUSTOM_SYMBOL'] == symb) &
                (masterList['SEM_EXM_EXCH_ID'] == 'NSE')
                ]
            result = filtered_df['SEM_SMST_SECURITY_ID'].values
            result = result[0]
            segment = 2
            inst_type = filtered_df['SEM_INSTRUMENT_NAME'].values[0]

        print(segment, str(result), inst_type)
        return (segment, str(result), inst_type)
    except:
        print("Symbol is wrong: ", inst)


def getNiftyExpiryDate(next=0):
    expiry = {
        datetime.datetime(2024, 2, 1).date(): "24201",
        datetime.datetime(2024, 2, 8).date(): "24208",
        datetime.datetime(2024, 2, 15).date(): "15 FEB",
        datetime.datetime(2024, 2, 22).date(): "22 FEB",
        datetime.datetime(2024, 2, 29).date(): "29 FEB",
        datetime.datetime(2024, 3, 7).date(): "07 MAR",
        datetime.datetime(2024, 3, 14).date(): "14 MAR",
        datetime.datetime(2024, 3, 21).date(): "21 MAR",
        datetime.datetime(2024, 3, 28).date(): "28 MAR",
        datetime.datetime(2024, 4, 4).date(): "04 APR",
        datetime.datetime(2024, 4, 10).date(): "10 APR",
        datetime.datetime(2024, 4, 18).date(): "18 APR",
        datetime.datetime(2024, 4, 25).date(): "25 APR",
        datetime.datetime(2024, 5, 2).date(): "02 MAY",
        datetime.datetime(2024, 5, 9).date(): "09 MAY",
        datetime.datetime(2024, 5, 16).date(): "16 MAY",
        datetime.datetime(2024, 5, 23).date(): "23 MAY",
        datetime.datetime(2024, 5, 30).date(): "30 MAY",
        datetime.datetime(2024, 6, 6).date(): "06 JUN",
        datetime.datetime(2024, 6, 13).date(): "13 JUN",
        datetime.datetime(2024, 6, 20).date(): "20 JUN",
        datetime.datetime(2024, 6, 27).date(): "27 JUN",
        datetime.datetime(2024, 7, 4).date(): "04 JUL",
        datetime.datetime(2024, 7, 11).date(): "11 JUL",
        datetime.datetime(2024, 7, 18).date(): "18 JUL",
        datetime.datetime(2024, 7, 25).date(): "25 JUL",
        datetime.datetime(2024, 8, 1).date(): "01 AUG",
        datetime.datetime(2024, 8, 8).date(): "08 AUG",
        datetime.datetime(2024, 8, 14).date(): "14 AUG",
        datetime.datetime(2024, 8, 22).date(): "22 AUG",
        datetime.datetime(2024, 8, 29).date(): "29 AUG",
        datetime.datetime(2024, 9, 5).date(): "05 SEP",
        datetime.datetime(2024, 9, 12).date(): "12 SEP",
        datetime.datetime(2024, 9, 19).date(): "19 SEP",
        datetime.datetime(2024, 9, 26).date(): "26 SEP",
        datetime.datetime(2024, 10, 3).date(): "03 OCT",
        datetime.datetime(2024, 10, 10).date(): "10 OCT",
        datetime.datetime(2024, 10, 17).date(): "17 OCT",
        datetime.datetime(2024, 10, 24).date(): "24 OCT",
        datetime.datetime(2024, 10, 31).date(): "31 OCT",
        datetime.datetime(2024, 11, 7).date(): "07 NOV",
        datetime.datetime(2024, 11, 14).date(): "14 NOV",
        datetime.datetime(2024, 11, 21).date(): "21 NOV",
        datetime.datetime(2024, 11, 28).date(): "28 NOV",
        datetime.datetime(2024, 12, 5).date(): "05 DEC",
        datetime.datetime(2024, 12, 12).date(): "12 DEC",
        datetime.datetime(2024, 12, 19).date(): "19 DEC",
        datetime.datetime(2024, 12, 26).date(): "26 DEC",
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
        datetime.datetime(2024, 2, 7).date(): "24207",
        datetime.datetime(2024, 2, 14).date(): "14 FEB",
        datetime.datetime(2024, 2, 21).date(): "21 FEB",
        datetime.datetime(2024, 2, 29).date(): "28 FEB",
        datetime.datetime(2024, 3, 6).date(): "06 MAR",
        datetime.datetime(2024, 3, 13).date(): "13 MAR",
        datetime.datetime(2024, 3, 20).date(): "20 MAR",
        datetime.datetime(2024, 3, 27).date(): "27 MAR",
        datetime.datetime(2024, 4, 3).date(): "03 APR",
        datetime.datetime(2024, 4, 10).date(): "10 APR",
        datetime.datetime(2024, 4, 16).date(): "16 APR",
        datetime.datetime(2024, 4, 24).date(): "24 APR",
        datetime.datetime(2024, 4, 30).date(): "30 APR",
        datetime.datetime(2024, 5, 8).date(): "08 MAY",
        datetime.datetime(2024, 5, 15).date(): "15 MAY",
        datetime.datetime(2024, 5, 22).date(): "22 MAY",
        datetime.datetime(2024, 5, 29).date(): "29 MAY",
        datetime.datetime(2024, 6, 5).date(): "05 JUN",
        datetime.datetime(2024, 6, 12).date(): "12 JUN",
        datetime.datetime(2024, 6, 19).date(): "19 JUN",
        datetime.datetime(2024, 6, 26).date(): "26 JUN",
        datetime.datetime(2024, 7, 3).date(): "03 JUL",
        datetime.datetime(2024, 7, 10).date(): "10 JUL",
        datetime.datetime(2024, 7, 16).date(): "16 JUL",
        datetime.datetime(2024, 7, 24).date(): "24 JUL",
        datetime.datetime(2024, 7, 31).date(): "31 JUL",
        datetime.datetime(2024, 8, 7).date(): "07 AUG",
        datetime.datetime(2024, 8, 14).date(): "14 AUG",
        datetime.datetime(2024, 8, 21).date(): "21 AUG",
        datetime.datetime(2024, 8, 28).date(): "28 AUG",
        datetime.datetime(2024, 9, 4).date(): "04 SEP",
        datetime.datetime(2024, 9, 11).date(): "11 SEP",
        datetime.datetime(2024, 9, 18).date(): "18 SEP",
        datetime.datetime(2024, 9, 25).date(): "25 SEP",
        datetime.datetime(2024, 10, 1).date(): "01 OCT",
        datetime.datetime(2024, 10, 9).date(): "09 OCT",
        datetime.datetime(2024, 10, 16).date(): "16 OCT",
        datetime.datetime(2024, 10, 23).date(): "23 OCT",
        datetime.datetime(2024, 10, 30).date(): "30 OCT",
        datetime.datetime(2024, 11, 6).date(): "06 NOV",
        datetime.datetime(2024, 11, 13).date(): "13 NOV",
        datetime.datetime(2024, 11, 20).date(): "20 NOV",
        datetime.datetime(2024, 11, 27).date(): "27 NOV",
        datetime.datetime(2024, 12, 4).date(): "04 DEC",
        datetime.datetime(2024, 12, 11).date(): "11 DEC",
        datetime.datetime(2024, 12, 18).date(): "18 DEC",
        datetime.datetime(2024, 12, 24).date(): "24 DEC",
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
        datetime.datetime(2024, 2, 27).date(): "27 FEB",
        datetime.datetime(2024, 3, 5).date(): "05 MAR",
        datetime.datetime(2024, 3, 12).date(): "12 MAR",
        datetime.datetime(2024, 3, 19).date(): "19 MAR",
        datetime.datetime(2024, 3, 26).date(): "26 MAR",
        datetime.datetime(2024, 4, 2).date(): "02 APR",
        datetime.datetime(2024, 4, 9).date(): "09 APR",
        datetime.datetime(2024, 4, 16).date(): "16 APR",
        datetime.datetime(2024, 4, 23).date(): "23 APR",
        datetime.datetime(2024, 4, 30).date(): "30 APR",
        datetime.datetime(2024, 5, 7).date(): "07 MAY",
        datetime.datetime(2024, 5, 14).date(): "14 MAY",
        datetime.datetime(2024, 5, 21).date(): "21 MAY",
        datetime.datetime(2024, 5, 28).date(): "28 MAY",
        datetime.datetime(2024, 6, 4).date(): "04 JUN",
        datetime.datetime(2024, 6, 11).date(): "11 JUN",
        datetime.datetime(2024, 6, 18).date(): "18 JUN",
        datetime.datetime(2024, 6, 25).date(): "25 JUN",
        datetime.datetime(2024, 7, 2).date(): "02 JUL",
        datetime.datetime(2024, 7, 9).date(): "09 JUL",
        datetime.datetime(2024, 7, 16).date(): "16 JUL",
        datetime.datetime(2024, 7, 23).date(): "23 JUL",
        datetime.datetime(2024, 7, 30).date(): "30 JUL",
        datetime.datetime(2024, 8, 6).date(): "06 AUG",
        datetime.datetime(2024, 8, 13).date(): "13 AUG",
        datetime.datetime(2024, 8, 20).date(): "20 AUG",
        datetime.datetime(2024, 8, 27).date(): "27 AUG",
        datetime.datetime(2024, 9, 3).date(): "03 SEP",
        datetime.datetime(2024, 9, 10).date(): "10 SEP",
        datetime.datetime(2024, 9, 17).date(): "17 SEP",
        datetime.datetime(2024, 9, 24).date(): "24 SEP",
        datetime.datetime(2024, 10, 1).date(): "01 OCT",
        datetime.datetime(2024, 10, 8).date(): "08 OCT",
        datetime.datetime(2024, 10, 15).date(): "15 OCT",
        datetime.datetime(2024, 10, 22).date(): "22 OCT",
        datetime.datetime(2024, 10, 29).date(): "29 OCT",
        datetime.datetime(2024, 11, 5).date(): "05 NOV",
        datetime.datetime(2024, 11, 12).date(): "12 NOV",
        datetime.datetime(2024, 11, 19).date(): "19 NOV",
        datetime.datetime(2024, 11, 26).date(): "26 NOV",
        datetime.datetime(2024, 12, 3).date(): "03 DEC",
        datetime.datetime(2024, 12, 10).date(): "10 DEC",
        datetime.datetime(2024, 12, 17).date(): "17 DEC",
        datetime.datetime(2024, 12, 24).date(): "24 DEC",
        datetime.datetime(2024, 12, 31).date(): "31 DEC",
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
        datetime.datetime(2024, 5, 13).date(): "13 MAY",
        datetime.datetime(2024, 5, 20).date(): "20 MAY",
        datetime.datetime(2024, 5, 27).date(): "27 MAY",
        datetime.datetime(2024, 6, 3).date(): "03 JUN",
        datetime.datetime(2024, 6, 10).date(): "10 JUN",
        datetime.datetime(2024, 6, 17).date(): "17 JUN",
        datetime.datetime(2024, 6, 24).date(): "24 JUN",
        datetime.datetime(2024, 7, 1).date(): "01 JUL",
        datetime.datetime(2024, 7, 8).date(): "08 JUL",
        datetime.datetime(2024, 7, 15).date(): "15 JUL",
        datetime.datetime(2024, 7, 22).date(): "22 JUL",
        datetime.datetime(2024, 7, 29).date(): "29 JUL",
        datetime.datetime(2024, 8, 5).date(): "05 AUG",
        datetime.datetime(2024, 8, 12).date(): "12 AUG",
        datetime.datetime(2024, 8, 19).date(): "19 AUG",
        datetime.datetime(2024, 8, 26).date(): "26 AUG",
        datetime.datetime(2024, 9, 2).date(): "02 SEP",
        datetime.datetime(2024, 9, 9).date(): "09 SEP",
        datetime.datetime(2024, 9, 16).date(): "16 SEP",
        datetime.datetime(2024, 9, 23).date(): "23 SEP",
        datetime.datetime(2024, 9, 30).date(): "30 SEP",
        datetime.datetime(2024, 10, 7).date(): "07 OCT",
        datetime.datetime(2024, 10, 14).date(): "14 OCT",
        datetime.datetime(2024, 10, 21).date(): "21 OCT",
        datetime.datetime(2024, 10, 28).date(): "28 OCT",
        datetime.datetime(2024, 11, 4).date(): "04 NOV",
        datetime.datetime(2024, 11, 11).date(): "11 NOV",
        datetime.datetime(2024, 11, 18).date(): "18 NOV",
        datetime.datetime(2024, 11, 25).date(): "25 NOV",
        datetime.datetime(2024, 12, 2).date(): "02 DEC",
        datetime.datetime(2024, 12, 9).date(): "09 DEC",
        datetime.datetime(2024, 12, 16).date(): "16 DEC",
        datetime.datetime(2024, 12, 23).date(): "23 DEC",
        datetime.datetime(2024, 12, 30).date(): "30 DEC",
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
        datetime.datetime(2024, 3, 28).date(): "28 MAR",
        datetime.datetime(2024, 4, 25).date(): "25 APR",
        datetime.datetime(2024, 5, 30).date(): "30 MAY",
        datetime.datetime(2024, 6, 27).date(): "27 JUN",
        datetime.datetime(2024, 7, 25).date(): "25 JUL",
        datetime.datetime(2024, 8, 29).date(): "29 AUG",
        datetime.datetime(2024, 9, 26).date(): "26 SEP",
        datetime.datetime(2024, 10, 31).date(): "31 OCT",
        datetime.datetime(2024, 11, 28).date(): "28 NOV",
        datetime.datetime(2024, 12, 26).date(): "26 DEC",

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
        datetime.datetime(2024, 3, 27).date(): "27 MAR",
        datetime.datetime(2024, 4, 30).date(): "30 APR",
        datetime.datetime(2024, 5, 29).date(): "29 MAY",
        datetime.datetime(2024, 6, 26).date(): "26 JUN",
        datetime.datetime(2024, 7, 31).date(): "31 JUL",
        datetime.datetime(2024, 8, 28).date(): "28 AUG",
        datetime.datetime(2024, 9, 25).date(): "25 SEP",
        datetime.datetime(2024, 10, 30).date(): "30 OCT",
        datetime.datetime(2024, 11, 27).date(): "27 NOV",
        datetime.datetime(2024, 12, 24).date(): "24 DEC",

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
    expiry = {datetime.datetime(2024, 2, 20).date(): "FEB",
                       datetime.datetime(2024, 3, 26).date(): "26 MAR",
                       datetime.datetime(2024, 4, 30).date(): "30 APR",
                       datetime.datetime(2024, 5, 28).date(): "28 MAY",
                       datetime.datetime(2024, 6, 25).date(): "25 JUN",
                       datetime.datetime(2024, 7, 30).date(): "30 JUL",
                       datetime.datetime(2024, 8, 27).date(): "27 AUG",
                       datetime.datetime(2024, 9, 24).date(): "24 SEP",
                       datetime.datetime(2024, 10, 29).date(): "29 OCT",
                       datetime.datetime(2024, 11, 26).date(): "26 NOV",
                       datetime.datetime(2024, 12, 31).date(): "31 DEC",
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
    expiry = {datetime.datetime(2024, 5, 27).date(): "27 MAY",
              datetime.datetime(2024, 6, 24).date(): "24 JUN",
              datetime.datetime(2024, 7, 29).date(): "29 JUL",
              datetime.datetime(2024, 8, 26).date(): "26 AUG",
              datetime.datetime(2024, 9, 30).date(): "30 SEP",
              datetime.datetime(2024, 10, 28).date(): "28 OCT",
              datetime.datetime(2024, 11, 25).date(): "25 NOV",
              datetime.datetime(2024, 12, 30).date(): "30 DEC",
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
        name = "IN:BANKNIFTY"
    elif stock == "NIFTY":
        name = "IN:NIFTY"
    elif stock == "FINNIFTY":
        name = "IN:FINNIFTY"
    elif stock == "MIDCPNIFTY":
        name = "IN:MIDCPNIFTY"
    return name

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

    # elif stock =="SENSEX":
    #     return getSensexExpiryDate_month(next_exp)
    else:
        return getNiftyExpiryDate_month(next_exp)

def getOptionFormat(stock, intExpiry, strike, ce_pe):
    if ce_pe == "CE":
        cepeword = "CALL"
    else:
        cepeword = "PUT"
    return "OP:" + str(stock) + " " + str(intExpiry)+ " " + str(strike) + " " + str(cepeword)

def getFutureFormat(stock, intExpiry):
    return "FUT:"+str(stock)+" "+str(intExpiry)+" "+str('FUT')

def getLTP(instrument):
    url = "http://localhost:4001/ltp?instrument=" + instrument
    try:
        resp = requests.get(url)
    except Exception as e:
        print(e)
    data = resp.json()
    return data

def manualLTP(symbol,dhan):
    dhan = dhanhq("1101643703","eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzE3MzEyNDk3LCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMTY0MzcwMyJ9.EPl1LKrg4qNNkPus59FozJYQSpjtDMU4n7f0B8IIVLBc38hqsFmmPYaIokYb9uYSLMHt5q_ZYKvefhA1x_SQUw")
    position = symbol.find(':')
    exch = symbol[:position]
    symb = symbol[position+1:]
    res = getSecurityId(symbol)
    if exch == "EQ":
        exch1 = "NSE_EQ"
    elif exch == "FUT" or exch == "OP":
        exch1 = "NSE_FNO"
    res_data =dhan.intraday_minute_data(
                        security_id=res[1],
                        exchange_segment=exch1,
                        instrument_type=res[2]
                    )
    print(res_data)
# manualLTP("EQ:RELIANCE",1)

def placeOrder(inst ,t_type,qty,order_type,price,variety,dhan,papertrading=0):
    position = inst.find(':')
    exch = inst[:position]
    symb = inst[position+1:]

    dt = datetime.datetime.now()
    #papertrading = 0 #if this is 1, then actual trades will get placed
    print(dt.hour,":",dt.minute,":",dt.second ," => ",t_type," ",symb," ",qty," ",order_type)

    res = getSecurityId(inst)
    security_id = res[1]

    if(t_type=="BUY"):
        t_type1=dhan.BUY
    elif(t_type=="SELL"):
        t_type1=dhan.SELL

    if(order_type=="MARKET"):
        order_type1 = dhan.MARKET
        price = 0
    elif(order_type=="LIMIT"):
        order_type1 = dhan.LIMIT

    if exch == "EQ":
        exch1 = dhan.NSE
    elif exch == "FUT" or exch == "OP":
        exch1 = dhan.FNO

    try:
        if papertrading == 1:
            orderid = dhan.place_order(security_id=security_id,   #hdfcbank
                                 exchange_segment=exch1,
                                 transaction_type=t_type1,
                                 quantity=qty,
                                 order_type=order_type1,
                                 product_type=dhan.INTRA,
                                 price=0)
            print(orderid)
            return orderid
        else:
            return 0

    except Exception as e:
        print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , "Failed : {} ".format(e))


