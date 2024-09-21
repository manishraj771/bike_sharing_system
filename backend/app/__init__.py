# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Load the configuration
    app.config.from_object('config.Config')

    # Initialize the database and migrations
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and set up routes after app initialization to avoid circular imports
    with app.app_context():
        from app.routes import setup_routes
        setup_routes(app)

    return app
