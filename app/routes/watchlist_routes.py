from flask import Blueprint, jsonify, request
from app.services.watchlist_service import WatchlistService

bp = Blueprint('watchlist', __name__, url_prefix='/api/watchlist')

@bp.route('', methods=['GET'])
def get_watchlist():
    try:
        watchlist_items = WatchlistService.get_all_watchlist_items()
        return jsonify(watchlist_items), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/<string:ticker>', methods=['GET'])
def get_watchlist_item(ticker):
    try:
        item = WatchlistService.get_watchlist_item(ticker)
        if item:
            return jsonify(item.to_dict()), 200
        return jsonify({"error": "Ticker not found in watchlist"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('', methods=['POST'])
def add_to_watchlist():
    try:
        data = request.json
        if 'ticker' not in data:
            return jsonify({"error": "Ticker is required"}), 400
        new_item = WatchlistService.add_to_watchlist(data['ticker'])
        return jsonify(new_item.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/<string:ticker>', methods=['DELETE'])
def remove_from_watchlist(ticker):
    try:
        WatchlistService.remove_from_watchlist(ticker)
        return jsonify({"message": "Ticker removed from watchlist"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500