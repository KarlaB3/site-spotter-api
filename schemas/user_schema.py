from main import ma
from marshmallow.validate import Length

class UserSchema(ma.Schema):
    class Meta:
        # Declare user schema fields and display in order
        ordered = True
        fields = ("user_id", "email", "password")
        # Validate minimum length requirement for password and set required fields
        password = ma.String(validate = Length(min = 8))
        email = ma.String(required = True)

# Single user schema to retrieve one user record
user_schema = UserSchema()
# Many users schema to retrieve many user records
users_schema = UserSchema(many = True)
