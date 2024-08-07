import datetime


class PriceData:
    def __init__(self, highs={}, lows={}, volume=0, current_price=0,
                 timestamp=datetime.datetime.now()):
        self.__highs = highs
        self.__lows = lows
        self.__volume = volume
        self.__current_price = current_price
        self.__timestamp = timestamp

    @property
    def highs(self):
        return self.__highs

    @highs.setter
    def highs(self, value):
        self.__highs = value

    @property
    def low(self):
        return self.__lows

    @low.setter
    def low(self, value):
        self.__lows = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    @property
    def current_price(self):
        return self.__current_price

    @current_price.setter
    def current_price(self, value):
        self.__current_price = value

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, value):
        self.__timestamp = value

    def to_dict(self):
        return {
            'highs': self.__highs,
            'lows': self.__lows,
            'volume': self.__volume,
            'current_price': self.__current_price,
            'timestamp': self.__timestamp
        }


class PriceHistory:
    def __init__(self, open=[], close=[], high=[], low=[], volume=[], timestamp = datetime.datetime.now()):
        self.__open = open
        self.__close = close
        self.__high = high
        self.__low = low
        self.__volume = volume
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
            'open': self.__open,
            'close': self.__close,
            'high': self.__high,
            'low': self.__low,
            'volume': self.__volume,
            'timestamp': self.__timestamp

        }