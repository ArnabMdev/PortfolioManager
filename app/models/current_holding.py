import datetime

from app import db


class CurrentHolding(db.Model):
    __tablename__ = 'current_holdings'
    ticker = db.Column(db.String(20), nullable=False, primary_key=True)
    stock_name = db.Column(db.String(255), nullable=False, index=True)
    user_id = db.Column(db.String(255), nullable=False, index=True, default="user1")
    asset_type = db.Column(db.String(50), nullable=False)
    qty = db.Column(db.Float, nullable=False, default=0)
    avg_buy_price = db.Column(db.Float, nullable=False, default=0)
    buy_timestamp = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id="user1", ticker="", stock_name="", asset_type="", qty=0, avg_buy_price=0,
                 buy_timestamp=datetime.datetime.now()):
        self.user_id = user_id
        self.stock_name = stock_name
        self.ticker = ticker
        self.asset_type = asset_type
        self.qty = qty
        self.avg_buy_price = avg_buy_price
        self.buy_timestamp = buy_timestamp

    def to_dict(self):
        return {
            "ticker": self.ticker,
            "stock_name": self.stock_name,
            "user_id": self.user_id,
            "asset_type": self.asset_type,
            "qty": self.qty,
            "avg_price": self.avg_buy_price,
            "buy_timestamp": self.buy_timestamp
        }

    @staticmethod
    def from_dict(data):
        return CurrentHolding(**data)


