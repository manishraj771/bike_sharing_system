from flask import Flask
from app.routes import routes_bp  # Import the Blueprint for routes

def create_app():
    app = Flask(__name__)
    
    # Register the blueprint for routes
    app.register_blueprint(routes_bp)
    
    return app
