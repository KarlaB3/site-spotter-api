from main import db

class Site(db.Model):
    # Define the table name
    __tablename__ = "sites"
    # Set the table attributes
    site_id = db.Column(db.Integer(), primary_key=True)
    size = db.Column(db.String())
    power = db.Column(db.Boolean())
    location = db.Column(db.String())
    centre_id = db.Column(db.Integer, db.ForeignKey("centres.centre_id"), nullable=False)

