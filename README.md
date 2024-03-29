# SITE SPOTTER API 
Site Spotter lists casual leasing sites in shopping centres across Australia. The Site Spotter API is a CRUD RESTful API that allows for user access to create, read, update and delete records in the Site Spotter PostgreSQL database containing retail property landlord, shopping centre and casual leasing site records.

##  Links
GitHub Link: https://github.com/KarlaB3/site-spotter-api   
Trello Project Link: https://trello.com/b/6sGcY3EH/sitespotter-api   

## The Problem
The signing of long term lease deals between retailers and shopping centre landlords has declined since COVID-19. During this period many retailers were forbidden to trade due to mandatory lockdowns but still pay rent, impacting their ability to generate income and in some cases putting them into debt or forcing them to shut down operations altogether.

Many retailers are now wary to commit to long term lease deals spanning over years, preferring shorter term arrangements. This has caused many shopping centre landlords to refocus their efforts on attracting retailers to their centres by offering casual leases. 

Casual lease sites are typically listed on individual shopping centre websites, and teams of leasing executives are employed by landlords to proactively approach and sell these sites to retailers. On the flipside, retailers must contact individual landlords and shopping centres to enquire about casual leasing sites. This creates additional effort on the part of both landlords and retailers to find relevant sites for casual lease.

## The Solution
Site Spotter takes the work out of finding and selling casual leasing sites by aggregating a database of shopping centre landlords, retailers and sites across Australia. 

Information about landlords, the centres they own and the available sites within those centres is readily available via the Site Spotter API and can be searched by centre location (state, suburb, postcode) and site metrics (size, power availability, location within the centre). 

The Site Spotter API also allows for the creation, update and deletion of landlord, centre, and site details if they are incorrect or no longer valid.

## Tech Stack
### PostgreSQL 
PostgreSQL is the database of choice for Site Spotter. It is an open source object-relational database system that uses a variation of standard SQL query language and supports objects, classes and inheritance. It was chosen for the following reasons (Juba, Vannahme & Volkov 2015, pp. 31-33; The PostgreSQL Global Development Group, 2023): 
* Free and open source, so there is no cost associated with using PostgreSQL. 
* Extensible, so data types, functions, languages and operators can be defined.
* Updated regularly, with at least one minor release made every quarter.
* Supported by a large open source community dedicated to continually improving and adding new features and extensions.
* Cross platform, so it runs on modern operating systems including Mac, Windows and Linux.
* Largely conforms to standard SQL 
* Atomicity, Consistency, Isolation, and Durability (ACID) compliant, meaning data can be processed in an accurate and reliable manner using PostgreSQL.
* Supports many popular programming languages such as Python and JavaScript.

Despite the benefits as listed above, there are also some drawbacks with PostgreSQL that were taken into consideration when choosing a relational database management system (Hristozov, 2019; Panchenko, 2021):
* Cloud support for extensions can be limited, meaning an on-premise solution may need to be used if the database grows.
* Despite its popularity, there are not as many third party tools or developers that support and specialise in PostgreSQL compared to MySQL.
* Slower performance for read-only commands compared to MySQL.

### Flask
Flask is a Web Server Gateway Interface (WSGI) application framework. Flask is written in Python, and is considered a microframework with minimal dependencies or boilerplate code, but supported by a vast library of extensions and libraries (Python Basics 2021).

Flask was chosen because it can support a Model, View and Controller (MVC) architectural pattern where each component handles a specific task in developing and executing an application. MVC allows for Site Spotter to more easily expand in size and scope and be developed and maintained by multiple developers (Hernandez 2021). 

### SQLAlchemy and Flask-SQLAlchemy
Object Relational Mapping is a technique that allows for object-oriented programs and relational databases to connect. An Object Relational Mapper (ORM) is the tool that allows developers using object-oriented programming to interact with relational databases (Abba, I.V. 2022). 

SQLAlchemy is the SQL toolkit used for the Site Spotter API because it can directly access and interact with the PostgreSQL database using Python objects and methods. The Flask-SQLAlchemy extension provides further SQLAlchemy support with tools and methods to simplify communication with databases.

