
# import getNotification
import threading
import ast
import re
import pytz
from fyers_apiv3 import fyersModel
from kite_trade import *
from kiteconnect import KiteConnect
import upstox_client
from dhanhq import dhanhq
import getInstrument
# from upstox_client.rest import ApiException
from NorenApi import NorenApi
from pmClient import PMClient
from APIConnect.APIConnect import APIConnect
from constants.exchange import ExchangeEnum
from constants.order_type import OrderTypeEnum
from constants.product_code import ProductCodeENum
from constants.duration import DurationEnum
from constants.action import ActionEnum
from constants.asset_type import AssetTypeEnum
from constants.chart_exchange import ChartExchangeEnum
from constants.intraday_interval import IntradayIntervalEnum
# from breeze_connect import BreezeConnect
from SmartApi import SmartConnect
from Connect_iifl import XTSConnect,XTSCommon
from pya3 import *
import gzip
from io import BytesIO
import requests
import pandas as pd
# import datetime
import os
import calendar
import pyotp
import traceback
# import time
import datetime
# import multiprocessing
import time
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

with open(resource_path('symbol_mapping.txt'),'r') as f:
    symbol_to_id_iifl = ast.literal_eval(f.read())[0]
alerts=[]
brokers=[]
# getNotification.login_and_get_tv_alerts(username,password,alerts)

def updateExchanges():
    global brokers
    with open(resource_path("config.txt"),'w') as f:
        f.write(str(brokers))
    getExchanges()

def getExchanges():
    global brokers
    with open(resource_path('config.txt'),'r') as f:
        brokers = ast.literal_eval(f.read())

# def login_angel():
angel_trading_obj = None
angel_hist_obj = None
getExchanges()
for b in brokers:
    try:
        if(b['name']=='angel'):
            # print(x)
            totp=pyotp.TOTP(b['params']['otp_token']).now()
            angel_trading_obj=SmartConnect(api_key=b['params']['trading_api'])
            trading_session=angel_trading_obj.generateSession(b['params']['username'],b['params']['password'],totp)
            print(trading_session)
            time.sleep(10)
            totp=pyotp.TOTP(b['params']['otp_token']).now()
            angel_hist_obj=SmartConnect(api_key=b['params']['historical_api'])
            hist_session=angel_hist_obj.generateSession(b['params']['username'],b['params']['password'],totp)
            print(hist_session)
        # if(b['name']=='iifl'):

    except:
        print("Angel not logged in all accounts.")
    try:
        if b['name']=='iifl' and b['timestamp'] == str(datetime.datetime.now().date()):
            api_key    = b['params']['Interactive_api_key']
            secret_key     = b['params']['Interactive_api_secret']
            m_api_key = b['params']['Market_api_key']
            m_secret_key = b['params']['Market_api_secret']
            api_iifl = XTSConnect(api_key, secret_key, 'WEBAPI')
            api_iifl_res = api_iifl.interactive_login()
            api_iifl_m = XTSConnect(m_api_key,m_secret_key,'WEBAPI')
            xtm_api_m_res = api_iifl_m.marketdata_login()
    except:
        print("IIFL error")


# Nuvama
token = pd.read_csv(resource_path('instruments/instruments.csv'),usecols=range(12))
# print(token)

def get_exch_type_angel(symbol, exp):
    if exp == 'NO':
        if symbol[:3] == 'NSE': return 1
        elif symbol[:3] == 'BSE': return 3
    if exp == 'YES':
        if symbol[:3] == 'NFO': return 2
        elif symbol[:3] == 'BSE': return 4
        elif symbol[:3] == 'MCX': return 5
        elif symbol[:3] == 'NCDEX': return 6
        elif symbol[:3] == 'CDS': return 7

def get_tokens_angel(symbols):
    allinst = pd.read_json('https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json')
    for i in range(len(allinst)):
        if symbols[4:] == "NIFTY":
            return 99926000
        elif symbols[4:] == "BANKNIFTY":
            return 99926009
        elif symbols[4:] == "FINNIFTY":
            return 99926037
        elif symbols[4:] == "MIDCPNIFTY":
            return 99926074
        elif allinst['symbol'][i] == symbols[4:] and allinst['exch_seg'][i] == symbols[:3]:
            if allinst['expiry'][i] == "":
                exch = get_exch_type_angel(symbols, 'NO')
            else:
                exch = get_exch_type_angel(symbols, 'YES')
            # print(exch)
            # symbol_token=allinst['token'][i]
            print(allinst['token'][i])
            return allinst['token'][i]

