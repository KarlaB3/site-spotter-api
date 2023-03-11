from flask import Blueprint, jsonify, request
from main import db
from models.centres import Centre
from schemas.centre_schema import centre_schema, centres_schema
from flask_jwt_extended import jwt_required

# Set all routes related to Centres to start with /centres prefix
centres = Blueprint('centres', __name__, url_prefix="/centres")

# Retrieve all centres from the centres table
@centres.get("/")
def get_centres():
    centres_list = Centre.query.all()
    result = centres_schema.dump(centres_list)
    return jsonify(result)

# Retrieve a centre based on the centre_id field
@centres.get("/<int:centre_id>")
def get_centre(centre_id):
    centre = Centre.query.get(centre_id)
    # Display error message if the Centre ID doesn't exist in the database
    if not centre:
        return jsonify("Error: Centre ID not found. Please search again using a valid Centre ID.")
    # elif type(centre) != int:
    #     # Display error message if the Centre ID doesn't exist in the database
    #     return jsonify("Error: Incorrect Centre ID search type. Please use a number.")
    result = centre_schema.dump(centre)
    return jsonify(result)
