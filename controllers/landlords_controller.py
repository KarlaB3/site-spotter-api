from flask import Blueprint, jsonify, request, abort
from main import db
from flask_jwt_extended import jwt_required
from models.landlords import Landlord
from schemas.landlord_schema import landlord_schema, landlords_schema

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
        return abort(401, "Error: Landlord ID not found. Please try again using a valid Landlord ID.")
    # elif isinstance(id_landlord, str):
    #     abort(404, description = "Landlord ID not found")
    result = landlord_schema.dump(id_landlord)
    return jsonify(result)

# Create a new landlord record
@landlords.post("/")
@jwt_required()
def create_landlord():
    # Retrieve landlord schema and fields
    landlord_fields = landlord_schema.load(request.json)
    # Declare fields to be added as part of the landlord record
    new_landlord = Landlord(
    landlord_name = landlord_fields["landlord_name"],
    landlord_email = landlord_fields["landlord_email"],
    landlord_phone = landlord_fields["landlord_phone"],
    user_id = landlord_fields["user_id"])
    # Add landlord to the database
    db.session.add(new_landlord)
    # Commit landlord changes to the database
    db.session.commit()
    return jsonify(landlord_schema.dump(new_landlord)), 200

# Delete a landlord record using landlord_id field
@landlords.delete("/<int:landlord_id>")
@jwt_required()
def delete_landlord(landlord_id):
    # Check if landlord exists in the database using the landlord_id field
    landlord = Landlord.query.get(landlord_id)
    # Display error message if the landlord_id doesn't exist
    if not landlord:
        return abort(400, description = "Error: Landlord record doesn't exist. Please try again.")
    # Delete landlord from the database
    db.session.delete(landlord)
    # Commit landlord changes to the database
    db.session.commit()
    return jsonify("Message: Landlord successfully deleted."), 200

# Update a landlord record using landlord_id field
@landlords.put("/<int:landlord_id>")
@jwt_required()
def update_landlord(landlord_id):
    # Check if landlord exists in the database using the landlord_id field
    landlord = Landlord.query.get(landlord_id)
    # Display error message if the landlord_id doesn't exist
    if not landlord:
        return abort(400, description = "Error: Landlord record doesn't exist. Please try again.")
    # Retrieve landlord schema and fields
    landlord_fields = landlord_schema.load(request.json)
     # Declare fields to be updated
    landlord.name = landlord_fields["landlord_name"]
    landlord.email = landlord_fields["landlord_email"]
    landlord.phone = landlord_fields["landlord_phone"]
    # Commit landlord updates to the database
    db.session.commit()
    return jsonify(landlord_schema.dump(landlord)), 201




# @landlords.errorhandler(404)
# def not_found(e):
#     return jsonify(error = str(e)), 404