def extract_code_strike_expiry_icici(stock : str):
    exchange_code = stock.split(":")[0]
    stock_name = stock.split(":")[1]
    expiry = ""
    right = ""
    strike = ""

    opt_search = re.search(r"(\d{2}\w{3})(\d+|\d+\.\d+)(CE|PE)", stock_name)
    fut_search = re.search(r"(\d{2}\w{3})(FUT)", stock_name)

    if opt_search:
        stock_name = stock_name.replace(opt_search[0], "")
        expiry = opt_search[1]
        strike = opt_search[2]
        right = opt_search[3]

    elif fut_search:
        stock_name = stock_name.replace(fut_search[0], "")
        expiry = fut_search[1]

    return [
        exchange_code,
        stock_name,
        expiry,
        strike,
        right
    ]

def expiry_to_date_icici(expiry1):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    full_date = ""

    search = re.search(r"(\d{2})(\w{3})", expiry1)
    month = search[2]
    date = month[1]+month[2]

    month = month[0] + month[1:].lower()

    month = months[int(month[0])-1] if month[0].isnumeric() else month
    # print(month)
    if month[0] == "O":
        month = "Oct"
    elif month[0] == "N":
        month = "Nov"
    elif month[0] == "D":
        month = "Dec"

    if date.isnumeric():
        full_date = date+"-"+month+"-20"+search[1]
    else:
        lastdate = calendar.monthrange(int("20"+search[1]), months.index(month)+1)
        # print(lastdate)
        # lastdate = calendar.monthrange(int("20"+search[1]),11)
        # print(lastdate)
        # lastdate = lastdate[1]
        # if month == "Nov":
        #     full_date = "30-"+month+"-20"+search[1]
        # else:
        full_date = str(lastdate[1])+"-"+month+"-20"+search[1]
    print(full_date)
    return full_date

def get_tradingSymbol_exchangeToken_nuvama(symbolname):
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

def placeOrder_alice(username,api_key,inst, sym_type ,t_type,qty,order_type,price, papertrading=False):
    alice = Aliceblue(user_id=username,api_key=api_key)
    sessionid = alice.get_session_id()
    print(sessionid)
    inst = getInstrument.getInstrumentName(inst,sym_type,'alice',alice)
    print(inst)
    # quit()
    exch = inst[:3]
    symb = inst[4:]
    #paperTrading = 0 #if this is 1, then real trades will be placed
    if( t_type=="BUY"):
        t_type=TransactionType.Buy
    else:
        t_type=TransactionType.Sell

    #OrderType.Market, OrderType.Limit, OrderType.StopLossMarket, OrderType.StopLossLimit
    #ProductType.Delivery, ProductType.Intraday

    if(order_type=="M"):
        order_type=OrderType.Market
    elif(order_type=="L"):
        order_type=OrderType.Limit
    variety = 'regular'
    if variety == "regular":
        is_amo = False
    else:
        is_amo = True
    print(alice.get_instrument_by_symbol(exch, symb))
    try:
        if(papertrading == False):
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
            return order_id,inst

        else:
            order_id=0
            return order_id,inst

    except Exception as e:
        print(" => ", symb , "Failed : {} ".format(e))

def placeOrder_angel(inst,sym_type ,t_type,qty,order_type,price,trigger_price,product, papertrading=False):
    global angel_trading_obj, angel_hist_obj
    # inst = getOptionName.getOption(fyers,inst,'fyers')
    inst = getInstrument.getInstrumentName(inst,sym_type,'angel',angel_hist_obj)
    # inst = getOptionName.getOption(angel_hist_obj,inst,'angel')
    print(inst)
    # quit()
    if trading_session['message'] == 'SUCCESS':
        print("Connection Successful")
    else:
        print(trading_session['message'])
        return 0
    variety = 'NORMAL'
    exch = inst[:3]
    symbol_name = inst[4:]
    #papertrading = 0 #if this is 1, then real trades will be placed
    token = get_tokens_angel(inst)
    # print(token)
    if order_type=='M':
        order_type="MARKET"
    elif order_type=='L':
        order_type='LIMIT'
    elif order_type=='SL':
        order_type='STOPLOSS_LIMIT'

    if product=='NRML':
        product = 'CARRYFORWARD'
    elif product == 'MIS':
        product = 'INTRADAY'
    elif product == 'CNC':
        product = 'DELIVERY'

    try:
        if (papertrading == False):
            Targetorderparams = {
                "variety": "NORMAL",
                "tradingsymbol": symbol_name,
                "symboltoken": token,
                "transactiontype": t_type,
                "exchange": exch,
                "ordertype": order_type,
                "producttype": product,
                "duration": "DAY",
                "price": price,
                "squareoff": 0,
                "stoploss": 0,
                "triggerprice": trigger_price,
                "trailingStopLoss": 0,
                "quantity": qty
            }

            print(Targetorderparams)
            orderId = angel_trading_obj.placeOrder(Targetorderparams)
            print("The order id is: {}".format(orderId))
            return orderId, inst
        else:
            return 0, inst
    except Exception as e:
        traceback.print_exc()
        print("Order placement failed: {}".format(e))
        return "Failed due to"+str(e), inst

