from app import db
from datetime import datetime

class Watchlist(db.Model):
    __tablename__ = 'watchlist'

    ticker = db.Column(db.String(20), nullable=False)

    def __init__(self,ticker=""):
        self.ticker = ticker

    def to_dict(self):
        return {
            'ticker': self.ticker,
        }

    @staticmethod
    def to_object(data):
        return Watchlist(**data)