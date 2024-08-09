import datetime
import os.path
import yfinance as yf
import pandas as pd

from app.services.current_holding_service import CurrentHoldingService
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter
from app.models.price_data import PriceData
from app.models.price_history import PriceHistory
from app.services.previous_holding_service import PreviousHoldingService


class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass


class PriceDataService:
    session = CachedLimiterSession(
        limiter=Limiter(RequestRate(2, Duration.SECOND * 5)),  # max 2 requests per 5 seconds
        bucket_class=MemoryQueueBucket,
        backend=SQLiteCache("yfinance.cache"),
    )

    @staticmethod
    def get_nse_stock_list():
        try:
            app_root = os.path.dirname(__file__)
            tickers = \
            pd.read_csv(filepath_or_buffer=os.path.join(app_root, 'StockData.csv', ), index_col=0, header=None)[
                1].tolist()
            # tickers = ['ZOMATO','TATAMOTORS']
            ticker_list = []
            for tick in tickers:
                ticker_list.append(str(tick) + str('.NS'))
            return ticker_list
        except Exception as err:
            print(err)
            return []

    def get_nse_stock_data(self, starts_with):
        try:
            tickers = PriceDataService.get_nse_stock_list()
            ticker_list = []
            for tick in tickers:
                if tick.startswith(starts_with.upper()):
                    ticker_list.append(tick)
            raw_price_data = yf.Tickers(ticker_list, session=self.session)
            price_data_list = []
            for k, v in raw_price_data.tickers.items():
                if k is None or v is None:
                    continue
                price_data = PriceData(
                    ticker=k,
                    stock_name=v.info.get('longName'),
                    current_price=v.info.get('currentPrice'),
                    volume=v.info.get('volume'),
                )
                price_data_list.append(price_data)
            return price_data_list
        except Exception as err:
            print(err)
            return {}

    def get_stock_data(self, tickers):
        try:
            raw_price_data = yf.Tickers(tickers, session=self.session)
            price_data_list = []
            for k, v in raw_price_data.tickers.items():
                if k is None or v is None:
                    continue
                # print(v.info)
                price_data = PriceData(
                    ticker=k,
                    stock_name=v.info.get('longName'),
                    current_price=v.info.get('currentPrice'),
                    volume=v.info.get('volume'),
                )
                price_data_list.append(price_data)
            return price_data_list
        except Exception as err:
            print(err)
            return {}

    def get_nse_stock_history(self, ticker, period, interval):
        try:
            tick = yf.Ticker(ticker, session=self.session)
            print(tick)
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
        holdings = CurrentHoldingService.get_all_holdings()
        ticker_list = []
        for holding in holdings:
            ticker_list.append(holding.ticker)
        news_list = {}
        for ticker in ticker_list:
            news_list[ticker] = yf.Ticker(ticker).news
            # print(yf.Ticker(ticker))
        return news_list

    def get_profits_from_holdings(self):
        try:
            current_holdings = CurrentHoldingService.get_all_holdings()
            previous_holdings = PreviousHoldingService.get_all_holdings()
            current_ticker_list = [holding.ticker for holding in current_holdings]
            previous_ticker_list = [holding.ticker for holding in previous_holdings]
            price_data = self.get_stock_data(tickers=current_ticker_list)
            unrealised_profits = []
            current_values = []
            realised_profits = []
            sale_prices = []
            for i in range(len(current_holdings)):
                unrealised_profit = current_holdings[i].avg_buy_price - price_data[i].current_price
                unrealised_profits.append(unrealised_profit * current_holdings[i].qty)
                current_values.append(price_data[i].current_price)

            for i in range(len(previous_holdings)):
                realised_profit = previous_holdings[i].avg_sell_price - previous_holdings[i].avg_buy_price
                realised_profits.append(realised_profit * previous_holdings[i].qty)
                sale_prices.append(
                    (previous_holdings[i].avg_sell_price * previous_holdings[i]) * previous_holdings[i].qty)
            return {
                'current_holdings': current_holdings,
                'realised_profits': realised_profits,
                'current_values': current_values,
                'previous_holdings': previous_holdings,
                'unrealised_profits': unrealised_profits,
                'sale_prices': sale_prices,
                'timestamp': datetime.datetime.now(),
            }
        except Exception as err:
            print(err)
            return {}


if __name__ == '__main__':
    pds = PriceDataService()
    print(pds.get_profits_from_holdings())
    # pds.get_nse_stock_history('MSFT',)
    # print(pds.get_nse_stock_data("a"))
    # print(yf.Ticker('MSFT').info)
    # pds.get_news_from_holdings()
    # print(pds.get_nse_stock_history('ZOMATO.NS','1d','90m').to_dict())
    # print(pds.get_nse_stock_data(start=0, end=20))
    # print(yf.Ticker('AAPL').news)
