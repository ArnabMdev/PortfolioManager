from app import db


class Holding(db.Model):
    __tablename__ = 'holdings'
    ticker = db.Column(db.String(20), nullable=False, primary_key=True)
    user_id = db.Column(db.String(255), nullable=False, index=True, default="user1")
    asset_type = db.Column(db.String(50), nullable=False)
    qty = db.Column(db.Float, nullable=False, default=0)
    avg_price = db.Column(db.Float, nullable=False, default=0)

    def __init__(self, user_id="user1", ticker="", asset_type="", qty=0, avg_price=0):
        self.user_id = user_id
        self.ticker = ticker
        self.asset_type = asset_type
        self.qty = qty
        self.avg_price = avg_price

    def to_dict(self):
        return {
            "ticker": self.ticker,
            "user_id": self.user_id,
            "asset_type": self.asset_type,
            "qty": self.qty,
            "avg_price": self.avg_price
        }

    @staticmethod
    def from_dict(data):
        return Holding(**data)


