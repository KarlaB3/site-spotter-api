from main import ma

class CentreSchema(ma.Schema):
    class Meta:
        # Declare centre schema fields and display in order
        ordered = True
        fields = ("centre_id", "centre_name", "suburb", "postcode", "state")

# Single centre schema to retrieve one centre record
centre_schema = CentreSchema()
# Many centres schema to retrieve many centre records
centres_schema = CentreSchema(many = True)