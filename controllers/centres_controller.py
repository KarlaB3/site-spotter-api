from flask import Blueprint, jsonify, request, abort
from main import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.centres import Centre
from models.users import User
from schemas.centre_schema import centre_schema, centres_schema

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
        return abort(404, description = "Error: Centre ID not found. Please search again using a valid Centre ID.")
    result = centre_schema.dump(centre)
    return jsonify(result), 200
    
# Retrieve a centre based on the centre attributes
@centres.get("/search")
def search_centres():
    if request.args.get("centre_name"):
        name_centre = Centre.query.filter_by(centre_name = request.args.get("centre_name"))
        result = centres_schema.dump(name_centre)
        return jsonify(result), 200
    elif request.args.get("suburb"):
        suburb_centre = Centre.query.filter_by(suburb = request.args.get("suburb"))
        result = centres_schema.dump(suburb_centre)
        return jsonify(result), 200
    elif request.args.get("postcode"):
        postcode_centre = Centre.query.filter_by(postcode = request.args.get("postcode"))
        result = centres_schema.dump(postcode_centre)
        return jsonify(result), 200
    elif request.args.get("state"):
        state_centre = Centre.query.filter_by(state = request.args.get("state"))
        result = centres_schema.dump(state_centre)
        return jsonify(result), 200
    else:
        return abort(404, description = "Error: Information not found.")
    
# Create a new centre record
@centres.post("/")
@jwt_required()
def create_centre():
    # Retrieve centre schema and fields
    centre_fields = centre_schema.load(request.json)
    # Retrieve user ID from JWT
    existing_user = get_jwt_identity()
    # Check if user exists in the database
    user = User.query.get(existing_user)
    # Display error message if the user doesn't exist in the database
    if not user:
        return abort(404, description = "Error: User not found. Please try again using a registered User.")
    # Declare fields to be added as part of the centre record
    new_centre = Centre()
    new_centre.centre_name = centre_fields["centre_name"]
    new_centre.suburb = centre_fields["suburb"]
    new_centre.postcode = centre_fields["postcode"]
    new_centre.state = centre_fields["state"]
    new_centre.user_id = existing_user
    new_centre.landlord_id = existing_user
    # Add centre to the database
    db.session.add(new_centre)
    # Commit centre changes to the database
    db.session.commit()
    return jsonify(centre_schema.dump(new_centre)), 201

# Update a centre record using centre_id field
@centres.put("/<int:centre_id>")
@jwt_required()
def update_centre(centre_id):
    # Retrieve user ID from JWT
    existing_user = get_jwt_identity()
    # Check if user exists in the database
    user = User.query.get(existing_user)
    # Display error message if the user doesn't exist in the database
    if not user:
        return abort(404, description = "Error: User not found. Please try again using a registered User.")
    centre = Centre.query.get(centre_id)
    if not centre:
        return abort(404, description = "Error: Centre record does not exist. Please try again.")
    centre_fields = centre_schema.load(request.json)
    centre.centre_name = centre_fields["centre_name"]
    centre.suburb = centre_fields["suburb"]
    centre.postcode = centre_fields["postcode"]
    centre.state = centre_fields["state"]
    centre.user_id = existing_user
    # Commit centre changes to the database
    db.session.commit()
    return jsonify(centre_schema.dump(centre)), 201

# Delete a centre record using centre_id field
@centres.delete("/<int:centre_id>")
@jwt_required()
def delete_centre(centre_id):
    # Retrieve user ID from JWT
    existing_user = get_jwt_identity()
    # Check if user exists in the database
    user = User.query.get(existing_user)
    # Display error message if the user doesn't exist in the database
    if not user:
        return abort(404, description = "Error: User not found. Please try again using a registered User.")
    # Display error message if the user isn't an administrator
    if not user.admin:
        return abort(401, description = "Error: You are not authorised to complete this action. Only administrators can delete Centre records.")
    # Check if centre exists in the database using the centre_id field
    centre = Centre.query.get(centre_id)
    # Display error message if the centre_id doesn't exist
    if not centre:
        return abort(404, description = "Error: Centre record doesn't exist. Please try again.")
    # Delete centre from the database
    db.session.delete(centre)
    # Commit centre changes to the database
    db.session.commit()
    return jsonify("Message: Centre successfully deleted."), 201