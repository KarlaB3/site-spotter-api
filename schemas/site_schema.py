from main import ma 
# from schemas.centre_schema import CentreSchema
# from schemas.landlord_schema import LandlordSchema

class SiteSchema(ma.Schema):
    class Meta:
        # Declare site schema fields and display in order
        ordered = True
        fields = ("site_id", "size", "power", "location")
    #landlords = fields.List(fields.Nested(LandlordSchema, only = ("landlord_name", "landlord_email", "landlord_phone")))
    #centres = fields.List(fields.Nested(CentreSchema, only = ("centre_name", "suburb", "postcode", "state", "traffic", "sales")))

# Single site schema to retrieve one site record
site_schema = SiteSchema()
# Many sites schema to retrieve many site records
sites_schema = SiteSchema(many = True)