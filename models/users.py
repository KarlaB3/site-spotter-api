from main import db

class Users(db.Model):
    # Define the table name
    __tablename__ = "users"
    # Set the table attributes
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
    # Set the relationship with the landlords table
    landlords = db.relationship(
        "Landlord",
        backref = "user",
        cascade = "all, delete"

    )