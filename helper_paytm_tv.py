import datetime
import time
import requests
from datetime import timedelta
from pytz import timezone
import pandas as pd
import pytz
from pyPMClient.pmClient import PMClient
#https://github.com/paytmmoney/pyPMClient
#https://developer.paytmmoney.com/docs/api/place-regular-order


def relogin():
    api_key = open("paytm_api_key.txt",'r').read()
    secret_key = open("paytm_secret_key.txt",'r').read()
    paytm_access_token = open("paytm_access_token.txt",'r').read()
    paytm_public_token = open("paytm_public_token.txt",'r').read()
    paytm_read_token = open("paytm_read_token.txt",'r').read()

    # Initialize PMClient using apiKey, apiSecret & jwt tokens if user has already generated.
    pm = PMClient(api_secret=secret_key, api_key=api_key, access_token=paytm_access_token, public_access_token=paytm_public_token, read_access_token=paytm_read_token)

    return pm

def getNiftyExpiryDate():
    nifty_expiry = {
        datetime.datetime(2024, 2, 1).date(): "01 FEB",
        datetime.datetime(2024, 2, 8).date(): "08 FEB",
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
    }

    today = datetime.datetime.now().date()

    for date_key, value in nifty_expiry.items():
        if today <= date_key:
            print(value)
            return value

def getBankNiftyExpiryDate():
    banknifty_expiry = {
        datetime.datetime(2024, 2, 7).date(): "07 FEB",
        datetime.datetime(2024, 2, 14).date(): "14 FEB",
        datetime.datetime(2024, 2, 21).date(): "21 FEB",
        datetime.datetime(2024, 2, 29).date(): "29 FEB",
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
    }

    today = datetime.datetime.now().date()

    for date_key, value in banknifty_expiry.items():
        if today <= date_key:
            print(value)
            return value

def getIndexSpot(stock):
    if stock == "BANKNIFTY":
        name = "NSE:BANKNIFTY-INDEX"
    elif stock == "NIFTY":
        name = "NSE:NIFTY-INDEX"

    return name

def getOptionFormat(stock, intExpiry, strike, ce_pe):
    if ce_pe == "CE":
        return "NSE" +str(stock) +" " + str(intExpiry)+" "+str(strike)+" "+"CALL"
    else:
        return "NSE" +str(stock) +" " + str(intExpiry)+" "+str(strike)+" "+"PUT"

def getLTP(instrument):
    url = "http://localhost:4001/ltp?instrument=" + instrument
    try:
        resp = requests.get(url)
    except Exception as e:
        print(e)
    data = resp.json()
    return data

def getSecurityId(symbolname):
    token = pd.read_csv('security_master.csv',usecols=range(12))
    exch = symbolname[:3]
    name = symbolname[4:]
    if "-" in name:
        namestripped = name.split('-')
    else:
        temp = name + "-CE"
        namestripped = temp.split('-')
    scripId = ""
    scripType=""
    try:
        if(namestripped[-1].upper()=='INDEX'):
            scripId = str(token[(token['name'] == namestripped[0].upper()) & (token['exchange'] == exch) & (token['instrument_type'] == 'I')]['security_id'].values[0])
            scripType='INDEX'
        elif(namestripped[-1].upper()=='EQ'):
            scripId = str(token[(token['symbol'] == namestripped[0].upper()) & (token['exchange'] == exch) & (token['instrument_type'] == 'ES')]['security_id'].values[0])
            scripType="EQUITY"
        elif(namestripped[-1].upper()=='ETF'):
            scripId = str(token[(token['symbol'] == namestripped[0].upper()) & (token['exchange'] == exch) & (token['instrument_type'] == 'ETF')]['security_id'].values[0])
            scripType='ETF'
        elif(namestripped[-1].upper()=="FUT"):
            scripId = str(token[(token['symbol'] == name) & (token['exchange'] == exch)]['security_id'].values[0])
            scripType='FUTURE'
        elif(namestripped[-1].upper() in ['CE','PE']):
            #scripId = str(token[(token['symbol'] == name) & (token['exchange'] == exch)]['security_id'].values[0])
            scripId = str(token[(token['name'] == name) & (token['exchange'] == exch)]['security_id'].values[0])
            scripType='OPTION'
        else:
            raise IndexError
    except IndexError as e:
        print("Skipping", symbolname)
    else:
        return (scripId,scripType)

def placeOrder(inst ,t_type,qty,order_type,price,variety,pm,papertrading=0):
    exch = inst[:3]
    symb = inst[4:]
    dt = datetime.datetime.now()
    #papertrading = 0 #if this is 1, then actual trades will get placed
    print(dt.hour,":",dt.minute,":",dt.second ," => ",t_type," ",symb," ",qty," ",order_type)

    '''
    Type of product (C/I/B/V/M)
    C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), 
    M (Margin (Valid for Segment='D'))    
    B (Bracket order (Valid for Segment= E/D)), 
    V (Cover Order (Valid for Segment= E/D)),
    '''

    if "-" in inst:
        namestripped = inst.split('-')
    else:
        temp = inst + "-CE"
        namestripped = temp.split('-')

    if(namestripped[-1].upper()=='EQ'):
        segment = "E"
        product = "C"
    else:
        segment = "D"
        product = "I"


    if(order_type=="MARKET"):
        type1 = "MKT"
        price = 0
    elif(order_type=="LIMIT"):
        type1 = "LMT"

    if(t_type=="BUY"):
        t_type="Buy"
    elif(t_type=="SELL"):
        t_type="Sell"

    (scripId,scripType) = getSecurityId(inst)

    try:
        if (papertrading == 1):
            # Regular Order
            orderid = pm.place_order(txn_type = t_type,
                                     exchange = "NSE",
                                     segment = segment,
                                     product = product,
                                     security_id = scripId,
                                     quantity = qty,
                                     validity = "DAY",
                                     order_type = type1,
                                     price = price,
                                     off_mkt_flag = False)
            print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , orderid)
            return orderid
        else:
            return 0

    except Exception as e:
        print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , "Failed : {} ".format(e))

