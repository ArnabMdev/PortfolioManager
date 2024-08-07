import datetime
import os.path
import yfinance as yf
import pandas as pd

from app.models.holding import Holding
from holding_service import HoldingService
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter
from app.models.price_data_models import PriceData, PriceHistory


class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass


class PriceDataService:
    session = CachedLimiterSession(
        limiter=Limiter(RequestRate(2, Duration.SECOND * 5)),  # max 2 requests per 5 seconds
        bucket_class=MemoryQueueBucket,
        backend=SQLiteCache("yfinance.cache"),
    )

    def get_nse_stock_list(self, start: int, end: int):
        try:
            app_root = os.path.dirname(__file__)
            tickers = pd.read_csv(filepath_or_buffer=os.path.join(app_root, 'StocksTraded.csv'), index_col=1)['Symbol '].tolist()
            # tickers = ['ZOMATO','TATAMOTORS']
            ticker_list = []
            for i in range(start, min(end,len(tickers)), 1):
                ticker_list.append(tickers[i] + ".NS")
            return ticker_list
        except Exception as err:
            print(err)
            return []

    def get_nse_stock_data(self, start: int, limit: int):
        try:
            tickers = self.get_nse_stock_list(start, start + limit)
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

    def get_nse_stock_history(self, ticker, period, interval):
        try:
            tick = yf.Ticker(ticker, session=self.session)
            raw_data = tick.history(period=period, interval=interval)
            price_history = PriceHistory(
                open=raw_data['Open'].tolist(),
                high=raw_data['High'].tolist(),
                low=raw_data['Low'].tolist(),
                close=raw_data['Close'].tolist(),
                volume=raw_data['Volume'].tolist(),
                timestamp=raw_data.index.tolist()
            )
            return price_history

        except Exception as err:
            print(err)
            return {}

    def get_news_from_holdings(self):
        holdings = HoldingService.get_all_holdings()
        ticker_list = []
        for holding in holdings:
            ticker_list.append(holding.ticker)
        news_list= {}
        for ticker in ticker_list:
            news_list[ticker] = yf.Ticker(ticker).news
            # print(yf.Ticker(ticker))
        return news_list





if __name__ == '__main__':
    pds = PriceDataService()
    # pds.get_news_from_holdings()
    # print(pds.get_nse_stock_history('MSFT','1d','90m').to_dict())
    # print(pds.get_nse_stock_data(start=0, end=20))
    # print(yf.Ticker('AAPL').news)