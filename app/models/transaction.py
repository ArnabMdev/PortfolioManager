from app import db
from datetime import datetime

class Transaction(db.Model):
    __tablename__ = 'transactions'

    txn_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticker = db.Column(db.String(255), nullable=False)
    stock_name = db.Column(db.String(255), nullable=False)
    txn_type = db.Column(db.String(50), nullable=False, default="buy")
    qty = db.Column(db.Float, nullable=False, default=0)
    price_rate = db.Column(db.Float, nullable=False, default=0)
    txn_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self,ticker="", stock_name ="", txn_type="buy", qty=0, price_rate=0, txn_date=None):
        self.ticker = ticker
        self.stock_name = stock_name
        self.txn_type = txn_type
        self.qty = qty
        self.price_rate = price_rate
        self.txn_date = txn_date if txn_date else datetime.utcnow()

    def to_dict(self):
        return {
            'txn_id': self.txn_id,
            'ticker': self.ticker,
            'stock_name': self.stock_name,
            'txn_type': self.txn_type,
            'qty': self.qty,
            'price_rate': self.price_rate,
            'txn_date': self.txn_date.isoformat() if self.txn_date else None
        }

    @staticmethod
    def to_object(data):
        return Transaction(**data)