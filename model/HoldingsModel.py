class Holding:
    def __init__(self,asset_id, ticker="", asset_type="", qty=0,):
        self.__asset_id = asset_id
        self.__ticker = ticker
        self.__asset_type = asset_type
        self.__qty = qty
        
    @property
    def asset_id(self):
        return self.__asset_id
    
    @property
    def ticker(self):
        return self.__ticker
    
    @property
    def asset_type(self):
        return self.__asset_type
    
    @property
    def qty(self):
        return self.__qty
    
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
    
    def to_dict(self):
        return {
            "asset_id" : self.__asset_id,
            "ticker" : self.__ticker,
            "asset_type" : self.__asset_type,
            "qty" : self.__qty
            }
        
    def to_object(data):
        return Holding(**data)
        