from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import (user_routes, transaction_routes, holding_routes,
                         price_data_route, transaction_routes, price_history_route,stock_news)
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(holding_routes.bp)
    app.register_blueprint(price_data_route.bp)
    app.register_blueprint(price_history_route.bp)
    app.register_blueprint(transaction_routes.bp)
    app.register_blueprint(stock_news.bp)

    return app