def placeOrder_dhan(inst,sym_type,t_type,qty,order_type,price,trigger_price,product, papertrading=False):
    dhan = dhanhq("client_id","access_token")
    inst = getInstrument.getInstrumentName(inst,sym_type,'dhan',dhan)
    # inst = getOptionName.getOption(angel_hist_obj,inst,'angel')
    print(inst)
    # quit()
    variety = 'NORMAL'
    exch = inst[:3]
    symbol_name = inst[4:]
    #papertrading = 0 #if this is 1, then real trades will be placed
    token = get_tokens_angel(inst)
    # print(token)
    if order_type=='M':
        order_type=dhan.MARKET
    elif order_type=='L':
        order_type=dhan.LIMIT
    elif order_type=='SL':
        order_type=dhan.SL

    if product=='NRML':
        product = dhan.MARGIN
    elif product == 'MIS':
        product = dhan.INTRA
    elif product == 'CNC':
        product = dhan.CNC

    try:
        if (papertrading == False):
            orderId = dhan.place_order(
                tag='',
                transaction_type=t_type,
                exchange_segment=dhan.NSE,
                product_type=product,
                order_type=order_type,
                validity='DAY',
                security_id='1333',
                quantity=qty,
                disclosed_quantity=0,
                price=price,
                trigger_price=trigger_price,
                after_market_order=False,
                amo_time='OPEN',
                bo_profit_value=0,
                bo_stop_loss_Value=0,
                drv_expiry_date=None,
                drv_options_type=None,
                drv_strike_price=None
            )
            print("The order id is: {}".format(orderId))
            return orderId, inst
        else:
            return 0, inst
    except Exception as e:
        traceback.print_exc()
        print("Order placement failed: {}".format(e))
        return "Failed due to"+str(e), inst

def placeOrder_fyers(access_token,client_id,inst,sym_type ,t_type,qty,order_type,price,trigger_price,product,papertrading=False):
    fyers = fyersModel.FyersModel(token=access_token,is_async=False,client_id=client_id,log_path="")
    inst = getInstrument.getInstrumentName(inst,sym_type,'fyers',fyers)
    # ltp = getInstrument.findManualPrice(inst,'fyers',)
    print(inst)
    # quit()
    exch = inst[:3]
    symb = inst[4:]
    dt = datetime.datetime.now()
    #papertrading = 0 #if this is 1, then actual trades will get placed
    print(dt.hour,":",dt.minute,":",dt.second ," => ",t_type," ",symb," ",qty," ",order_type)
    if(order_type=="M"):
        type1 = 2
        price = 0

    elif(order_type=="L"):
        type1 = 1
    elif (order_type=='SL'):
        type1 = 4

    if(t_type=="BUY"):
        side1=1
    elif(t_type=="SELL"):
        side1=-1

    if(product=='MIS'):
        product='INTRADAY'
    elif(product=='NRML'):
        product='MARGIN'
    elif(product=='CNC'):
        product='CNC'

    data =  {
        "symbol":inst,
        "qty":qty,
        "type":type1,
        "side":side1,
        "productType":product,
        "limitPrice":price,
        "stopPrice":trigger_price,
        "validity":"DAY",
        "disclosedQty":0,
        "offlineOrder":False,
        "stopLoss":0,
        "takeProfit":0
    }
    try:
        if (papertrading == False):
            orderid = fyers.place_order(data)
            print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , orderid)
            try:
                orderid = orderid['id']
            except:
                orderid = orderid['message']
            return orderid,inst
        else:
            return 0,inst


    except Exception as e:
        print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , "Failed : {} ".format(e))
        return e, inst

