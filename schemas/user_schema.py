from main import ma

class UserSchema(ma.Schema):
    class Meta:
        # Declare user schema fields and display in order
        ordered = True
        fields = ("user_id", "email", "password")
        email = ma.String(required=True)
        password = ma.String(required=True)

# Single user schema to retrieve one user record
user_schema = UserSchema()
# Many users schema to retrieve many user records
users_schema = UserSchema(many = True)
