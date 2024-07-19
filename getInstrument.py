import time
import ast
import pandas as pd
# import importlib
import sys
import os
from nse_ltp import NationalStockExchange


def importhelper(broker):
    if(broker == 'angel'):
        import helper_angel_tv as helper
    elif(broker == "alice"):
        import helper_alice_tv as helper
    elif(broker == "dhan"):
        import helper_dhan_tv as helper
    elif(broker == "fyers"):
        import helper_fyers_tv as helper
    # elif(broker == "icici"):
    #     import helper_icici_tv as helper
    elif(broker == "iifl"):
        import helper_iifl_tv as helper
    elif(broker == "nuvama"):
        import helper_nuvama_tv as helper
    elif(broker == "upstox"):
        import helper_upstox_tv as helper
    elif(broker == "zerodha"):
        import helper_zerodha_tv as helper
    elif(broker == "shoonya"):
        import helper_shoonya_tv as helper
    return helper
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

# options_roundoff_df = pd.read_csv(resource_path('optionstrike_data.csv'))


def getInstrumentName(symbol,sym_type,broker,object):
    global nsee
    nsee = NationalStockExchange()
    if sym_type == 'O':
        inst =  getOption(symbol,broker,object)
        # if (inst[:3] == "ERR"):
        #     quit()
        return inst
    elif sym_type == 'E':
        return getEquity(symbol,broker,object)
    elif sym_type == 'F':
        return getFuture(symbol,broker,object)

def getEquity(symbol,broker,object):

    if broker.lower() in ['angel','fyers','shoonya','alice']:
        instr =  'NSE:'+symbol.upper()+'-EQ'
    elif broker.lower() in ['zerodha','icici','nuvama']:
        instr =  'NSE:'+symbol.upper()
    elif broker.lower() in ['upstox']:
        instr =  symbol.upper()
    elif broker.lower() in ['iifl']:
        instr =  symbol.upper()+'-EQ'
    # ltp = findManualPrice(instr,broker,helper,object,type="")
    # if (ltp)
    # helper = importlib.import_module('helper_'+broker+'_tv')
    # if broker=='icici':
    #     ltp = helper.manualLTP(instr,object,'equity')
    # elif broker=='nuvama':
    #     ltp = findManualPrice(instr,broker,object,type="EQUITY")
    # else:
    #     ltp = findManualPrice(instr,broker,object)
    return instr

def getFuture(symbol,broker,object):
    symb = symbol.split('_')
    symbol = symb[0]
    exp = 0
    try:
        if symb[1] == 'NM':
            exp=1
    except:
        exp=0
    helper = importhelper(broker.lower())
    # equity=0
    # try:
    #     name = helper.getIndexSpot(symbol)
    # except:
    #     # name, ltp = getEquity(symbol,broker)
    #     equity=1
    # ---------------------------------------------------

    intExpiry = helper.getCurrentExpiry_month(symbol,exp)
    # return symbol
    # print(intExpiry)
    # print(broker)
    if broker == 'zerodha':
        instr =  helper.getFutureFormat(symbol,intExpiry)
    else:
        instr =  helper.getFutureFormat(symbol,intExpiry)
    # typee="FUTUREINDEX"
    # if equity==1:
    #     typee="FUTURESTOCK"
    # ltp = findManualPrice(instr,broker,object,type=typee)
    return instr