# def placeOrder_icici(api_key,secret_key,session_key,inst,sym_type ,t_type,qty,order_type,price,trigger_price,product, papertrading=False):
#     breeze = BreezeConnect(api_key=api_key)
#     breeze.generate_session(api_secret=secret_key, session_token=session_key)
#     exchange_code = ""
#     stock_name = ""
#     expiry1 = ""
#     strike = ""
#     right = ""
#     expiry_date_string = ""
#     inst = getInstrument.getInstrumentName(inst,sym_type,'icici',breeze)
#
#     print(inst)
#     if sym_type!='E':
#         try:
#             [exchange_code, stock_name, expiry1, strike, right] = extract_code_strike_expiry_icici(inst)
#         except Exception as e:
#             print(e)
#         print(expiry1)
#         if expiry1:
#             expiry_date_string = datetime.datetime.strptime(f"{expiry_to_date_icici(expiry1)} 06:00:00","%d-%b-%Y %H:%M:%S").isoformat()[:19] + '.000Z'
#     else:
#         stock_name = inst
#
#     print("-------------")
#     print(inst)
#     # quit()
#
#     if (t_type == "BUY"):
#         action = "buy"
#     else:
#         action = "sell"
#     if order_type=='M':
#         order_type="market"
#     elif order_type=='L':
#         order_type='limit'
#     elif order_type=='SL':
#         order_type='stoploss'
#
#     # if product=='MIS' and sym_type=='O':
#     if sym_type == 'O':
#         product='options'
#     elif sym_type == 'F':
#         product = 'futures'
#     elif sym_type == 'E':
#         product = 'cash'
#
#     # if order_type == "MARKET":
#     #     order_type1 = "market"
#     # elif order_type == "LIMIT":
#     #     order_type1 = "limit"
#
#     #papertrading = 0 #if this is 1, then real trades will be placed
#
#     dt = datetime.datetime.now()
#     print(dt.hour,":",dt.minute,":",dt.second ," => ",t_type," ",inst," ",qty," ",order_type)
#     # print(type(stock_name))
#     # print(type(exchange_code))
#     # print(type(product))
#     # print(type(action))
#     # print(type(order_type))
#     # print(type(trigger_price))
#     # print(type(qty))
#     # print(type(price))
#     # print(type(expiry_date_string))
#     # print(type(right))
#     # print(type(strike))
#     try:
#         if (papertrading == False):
#             # return stock_name, exchange_code, action, order_type1, qty, price, expiry_date_string, right, strike
#             order_id = breeze.place_order(
#                 stock_code=stock_name, #
#                 exchange_code=exchange_code, #
#                 product=product, #
#                 action=action,
#                 order_type=order_type,
#                 stoploss=str(trigger_price),
#                 quantity=str(qty),
#                 price=str(price),
#                 validity="day",
#                 validity_date="",
#                 disclosed_quantity="0",
#                 expiry_date=expiry_date_string, #
#                 right=str(right), #
#                 strike_price=str(strike), #
#                 user_remark="")
#
#             print(dt.hour,":",dt.minute,":",dt.second ," => ", inst , int(order_id) )
#             return order_id,inst
#         else:
#             return 0, inst
#
#     except Exception as e:
#         print(dt.hour,":",dt.minute,":",dt.second ," => ", inst , "Failed : {} ".format(e))
#         return e, inst

def placeOrder_nuvama(api_key,api_secret,request_id,inst,sym_type ,t_type,qty,order_type,price,trigger_price,product, papertrading=False):
    api_connect = APIConnect(api_key, api_secret, request_id, True)
    inst = getInstrument.getInstrumentName(inst,sym_type,'nuvama',api_connect)
    print(inst)
    # quit()
    exch = inst[:3]
    symb = inst[4:]
    tradingsymbol, exchangetoken = get_tradingSymbol_exchangeToken_nuvama(inst)
    print(tradingsymbol)
    print(exchangetoken)
    dt = datetime.datetime.now()
    #papertrading = 0 #if this is 1, then actual trades will get placed
    print(dt.hour,":",dt.minute,":",dt.second ," => ",t_type," ",symb," ",qty," ",order_type)

    if(order_type=="M"):
        order_type = OrderTypeEnum.MARKET
    elif(order_type=="L"):
        order_type = OrderTypeEnum.LIMIT
    elif(order_type=='SL'):
        order_type=OrderTypeEnum.STOP_LIMIT

    if(t_type=="BUY"):
        action = ActionEnum.BUY
    elif(t_type=="SELL"):
        action = ActionEnum.SELL

    if(exch=="NSE"):
        exchange = ExchangeEnum.NSE
    elif(exch=="NFO"):
        exchange = ExchangeEnum.NFO

    if product=='MIS':
        product=ProductCodeENum.MIS
    elif product=='NRML':
        product=ProductCodeENum.NRML
    elif product=='CNC':
        product=ProductCodeENum.CNC
    try:
        if (papertrading == False):
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
                                             TriggerPrice=trigger_price,
                                             ProductCode = product)

            print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , orderid)
            oid = ast.literal_eval(orderid)
            print(oid)
            return oid['data']['oid'], inst
        else:
            return 0, inst

    except Exception as e:
        print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , "Failed : {} ".format(e))
        return 0,inst


####################################################################################
# formatting of arguments left in paytm


def placeOrder_Paytm(inst,api_key,api_secret,request_token,access_token,public_access_token,read_access_token,qty,order_type,price,trigger_price,product,papertrading=False):
    pm = PMClient(api_key=api_key, api_secret=api_secret)

    pm.generate_session(request_token)

    pm.set_access_token(access_token)
    pm.set_public_access_token(public_access_token)
    pm.set_read_access_token(read_access_token)
    exch = inst[:3]
    symb = inst[4:]
    dt = datetime.datetime.now()
    if papertrading == 1:
        try:
            res = pm.place_order(
                txn_type="S",
                exchange=exch,
                segment="E",
                product="I",
                security_id="772",
                quantity=qty,
                validity="DAY",
                order_type=order_type,
                price=price,
                source="N",
                off_mkt_flag=False,
                trigger_price=trigger_price
            )
            print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , res)
            return res, inst
            # logging.info("Response : {}".format(res))
        except Exception as e:
            # logging.info("Error : {}".format(e))
            print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , "Failed : {} ".format(e))
    elif papertrading==0:
        return 0, inst

