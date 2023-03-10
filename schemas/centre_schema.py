from main import ma
from marshmallow import fields
# from schemas.landlord_schema import LandlordSchema
# from schemas.site_schema import SiteSchema


class CentreSchema(ma.Schema):
    class Meta:
        # Declare centre schema fields and display in order
        ordered = True
        fields = ("centre_id", "centre_name", "suburb", "postcode", "state", "traffic", "sales")
    #landlords = fields.List(fields.Nested(LandlordSchema, only = ("landlord_name", "landlord_email", "landlord_phone")))
    #sites = fields.List(fields.Nested(SiteSchema, only = ("site_id", "size", "power", "location")))


# Single centre schema to retrieve one centre record
centre_schema = CentreSchema()
# Many centres schema to retrieve many centre records
centres_schema = CentreSchema(many = True)