from main import ma 

class SiteSchema(ma.Schema):
    class Meta:
        # Declare site schema fields and display in order
        ordered = True
        fields = ("site_id", "size", "power", "location", "centre_id", "centre")
        load_only = ["centre_id"]
    centre = ma.Nested("CentreSchema", only=("centre_name",))

# Single site schema to retrieve one site record
site_schema = SiteSchema()
# Many sites schema to retrieve many site records
sites_schema = SiteSchema(many = True)