SQLAlchemy is used in the Site Spotter API for:
* Translating Python classes to tables and automatically loading tables from the PostgreSQL database.
* Converting function calls and expressions to SQL statements, giving Site Spotter the full range of possible expressions, operators and functions and joins (SQLAlchemy, 2023).
* Rather than writing raw SQL queries, SQLAlchemy uses a simple Pythonic domain language to more efficiently query data (SQLAlchemy, 2023). 
* Supporting and enforcing meaningful relationship declarations, primary key constraints, mutability and cascade delete functions (SQLAlchemy, 2023).

### Marshmallow and Flask-Marshmallow
Marshmallow is a Python library used by Site Spotter to help convert data into a format suitable for display in JavaScript Object Notation (JSON) format. The Flask-Marshmallow extension provides additional integration support between Flask and Marshmallow and also integrates with Flask-SQLAlchemy. Site Spotter uses Marshmallow to create the database schemas by declaring the table fields to be retrieved and exposed in JSON format.

### Flask-JWT-Extended
JSON web tokens (JWT) are used for handling user authentication and session management. Using JWT and the Flask-JWT-Extended extension, the Site Spotter API can create temporary access token (1 day validity) to preserve a user's authentication state during their Site Spotter session.

### Flask-Bcrypt
Cryptography is used by Site Spotter for encrypting sensitive user data at rest. The Flask-bcrypt Python module invokes hashing of passwords when registering new users and storing existing user logins in a database.

### Psycopg
Pyscopg is a PostgreSQL database adapter for Python. It is used by Site Spotter to assist with connecting to the PostgreSQL database and running SQL queries against the database.

### Other Platforms
* VS Code for code writing and testing.
* Ubuntu operating system for postgreSQL database management.
* Insomnia for testing the API.

## How to Set Up and Use Site Spotter
Step 1: Using the terminal window, create and navigate to the site_spotter folder.

```mkdir directory_name && cd directory_name```

Step 2: Create a virtual environment and activate it. 

```virtualenv venv && source venv/bin/activate```

Step 3: Initialise your git repo and add venv to the .gitignore file.

``` git init && echo 'venv/' > .gitignore ```

Step 4: Install all necessary modules from the requirements.txt file located in the zip file's 'src' folder.

```pip install -r requirements.txt```

Step 5: Activate PostgreSQL with your username or default username (postgres)/

``` sudo -u postgres psql ```

Step 6: Create the site_spotter database:

``` CREATE DATABASE site_spotter;```

Step 7: Create a database user called db_dev with password 123456.

``` CREATE USER db_dev WITH PASSWORD '123456';```

Step 8: Grant all database privileges to db_dev user.

``` GRANT ALL PRIVILEGES ON DATABASE site_spotter to db_dev;```

Step 9: In VS Code open the site_spotter directory and files and  create and seed the tables then run Flask.

```
code .
flask db create
flask db seed
flask run
```
To drop tables from the database use the ``` flask db drop ``` command.

#### Insomnia Tips
In Insomnia, append any search URI with the specific attribute to be searched 

``` /search?[attribute]=[search_term]```

When searching for a string with spaces, represent the space using ```%20```. 

For example:

```/search?centre_name=Lend%20Lease```

## API Endpoints
All Site Spotter API endpoints are listed below, and in this Google Sheet: https://bit.ly/3JqsZZv

