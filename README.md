# SITE SPOTTER API 
Site Spotter is a web application that lists casual leasing sites in shopping centres across Australia. The Site Spotter web API allows for user access to create, read, update and delete records in the Site Spotter PostgreSQL database containing retail property landlord, shopping centre and casual leasing site records.

##  Links
GitHub Link: https://github.com/KarlaB3/site-spotter-api   
Trello Project Link: https://trello.com/b/6sGcY3EH/sitespotter-api   

## The Problem
The signing of long term lease deals between retailers and shopping centre landlords has declined since COVID-19. During this period many retailers were forbidden to trade due to mandatory lockdowns but still pay rent, impacting their ability to generate income and in some cases putting them into debt or forcing them to shut down operations altogether.

Many retailers are now wary to commit to long term lease deals spanning over years, preferring shorter term arrangements. This has caused many shopping centre landlords to refocus their efforts on attracting retailers to their centres by offering casual leases. 

Casual lease sites are typically listed on individual shopping centre websites, and teams of leasing executives are employed by landlords to proactively approach and sell these sites to retailers. On the flipside, retailers must contact individual landlords and shopping centres to enquire about casual leasing sites. This creates additional effort on the part of both landlords and retailers to find relevant sites for casual lease.

## The Solution
Site Spotter has been designed to take the work out of finding and selling casual leasing sites by aggregating a database of shopping centre landlords, retailers and sites across Australia. 

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

### Flask-SQLAlchemy

key functionalities
benefits

### Marshmallow

### Flask-JWT-Extended

### Flask-Bcrypt

### psycopg2

### Other
* VS Code
* Ubuntu
* Insomnia

## How to Set Up and Use Site Spotter
instructions on how to set up the environment and users.
install all files requirements.txt
create db in postgres
create db_dev user in postgres with password as xyz 
DATABASE_URL = "postgresql+psycopg2://db_dev:123456@localhost:5432/site_spotter"
SECRET_KEY = "s3cr3T_K3Y"
grant all schema privileges to db_dev user, include error handling notes you've used in the past

instructions on how to search in Insomnia, including representing spaces between strings in a record as %20 e.g, Lend%20Lease
append any search URI with /search?[attribute]= then enter search term - note it must be as entered exactly in the database for Insomnia to return expected data
users you can use for authentication testing:
admin user
{
	"email": "admin@sitespotter.com.au",
	"password": "admin111"
}

standard user
{
	"email": "user1@sitespotter.com.au",
	"password": "user1111"
}

## How It Works
Document all endpoints for your API. Endpoint documentation should include: 
HTTP request verb GET POST PUT PATCH DELETE  
Required data where applicable - what each end point achieves e.g. GET brings up a list of CML sites, POST adds a new centre and site. NEED ALL POSSIBLE END POINTS
Expected response data “e.g. incorrect login, please try again” or “tables seeded”  when deleting landlord, centre still exists, when deleting centre, site must be deleted
Authentication methods where applicable:
    Admin users - CUD - any admin user can perform these functions as long as they're an administrator
    Standard users - CU - any user can perform these functions as long as they're a user
    Anyone can R 

ERD physical with attributes and values (pk/fk, format, syntax, null or not null) - screenshot  

Discuss the database relations to be implemented in your application i.e explain the relationships involved in your database based on an ERD that represents the planned database 

Describe your projects models in terms of the relationships they have with each other i.e. Explain the models and relationships involved in the database based on the Flask / SQLAlchemy / etc code that you've implemented ( based on what you ended up coding in your API.Use terminology appropriate to Flask/SQLAlchemy/etc)  


## Project Management
Describe the way tasks are allocated and tracked in your project  
Public Trello board and link: https://trello.com/b/6sGcY3EH/sitespotter-api   
Explain the project management process:
* Method used - agile methodology
* Priorities 
what else?

## References
Juba, S, Vannahme, A, & Volkov, A, 2015, Learning PostgreSQL, e-book, Packt Publishing, Birmingham, https://ebookcentral.proquest.com/lib/redhill-ebooks/reader.action?docID=4191180

Hernandez, R 2021, ‘The Model View Controller Pattern – MVC Architecture and Frameworks Explained’, freeCodeCamp, 19 April, viewed 8 February 2023, https://www.freecodecamp.org/news/the-model-view-controller-pattern-mvc-architecture-and-frameworks-explained 

Hristozov, K 2019, ‘MySQL vs PostgreSQL -- Choose the Right Database for Your Project’, Okta Developer, web log post, 19 July, viewed 8 February 2023, https://developer.okta.com/blog/2019/07/19/mysql-vs-postgres 

Panchenko, I 2021, PostgreSQL benefits and challenges: A snapshot, viewed 8 February 2023, https://www.infoworld.com/article/3619531/postgresql-benefits-and-challenges-a-snapshot.html 

Python Basics 2021, What is Flask Python, viewed 8 February 2023, https://pythonbasics.org/what-is-flask-python 

The PostgreSQL Global Development Group 2023, About, viewed 8 February 2023, https://www.postgresql.org/about 