from main import db
from flask import Blueprint
from main import bcrypt
from models.centres import Centre
from models.landlords import Landlord
from models.sites import Site
from models.users import User

db_commands = Blueprint ("db", __name__)

# CLI command to create tables
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables have been created")

# CLI command to seed tables
@db_commands.cli.command("seed")
def seed_db():
    # Create landlord objects