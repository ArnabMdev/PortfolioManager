from app import db
from app.models.transaction import Transaction
from app.services.holding_service import HoldingService
from sqlalchemy.exc import SQLAlchemyError


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
            holdings = HoldingService.get_holdings_by_ticker(new_transaction.ticker)
            if new_transaction.txn_type == 'buy':
                if len(holdings) == 0:
                    HoldingService.create_holding({
                        'user_id': 'user1',
                        'ticker': new_transaction.ticker,
                        'asset_type': 'Equity',
                        'qty': new_transaction.qty,
                        'avg_price': new_transaction.price_rate,
                    })
                else:
                    HoldingService.update_avg_price(new_transaction.ticker, new_transaction.qty,
                                                    new_transaction.price_rate)
            elif new_transaction.txn_type == 'sell':
                if len(holdings) == 0:
                    return -1
                HoldingService.update_holding_quantity(new_transaction.ticker, new_transaction.qty)
            db.session.add(new_transaction)
            db.session.commit()
            return new_transaction
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to create transaction: {str(e)}")

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