def getOption(symbol,broker,object):
    # import helper_fyers as helper
    helper = importhelper(broker.lower())
    # helper = importlib.import_module(resource_path('helper_'+broker+'_tv'))
    symbol_option = symbol.split('_')
    option={}
    if len(symbol_option) == 1:
        return symbol
    option['name'] = symbol_option[0]
    option['strike'] = symbol_option[1]
    option['expiry'] = symbol_option[2]
    option['cepe'] = symbol_option[3]
    if len(option['strike'].split('+')) > 1:
        if option['strike'].split('+')[0] == 'ATM':
            return findStrikePriceATM(helper,broker,option['name'],int(option['strike'].split('+')[1]),option['cepe'],option['expiry'],object)
        elif option['strike'].split('+')[0] == 'PREM':
            return findStrikePricePremium(helper,broker,option['name'],int(option['strike'].split('+')[1]),option['cepe'],option['expiry'],object)
    elif len(option['strike'].split('-')) > 1:
        if option['strike'].split('-')[0] == 'ATM':
            return findStrikePriceATM(helper,broker,option['name'],-1*int(option['strike'].split('-')[1]),option['cepe'],option['expiry'],object)
        elif option['strike'].split('-')[0] == 'PREM':
            return findStrikePricePremium(helper,broker,option['name'],int(option['strike'].split('-')[1]),option['cepe'],option['expiry'],object)
    elif option['strike'] == 'ATM':
        return findStrikePriceATM(helper,broker,option['name'],0,option['cepe'],option['expiry'],object)
    else:
        return findStrikePrice(helper,option['name'],option['strike'],option['cepe'],option['expiry'],broker,object)

def findStrikePrice(helper,stock,strike,cepe,expiry,broker,object):
    # equity=0
    # try:
    #     name = helper.getIndexSpot(stock)
    # except:
    #     name = getEquity(stock,broker)
    #     equity=1
    if expiry.upper() == 'W':
        if stock == "BANKNIFTY":
            intExpiry=helper.getBankNiftyExpiryDate()
        elif stock == "NIFTY":
            intExpiry=helper.getNiftyExpiryDate()
        elif stock == "FINNIFTY":
            intExpiry=helper.getFinNiftyExpiryDate()
        elif stock == "MIDCPNIFTY":
            intExpiry=helper.getMidCapNiftyExpiryDate()
    elif expiry.upper() == 'NW':
        if stock == "BANKNIFTY":
            intExpiry=helper.getBankNiftyExpiryDate(1)
        elif stock == "NIFTY":
            intExpiry=helper.getNiftyExpiryDate(1)
        elif stock == "FINNIFTY":
            intExpiry=helper.getFinNiftyExpiryDate(1)
        elif stock == "MIDCPNIFTY":
            intExpiry=helper.getMidCapNiftyExpiryDate(1)
    elif expiry.upper() == 'M':
        intExpiry = helper.getCurrentExpiry_month(stock,0)
    elif expiry.upper() == 'NM':
        intExpiry = helper.getCurrentExpiry_month(stock,1)
    if broker == 'zerodha':
        instr = helper.getOptionFormat(stock, intExpiry[0], strike, cepe)
    else:
        instr = helper.getOptionFormat(stock, intExpiry, strike, cepe)
    # typee="OPTIONINDEX"
    # if equity==1:
    #     typee="OPTIONSTOCK"
    # print(instr)
    # ltp = findManualPrice(instr,broker,object,type=typee)
    return instr

