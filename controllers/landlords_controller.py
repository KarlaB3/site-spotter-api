from flask import Blueprint, jsonify, request
from main import db
from models.landlords import Landlord
from schemas.landlord_schema import landlord_schema, landlords_schema
from flask_jwt_extended import jwt_required

# Set all routes related to Landlords to start with /landlords prefix
landlords = Blueprint('landlords', __name__, url_prefix="/landlords")

# Retrieve all landlords from the landlords table
@landlords.get("/")
def get_landlords():
    landlords_list = Landlord.query.all()
    result = landlords_schema.dump(landlords_list)
    return jsonify(result)

# Retrieve a landlord based on the landlord_id field
@landlords.get("/<int:landlord_id>")
def get_landlord(landlord_id):
    landlord = Landlord.query.get(landlord_id)
    # Display error message if the Landlord ID doesn't exist in the database
    if not landlord: 
        return jsonify("Error: Landlord ID not found. Please try again using a valid Landlord ID.")
    result = landlord_schema.dump(landlord)
    return jsonify(result)


