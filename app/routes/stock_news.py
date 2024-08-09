from flask import Blueprint, jsonify, request
from app.services.price_data_service import PriceDataService
import pandas as pd

from app.services.watchlist_service import WatchlistService

bp = Blueprint('stock_news', __name__, url_prefix='/api/stock_news')
price_data_service = PriceDataService()


@bp.route('/', methods=['GET'])
def get_stock_news():
    try:
        stock_news = WatchlistService.get_news_from_watchlist()
        if stock_news is not None:
            response = jsonify(stock_news)
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.status = 200
            return response
        return jsonify({'error': 'No news found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