def placeOrder_iifl(token,userId,inst,sym_type ,t_type,qty,order_type,price,trigger_price,product, papertrading=False):
    # api = NorenApi()
    # api.set_session(userid=api_key, password=password,usertoken=user_token)
    # api_iifl = XTSCommon(token,userId)
    inst = getInstrument.getInstrumentName(inst,sym_type,'iifl',api_iifl_m)
    print(inst)
    # quit()
    sid = symbol_to_id_iifl[inst].split('|')
    # exch = inst[:3]
    # symb = inst[4:]
    #paperTrading = 0 #if this is 1, then real trades will be placed
    if( t_type=="BUY"):
        t_type=api_iifl.TRANSACTION_TYPE_BUY
    else:
        t_type=api_iifl.TRANSACTION_TYPE_SELL

    if(order_type=="M"):
        order_type=api_iifl.ORDER_TYPE_MARKET
    elif(order_type=="L"):
        order_type=api_iifl.ORDER_TYPE_LIMIT
    elif(order_type=="SL"):
        order_type=api_iifl.ORDER_TYPE_STOPLIMIT

    if product=='MIS':
        product=api_iifl.PRODUCT_MIS
    elif product=='NRML':
        product=api_iifl.PRODUCT_NRML
    elif product=='CNC':
        product=api_iifl.PRODUCT_NRML
    segments_dict = {'1':"NSECM",'2' :"NSEFO", '3':"NSECD", '11':"BSECM", '12':"BSEFO", '51':"MCXFO"}
    try:
        if(papertrading == False):
            order_id = api_iifl.place_order(exchangeSegment=segments_dict[sid[0]],
                                            exchangeInstrumentID=int(sid[1]),
                                            productType=product,
                                            orderType=order_type,
                                            orderSide=t_type,
                                            timeInForce=api_iifl.VALIDITY_DAY,
                                            disclosedQuantity=0,
                                            orderQuantity=qty,
                                            limitPrice=price,
                                            stopPrice=trigger_price,
                                            orderUniqueIdentifier="454845",
                                            clientID=userId
                                            )
            if order_id['type'] != 'error':
                order_id = order_id['result']['AppOrderID']
            else:
                order_id = 'Error placing order'
            print(" => ", inst, order_id)
            return order_id, inst

        else:
            order_id=0
            return order_id, inst

    except Exception as e:
        print(" => ", inst , "Failed : {} ".format(e))
        return 0,inst
def placeOrder_shoonya(user_id,password,user_token,inst,sym_type ,t_type,qty,order_type,price,trigger_price,product, papertrading=False):
    api = NorenApi()
    api.set_session(userid=user_id, password=password,usertoken=user_token)
    inst = getInstrument.getInstrumentName(inst,sym_type,'shoonya',api)
    print(inst)
    # quit()

    exch = inst[:3]
    symb = inst[4:]
    #paperTrading = 0 #if this is 1, then real trades will be placed
    if( t_type=="BUY"):
        t_type="B"
    else:
        t_type="S"

    if(order_type=="M"):
        order_type="MKT"
    elif(order_type=="L"):
        order_type="LMT"
    elif(order_type=="SL"):
        order_type="SL-LMT"

    if product=='MIS':
        product='I'
    elif product=='NRML':
        product='M'
    elif product=='CNC':
        product='C'

    try:
        if(papertrading == False):
            order_id = api.place_order(buy_or_sell=t_type,  #B, S
                                       product_type=product, #C CNC, M NRML, I MIS
                                       exchange=exch,
                                       tradingsymbol=symb,
                                       quantity = qty,
                                       discloseqty=qty,
                                       price_type= order_type, #LMT, MKT, SL-LMT, SL-MKT
                                       price = price,
                                       trigger_price=trigger_price,
                                       amo="NO",#YES, NO
                                       retention="DAY"
                                       )
            print(" => ", symb , order_id['norenordno'] )
            return order_id['norenordno'], inst

        else:
            order_id=0
            return order_id, inst

    except Exception as e:
        print(" => ", symb , "Failed : {} ".format(e))
        return 0,inst

