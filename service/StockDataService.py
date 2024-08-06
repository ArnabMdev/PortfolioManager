import yfinance as yf
import pandas as pd
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter
class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass

session = CachedLimiterSession(
    limiter=Limiter(RequestRate(2, Duration.SECOND*5)),  # max 2 requests per 5 seconds
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("yfinance.cache"),
)

def getNSEStocks(start:int, end:int, period:str):
    try:
        tickers = pd.read_html('https://ournifty.com/stock-list-in-nse-fo-futures-and-options.html#:~:text=NSE%20F%26O%20Stock%20List%3A%20%20%20%20SL,%20%201000%20%2052%20more%20rows%20')[0]
        tickers = tickers.SYMBOL.to_list()
        for i in range(len(tickers)):
            tickers[i] = tickers[i] + ".NS"
        price_data = yf.Tickers(tickers[20:25] ,session=session)
        # print(price_data.tickers)
        for k,v in price_data.tickers.items():
            print(k + ' ' + str(v.info['currentPrice']))
    except Exception as err:
        print(err)
        return {}
        
    
if __name__ == '__main__':
    getNSEStocks(0,25,"5d")