from main import db

class Landlord(db.Model):
    # Define the table name
    __tablename__ = "landlords"
    # Set the Landlords table attributes
    landlord_id = db.Column(db.Integer, primary_key=True)
    landlord_name = db.Column(db.String(), nullable=False)
    landlord_email = db.Column(db.String())
    landlord_phone = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    # Set the relationships to other tables
    #centres = db.relationship("Centre", backref = "landlord", lazy = "True", cascade = "all, delete")
    #sites = db.relationship("Site", backref = "landlord", lazy = "True", cascade = "all, delete")