def modifyOrder(oid,inst ,t_type,qty,order_type,price,variety,pm):
    exch = inst[:3]
    symb = inst[4:]
    dt = datetime.datetime.now()
    #papertrading = 0 #if this is 1, then actual trades will get placed
    print(dt.hour,":",dt.minute,":",dt.second ," => ",t_type," ",symb," ",qty," ",order_type)

    '''
    Type of product (C/I/B/V/M)
    C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), 
    M (Margin (Valid for Segment='D'))    
    B (Bracket order (Valid for Segment= E/D)), 
    V (Cover Order (Valid for Segment= E/D)),
    '''

    if "-" in inst:
        namestripped = inst.split('-')
    else:
        temp = inst + "-CE"
        namestripped = temp.split('-')

    if(namestripped[-1].upper()=='EQ'):
        segment = "E"
        product = "C"
    else:
        segment = "D"
        product = "I"


    if(order_type=="MARKET"):
        type1 = "MKT"
        price = 0
    elif(order_type=="LIMIT"):
        type1 = "LMT"

    if(t_type=="BUY"):
        t_type="Buy"
    elif(t_type=="SELL"):
        t_type="Sell"

    (scripId,scripType) = getSecurityId(inst)

    try:
        orderid = pm.modify_order(txn_type = t_type,
                               exchange = "NSE",
                               segment = segment,
                               product = product,
                               security_id = scripId,
                               quantity = qty,
                               validity = "DAY",
                               order_type = type1,
                               price = price,
                               order_no = oid,
                               off_mkt_flag = False)
        print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , orderid)
        return orderid

    except Exception as e:
        print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , "Failed : {} ".format(e))

def cancelOrder(oid,inst ,t_type,qty,order_type,price,variety,pm):
    exch = inst[:3]
    symb = inst[4:]
    dt = datetime.datetime.now()
    #papertrading = 0 #if this is 1, then actual trades will get placed
    print(dt.hour,":",dt.minute,":",dt.second ," => ",t_type," ",symb," ",qty," ",order_type)

    '''
    Type of product (C/I/B/V/M)
    C ((Cash and Carry / Delivery) Valid only for Segment='E'), I (Intraday (Valid for Segment= E/D)), 
    M (Margin (Valid for Segment='D'))    
    B (Bracket order (Valid for Segment= E/D)), 
    V (Cover Order (Valid for Segment= E/D)),
    '''

    if "-" in inst:
        namestripped = inst.split('-')
    else:
        temp = inst + "-CE"
        namestripped = temp.split('-')

    if(namestripped[-1].upper()=='EQ'):
        segment = "E"
        product = "C"
    else:
        segment = "D"
        product = "I"


    if(order_type=="MARKET"):
        type1 = "MKT"
        price = 0
    elif(order_type=="LIMIT"):
        type1 = "LMT"

    if(t_type=="BUY"):
        t_type="Buy"
    elif(t_type=="SELL"):
        t_type="Sell"

    (scripId,scripType) = getSecurityId(inst)

    try:
        orderid = pm.cancel_order(txn_type = t_type,
                                  exchange = "NSE",
                                  segment = segment,
                                  product = product,
                                  security_id = scripId,
                                  quantity = qty,
                                  validity = "DAY",
                                  order_type = type1,
                                  price = price,
                                  order_no = oid,
                                  off_mkt_flag = False)
        print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , orderid)
        return orderid

    except Exception as e:
        print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , "Failed : {} ".format(e))


def getOrders(pm):
    return pm.order_book()

def manualLTP(pm, inst):
    (scripId,scripType) = getSecurityId(inst)
    exch = inst[:3]
    full_id = [exch + ":" + scripId + ":" + scripType]
    print(full_id)

    a = pm.get_live_market_data("FULL",full_id)
    ltp = a['data'][0]['last_price']
    print(ltp)
    #a = pm.get_live_market_data("FULL",preference)
    #print(a)

def getMargin(pm):
    return pm.funds_summary()

def getPositions(pm):
    return pm.position()

def getHoldings(pm):
    return pm.holdings_value()


def getDailyOHLC(pm, inst):
    (scripId,scripType) = getSecurityId(inst)
    exch = inst[:3]
    full_id = [exch + ":" + scripId + ":" + scripType]
    print(full_id)

    a = pm.get_live_market_data("FULL",full_id)

    ltp = a['data'][0]['last_price']
    open = a['data'][0]['ohlc']['open']
    high = a['data'][0]['ohlc']['high']
    low = a['data'][0]['ohlc']['low']
    close = a['data'][0]['ohlc']['close']
    print (open, high, low, ltp)

    return open, high, low, ltp
