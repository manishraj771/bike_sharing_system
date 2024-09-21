class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bike_sharing.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecretkey'
    STRIPE_API_KEY = 'your_stripe_api_key'
    API_BASE_URL = 'http://127.0.0.1:5000'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_bike_sharing.db'
    TESTING = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@hostname/db_name'
