from flask import Blueprint, jsonify, request
from app.models.user import User
from app.services.user_service import UserService
from app import db

bp = Blueprint('users', __name__, url_prefix='/api/users')
user_service = UserService()

@bp.route('', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify([user.to_dict() for user in users])

@bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = user_service.get_user_by_id(id)
    if user:
        return jsonify(user.to_dict())
    return jsonify({'error': 'User not found'}), 404

@bp.route('', methods=['POST'])
def create_user():
    data = request.json
    new_user = user_service.create_user(data)
    return jsonify(new_user.to_dict()), 201

@bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    updated_user = user_service.update_user(id, data)
    if updated_user:
        return jsonify(updated_user.to_dict())
    return jsonify({'error': 'User not found'}), 404

@bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    if user_service.delete_user(id):
        return '', 204
    return jsonify({'error': 'User not found'}), 404