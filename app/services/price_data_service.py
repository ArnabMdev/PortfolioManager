import datetime
import yfinance as yf
import pandas as pd
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter

from app.models.price_data_model import PriceData


class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass


class PriceDataService:
    session = CachedLimiterSession(
        limiter=Limiter(RequestRate(2, Duration.SECOND * 5)),  # max 2 requests per 5 seconds
        bucket_class=MemoryQueueBucket,
        backend=SQLiteCache("../../yfinance.cache"),
    )

    def get_nse_stock_list(self,start: int, end: int):
        tickers = pd.read_csv('../data/StocksTraded.csv', index_col=1)['Symbol '].tolist()
        ticker_list = []
        for i in range(start, end, 1):
            ticker_list.append(tickers[i] + ".NS")
        return ticker_list

    def get_nse_stock_data(self, start: int, end: int):
        try:
            tickers = self.get_nse_stock_list(start, end)
            raw_price_data = yf.Tickers(tickers, session=self.session)
            price_datas = {}
            for k, v in raw_price_data.tickers.items():
                if k is None or v is None:
                    continue
                # print(v.info)
                price_data = PriceData(
                    highs={
                        'dayHigh': v.info['dayHigh'],
                        'regularMarketDayHigh': v.info['regularMarketDayHigh'],
                        'fiftyTwoWeekHigh': v.info['fiftyTwoWeekHigh']
                    },
                    lows={
                        'dayLow': v.info['dayLow'],
                        'regularMarketDayLow': v.info['regularMarketDayLow'],
                        'fiftyTwoWeekLow': v.info['fiftyTwoWeekLow']
                    },
                    volume=v.info['volume'],
                    current_price=v.info['currentPrice'],
                    timestamp=datetime.datetime.now()
                )
                price_datas[k] = price_data
            return price_datas
        except Exception as err:
            print(err)
            return {}

    def get_nse_stock_history(self, ticker, period):
        try:
            tick = yf.Ticker(ticker, session=self.session)
            raw_data = tick.history(period=period, interval='90m')
            return raw_data.to_json()
        except Exception as err:
            print(err)
            return {}


if __name__ == '__main__':
    a = get_nse_stock_history('ZOMATO.NS', '1d')
    print(a)
