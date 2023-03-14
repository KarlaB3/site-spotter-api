from datetime import timedelta
from flask import Blueprint, jsonify, request, abort
from main import db
from models.users import User
from schemas.user_schema import user_schema, users_schema
from main import bcrypt
from flask_jwt_extended import create_access_token
#from marshmallow.exceptions import ValidationError  ---> FOR ERROR HANDLING

# Set all routes related to Users to start with /users prefix
users = Blueprint('users', __name__, url_prefix="/users")

# @users.errorhandler(ValidationError) ---> FOR ERROR HANDLING
# def register_validation_error(error):
#     #print(error.messages)
#     return error.messages, 400

# Register new users
@users.post("/register")
def register_user():
    # Retrieve user schema and fields
    user_fields = user_schema.load(request.json)
    # Check if user is already in the database using the email field
    new_user = User.query.filter_by(email = user_fields["email"]).first()
    # Display error message if the email has already been registered to a user
    if new_user:
        return jsonify("Error: Email is already registered. Please login or register with a different email.")
    # Crate user new using email and encyrpted password
    new_user = User(email = user_fields["email"], password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8"))
    # Add user to the database
    db.session.add(new_user)
    # Commit user changes to the database
    db.session.commit()
    # Generate the JSON web token with 1 day expiry 
    token = create_access_token(identity=str(new_user.user_id), expires_delta=timedelta(days=1)) 
    return {"email": new_user.email, "token": token}

# Existing user login
@users.post("/login")
def login_user():
    # Retrieve user details
    user_fields = user_schema.load(request.json)
    # Check if user is already in the database using the email field
    user = User.query.filter_by(email = user_fields["email"]).first()
    # Display error message if the email and password combination is incorrect or does not exist
    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, "Error: Incorrect username and/or password. Please try again")
     # Generate the JSON web token with 1 day expiry 
    token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1)) 
    return {"email": user.email, "token": token}

