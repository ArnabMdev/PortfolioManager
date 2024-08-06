from flask import Blueprint, jsonify, request
from app.services.price_data_service import PriceDataService

bp = Blueprint('price_data', __name__, url_prefix='/api/price_data')
price_data_service = PriceDataService()

@bp.route('', methods=['GET'])
def get_price_data():
    users = price_data_service.get_nse_stock_data()
    return jsonify([user.to_dict() for user in users])

@bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = price_data_service.get_user_by_id(id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({'error': 'User not found'}), 404

@bp.route('', methods=['POST'])
def create_user():
    data = request.json
    new_user = price_data_service.create_user(data)
    return jsonify(new_user.to_dict()), 201

@bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    updated_user = price_data_service.update_user(id, data)
    if updated_user:
        return jsonify(updated_user.to_dict())
    return jsonify({'error': 'User not found'}), 404

@bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    if price_data_service.delete_user(id):
        return '', 204
    return jsonify({'error': 'User not found'}), 404