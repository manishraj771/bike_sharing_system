from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.routes import routes_bp  # Import the Blueprint for routes
from config import Config

# Initialize the database
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize database and migrations
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register the blueprint for routes
    app.register_blueprint(routes_bp)
    
    return app
