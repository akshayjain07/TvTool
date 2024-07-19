import json
import requests
from datetime import datetime as dt 


INDICES = {
"NIFTY" : "NIFTY%2050",
"BANKNIFTY" : "NIFTY%20BANK",
"FINNIFTY" : "NIFTY%20FINANCIAL%20SERVICES",
"MIDCPNIFTY" : "NIFTY%20MIDCAP%20SELECT",
"NIFTY100" : "NIFTY%20100",
"NIFTY200" : "NIFTY%20200",
"NIFTY500" : "NIFTY%20500",
}

OPTIONS = {
"NIFTY" : "nse50_opt",
"BANKNIFTY" : "nifty_bank_opt",
"FINNIFTY" : "finnifty_opt",
"MIDCPNIFTY" : "niftymidcap_opt",
}

class NationalStockExchange:
    def __init__(self, session_refresh_interval=300) -> None:
        self.session_refresh_interval = session_refresh_interval 
        self._create_session()
        self.base_url = "https://www.nseindia.com/api"

        

    def _create_session(self):
        home_url = "https://nseindia.com"
        self._session = requests.Session()
        self._session.headers.update(self._nse_headers())
        self._session.get(home_url)
        self._session_init_time = dt.now()

    def _nse_headers(self):
        """
        Builds right set of headers for requesting http://nseindia.com
        :return: a dict with http headers
        """
        return {"Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.5",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
                }

    def _fetch(self, url):
        time_diff = dt.now() - self._session_init_time
        if time_diff.seconds < self.session_refresh_interval:
            return self._session.get(url)
        else:
            print("time diff is ", time_diff.seconds)
            print("re-initing the session because of expiry")
            self.create_session()
            return self._session.get(url)
    
    def get_LTP(self, instrument, expiry=None, strike=None, cepe=None):
        """
        Returns LTP of provided index or stock or option.
        """
        try:
            
            if instrument.startswith("NSE"):
                instrument = instrument.split(":")[1]
                if "NIFTY" not in instrument:
                    # Fetch LTP for stock option
                    res = self._fetch(self.base_url+"/quote-equity?symbol="+instrument)
                    return {
                        "name":instrument,
                        "ltp":json.loads(res.content)["priceInfo"]["lastPrice"],
                        }
                else:
                    # Fetch LTP for index
                    res = self._fetch(self.base_url + "/equity-stockIndices?index=" + INDICES[instrument])
                    return {
                        "name": instrument,
                        "ltp": json.loads(res.content)["data"][0]["lastPrice"],
                    }
            elif instrument.startswith("NFO") and expiry and strike and cepe:
                instrument = instrument.split(":")[1]
                # Fetch LTP for stock option
                option_type = "Call" if cepe == "CE" else "Put"
                res = self._fetch(self.base_url + "/liveEquity-derivatives?index=" + OPTIONS[instrument])
                data = json.loads(res.content)["data"]
                ltp = next(
                    obj["lastPrice"]
                    for obj in data
                    if obj["contract"] == instrument + " " + expiry and obj["strikePrice"] == strike and obj["optionType"] == option_type
                )
                return {
                    "name": instrument + " " + str(strike) + " " + expiry + " " + cepe,
                    "ltp": ltp,
                }
            else:
                return{
                    "name":instrument,
                    "error":"Instrument not found"
                }


        except Exception as e:
            return {
                "name":instrument,
                "error": str(e)
            }


# usage Indices
# app = NationalStockExchange()
#
# # get ltp for only defined indices
# print(app.get_LTP("NSE:NIFTY"))
# print(app.get_LTP("NSE:FINNIFTY"))
# print(app.get_LTP("NSE:MIDCPNIFTY"))
# print(app.get_LTP("NSE:BANKNIFTY"))
#
#
# # equity
# print(app.get_LTP("NSE:PNB"))
# print(app.get_LTP("NSE:USHAMART"))
# print(app.get_LTP("NSE:TATATECH"))
#
# # options
# print(app.get_LTP("NFO:NIFTY","30-May-2024",22900,"CE"))
# print(app.get_LTP("NFO:BANKNIFTY","05-Jun-2024",48900,"PE"))
