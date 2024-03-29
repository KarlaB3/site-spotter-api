from main import db

class User(db.Model):
    # Define the table name
    __tablename__ = "users"
    # Set the table attributes
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
    # Set the relationship with other tables
    landlord = db.relationship("Landlord", back_populates="user")
    centre = db.relationship("Centre", back_populates="user")
    site = db.relationship("Site", back_populates="user")