from flask import Blueprint, jsonify, request
from app.services.price_data_service import PriceDataService
import pandas as pd

bp = Blueprint('stock_news', __name__, url_prefix='/api/stock_news')
price_data_service = PriceDataService()


@bp.route('/', methods=['GET'])
def get_stock_news():
    try:
        stock_news = price_data_service.get_news_from_holdings()
        if stock_news is not None:
            return jsonify(stock_news)
        return jsonify({'error': 'No news found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