| URI               | METHOD | DETAILS                                                                                   | EXPECTED RESPONSE DATA                                              | AUTHENTICATION                                  |
| ----------------- | ------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------- |
| /landlords/all    | GET    | Retrieve all landlord records                                                             | 200 OK for successful retrieval of record                           | N/A                                             |
| /landlords/id     | GET    | Retrieve specific landlord record based on landlord_id query                              | 200 OK for successful retrieval of record                           | N/A                                             |
| /landlords/id     | GET    | Retrieve specific landlord record based on landlord_id query                              | 404 NOT FOUND if landlord record doesn't exist                      | N/A                                             |
| /landlords/search | GET    | Retrieve specific landlord record based on landlord_name query                            | 200 OK for successful retrieval of record                           | N/A                                             |
| /landlords/search | GET    | Retrieve specific landlord record based on landlord_name query                            | 404 NOT FOUND if landlord record doesn't exist                      | N/A                                             |
| /landlords/create | POST   | Create a new landlord record                                                              | 201 CREATED for successful record creation                          | Only registered users can create a new landlord |
| /landlords/create | POST   | Create a new landlord record                                                              | 404 NOT FOUND if user record doesn't exist                          |                                                 |
| /landlords/update | PUT    | Update landlord record based on landlord_id query                                         | 201 CREATED for successful record update                            | Only registered users can update a landlord     |
| /landlords/update | PUT    | Update landlord record based on landlord_id query                                         | 404 NOT FOUND if user record doesn't exist                          |                                                 |
| /landlords/delete | DELETE | Delete specific landlord record and associated centre record/s based on landlord_id query | 201 CREATED for successful record update                            | Only admin users can delete a landlord          |
| /landlords/delete | DELETE | Delete specific landlord record and associated centre record/s based on landlord_id query | 404 NOT FOUND if user record doesn't exist                          |                                                 |
| /landlords/delete | DELETE | Delete specific landlord record and associated centre record/s based on landlord_id query | 401 UNAUTHORIZED if not admin user                                  |                                                 |
| /centres/all      | GET    | Retrieve all centre records                                                               | 200 OK for successful retrieval of record                           | N/A                                             |
| /centres/id       | GET    | Retrieve specific centre record based on centre_id query                                  | 200 OK for successful retrieval of record                           | N/A                                             |
| /centres/id       | GET    | Retrieve specific centre record based on centre_id query                                  | 404 NOT FOUND if centre record doesn't exist                        | N/A                                             |
| /centres/search   | GET    | Retrieve specific centre record based on centre_name, suburb, postcode, state queries     | 200 OK for successful retrieval of record                           | N/A                                             |
| /centres/search   | GET    | Retrieve specific centre record based on centre_name, suburb, postcode, state queries     | 404 NOT FOUND if centre record doesn't exist                        | N/A                                             |
| /centres/create   | POST   | Create a new centre record                                                                | 201 CREATED for successful record creation                          | Only registered users can create a new centre   |
| /centres/create   | POST   | Create a new centre record                                                                | 404 NOT FOUND if user record doesn't exist                          | N/A                                             |
| /centres/update   | PUT    | Update specific centre record based on centre_id query                                    | 201 CREATED for successful record update                            | Only registered users can update a centre       |
| /centres/update   | PUT    | Update specific centre record based on centre_id query                                    | 404 NOT FOUND if user record doesn't exist                          | N/A                                             |
| /centres/delete   | DELETE | Delete specific centre record and associated site records based on centre_id query        | 201 CREATED for successful record update                            | Only admin users can delete a centre            |
| /centres/delete   | DELETE | Delete specific centre record and associated site records based on centre_id query        | 404 NOT FOUND if user record doesn't exist                          | N/A                                             |
| /centres/delete   | DELETE | Delete specific centre record and associated site records based on centre_id query        | 401 UNAUTHORIZED if not admin user                                  | N/A                                             |
| /sites/all        | GET    | Retrieve all site records                                                                 | 200 OK for successful retrieval of record                           | N/A                                             |
| /sites/id         | GET    | Retrieve specific site record based on site_id query                                      | 200 OK for successful retrieval of record                           | N/A                                             |
| /sites/id         | GET    | Retrieve specific site record based on site_id query                                      | 404 NOT FOUND if site record doesn't exist                          | N/A                                             |
| /sites/search     | GET    | Retrieve specific site record based on size, power, location queries                      | 200 OK for successful retrieval of record                           | N/A                                             |
| /sites/search     | GET    | Retrieve specific site record based on size, power, location queries                      | 404 NOT FOUND if site record doesn't exist                          | N/A                                             |
| /sites/create     | POST   | Create a new site record                                                                  | 201 CREATED for successful record creation                          | Only registered users can create a new site     |
| /sites/create     | POST   | Create a new site record                                                                  | 404 NOT FOUND if user record doesn't exist                          | N/A                                             |
| /sites/update     | PUT    | Update specific site record based on site_id query                                        | 201 CREATED for successful record update                            | Only registered users can update a site         |
| /sites/update     | PUT    | Update specific site record based on site_id query                                        | 404 NOT FOUND if user record doesn't exist                          | N/A                                             |
| /sites/delete     | DELETE | Delete specific site record and associated site records based on site_id query            | 201 CREATED for successful record update                            | Only admin users can delete a site              |
| /sites/delete     | DELETE | Delete specific site record and associated site records based on site_id query            | 404 NOT FOUND if user record doesn't exist                          | N/A                                             |
| /sites/delete     | DELETE | Delete specific site record and associated site records based on site_id query            | 401 UNAUTHORIZED if not admin user                                  | N/A                                             |
| /users/register   | POST   | Create new user record                                                                    | 409 CONFLICT if user is already registered                          | N/A                                             |
| /users/register   | POST   | Create new user record                                                                    | User email and JSON web token on successful user registration       | N/A                                             |
| /users/login      | POST   | Login registered user                                                                     | 401 UNAUTHORIZED if user record doesn't exist or password incorrect | N/A                                             |
| /users/login      | POST   | Login registered user                                                                     | User email and JSON web token on successful user login              | N/A                                             |



