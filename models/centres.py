from main import db

class Centre(db.Model):
    # Define the table name
    __tablename__ = "centres"
    # Set the table attributes
    centre_id = db.Column(db.Integer(), primary_key=True)
    centre_name = db.Column(db.String(), nullable=False)
    suburb = db.Column(db.String())
    postcode = db.Column(db.String())
    state = db.Column(db.String())
    landlord_id = db.Column(db.Integer, db.ForeignKey("landlords.landlord_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    # Set the relationship with other tables
    landlord = db.relationship("Landlord", back_populates="centre")
    user = db.relationship("User", back_populates="centre")
    site = db.relationship("Site", back_populates="centre")




