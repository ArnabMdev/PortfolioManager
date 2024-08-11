from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from .config import Config
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()
migrate = Migrate()

#swagger configs
SWAGGER_URL= '/api/docs'
API_URL= '/static/swagger.json'
SWAGGER_BLUEPRINT= get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'StashDash APIs'
    }
)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

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
    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix= SWAGGER_URL)

    return app
