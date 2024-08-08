from flask import Blueprint, jsonify, request
from app.services.price_data_service import PriceDataService
import pandas as pd

bp = Blueprint('price_history', __name__, url_prefix='/api/price_history')
price_data_service = PriceDataService()


@bp.route('/<ticker>/<period>/<interval>', methods=['GET'])
def get_price_history(ticker, period, interval):
    try:
        price_history = price_data_service.get_nse_stock_history(ticker, period, interval)
        if price_history is not None:
            response = jsonify({ticker : price_history.to_dict()})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        return jsonify({'error': 'No data found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
