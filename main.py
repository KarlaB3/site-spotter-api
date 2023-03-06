from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the database object
db = SQLAlchemy()

# Create and configure the Flask app object
def create_app():
    app = Flask(__name__)
    app.config.from_object("config.app_config")

    db.init_app(app)

    return app