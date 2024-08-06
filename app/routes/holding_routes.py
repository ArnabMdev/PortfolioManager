from flask import Blueprint, request, jsonify
from app.services.holding_service import HoldingService  

bp = Blueprint('holdings', __name__, url_prefix='/api/holdings')

@bp.route('/', methods=['GET'])
def get_all_holdings():
    try:
        holdings = HoldingService.get_all_holdings()
        return jsonify([holding.to_dict() for holding in holdings]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/<int:asset_id>', methods=['GET'])
def get_holding_by_asset_id(asset_id):
    try:
        holding = HoldingService.get_holding_by_asset_id(asset_id)
        if not holding:
            return jsonify({'error': 'Holding not found'}), 404
        return jsonify(holding.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/user/<int:user_id>', methods=['GET'])
def get_holdings_by_user_id(user_id):
    try:
        holdings = HoldingService.get_holdings_by_user_id(user_id)
        return jsonify([holding.to_dict() for holding in holdings]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/', methods=['POST'])
def create_holding():
    data = request.get_json()
    try:
        new_holding = HoldingService.create_holding(data)
        return jsonify(new_holding.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/<int:asset_id>', methods=['PUT'])
def update_holding(asset_id):
    data = request.get_json()
    try:
        updated_holding = HoldingService.update_holding(asset_id, data)
        return jsonify(updated_holding.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/<int:asset_id>', methods=['DELETE'])
def delete_holding(asset_id):
    try:
        result = HoldingService.delete_holding(asset_id)
        if result:
            return jsonify({'message': 'Holding deleted successfully'}), 200
        else:
            return jsonify({'error': 'Holding not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/ticker/<string:ticker>', methods=['GET'])
def get_holdings_by_ticker(ticker):
    try:
        holdings = HoldingService.get_holdings_by_ticker(ticker)
        return jsonify([holding.to_dict() for holding in holdings]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/asset_type/<string:asset_type>', methods=['GET'])
def get_holdings_by_asset_type(asset_type):
    try:
        holdings = HoldingService.get_holdings_by_asset_type(asset_type)
        return jsonify([holding.to_dict() for holding in holdings]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/<int:asset_id>/quantity', methods=['PUT'])
def update_holding_quantity(asset_id):
    data = request.get_json()
    quantity_change = data.get('quantity_change', 0)
    try:
        updated_holding = HoldingService.update_holding_quantity(asset_id, quantity_change)
        return jsonify(updated_holding.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