def findStrikePriceATM(helper,broker,stock,otm,cepe,expiry,object=None):
    equity=0
    # try:
    #     name = helper.getIndexSpot(stock)
    # except:
    #     # name = getEquity(stock,broker,object)
    #     equity=1
    #     print("Stock options not available right now.")
    #     return "ERR:Stock options not available for ATM selection."
    strikeList=[]
    prev_diff = 10000
    closest_Strike=10000
    if expiry.upper() == 'W':
        if stock == "BANKNIFTY":
            intExpiry=helper.getBankNiftyExpiryDate()
        elif stock == "NIFTY":
            intExpiry=helper.getNiftyExpiryDate()
        elif stock == "FINNIFTY":
            intExpiry=helper.getFinNiftyExpiryDate()
        elif stock == "MIDCPNIFTY":
            intExpiry=helper.getMidCapNiftyExpiryDate()
    elif expiry.upper() == 'NW':
        if stock == "BANKNIFTY":
            intExpiry=helper.getBankNiftyExpiryDate(1)
        elif stock == "NIFTY":
            intExpiry=helper.getNiftyExpiryDate(1)
        elif stock == "FINNIFTY":
            intExpiry=helper.getFinNiftyExpiryDate(1)
        elif stock == "MIDCPNIFTY":
            intExpiry=helper.getMidCapNiftyExpiryDate(1)
    elif expiry.upper() == 'M':
        intExpiry = helper.getCurrentExpiry_month(stock,0)
    elif expiry.upper() == 'NM':
        intExpiry = helper.getCurrentExpiry_month(stock,1)
    try:
        ltp = nsee.get_LTP('NSE:'+stock)['ltp']
    except:
        return "Error in getting LTP from NSE"
    # if broker=='icici':
    #     # ltp = findManualPrice(name,broker,helper,object)
    #     a = helper.getHistorical(name,1,1,object)
    #     ltp = float(a['close'].iloc[-1])
    # elif broker=='nuvama':
    #     if(equity==0):
    #         ltp = findManualPrice(name,broker,object,type="INDEX")
    #     else:
    #         ltp = findManualPrice(name,broker,object,type="EQUITY")
    # elif broker=='zerodha':
    #     try:
    #         ltp = nsee.get_LTP('NSE:'+stock)['ltp']
    #     except:
    #         return "Error in getting LTP from NSE"
    #     # print("LTP-------------",ltp)
    # else:
    #     ltp = findManualPrice(name,broker,object)
    # print(ltp)
    if stock == "BANKNIFTY":
        closest_Strike = int(round((ltp / 100),0) * 100)
        print(closest_Strike)
    elif stock == "NIFTY" or stock == "FINNIFTY":
        closest_Strike = int(round((ltp / 50),0) * 50)  #21840/50 436.8 = 437*50 = 21850
        print(closest_Strike)
    elif stock == "MIDCPNIFTY":
        closest_Strike = int(round((ltp / 25),0) * 25)  #21840/50 436.8 = 437*50 = 21850
        print(closest_Strike)
    # else:
    #     round_off = options_roundoff_df[options_roundoff_df['stock']==stock]['roundoff']
    #     print(round_off)
    #     print(ltp)
    #     closest_Strike = (int(ltp / round_off)) * int(round_off)
    if broker == 'zerodha':
        instr = helper.getOptionFormat(stock, intExpiry[0], closest_Strike+otm,cepe)
    else:
        instr = helper.getOptionFormat(stock, intExpiry, closest_Strike+otm,cepe)

    # if equity ==0:
    #     ltp = findManualPrice(instr,broker,object,type="OPTIONINDEX")
    # if equity ==1:
    #     ltp = findManualPrice(instr,broker,object,type="OPTIONSTOCK")

    return instr


