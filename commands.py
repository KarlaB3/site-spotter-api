from main import db
from flask import Blueprint
from main import bcrypt
from models.centres import Centre
from models.landlords import Landlord
from models.sites import Site
from models.users import User

db_commands = Blueprint ("db", __name__)

# CLI command to create tables
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables have been created")

# CLI command to drop tables
@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables have been dropped")

# CLI command to seed tables
@db_commands.cli.command("seed")
def seed_db():
    # Users data to be seeded to the users table
    admin_user = User(
        email = "admin@sitespotter.com.au",
        password = bcrypt.generate_password_hash("admin000").decode("utf-8"),
        admin = True
    )

    user1 = User(
        email = "brandspace@westfield.com.au",
        password = bcrypt.generate_password_hash("westfield111").decode("utf-8"),
        admin = False
    )

    user2 = User(
        email = "leasing@mirvac.com.au",
        password = bcrypt.generate_password_hash("mirvac222").decode("utf-8"),
        admin = False
    )

    user3 = User(
        email = "leasing@lendlease.com.au",
        password = bcrypt.generate_password_hash("lendlease333").decode("utf-8"),
        admin = False
    )

    user4 = User(
        email = "popup.retail@vicinity.com.au",
        password = bcrypt.generate_password_hash("vicinity444").decode("utf-8"),
        admin = False
    )

    user5 = User(
        email = "leasing@stockland.com.au",
        password = bcrypt.generate_password_hash("stockland555").decode("utf-8"),
        admin = False
    )
    # Add user data to the users table
    db.session.add_all([admin_user, user1, user2, user3, user4, user5])
    # Commit user data to the users table
    db.session.commit()

    # Landlords data to be seeded to the landlords table
    landlord1 = Landlord(
        landlord_name = "Westfield",
        landlord_email = "brandspace@westfield.com.au",
        landlord_phone = "02 9358 7441",
        user_id = user1.user_id
    )

    landlord2 = Landlord(
        landlord_name = "Mirvac",
        landlord_email = "cml@mirvac.com.au",
        landlord_phone = "02 9080 8000",
        user_id = user2.user_id
    )

    landlord3 = Landlord(
        landlord_name = "Lend Lease",
        landlord_email = "ashley.bell@lendlease.com",
        landlord_phone = "0477 716 559",
        user_id = user3.user_id
    )

    landlord4 = Landlord(
        landlord_name = "Vicinity Centres",
        landlord_email = "popup.retail@vicinity.com.au",
        landlord_phone = "03 7001 4000",
        user_id = user4.user_id
    )

    landlord5 = Landlord(
        landlord_name = "Stockland",
        landlord_email = "s-connect@stockland.com.au",
        landlord_phone = "1800 72 71 70",
        user_id = user5.user_id
    )
    # Add landlord data to the landlords table
    db.session.add_all([landlord1, landlord2, landlord3, landlord4, landlord5])
    # Commit landlord data to the landlords table
    db.session.commit()

    # Centres data to be seeded to the centres table
    centre1 = Centre(
        centre_name = "Westfield Eastgardens",
        suburb = "Eastgardens",
        postcode = "2036",
        state = "NSW",
        landlord_id = landlord1.landlord_id,
        user_id = user1.user_id
    )

    centre2 = Centre(
        centre_name = "Banksia Grove",
        suburb = "Joondalup",
        postcode = "6027",
        state = "WA",
        landlord_id = landlord2.landlord_id,
        user_id = user2.user_id
    )

    centre3 = Centre(
        centre_name = "Lakeside Joondalup",
        suburb = "Joondalup",
        postcode = "6027",
        state = "WA",
        landlord_id = landlord3.landlord_id,
        user_id = user3.user_id
    )

    centre4 = Centre(
        centre_name = "Castle Plaza",
        suburb = "Edwardstown",
        postcode = "5039",
        state = "SA",
        landlord_id = landlord4.landlord_id,
        user_id = user4.user_id
    )
    
    centre5 = Centre(
        centre_name = "Stockland Wendouree",
        suburb = "Wendouree",
        postcode = "3355",
        state = "VIC",
        landlord_id = landlord5.landlord_id,
        user_id = user5.user_id
    )

    centre6 = Centre(
        centre_name = "Westfield Belconnen",
        suburb = "Belconnen",
        postcode = "2617",
        state = "ACT",
        landlord_id = landlord1.landlord_id,
        user_id = user1.user_id
    )
    
    centre7 = Centre(
        centre_name = "Cairns Central",
        suburb = "Cairns",
        postcode = "4870",
        state = "QLD",
        landlord_id = landlord3.landlord_id,
        user_id = user3.user_id
    )

    centre8 = Centre(
        centre_name = "Stockland Cairns",
        suburb = "Cairns",
        postcode = "4870",
        state = "QLD",
        landlord_id = landlord5.landlord_id,
        user_id = user5.user_id
    )

    centre9 = Centre(
        centre_name = "Stockland Merrylands",
        suburb = "Merrylands",
        postcode = "2160",
        state = "NSW",
        landlord_id = landlord5.landlord_id,
        user_id = user5.user_id
    )

    centre10 = Centre(
        centre_name = "Craigieburn Central",
        suburb = "Craigieburn",
        postcode = "3074",
        state = "VIC",
        landlord_id = landlord3.landlord_id,
        user_id = user3.user_id
    )
    # Add centre data to the centres table
    db.session.add_all([centre1, centre2, centre3, centre4, centre5, centre6, centre7, centre8, centre9, centre10])
    # Commit centre data to the centres table
    db.session.commit()
    
    # Site data to be seeded to the sites table
    site1 = Site(
        size = "4m x 4m",
        power = True,
        location = "Outside supermarket",
        centre_id = centre1.centre_id,
        user_id = user1.user_id
    )

    site2 = Site(
        size = "3m x 2m",
        power = True,
        location = "Near food court",
        centre_id = centre2.centre_id,
        user_id = user2.user_id
    )

    site3 = Site(
        size = "5m x 3.3m",
        power = True,
        location = "Near food court",
        centre_id = centre3.centre_id,
        user_id = user3.user_id
    )

    site4 = Site(
        size = "2m x 1.5m",
        power = False,
        location = "Fashion precinct",
        centre_id = centre4.centre_id,
        user_id = user4.user_id
    )

    site5 = Site(
        size = "10m x 6.5m",
        power = False,
        location = "Centre Court",
        centre_id = centre5.centre_id,
        user_id = user5.user_id
    )

    site6 = Site(
        size = "12m x 8m",
        power = True,
        location = "Centre Court",
        centre_id = centre1.centre_id,
        user_id = user1.user_id
    )

    site7 = Site(
        size = "2m x 3m",
        power = False,
        location = "Fashion precinct",
        centre_id = centre9.centre_id,
        user_id = user5.user_id
    )

    site8 = Site(
        size = "5m x 5m",
        power = True,
        location = "Near food court",
        centre_id = centre9.centre_id,
        user_id = user5.user_id
    )

    site9 = Site(
        size = "2m x 1m",
        power = False,
        location = "Fashion precinct",
        centre_id = centre10.centre_id,
        user_id = user3.user_id
    )

    site10 = Site(
        size = "3m x 2.5m",
        power = False,
        location = "Outside supermarket",
        centre_id = centre6.centre_id,
        user_id = user3.user_id
    )
    # Add site data to the sites table
    db.session.add_all([site1, site2, site3, site4, site5, site6, site7, site8, site9, site10])
    # Commit site data to the sites table
    db.session.commit()
    print("Tables have been seeded")