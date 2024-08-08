from app import db
from sqlalchemy.dialects.mysql import JSON
import datetime


class PriceData(db.Model):
    __tablename__ = 'price_data'

    ticker = db.Column(db.String(20), nullable=False, index=True, primary_key=True)
    stock_name = db.Column(db.String(20), nullable=False, index=True)
    current_price = db.Column(db.Float, nullable=False, default=0)
    volume = db.Column(db.Float, nullable=False, default=0)

    def __init__(self, ticker, stock_name= "",current_price=0,volume=0):
        self.ticker = ticker
        self.stock_name = stock_name
        self.current_price = current_price
        self.volume = volume

    def to_dict(self):
        return {
            'ticker': self.ticker,
            'stock_name': self.stock_name,
            'current_price': self.current_price,
            'volume': self.volume
        }

    @staticmethod
    def from_dict(data):
        return PriceData(**data)
