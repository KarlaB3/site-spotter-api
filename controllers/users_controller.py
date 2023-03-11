from flask import Blueprint, jsonify, request, abort
from main import db
from models.users import User
from schemas.user_schema import user_schema, users_schema
from main import bcrypt
from marshmallow.exceptions import ValidationError

# Set all routes related to Users to start with /users prefix
users = Blueprint('users', __name__, url_prefix="/users")

@users.errorhandler(ValidationError)
def register_validation_error(error):
    #print(error.messages)
    return error.messages, 400

# Register new users
@users.post("/register")
def register_user():
    # Retrieve user details
    user_fields = user_schema.load(request.json)
    # Check if user is already in the database using the email field
    user = User.query.filter_by(email = user_fields["email"]).first()
    # Display error message if the email is has already been registered to a user
    if user:
        return jsonify("Error: Email is already registered. Please login or register with a different email.")
    # Crate user new using email and hashed password
    user = User(email = user_fields["email"], password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8"))
    # Set admin attribute to false
    user.admin = False
    # Add user to the database
    db.session.add(user)
    # Commit user changes to the database
    db.session.commit()
    return jsonify("User successfully registered")
    # generate the token setting the identity (user.id) and expiry time (1 day)  --> ONLY IF YOU WANT TO USE AN ACCESS TOKEN, WHICH ISN'T NECESSARY
    # token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1)) 
    # return {"username": user.username, "token": token}

# Allow users to login
@users.post("/login")
def login_user():
    # Retrieve user details
    user_fields = user_schema.load(request.json)
    # Check if user is already in the database using the email field
    user = User.query.filter_by(email = user_fields["email"]).first()
    # Display error message if the email and password combination is incorrect or does not exist
    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, "Incorrect username and/or password. Please try again")
    return jsonify("Login successful")