def findStrikePricePremium(helper,broker,stock,premium,cepe,expiry,object=None):
    equity=0
    # try:
    #     name = helper.getIndexSpot(stock)
    # except:
    #     # name = getEquity(stock,broker,object)
    #     equity=1
    #     print("Stock options not available right now.")
    #     return "ERR:Stock options not available for premium selection"
    strikeList=[]
    prev_diff = 10000
    closest_Strike=10000
    if expiry.upper() == 'W':
        if stock == "BANKNIFTY":
            intExpiry=helper.getBankNiftyExpiryDate()
        elif stock == "NIFTY":
            intExpiry=helper.getNiftyExpiryDate()
        elif stock == "FINNIFTY":
            intExpiry=helper.getFinNiftyExpiryDate()
        elif stock == "MIDCPNIFTY":
            intExpiry=helper.getMidCapNiftyExpiryDate()
    elif expiry.upper() == 'NW':
        if stock == "BANKNIFTY":
            intExpiry=helper.getBankNiftyExpiryDate(1)
        elif stock == "NIFTY":
            intExpiry=helper.getNiftyExpiryDate(1)
        elif stock == "FINNIFTY":
            intExpiry=helper.getFinNiftyExpiryDate(1)
        elif stock == "MIDCPNIFTY":
            intExpiry=helper.getMidCapNiftyExpiryDate(1)
    elif expiry.upper() == 'M':
        intExpiry = helper.getCurrentExpiry_month(stock,0)
    elif expiry.upper() == 'NM':
        intExpiry = helper.getCurrentExpiry_month(stock,1)

    # if broker=='icici':
    #     ltp = helper.manualLTP(name,object,'equity')
    # elif broker=='nuvama':
    #     if(equity==0):
    #         ltp = findManualPrice(name,broker,object,type="INDEX")
    #     else:
    #         ltp = findManualPrice(name,broker,object,type="EQUITY")
    # else:
    #     ltp = findManualPrice(name,broker,object)

    try:
        ltp = nsee.get_LTP('NSE:'+stock)['ltp']
    except:
        return "Error in getting LTP from NSE"

    if stock == "BANKNIFTY":
        for i in range(-10, 10):
            strike = (int(ltp / 100) + i) * 100
            strikeList.append(strike)
    elif stock == "NIFTY" or stock == "FINNIFTY":
        for i in range(-10, 10):
            strike = (int(ltp / 100) + i) * 100   #220+1 = 22100
            strikeList.append(strike)
            strikeList.append(strike+50)
    elif stock == 'MIDCPNIFTY':
        for i in range(-5,5):
            strike = (int(ltp / 100) + i) * 100   #220+1 = 22100
            strikeList.append(strike)
            strikeList.append(strike+25)
            strikeList.append(strike+50)
            strikeList.append(strike+75)
    # else:
    # round_off = options_roundoff_df[options_roundoff_df['stock']==stock]['roundoff'].iloc[0]
    # print(round_off)
    # # print(ltp)
    # for i in range(-10, 10):
    #     strike = (int(ltp / round_off) + i) * round_off   #220+1 = 22100
    #     strikeList.append(strike)
    # strikeList.append(strike+50)
    # closest_Strike = (int(ltp / round_off)) * int(round_off)

    prev_diff = 10000
    for strike in strikeList:
        # print(intExpiry)
        # print(strike)
        # print(stock)
        # print(helper.getOptionFormat(stock,intExpiry,strike,cepe))
        typee="OPTIONINDEX"
        if equity==1:
            typee="OPTIONSTOCK"
        if broker == 'zerodha':
            ltp_option = nsee.get_LTP("NFO:"+stock,str(intExpiry[1]),strike,cepe)['ltp']
        else:
            ltp_option = findManualPrice(helper.getOptionFormat(stock,intExpiry,strike,cepe),broker,object,type=typee)
        if(broker=='icici'):
            time.sleep(1)
        # print(ltp_option)
        diff = abs(ltp_option - premium)
        # print("diff==>", diff)
        if (diff < prev_diff):
            closest_Strike = strike
            prev_diff = diff
    # print("closest",closest_Strike)
    if broker == 'zerodha':
        instr = helper.getOptionFormat(stock, intExpiry[0], closest_Strike, cepe)
    else:
        instr = helper.getOptionFormat(stock, intExpiry, closest_Strike, cepe)
    # ltp = findManualPrice(helper.getOptionFormat(stock,intExpiry,strike,cepe),broker,object,type=typee)
    return instr

def findManualPrice(symbol,broker,object=None,type=None):
    # helper = importlib.import_module(resource_path('helper_'+broker+'_tv'))
    helper = importhelper(broker.lower())
    if broker == 'nuvama':
        his = helper.getHistorical(symbol, 1,1,type,object)
        ltp = (his['close'].iloc[-1])
        print(ltp)
        return ltp
    if broker == 'iifl':
        return helper.manualLTP(symbol,object,symbol_to_id_iifl)
    return helper.manualLTP(symbol,object)
    # elif (nuvama_broker == 1):
    #     return helper.getLTP(symbol)
    # else:
    #     return helper.manualLTP(symbol)