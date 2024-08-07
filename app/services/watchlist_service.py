from app import db
from .watchlist import Watchlist
from sqlalchemy.exc import SQLAlchemyError

class WatchlistService:
    @staticmethod
    def get_all_watchlist_items():
        try:
            return Watchlist.query.all()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve watchlist items: {str(e)}")

    @staticmethod
    def get_watchlist_item(ticker):
        try:
            return Watchlist.query.filter_by(ticker=ticker).first()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve watchlist item: {str(e)}")

    @staticmethod
    def add_to_watchlist(ticker):
        try:
            existing_item = Watchlist.query.filter_by(ticker=ticker).first()
            if existing_item:
                raise Exception("Ticker already in watchlist")
            new_item = Watchlist(ticker=ticker)
            db.session.add(new_item)
            db.session.commit()
            return new_item
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to add to watchlist: {str(e)}")

    @staticmethod
    def remove_from_watchlist(ticker):
        try:
            item = Watchlist.query.filter_by(ticker=ticker).first()
            if not item:
                raise Exception("Ticker not found in watchlist")
            db.session.delete(item)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to remove from watchlist: {str(e)}")