## Relationships
### Entity Relationship Diagram (ERD)
![Site Spotter ERD](/images/site_spotter%20API%20ERD.jpg)

Several one-to-many relationships are represented and implemented in the Site Spotter database:
* Landlords, Centres and Sites are associated with one User, but one User can be associated with many Landlords, Centres and Sites.
* One Centre is associated with one Landlord, but one Landlord can be associated with many Centres.
* One Site is associated with one Centre, but one Centre can be associated with many Sites.

### Models
Models were created to define each Site Spotter table name, attributes and relationships with other tables. 
In Flask a model is a class representing a database table, where every class attribute reprsents a table field. For each model, a table name is defined, then attributes are declared including primary and foreign keys, data types and any other constraints.

**Users**  
In the Users model there are standard and admin users who can create and update landlord, centre and site records. Only admin users can delete landlord, centre and site records. Anyone with access to the API can read records.

The ``` back_populates ``` method is used to create the one to many relationship with landlords, centres and sites.
``` 
class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
    landlord = db.relationship("Landlord", back_populates="user")
    centre = db.relationship("Centre", back_populates="user")
    site = db.relationship("Site", back_populates="user") 
```

**Landlords**  
In the Landlords model user_id is set as the foreign key to create the connection between the landlords and users tables. Authentication is used in the landlords controller to ensure only users can create and update 
landlord records, and only admin users can delete landlord records.

The ``` back_populates ``` method is used to create the one to many relationship with users and centres and the cascade delete method associated with the centre relationship ensures that if a landlord is deleted then associated centres will be deleted, maintaining relationship integrity.

```
class Landlord(db.Model):
    __tablename__ = "landlords"
    landlord_id = db.Column(db.Integer, primary_key=True)
    landlord_name = db.Column(db.String(), nullable=False)
    landlord_email = db.Column(db.String())
    landlord_phone = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    user = db.relationship("User", back_populates="landlord")
    centre = db.relationship("Centre", back_populates="landlord", cascade="delete, merge, save-update")
```
**Centres**  
In the Centres model landlord_id and user_id are set as the foreign keys to create the connection between the tables. Authentication is used in the centres controller to ensure only users can create and update 
centre records, and only admin users can delete centre records.

The ``` back_populates ``` method is used to create the one to many relationship with users and landlords and the cascade delete method associated with the site relationship ensures that if a centre is deleted then associated sites will be deleted, maintaining relationship integrity.

