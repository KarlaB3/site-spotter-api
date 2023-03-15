from main import ma

class LandlordSchema(ma.Schema):
    class Meta:
        # Declare landlord schema fields and display in order
        ordered = True
        fields = ("landlord_id", "landlord_name", "landlord_email", "landlord_phone")

# Single landlord schema to retrieve one landlord record
landlord_schema = LandlordSchema()
# Many landlords schema to retrieve many landlord records
landlords_schema = LandlordSchema(many = True)