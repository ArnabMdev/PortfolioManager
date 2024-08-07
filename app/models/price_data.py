from app import db
from sqlalchemy.dialects.mysql import JSON
import datetime

class PriceData(db.Model):
    __tablename__ = 'price_data'

    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(20), nullable=False, index=True)
    open = db.Column(db.Float, nullable=False, default=0)
    close = db.Column(db.Float, nullable=False, default=0)
    highs = db.Column(JSON)
    lows = db.Column(JSON)
    volume = db.Column(db.Integer, nullable=False, default=0)
    current_price = db.Column(db.Float, nullable=False, default=0)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, ticker, open=0, close=0, highs={}, lows={}, volume=0, current_price=0, timestamp=None):
        self.ticker = ticker
        self.open = open
        self.close = close
        self.highs = highs
        self.lows = lows
        self.volume = volume
        self.current_price = current_price
        self.timestamp = timestamp or datetime.datetime.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'ticker': self.ticker,
            'open': self.open,
            'close': self.close,
            'highs': self.highs,
            'lows': self.lows,
            'volume': self.volume,
            'current_price': self.current_price,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None
        }

    @staticmethod
    def from_dict(data):
        return PriceData(**data)