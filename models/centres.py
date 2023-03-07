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
    traffic = db.Column(db.String())
    sales = db.Column(db.String())
    landlord_id = db.Column(db.Integer, db.ForeignKey("landlords.landlord_id"), nullable=False)



