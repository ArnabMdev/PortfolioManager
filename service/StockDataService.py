import datetime

import yfinance as yf
import pandas as pd
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter

from model.PriceDataModel import PriceData


class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass


session = CachedLimiterSession(
    limiter=Limiter(RequestRate(2, Duration.SECOND * 5)),  # max 2 requests per 5 seconds
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("../yfinance.cache"),
)


def get_nse_stock_list(start: int, end: int):
    tickers = pd.read_csv('../data/StocksTraded.csv',index_col=1)['Symbol '].tolist()
    ticker_list = []
    for i in range(start, end, 1):
        ticker_list.append(tickers[i] + ".NS")
    return ticker_list


def get_nse_stock_data(start: int, end: int):
    try:
        tickers = get_nse_stock_list(start, end)
        print(tickers)
        raw_price_data = yf.Tickers(tickers, session=session)
        print(raw_price_data.tickers)
        price_datas = []
        # for k, v in raw_price_data.tickers.items():
        #     if k is None or v is None:
        #         continue
        #     print(v.info)
            # price_data = PriceData(
            #     str(k),
            #     v.info['open'],
            #     v.info['close'],
            #     {
            #         'dayHigh': v.info['dayHigh'],
            #         'regularMarketDayHigh': v.info['regularMarketDayHigh'],
            #         'fiftyTwoWeekHigh': v.info['fiftyTwoWeekHigh']
            #     },
            #     {
            #         'dayLow': v.info['dayLow'],
            #         'regularMarketDayLow': v.info['regularMarketDayLow'],
            #         'fiftyTwoWeekLow': v.info['fiftyTwoWeekLow']
            #     },
            #     v.info['volume'],
            #     v.info['current_price'],
            #     datetime.datetime.now()
            # )
            # price_datas.append(price_data)
        return price_datas
    except Exception as err:
        print(err)
        return {}


if __name__ == '__main__':
    print(get_nse_stock_data(0, 25))
