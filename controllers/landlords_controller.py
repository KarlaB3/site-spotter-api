from flask import Blueprint, jsonify, request, abort
from main import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.landlords import Landlord
from models.users import User
from schemas.landlord_schema import landlord_schema, landlords_schema


# Set all routes related to Landlords to start with /landlords prefix
landlords = Blueprint('landlords', __name__, url_prefix="/landlords")

# Retrieve all landlords from the landlords table
@landlords.get("/")
def get_landlords():
    all_landlords = Landlord.query.all()
    result = landlords_schema.dump(all_landlords)
    return jsonify(result), 200

# Retrieve a landlord based on the landlord_id field
@landlords.get("/<int:landlord_id>")
def get_landlord_id(landlord_id):
    id_landlord = Landlord.query.get(landlord_id)
    # Display error message if the Landlord ID doesn't exist in the database
    if not id_landlord: 
        return abort(404, description = "Error: Landlord ID not found. Please try again using a valid Landlord ID.")
    result = landlord_schema.dump(id_landlord)
    return jsonify(result), 200

# Retrieve a landlord based on the landlord_name field
@landlords.get("/search")
def search_landlords():
    if request.args.get("landlord_name"):
        name_landlord = Landlord.query.filter_by(landlord_name = request.args.get("landlord_name"))
        result = landlords_schema.dump(name_landlord)
        return jsonify(result), 200
    else:
        return abort(404, description = "Error: Landlord name not found. Please try again using a valid Landlord name.")
    
# Create a new landlord record
@landlords.post("/")
@jwt_required()
def create_landlord():
    # Retrieve landlord schema and fields
    landlord_fields = landlord_schema.load(request.json)
    # Retrieve user ID from JWT
    existing_user = get_jwt_identity()
    # Check if user exists in the database
    user = User.query.get(existing_user)
    # Display error message if the user doesn't exist in the database
    if not user:
        return abort(404, description = "Error: User not found. Please try again using a registered User.")
    # Display error message if the user isn't an administrator
    if not user.admin:
        return abort(401, description = "Error: You are not authorised to complete this action. Only administrators can create new Landlord records.")
    # Declare fields to be added as part of the landlord record
    new_landlord = Landlord()
    new_landlord.landlord_name = landlord_fields["landlord_name"]
    new_landlord.landlord_email = landlord_fields["landlord_email"]
    new_landlord.landlord_phone = landlord_fields["landlord_phone"]
    new_landlord.user_id = existing_user
    # Add landlord to the database
    db.session.add(new_landlord)
    # Commit landlord changes to the database
    db.session.commit()
    return jsonify(landlord_schema.dump(new_landlord)), 201

# Update a landlord record using landlord_id field
@landlords.put("/<int:landlord_id>")
@jwt_required()
def update_landlord(landlord_id):
    # Retrieve user ID from JWT
    existing_user = get_jwt_identity()
    # Check if user exists in the database
    user = User.query.get(existing_user)
    # Display error message if the user doesn't exist in the database
    if not user:
        return abort(404, description = "Error: User not found. Please try again using a registered User.")
    # Display error message if the user isn't an administrator
    if not user.admin:
        return abort(401, description = "Error: You are not authorised to complete this action. Only administrators can update Landlord records.")
    landlord = Landlord.query.get(landlord_id)
    if not landlord:
        return abort(404, description = "Error: Landlord record does not exist. Please try again.")
    landlord_fields = landlord_schema.load(request.json)
    landlord.landlord_name = landlord_fields["landlord_name"]
    landlord.landlord_email = landlord_fields["landlord_email"]
    landlord.landlord_phone = landlord_fields["landlord_phone"]
    # Commit landlord changes to the database
    db.session.commit()
    return jsonify(landlord_schema.dump(landlord)), 201

# Delete a landlord record using landlord_id field
@landlords.delete("/<int:landlord_id>")
@jwt_required()
def delete_landlord(landlord_id):
    # Retrieve user ID from JWT
    existing_user = get_jwt_identity()
    # Check if user exists in the database
    user = User.query.get(existing_user)
    # Display error message if the user doesn't exist in the database
    if not user:
        return abort(404, description = "Error: User not found. Please try again using a registered User.")
    # Display error message if the user isn't an administrator
    if not user.admin:
        return abort(401, description = "Error: You are not authorised to complete this action. Only administrators can delete Landlord records.")
    # Check if landlord exists in the database using the landlord_id field
    landlord = Landlord.query.get(landlord_id)
    # Display error message if the landlord_id doesn't exist
    if not landlord:
        return abort(404, description = "Error: Landlord record doesn't exist. Please try again.")
    # Delete landlord from the database
    db.session.delete(landlord)
    # Commit landlord changes to the database
    db.session.commit()
    return jsonify("Message: Landlord successfully deleted."), 201