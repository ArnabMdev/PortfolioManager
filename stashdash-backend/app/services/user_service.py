from app.models.user import User
from app import db

class UserService:
    def get_all_users(self):
        return User.query.all()

    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    def create_user(self, user_data):
        new_user = User(username=user_data['username'], password_hash=user_data['password'])
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def update_user(self, user_id, user_data):
        user = User.query.get(user_id)
        if user:
            user.username = user_data.get('username', user.username)
            user.password_hash = user_data.get('password', user.password_hash)
            db.session.commit()
        return user

    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False