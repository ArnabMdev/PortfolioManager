
import datetime
class PriceHistory:
    def __init__(self, open=[], stock_name = "", close=[], high=[], low=[], volume=[], current_price =0, timestamp = datetime.datetime.now()):
        self.__open = open
        self.__stock_name = stock_name
        self.__close = close
        self.__high = high
        self.__low = low
        self.__volume = volume
        self.__current_price = current_price
        self.__timestamp = timestamp

    @property
    def open(self):
        return self.__open

    @open.setter
    def open(self, value):
        self.__open = value

    @property
    def close(self):
        return self.__close

    @close.setter
    def close(self, value):
        self.__close = value

    @property
    def high(self):
        return self.__high

    @high.setter
    def high(self, value):
        self.__high = value

    @property
    def low(self):
        return self.__low

    @low.setter
    def low(self, value):
        self.__low = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.__timestamp = value

    def to_dict(self):
        return {
            'stock_name' : self.__stock_name,
            'open': self.__open,
            'close': self.__close,
            'high': self.__high,
            'low': self.__low,
            'volume': self.__volume,
            'current_price' : self.__current_price,
            'timestamp': self.__timestamp

        }