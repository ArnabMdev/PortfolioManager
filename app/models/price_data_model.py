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
    def high(self):
        return self.__highs

    @high.setter
    def high(self, value):
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
