from app import db
from app.models.price_data import PriceData
from sqlalchemy.exc import SQLAlchemyError

class PriceDataService:
    @staticmethod
    def get_all_price_data():
        try:
            return PriceData.query.all()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve price data: {str(e)}")

    @staticmethod
    def get_price_data_by_id(data_id):
        try:
            return PriceData.query.get(data_id)
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve price data by id: {str(e)}")

    @staticmethod
    def get_price_data_by_ticker(ticker):
        try:
            return PriceData.query.filter_by(ticker=ticker).all()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve price data by ticker: {str(e)}")

    @staticmethod
    def create_price_data(data):
        try:
            new_price_data = PriceData.from_dict(data)
            db.session.add(new_price_data)
            db.session.commit()
            return new_price_data
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to create price data: {str(e)}")

    @staticmethod
    def update_price_data(data_id, data):
        try:
            price_data = PriceData.query.get(data_id)
            if not price_data:
                raise Exception("Price data not found")
            
            for key, value in data.items():
                if hasattr(price_data, key):
                    setattr(price_data, key, value)
            
            db.session.commit()
            return price_data
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to update price data: {str(e)}")

    @staticmethod
    def delete_price_data(data_id):
        try:
            price_data = PriceData.query.get(data_id)
            if not price_data:
                raise Exception("Price data not found")
            
            db.session.delete(price_data)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to delete price data: {str(e)}")

    @staticmethod
    def get_latest_price_data(ticker):
        try:
            return PriceData.query.filter_by(ticker=ticker).order_by(PriceData.timestamp.desc()).first()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve latest price data for ticker: {str(e)}")
