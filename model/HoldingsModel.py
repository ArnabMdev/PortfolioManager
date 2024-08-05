class HoldingsModel:
    def __init__(self,asset_id, ticker="", asset_type="", qty=0,):
        self.__asset_id = asset_id
        self.__ticker = ticker
        self.__asset_type = asset_type
        self.qty = qty
    
    def to_dict(self):
        return {
            "asset_id" : self.__asset_id,
            "ticker" : self.__ticker,
            "asset_type" : self.__asset_type,
            "qty" : self.__qty
            }
        