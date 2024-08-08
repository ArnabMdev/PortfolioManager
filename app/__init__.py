from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import (user_routes, transaction_routes, current_holding_routes, previous_holding_routes,
                         price_data_route, transaction_routes, price_history_route, stock_news, watchlist_routes)
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(current_holding_routes.bp)
    app.register_blueprint(previous_holding_routes.bp)
    app.register_blueprint(price_data_route.bp)
    app.register_blueprint(price_history_route.bp)
    app.register_blueprint(transaction_routes.bp)
    app.register_blueprint(stock_news.bp)
    app.register_blueprint(watchlist_routes.bp)

    return app
