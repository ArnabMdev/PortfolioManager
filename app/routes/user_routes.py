from flask import Blueprint, jsonify, request
from app.models.user import User
from app.services.user_service import UserService
from app import db

bp = Blueprint('users', __name__, url_prefix='/api/users')
user_service = UserService()


@bp.route('', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    response = jsonify([user.to_dict() for user in users])
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.status = 200
    return response


@bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = user_service.get_user_by_id(id)
    if user:
        response = jsonify(user.to_dict())
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status = 200
        return response
    return jsonify({'error': 'User not found'}), 404


@bp.route('', methods=['POST'])
def create_user():
    data = request.json
    new_user = user_service.create_user(data)
    response = jsonify(new_user.to_dict())
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.status = 201
    return response


@bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    updated_user = user_service.update_user(id, data)
    if updated_user:
        response = jsonify(updated_user.to_dict())
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status = 202
    return jsonify({'error': 'User not found'}), 404


@bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    if user_service.delete_user(id):
        response = jsonify({'msg': 'User successfully deleted'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.status = 204
        return response
    return jsonify({'error': 'User not found'}), 404
