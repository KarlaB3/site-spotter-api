from flask import Blueprint, jsonify, request, abort
from main import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.sites import Site
from schemas.site_schema import site_schema, sites_schema
from models.users import User

# Set all routes related to Sites to start with /sites prefix
sites = Blueprint('sites', __name__, url_prefix="/sites")

# Retrieve all sites from the sites table
@sites.get("/")
def get_sites():
    sites_list = Site.query.all()
    result = sites_schema.dump(sites_list)
    return jsonify(result)

# Retrieve a site based on the site_id field
@sites.get("/<int:site_id>")
def get_site(site_id):
    site = Site.query.get(site_id)
    # Display error message if the Site ID doesn't exist in the database
    if not site:
        return abort(404, "Error: Site ID not found. Please search again using a valid Site ID.")
    result = site_schema.dump(site)
    return jsonify(result), 200

# Retrieve a site based on the site attributes
@sites.get("/search")
def search_sites():
    if request.args.get("size"):
        size_site = Site.query.filter_by(size = request.args.get("size"))
        result = sites_schema.dump(size_site)
        return jsonify(result), 200
    elif request.args.get("power"):
        power_site = Site.query.filter_by(power = request.args.get("power"))
        result = sites_schema.dump(power_site)
        return jsonify(result), 200
    elif request.args.get("location"):
        location_site = Site.query.filter_by(location = request.args.get("location"))
        result = sites_schema.dump(location_site)
        return jsonify(result), 200
    else:
        return abort(404, description = "Error: Information not found.")
    
# Create a new site record
@sites.post("/")
@jwt_required()
def create_site():
    # Retrieve site schema and fields
    site_fields = site_schema.load(request.json)
    # Retrieve user ID from JWT
    existing_user = get_jwt_identity()
    # Check if user exists in the database
    user = User.query.get(existing_user)
    # Display error message if the user doesn't exist in the database
    if not user:
        return abort(404, description = "Error: User not found. Please try again using a registered User.")
    # Declare fields to be added as part of the site record
    new_site = Site()
    new_site.size = site_fields["size"]
    new_site.power = site_fields["power"]
    new_site.location = site_fields["location"]
    new_site.user_id = existing_user
    new_site.centre_id = existing_user
    # Add site to the database
    db.session.add(new_site)
    # Commit site changes to the database
    db.session.commit()
    return jsonify(site_schema.dump(new_site)), 201

# Update a site record using site_id field
@sites.put("/<int:site_id>")
@jwt_required()
def update_site(site_id):
    # Retrieve user ID from JWT
    existing_user = get_jwt_identity()
    # Check if user exists in the database
    user = User.query.get(existing_user)
    # Display error message if the user doesn't exist in the database
    if not user:
        return abort(404, description = "Error: User not found. Please try again using a registered User.")
    site = Site.query.get(site_id)
    if not site:
        return abort(404, description = "Error: Site record does not exist. Please try again.")
    site_fields = site_schema.load(request.json)
    site.size = site_fields["size"]
    site.power = site_fields["power"]
    site.location = site_fields["location"]
    site.user_id = existing_user
    site.centre_id = existing_user
    # Commit site changes to the database
    db.session.commit()
    return jsonify(site_schema.dump(site)), 201

# Delete a site record using site_id field
@sites.delete("/<int:site_id>")
@jwt_required()
def delete_site(site_id):
    # Retrieve user ID from JWT
    existing_user = get_jwt_identity()
    # Check if user exists in the database
    user = User.query.get(existing_user)
    # Display error message if the user doesn't exist in the database
    if not user:
        return abort(404, description = "Error: User not found. Please try again using a registered User.")
    # Display error message if the user isn't an administrator
    if not user.admin:
        return abort(401, description = "Error: You are not authorised to complete this action. Only administrators can delete Site records.")
    # Check if site exists in the database using the site_id field
    site = Site.query.get(site_id)
    # Display error message if the site_id doesn't exist
    if not site:
        return abort(404, description = "Error: Site record doesn't exist. Please try again.")
    # Delete site from the database
    db.session.delete(site)
    # Commit site changes to the database
    db.session.commit()
    return jsonify("Message: Site successfully deleted."), 201