def placeOrder_upstox(access_token,inst,sym_type ,t_type,qty,order_type,price,trigger_price,product, papertrading=False):
    # Configure OAuth2 access token for authorization: OAUTH2
    #https://upstox.com/developer/api-documentation/#tag/Order/operation/placeOrder
    gzipped_file_url  = "https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz"
    # Download the gzipped file from the URL
    response = requests.get(gzipped_file_url)
    gzipped_content = BytesIO(response.content)

    with gzip.open(gzipped_content, 'rb') as f:
        df2 = pd.read_csv(f)
    configuration = upstox_client.Configuration()
    api_version = '2.0'
    # Login and authorization
    configuration.access_token = access_token
    api_instance = upstox_client.OrderApi(upstox_client.ApiClient(configuration))
    api_quote_instance = upstox_client.MarketQuoteApi(upstox_client.ApiClient(configuration))
    inst = getInstrument.getInstrumentName(inst,sym_type,'upstox',api_quote_instance)
    print(inst)
    instrument_key = df2[df2['tradingsymbol'] == inst]['instrument_key'].values[0]
    # quit()

    #papertrading = 1 #if this is 1, then real trades will be placed
    dt = datetime.datetime.now()
    if order_type=='M':
        order_type="MARKET"
    elif order_type=='L':
        order_type='LIMIT'
    elif order_type=='SL':
        order_type='SL'

    if order_type == "MARKET":
        price = 0

    if product=='MIS':
        product='I'
    elif product=='NRML' or product=='CNC':
        product='D'
    try:
        if (papertrading == False):
            order_details = {
                "quantity": qty,
                "product": product,
                "validity": "DAY",
                "price": price,
                "tag": "string",
                "instrument_token": instrument_key,
                "order_type": order_type,
                "transaction_type": t_type,
                "disclosed_quantity": 0,
                "trigger_price": trigger_price,
                "is_amo": False
            }


            api_response = api_instance.place_order(order_details, api_version)
            print(dt.hour,":",dt.minute,":",dt.second ," => ", inst , api_response.data.order_id)
            return api_response.data.order_id, inst
        else:
            return 0, inst

    except Exception as e:
        print(dt.hour,":",dt.minute,":",dt.second ," => ", inst , "Failed : {} ".format(e))
        return "Error:"+str(e), inst

def placeOrder_zerodha(access_token,api_key,inst,sym_type ,t_type,qty,order_type,price,trigger_price,product, papertrading=0):
    kc = KiteConnect(api_key=api_key)
    kc.set_access_token(access_token)
    inst = getInstrument.getInstrumentName(inst,sym_type,'zerodha',kc)
    print(inst)
    # quit()
    exch = inst[:3]
    symb = inst[4:]
    #papertrading = 0 #if this is 1, then real trades will be placed
    dt = datetime.datetime.now()
    print(dt.hour,":",dt.minute,":",dt.second ," => ",t_type," ",symb," ",qty," ",order_type)
    if order_type=='M':
        order_type="MARKET"
    elif order_type=='L':
        order_type='LIMIT'

    if product=='NRML':
        product = kc.PRODUCT_NRML
    elif product == 'MIS':
        product = kc.PRODUCT_MIS
    elif product == 'CNC':
        product = kc.PRODUCT_CNC
    try:
        if (papertrading == False):
            order_id  = kc.place_order( variety = 'regular',
                                        tradingsymbol= symb ,
                                        exchange= exch,
                                        transaction_type= t_type,
                                        quantity= qty,
                                        order_type=order_type,
                                        product=product,
                                        price=price,
                                        trigger_price=trigger_price)


            try:
                order_id = order_id["data"]["order_id"]
            except:
                order_id = order_id['message']
            print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , order_id )
            return order_id, inst
        else:
            return 0, inst

    except Exception as e:
        print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , "Failed : {} ".format(e))
        return "Failed: "+str(e),inst

def placeOrder_zerodhaenc(enc,inst,sym_type ,t_type,qty,order_type,price,trigger_price,product, papertrading=False):
    # kc = KiteConnect(api_key=api_key)
    # kc.set_access_token(access_token)
    kc = KiteApp(enctoken=enc)
    # res = kc.login()

    # print(res.json())
    inst = getInstrument.getInstrumentName(inst,sym_type,'zerodha',kc)
    print(inst)
    # quit()
    exch = inst[:3]
    symb = inst[4:]
    #papertrading = 0 #if this is 1, then real trades will be placed
    dt = datetime.datetime.now()
    print(dt.hour,":",dt.minute,":",dt.second ," => ",t_type," ",symb," ",qty," ",order_type)
    if order_type=='M':
        order_type="MARKET"
    elif order_type=='L':
        order_type='LIMIT'

    if product=='NRML':
        product = kc.PRODUCT_NRML
    elif product == 'MIS':
        product = kc.PRODUCT_MIS
    elif product == 'CNC':
        product = kc.PRODUCT_CNC
    try:
        if (papertrading == False):
            order_id  = kc.place_order( variety = 'regular',
                                        tradingsymbol= symb ,
                                        exchange= exch,
                                        validity=kc.VALIDITY_DAY,
                                        transaction_type= t_type,
                                        quantity= qty,
                                        order_type=order_type,
                                        product=product,
                                        price=price,
                                        trigger_price=trigger_price)
            try:
                order_id = order_id["data"]["order_id"]
            except:
                order_id = order_id['message']
            print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , order_id )
            return order_id, inst
        else:
            return 0, inst

    except Exception as e:
        print(dt.hour,":",dt.minute,":",dt.second ," => ", symb , "Failed : {} ".format(e), order_id['message'])
        return "Failed: "+str(e),inst

