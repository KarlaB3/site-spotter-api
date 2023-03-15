import os

class Config(object):
    # Disable modification tracking to save memory
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    # Get the value of the secret key from .env
    JWT_SECRET_KEY = os.environ.get("SECRET_KEY")
    JSON_SORT_KEYS = False
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        # Get the value of the database URL from .env
        value = os.environ.get("DATABASE_URL")

        if not value:
            raise ValueError("DATABASE_URL is not set")
        
        return value

# Set up custom configurations for production, testing and development 
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True

environment = os.environ.get("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()
