from flask import Blueprint, request, jsonify
from app.services.current_holding_service import CurrentHoldingService
from app.services.price_data_service import PriceDataService

bp = Blueprint('current_holdings', __name__, url_prefix='/api/current_holdings')
pds = PriceDataService()


@bp.route('/', methods=['GET'])
def get_all_holdings():
    try:
        holdings = CurrentHoldingService.get_all_holdings()
        holdings_with_price = []
        for holding in holdings:
            holding_dict = holding.to_dict()
            holding_dict['current_price'] = pds.get_stock_price_data(ticker=holding_dict.get('ticker'))
            holdings_with_price.append(holding_dict)
        return jsonify(holdings_with_price), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/user/<int:user_id>', methods=['GET'])
def get_holdings_by_user_id(user_id):
    try:
        holdings = CurrentHoldingService.get_holdings_by_user_id(user_id)
        return jsonify([holding.to_dict() for holding in holdings]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/ticker/<string:ticker>', methods=['GET'])
def get_holdings_by_ticker(ticker):
    try:
        holdings = CurrentHoldingService.get_holdings_by_ticker(ticker)
        return jsonify([holding.to_dict() for holding in holdings]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/asset_type/<string:asset_type>', methods=['GET'])
def get_holdings_by_asset_type(asset_type):
    try:
        holdings = CurrentHoldingService.get_holdings_by_asset_type(asset_type)
        return jsonify([holding.to_dict() for holding in holdings]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
