from flask import Blueprint, jsonify, request
from main import db
from models.sites import Site
from schemas.site_schema import site_schema, sites_schema
from flask_jwt_extended import jwt_required

# Set all routes related to Sites to start with /sites prefix
sites = Blueprint('sites', __name__, url_prefix="/sites")

@sites.get("/")
def get_sites():
    # Retrieve all sites from the sites table
    sites_list = Site.query.all()
    result = sites_schema.dump(sites_list)
    return jsonify(result)


@sites.get("/<int:site_id>")
def get_site(site_id):
    # Retrieve a site based on the site_id field
    site = Site.query.get(site_id)
    if not site:
        # Display error message if the Site ID doesn't exist in the database
        return jsonify("Error: Site ID not found. Please search again using a valid Site ID.")
    # elif type(site) != int:
    #     # Display error message if the Site ID doesn't exist in the database
    #     return jsonify("Error: Incorrect Site ID search type. Please use a number.")
    else:
        result = site_schema.dump(site)
        return jsonify(result)