```
class Centre(db.Model):
    __tablename__ = "centres"
    centre_id = db.Column(db.Integer(), primary_key=True)
    centre_name = db.Column(db.String(), nullable=False)
    suburb = db.Column(db.String())
    postcode = db.Column(db.String())
    state = db.Column(db.String())
    landlord_id = db.Column(db.Integer, db.ForeignKey("landlords.landlord_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    landlord = db.relationship("Landlord", back_populates="centre", )
    user = db.relationship("User", back_populates="centre")
    site = db.relationship("Site", back_populates="centre", cascade="delete, merge, save-update")
```

**Sites**  
In the Sites model centre_id and user_id are set as the foreign keys to create the connection between the tables. Authentication is used in the sites controller to ensure only users can create and update 
site records, and only admin users can delete site records.

The ``` back_populates ``` method is used to create the one to many relationship with users and centres.

```
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
    user = db.relationship("User", back_populates="site")
    centre = db.relationship("Centre", back_populates="site")
```

## Project Management
The project and associated tasks were allocated and tracked using Trello. View the Trello project board here: https://trello.com/b/6sGcY3EH/sitespotter-api  

The project was broken down into five stages.

1. Initial Planning  
In the initial planning stage a full outline of the tasks and sub-tasks required to complete the project were listed in Trello in order of what was to be actioned and completed first. This ensured no steps were missed and provided a useful guideline for the order of operations.

![Site Spotter project step 1](/images/Step%201%20-%20elements%20to%20be%20started.png)

2. Planning Progress  
The first step, which was the initial approval of the API idea by Coder Academy educators, was critical to moving onto the rest of the project. Upon approval, an API plan was developed including a full problem and solution scope, target users, etc. Then decisions on the database design were made including defining database requirements, table attributes, constraints, relationships, data normalisation and designing an ERD.

![Site Spotter project step 2](/images/Database%20design.png)

3. Development & Testing  
The development and testing stages took the majority of project time. A checklist of development requirements was created to ensure no key steps were missed, and the API met all required planning and code elements. Testing was handled in Insomnia, to ensure the API produced the expected data and error messages.

![Site Spotter project step 3](/images/Development.png)

4. Documentation  
In this stage documentation (README.md) was written containing information about the problem solved by the Site Spotter API, how to set up and use Site Spotter, endpoints and relationships and the project management process.

5. Completion & Submission  
The fifth and final stage was to package up all files and documentation into a .zip file as per the assessment requirements, and submit via Canvas.

## References
Abba, I.V. 2022, What is an ORM – The Meaning of Object Relational Mapping Database Tools, 21 October, viewed 14 March 2023, https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools 

Juba, S, Vannahme, A, & Volkov, A, 2015, Learning PostgreSQL, e-book, Packt Publishing, Birmingham, https://ebookcentral.proquest.com/lib/redhill-ebooks/reader.action?docID=4191180

Hernandez, R 2021, ‘The Model View Controller Pattern – MVC Architecture and Frameworks Explained’, freeCodeCamp, 19 April, viewed 14 March 2023, https://www.freecodecamp.org/news/the-model-view-controller-pattern-mvc-architecture-and-frameworks-explained 

Hristozov, K 2019, ‘MySQL vs PostgreSQL -- Choose the Right Database for Your Project’, Okta Developer, web log post, 19 July, viewed 14 March 2023, https://developer.okta.com/blog/2019/07/19/mysql-vs-postgres 

Panchenko, I 2021, PostgreSQL benefits and challenges: A snapshot, viewed 14 March 2023, https://www.infoworld.com/article/3619531/postgresql-benefits-and-challenges-a-snapshot.html 

Python Basics 2021, What is Flask Python, viewed 14 March 2023, https://pythonbasics.org/what-is-flask-python 

SQLAlchemy 2023, Features and Philosophy, viewed 14 March 2023, https://www.sqlalchemy.org/features.html

The PostgreSQL Global Development Group 2023, About, viewed 14 March 2023, https://www.postgresql.org/about 