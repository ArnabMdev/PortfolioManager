from flask import Blueprint, jsonify, request
from app.services.price_data_service import PriceDataService
import pandas as pd

bp = Blueprint('price_data', __name__, url_prefix='/api/price_data')
price_data_service = PriceDataService()


@bp.route('/<string:start>', methods=['GET'])
def get_price_data(start):
    try:
        price_data_list = price_data_service.get_nse_stock_data(starts_with=start)
        print(price_data_list)
        if len(price_data_list) > 0:
            response = jsonify([price_data.to_dict() for price_data in price_data_list])
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.status = 200
            return response
        return jsonify({'error': 'failed to fetch stock data'}), 404
    except FileNotFoundError:
        return "CSV file not found"


@bp.route('', methods=['GET'])
def get_default_price_data():
    try:
        price_data_list = price_data_service.get_nse_stock_data("a")
        print(price_data_list)
        if len(price_data_list) > 0:
            response = jsonify([price_data.to_dict() for price_data in price_data_list])
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.status = 200
            return response
        return jsonify({'error': 'failed to fetch stock data'}), 404
    except FileNotFoundError:
        return "CSV file not found"


@bp.route('/list/<string:startswith>', methods=['GET'])
def get_stock_list(startswith):
    stock_list = price_data_service.get_nse_stock_list(starts_with=startswith)
    if len(stock_list) > 0:
        response = jsonify(stock_list)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status = 200
        return response
    return jsonify({'error': 'failed to fetch stock data'}), 500


@bp.route('/profits', methods=['GET'])
def get_profits():
    try:
        profits = price_data_service.get_profits_from_holdings()
        if len(profits) > 0:
            response = jsonify(profits)
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.status = 200
            return response
        return jsonify({'error': 'No profits to fetch'}), 404
    except Exception as err:
        return jsonify({'error': str(err)}), 500
