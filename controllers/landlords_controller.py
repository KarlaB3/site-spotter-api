from flask import Blueprint, jsonify, request, abort
from main import db
from models.landlords import Landlord
from schemas.landlord_schema import landlord_schema, landlords_schema
from flask_jwt_extended import jwt_required

# Set all routes related to Landlords to start with /landlords prefix
landlords = Blueprint('landlords', __name__, url_prefix="/landlords")

# Retrieve all landlords from the landlords table
@landlords.get("/")
def get_landlords():
    all_landlords = Landlord.query.all()
    result = landlords_schema.dump(all_landlords)
    return jsonify(result)
 
# Retrieve a landlord based on the landlord_name field
@landlords.get("/search")
def search_landlords():
    if request.args.get("landlord_name"):
        name_landlord = Landlord.query.filter_by(landlord_name = request.args.get("landlord_name"))
        result = landlords_schema.dump(name_landlord)
        return jsonify(result)
    else:
        return abort(401, "Error: Landlord name cannot be found. Please try again.")

# Retrieve a landlord based on the landlord_id field
@landlords.get("/<int:landlord_id>")
def get_landlord_id(landlord_id):
    id_landlord = Landlord.query.get(landlord_id)
    # Display error message if the Landlord ID doesn't exist in the database
    if not id_landlord: 
        return jsonify("Error: Landlord ID not found. Please try again using a valid Landlord ID.")
    result = landlord_schema.dump(id_landlord)
    return jsonify(result)