def main(x,orders,papertrading):
    getExchanges()
    # login_angel()
    if(x['placed']==0):
        # print(x)
        for b in brokers:
            if(x['broker'].lower()=='alice'):
                # if(b['active']==1):
                if(b['name']=='alice' and b['id']==int(x['broker_id']) and b['timestamp'] == str(datetime.datetime.now().date())):
                    # print(x)
                    #             instrument = 'NSE:'+str(x['symbol']).upper()+'-EQ'
                    oid,instr = placeOrder_alice(username=b['params']['username'],api_key=b['params']['api_key'],
                                                 inst=x['symbol'],t_type=x['direction'],sym_type=x['type'],qty=x['qty'],order_type=x['order_type'],price=0,papertrading=papertrading)
                    print("Order id:",oid)
                    x['placed']=1
                    x['order_symbol'] = instr
                    x['oid'] = oid
                    orders.append(x)
            if(x['broker'].lower()=='angel'):
                # for b in brokers:
                # if(b['active']==1):
                if(b['name']=='angel' and b['id']==int(x['broker_id']) and b['timestamp'] == str(datetime.datetime.now().date())):
                    # print(x)
                    oid, instr = placeOrder_angel(inst=x['symbol'],sym_type=x['type'],t_type=x['direction'],qty=x['qty'],order_type=x['order_type'],price=x['price'],trigger_price=x['trigger_price'],product=x['product'],papertrading=papertrading)
                    print("Order id:",oid)
                    x['placed']=1
                    x['oid'] = oid
                    x['order_symbol'] = instr
                    orders.append(x)
                    break
            if(x['broker'].lower()=='dhan'):
                if(b['name']=='dhan' and b['id']==int(x['broker_id']) and b['timestamp'] == str(datetime.datetime.now().date())):
                    oid, instr = placeOrder_dhan(inst=x['symbol'],sym_type=x['type'],t_type=x['direction'],qty=x['qty'],order_type=x['order_type'],price=x['price'],trigger_price=x['trigger_price'],product=x['product'],papertrading=papertrading)
                    print("Order id:",oid)
                    x['placed']=1
                    x['oid'] = oid
                    x['order_symbol'] = instr
                    orders.append(x)
                    break
            if(x['broker'].lower()=='fyers'):
                # for b in brokers:
                # if(b['active']==1):
                if(b['name']=='fyers' and b['id']==int(x['broker_id']) and b['timestamp'] == str(datetime.datetime.now().date())):
                    # print(x)
                    oid, instr = placeOrder_fyers(access_token=b['access_token'],client_id=b['params']['client_id'],
                                                  inst=x['symbol'],sym_type=x['type'],t_type=x['direction'],qty=x['qty'],order_type=x['order_type'],price=x['price'],trigger_price=x['trigger_price'],product=x['product'],papertrading=papertrading)
                    print("Order id:",oid)
                    x['placed']=1
                    x['order_symbol'] = instr
                    x['oid'] = oid
                    # dt = datetime.datetime.now()
                    # order_time = str(dt.hour)+":"+str(dt.minute)+":"+str(dt.second)+"  "+str(dt.day)+"/"+str(dt.month)+"/"+str(dt.year)
                    # order_time = time.localtime()
                    # x['time'] = order_time
                    orders.append(x)
                    break
                # else:
                #     print("Not Logged in Fyers")
            # if(x['broker'].lower()=='icici'):
            #     # for b in brokers:
            #     # if(b['active']==1):
            #     if(b['name']=='icici' and b['id']==int(x['broker_id']) and b['timestamp'] == str(datetime.datetime.now().date())):
            #         # print(x)
            #         oid,instr = placeOrder_icici(api_key=b['params']['api_key'],secret_key=b['params']['secret_key'],session_key=b['session_key'],
            #                                      inst=x['symbol'],sym_type=x['type'],t_type=x['direction'],qty=x['qty'],order_type=x['order_type'],price=x['price'],trigger_price=x['trigger_price'],product=x['product'],papertrading=papertrading)
            #         print("Order id:",oid)
            #         x['placed']=1
            #         x['oid'] = oid
            #         x['order_symbol'] = instr
            #         orders.append(x)
            #         break
            if(x['broker'].lower()=='iifl'):
                # for b in brokers:
                # if(b['active']==1):
                if(b['name']=='iifl' and b['id']==int(x['broker_id']) and b['timestamp'] == str(datetime.datetime.now().date())):
                    # print(x)
                    oid,instr = placeOrder_iifl(token=b['token'],userId=b['userId'],
                                                inst=x['symbol'],sym_type=x['type'],t_type=x['direction'],qty=x['qty'],order_type=x['order_type'],price=x['price'],trigger_price=x['trigger_price'],product=x['product'],papertrading=papertrading)
                    print("Order id:",oid)
                    x['placed']=1
                    x['oid'] = oid
                    x['order_symbol'] = instr
                    orders.append(x)
                    break
            if(x['broker'].lower()=='nuvama'):
                # for b in brokers:
                # if(b['active']==1):
                if(b['name']=='nuvama' and b['id']==int(x['broker_id']) and b['timestamp'] == str(datetime.datetime.now().date())):
                    # print(x)
                    oid, instr = placeOrder_nuvama(api_key=b['params']['api_key'],api_secret=b['params']['api_secret'],request_id=b['request_token'],
                                                   inst=x['symbol'],sym_type=x['type'],t_type=x['direction'],qty=x['qty'],order_type=x['order_type'],price=x['price'],trigger_price=x['trigger_price'],product=x['product'],papertrading=papertrading)
                    print("Order id:",oid)
                    x['placed']=1
                    x['oid'] = oid
                    x['order_symbol'] = instr
                    orders.append(x)
                    break
            if(x['broker'].lower()=='shoonya'):
                # for b in brokers:
                # if(b['active']==1):
                if(b['name']=='shoonya' and b['id']==int(x['broker_id']) and b['timestamp'] == str(datetime.datetime.now().date())):
                    # print(x)
                    oid, instr = placeOrder_shoonya(user_token=b['user_token'],user_id=b['params']['username'],password=b['params']['password'],
                                                    inst=x['symbol'],sym_type=x['type'],t_type=x['direction'],qty=x['qty'],order_type=x['order_type'],price=x['price'],trigger_price=x['trigger_price'],product=x['product'],papertrading=papertrading)
                    print("Order id:",oid)
                    x['placed']=1
                    x['oid'] = oid
                    x['order_symbol'] = instr
                    orders.append(x)
                    break
            if(x['broker'].lower()=='upstox'):
                # for b in brokers:
                # if(b['active']==1):
                if(b['name']=='upstox' and b['id']==int(x['broker_id']) and b['timestamp'] == str(datetime.datetime.now().date())):
                    # print(x)
                    oid, instr = placeOrder_upstox(access_token=b['access_token'],
                                                   inst=x['symbol'],sym_type=x['type'],t_type=x['direction'],qty=x['qty'],order_type=x['order_type'],price=x['price'],trigger_price=x['trigger_price'],product=x['product'],papertrading=papertrading)
                    print("Order id:",oid)
                    x['placed']=1
                    x['oid'] = oid
                    x['order_symbol'] = instr
                    orders.append(x)
                    break
            if(x['broker'].lower()=='zerodha-enc'):
                # for b in brokers:
                # if(b['active']==1):
                if(b['name']=='zerodha-enc' and b['id']==int(x['broker_id']) and b['timestamp'] == str(datetime.datetime.now().date())):
                    # print(x)
                    oid, instr = placeOrder_zerodhaenc(enc=b['enc_token'],
                                                       inst=x['symbol'],sym_type=x['type'],t_type=x['direction'],qty=x['qty'],order_type=x['order_type'],price=x['price'],trigger_price=x['trigger_price'],product=x['product'],papertrading=papertrading)
                    print("Order id:",oid)
                    x['placed']=1
                    x['order_symbol'] = instr
                    x['oid'] = oid
                    orders.append(x)
                    break
            if(x['broker'].lower()=='zerodha'):
                # for b in brokers:
                # if(b['active']==1):
                if(b['name']=='zerodha' and b['id']==int(x['broker_id']) and b['timestamp'] == str(datetime.datetime.now().date())):
                    # print(x)
                    oid, instr = placeOrder_zerodha(access_token=b['access_token'],api_key=b['params']['api_key'],
                                                    inst=x['symbol'],sym_type=x['type'],t_type=x['direction'],qty=x['qty'],order_type=x['order_type'],price=x['price'],trigger_price=x['trigger_price'],product=x['product'],papertrading=papertrading)
                    print("Order id:",oid)
                    x['placed']=1
                    x['order_symbol'] = instr
                    x['oid'] = oid
                    orders.append(x)
                    break
        return x
        # quit()




# order_time = time.localtime()
# print(time.strftime('%H:%M:%S %d:%m:%Y',order_time))