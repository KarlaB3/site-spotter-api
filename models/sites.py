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
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    # Set the relationship with other tables
    user = db.relationship('User', backref='sites')
    centre = db.relationship("Centre", back_populates="site")
    #landlord = db.relationship('Landlord', backref='sites')

