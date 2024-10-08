from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

from app.services.transaction_service import TransactionService
from datetime import datetime

bp = Blueprint('transactions', __name__, url_prefix='/api/transactions')

@bp.route('', methods=['GET'])
def get_all_transactions():
    try:
        transactions = TransactionService.get_all_transactions()
        return jsonify([t.to_dict() for t in transactions]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/<string:txn_id>', methods=['GET'])
def get_transaction(txn_id):
    try:
        transaction = TransactionService.get_transaction_by_id(txn_id)
        if transaction:
            return jsonify(transaction.to_dict()), 200
        return jsonify({"error": "Transaction not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('', methods=['POST'])
@cross_origin()
def create_transaction():
    try:
        data = request.json
        new_transaction = TransactionService.create_transaction(data)
        response = jsonify(new_transaction.to_dict())
        response.status = 200
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/ticker/<string:ticker>', methods=['GET'])
def get_transactions_by_ticker(ticker):
    try:
        transactions = TransactionService.get_transactions_by_ticker(ticker)
        response = jsonify([t.to_dict() for t in transactions])
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status = 200
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/date-range', methods=['GET'])
def get_transactions_by_date_range():
    try:
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        if not start_date or not end_date:
            return jsonify({"error": "Both start_date and end_date are required"}), 400
        
        start_date = datetime.fromisoformat(start_date)
        end_date = datetime.fromisoformat(end_date)
        
        transactions = TransactionService.get_transactions_by_date_range(start_date, end_date)
        response = jsonify([t.to_dict() for t in transactions])
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status = 200
        return response
    except ValueError:
        return jsonify({"error": "Invalid date format. Use ISO format (YYYY-MM-DD)"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500