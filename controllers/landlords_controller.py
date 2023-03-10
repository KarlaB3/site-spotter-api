from flask import Blueprint, jsonify, request
from main import db
from models.landlords import Landlord
from schemas.landlord_schema import landlord_schema, landlords_schema
from flask_jwt_extended import jwt_required

# Set all routes related to Landlords to start with /landlords prefix
landlords = Blueprint('landlords', __name__, url_prefix="/landlords")

@landlords.get("/")
def get_landlords():
    # Retrieve all landlords from the landlords table
    landlords_list = Landlord.query.all()
    result = landlords_schema.dump(landlords_list)
    return jsonify(result)


@landlords.get("/<int:landlord_id>")
def get_landlord(landlord_id):
    # Retrieve a landlord based on the landlord_id field
    landlord = Landlord.query.get(landlord_id)
    if not landlord:
        # Display error message if the Landlord ID doesn't exist in the database
        return jsonify("Error: Landlord ID not found. Please search again using a valid Landlord ID.")
    # elif type(landlord) != int:
    #     # Display error message if the Landlord ID doesn't exist in the database
    #     return jsonify("Error: Incorrect Landlord ID search type. Please use a number.")
    else:
        result = landlord_schema.dump(landlord)
        return jsonify(result)


