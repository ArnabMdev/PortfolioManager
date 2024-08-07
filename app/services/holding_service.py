from app import db
from app.models.holding import Holding
from sqlalchemy.exc import SQLAlchemyError

class HoldingService:
    @staticmethod
    def get_all_holdings():
        try:
            return Holding.query.all()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve holdings: {str(e)}")

    @staticmethod
    def get_holding_by_asset_id(asset_id):
        try:
            return Holding.query.get(asset_id)
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve holding: {str(e)}")

    @staticmethod
    def get_holdings_by_user_id(user_id):
        try:
            return Holding.query.filter_by(user_id=user_id).all()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve holdings for user: {str(e)}")

    @staticmethod
    def create_holding(data):
        try:
            new_holding = Holding(**data)
            db.session.add(new_holding)
            db.session.commit()
            return new_holding
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to create holding: {str(e)}")

    @staticmethod
    def update_holding(asset_id, data):
        try:
            holding = Holding.query.get(asset_id)
            if not holding:
                raise Exception("Holding not found")
            
            for key, value in data.items():
                if hasattr(holding, key):
                    setattr(holding, key, value)
            
            db.session.commit()
            return holding
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to update holding: {str(e)}")

    @staticmethod
    def delete_holding(asset_id):
        try:
            holding = Holding.query.get(asset_id)
            if not holding:
                raise Exception("Holding not found")
            
            db.session.delete(holding)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to delete holding: {str(e)}")

    @staticmethod
    def get_holdings_by_ticker(ticker):
        try:
            return Holding.query.filter_by(ticker=ticker).all()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve holdings by ticker: {str(e)}")

    @staticmethod
    def get_holdings_by_asset_type(asset_type):
        try:
            return Holding.query.filter_by(asset_type=asset_type).all()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve holdings by asset type: {str(e)}")

    @staticmethod
    def update_holding_quantity(asset_id, quantity_change):
        try:
            holding = Holding.query.get(asset_id)
            if not holding:
                raise Exception("Holding not found")
            
            holding.qty += quantity_change
            if holding.qty < 0:
                raise Exception("Holding quantity cannot be negative")
            
            db.session.commit()
            return holding
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to update holding quantity: {str(e)}")