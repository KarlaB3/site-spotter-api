from main import ma
from marshmallow import fields
# from schemas.centre_schema import CentreSchema
# from schemas.site_schema import SiteSchema

class LandlordSchema(ma.Schema):
    class Meta:
        # Declare landlord schema fields and display in order
        ordered = True
        fields = ("landlord_id", "landlord_name", "landlord_email", "landlord_phone", "user_id")
    #centres = fields.List(fields.Nested(CentreSchema, only = ("centre_name", "suburb", "postcode", "state", "traffic", "sales")))
    #sites = fields.List(fields.Nested(SiteSchema, only = ("site_id", "size", "power", "location")))

# Single landlord schema to retrieve one landlord record
landlord_schema = LandlordSchema()
# Many landlords schema to retrieve many landlord records
landlords_schema = LandlordSchema(many = True)