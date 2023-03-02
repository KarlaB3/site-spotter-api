from main import db

class Site(db.Model):
    # Define the table name
    __tablename__ = "sites"
    # Set the table attributes
    site_id = db.Column(db.Integer(), primary_key=True)
    size = db.Column(db.Integer(), nullable=False)
    power = db.Column(db.Boolean(), nullable=False)
    location = db.Column(db.String())
    centre_id = db.Column(db.Integer, db.ForeignKey("centres.id"), nullable=False)

