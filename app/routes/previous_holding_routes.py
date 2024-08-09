from flask import Blueprint, request, jsonify
from app.services.current_holding_service import CurrentHoldingService
from app.services.previous_holding_service import PreviousHoldingService

bp = Blueprint('previous_holdings', __name__, url_prefix='/api/previous_holdings')


@bp.route('/', methods=['GET'])
def get_all_holdings():
    try:
        holdings = PreviousHoldingService.get_all_holdings()
        response = jsonify([holding.to_dict() for holding in holdings])
        response.status = 200
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/user/<int:user_id>', methods=['GET'])
def get_holdings_by_user_id(user_id):
    try:
        holdings = PreviousHoldingService.get_holdings_by_user_id(user_id)
        response = jsonify([holding.to_dict() for holding in holdings])
        response.status = 200
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/ticker/<string:ticker>', methods=['GET'])
def get_holdings_by_ticker(ticker):
    try:
        holdings = PreviousHoldingService.get_holdings_by_ticker(ticker)
        response = jsonify([holding.to_dict() for holding in holdings])
        response.status = 200
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/asset_type/<string:asset_type>', methods=['GET'])
def get_holdings_by_asset_type(asset_type):
    try:
        holdings = PreviousHoldingService.get_holdings_by_asset_type(asset_type)
        response = jsonify([holding.to_dict() for holding in holdings])
        response.status = 200
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 500
