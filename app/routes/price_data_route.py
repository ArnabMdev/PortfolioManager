from flask import Blueprint, jsonify, request
from app.services.price_data_service import PriceDataService
import pandas as pd

bp = Blueprint('price_data', __name__, url_prefix='/api/price_data')
price_data_service = PriceDataService()


@bp.route('/', methods=['GET'])
def get_default_price_data():
    try:
        price_datas = price_data_service.get_nse_stock_data(0,26)
        if len(price_datas) > 0:
            return jsonify([{k:v.to_dict()} for k,v in price_datas.items()])
        return jsonify({'error': 'failed to fetch stock data'}), 404
    except FileNotFoundError:
            return "CSV file not found"

@bp.route('/<int:start>', methods=['GET'])
def get_price_data(start):
    price_datas = price_data_service.get_nse_stock_data(start=start, limit=26)
    if len(price_datas) > 0:
        return jsonify([{k: v.to_dict()} for k, v in price_datas.items()])
    return jsonify({'error': 'failed to fetch stock data'}), 500
