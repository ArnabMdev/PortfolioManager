from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

from app.services.watchlist_service import WatchlistService

bp = Blueprint('watchlist', __name__, url_prefix='/api/watchlist')


@bp.route('', methods=['GET'])
def get_watchlist():
    try:
        watchlist_items = WatchlistService.get_all_watchlist_items()
        response = jsonify(watchlist_items)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status = 200
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/<string:ticker>', methods=['GET'])
def get_watchlist_item(ticker):
    try:
        item = WatchlistService.get_watchlist_item(ticker)
        if item:
            response = jsonify(item.to_dict())
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.status = 200
            return response
        return jsonify({"error": "Ticker not found in watchlist"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('', methods=['POST'])
@cross_origin('*')
def add_to_watchlist():
    try:
        data = request.json
        if 'ticker' not in data:
            return jsonify({"error": "Ticker is required"}), 400
        new_item = WatchlistService.add_to_watchlist(data['ticker'])
        response = jsonify(new_item.to_dict())
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status = 201
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/<string:ticker>', methods=['DELETE'])
@cross_origin('*')
def remove_from_watchlist(ticker):
    try:
        WatchlistService.remove_from_watchlist(ticker)
        response = jsonify({"message": "Ticker removed from watchlist"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status = 204
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500
