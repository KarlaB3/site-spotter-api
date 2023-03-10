from flask import Blueprint, jsonify, request
from main import db
from models.users import User
from schemas.user_schema import user_schema, users_schema
from flask_jwt_extended import jwt_required

# Set all routes related to Users to start with /users prefix
users = Blueprint('users', __name__, url_prefix="/users")

@users.get("/")
def get_users():
    # Retrieve all users from the users table
    users_list = User.query.all()
    result = users_schema.dump(users_list)
    return jsonify(result)


@users.get("/<int:user_id>")
def get_user(user_id):
    # Retrieve a user based on the user_id field
    user = User.query.get(user_id)
    if not user:
        # Display error message if the User ID doesn't exist in the database
        return jsonify("Error: User ID not found. Please search again using a valid User ID.")
    # elif type(user) != int:
    #     # Display error message if the User ID doesn't exist in the database
    #     return jsonify("Error: Incorrect User ID search type. Please use a number.")
    else:
        result = user_schema.dump(user)
        return jsonify(result)