# SITE SPOTTER API 

## The Problem
What is the problem
Why is it a problem

## The Solution
Site Spotter is…  a blah blah blah

Trello Link:https://trello.com/b/6sGcY3EH/sitespotter-api 
GitHub Link: https://github.com/KarlaB3/site-spotter-api 

## Tech Stack
Why have you chosen this database system? What are the drawbacks compared to others?
Identify and discuss the key functionalities and benefits of an ORM
Detail any third party services that your app will use - what and why

## How to Set Up the Environment & Use
instructions on how to set up the environment and users.
install all files requirements.txt
create db in postgres
create db_dev user in postgres with password as xyz 
DATABASE_URL = "postgresql+psycopg2://db_dev:123456@localhost:5432/site_spotter"
SECRET_KEY = "s3cr3T_K3Y"
grant all schema privileges to db_dev user, include error handling notes you've used in the past

instructions on how to search in Insomnia, including representing spaces between strings in a record as %20 e.g, Lend%20Lease

## How It Works
Document all endpoints for your API. Endpoint documentation should include: 
HTTP request verb GET POST PUT PATCH DELETE  
Required data where applicable - what each end point achieves e.g. GET brings up a list of CML sites, POST adds a new centre and site. NEED ALL POSSIBLE END POINTS
Expected response data “e.g. incorrect login, please try again” or “tables seeded”
Authentication methods where applicable  
ERD physical with attributes and values (pk/fk, format, syntax, null or not null) - screenshot  
Discuss the database relations to be implemented in your application i.e explain the relationships involved in your database based on an ERD that represents the planned database   
Describe your projects models in terms of the relationships they have with each other i.e. Explain the models and relationships involved in the database based on the Flask / SQLAlchemy / etc code that you've implemented ( based on what you ended up coding in your API.Use terminology appropriate to Flask/SQLAlchemy/etc)  


## Project Management
Describe the way tasks are allocated and tracked in your project  
Public Trello board and link: https://trello.com/b/6sGcY3EH/sitespotter-api   
Explain the project management process:
* Method used - agile methodology
* Priorities 

