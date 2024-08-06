from app import db
from app.models.transaction import Transaction
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

class TransactionService:
    @staticmethod
    def get_all_transactions():
        try:
            return Transaction.query.all()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve transactions: {str(e)}")

    @staticmethod
    def get_transaction_by_id(txn_id):
        try:
            return Transaction.query.get(txn_id)
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve transaction: {str(e)}")

    @staticmethod
    def create_transaction(data):
        try:
            new_transaction = Transaction(**data)
            db.session.add(new_transaction)
            db.session.commit()
            return new_transaction
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to create transaction: {str(e)}")

    @staticmethod
    def update_transaction(txn_id, data):
        try:
            transaction = Transaction.query.get(txn_id)
            if not transaction:
                raise Exception("Transaction not found")
            
            for key, value in data.items():
                if hasattr(transaction, key):
                    setattr(transaction, key, value)
            
            db.session.commit()
            return transaction
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to update transaction: {str(e)}")

    @staticmethod
    def delete_transaction(txn_id):
        try:
            transaction = Transaction.query.get(txn_id)
            if not transaction:
                raise Exception("Transaction not found")
            
            db.session.delete(transaction)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to delete transaction: {str(e)}")

    @staticmethod
    def get_transactions_by_ticker(ticker):
        try:
            return Transaction.query.filter_by(ticker=ticker).all()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve transactions by ticker: {str(e)}")

    @staticmethod
    def get_transactions_by_date_range(start_date, end_date):
        try:
            return Transaction.query.filter(Transaction.txn_date.between(start_date, end_date)).all()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve transactions by date range: {str(e)}")