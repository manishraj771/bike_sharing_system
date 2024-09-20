from flask import Flask
from app.models import db
from app.routes import setup_routes
from app.utils import init_logging
from app.config import Config

def create_app():
    app = Flask(__name__)
    
    # Load configurations
    app.config.from_object(Config)
    
    # Initialize database
    db.init_app(app)
    
    # Initialize logging
    init_logging(app)

    # Setup routes
    setup_routes(app)

    return app
