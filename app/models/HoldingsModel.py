class Holding:
    def __init__(self,asset_id, user_id="user1", ticker="", asset_type="", qty=0,avg_price=0):
        self.__asset_id = asset_id
        self.__user_id = user_id
        self.__ticker = ticker
        self.__asset_type = asset_type
        self.__qty = qty
        self.__avg_price = avg_price

    @property
    def asset_id(self):
        return self.__asset_id
    
    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def ticker(self):
        return self.__ticker
    
    @property
    def asset_type(self):
        return self.__asset_type
    
    @property
    def qty(self):
        return self.__qty

    @property
    def avg_price(self):
        return self.__avg_price

    @asset_id.setter
    def asset_id(self,value):
        self.__asset_id = value
        
    @ticker.setter
    def ticker(self,value):
        self.__ticker = value
    
    @asset_type.setter
    def asset_type(self,value):
        self.__asset_type = value
        
    @qty.setter
    def qty(self,value):
        self.__qty = value

    @avg_price.setter
    def avg_price(self,value):
        self.__avg_price = value
    
    def to_dict(self):
        return {
            "asset_id" : self.__asset_id,
            "ticker" : self.__ticker,
            "asset_type" : self.__asset_type,
            "qty" : self.__qty,
            "avg_price" : self.__avg_price
            }
    
    @staticmethod
    def to_object(data):
        return Holding(**data)
        