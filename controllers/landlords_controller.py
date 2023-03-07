from flask import Blueprint, jsonify, request
from main import db
from models.landlords import Landlord

# Set all routes to to start with /landlords
landlords = Blueprint('landlords', __name__, url_prefix="/landlords")

@landlords.get("/")
def get_landlords():
    landlords_list = Landlord.query.all()
    #return landlords_schema.dump(landlords)
    return "List of Landlords retrieved"
