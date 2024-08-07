# transactions model
class Transaction:
    def __init__(self, txn_id, ticker="", txn_type="buy",qty=0,price_rate=0,txn_date=""):
        self.__txn_id = txn_id
        self.__ticker = ticker
        self.__tx_type = txn_type
        self.__qty = qty
        self.__price_rate = price_rate
        self.__txn_date = txn_date
    
    @property
    def txn_id(self):
        return self.__txn_id
    
    @property
    def ticker(self):
        return self.__ticker
    
    @property
    def txn_type(self):
        return self.__tx_type
    
    @property
    def qty(self):
        return self.__qty
    
    @property
    def price_rate(self):
        return self.__price_rate
    
    @property
    def txn_date(self):
        return self.__txn_date
    
    @ticker.setter
    def ticker(self, value):
        self.__ticker = value
    
    @txn_type.setter
    def txn_type(self, value):
        self.__txn_type = value
        
    @qty.setter
    def qty(self, value):
        self.__qty = value
    
    @price_rate.setter
    def price_rate(self, value):
        self.__price_rate = value
        
    @txn_date.setter
    def txn_date(self, value):
        self.__txn_date = value
        
    def to_dict(self):
        return {
            'txn_id' : self.__txn_id,
            'ticker': self.__ticker,
            'txn_type' : self.__txn_date,
            'qty' : self.__qty,
            'price_rate' : self.__price_rate,
            'txn_date' : self.__txn_date 
        }
    
    @staticmethod
    def to_object(data):
        return Transaction(**data)