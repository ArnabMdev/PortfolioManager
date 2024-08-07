from flask import Blueprint, request, jsonify
from app.services.price_data_service import PriceDataService  

bp = Blueprint('price_data', __name__, url_prefix='/api/price_data')

@bp.route('/', methods=['GET'])
def get_all_price_data():
    try:
        price_data_list = PriceDataService.get_all_price_data()
        return jsonify([price_data.to_dict() for price_data in price_data_list]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/<int:data_id>', methods=['GET'])
def get_price_data_by_id(data_id):
    try:
        price_data = PriceDataService.get_price_data_by_id(data_id)
        if not price_data:
            return jsonify({'error': 'Price data not found'}), 404
        return jsonify(price_data.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/ticker/<string:ticker>', methods=['GET'])
def get_price_data_by_ticker(ticker):
    try:
        price_data_list = PriceDataService.get_price_data_by_ticker(ticker)
        return jsonify([price_data.to_dict() for price_data in price_data_list]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/', methods=['POST'])
def create_price_data():
    data = request.get_json()
    try:
        new_price_data = PriceDataService.create_price_data(data)
        return jsonify(new_price_data.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/<int:data_id>', methods=['PUT'])
def update_price_data(data_id):
    data = request.get_json()
    try:
        updated_price_data = PriceDataService.update_price_data(data_id, data)
        return jsonify(updated_price_data.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/<int:data_id>', methods=['DELETE'])
def delete_price_data(data_id):
    try:
        result = PriceDataService.delete_price_data(data_id)
        if result:
            return jsonify({'message': 'Price data deleted successfully'}), 200
        else:
            return jsonify({'error': 'Price data not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/ticker/<string:ticker>/latest', methods=['GET'])
def get_latest_price_data(ticker):
    try:
        price_data = PriceDataService.get_latest_price_data(ticker)
        if not price_data:
            return jsonify({'error': 'Price data not found'}), 404
        return jsonify(price_data.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
