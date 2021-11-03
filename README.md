# nieghborhood_search
This is a neighborhood app where a user must signup first, be able to join a hood, one can see businesses and posts in only that wood they belong to.

# Description  
This is a neighborhood app where a user must signup first, be able to join a hood, one can see businesses and posts in only that wood they belong to. 
##  Live Link  
 Click [View Site](https://neighbor00.herokuapp.com/account/login/?next=/)  to visit the site
 
## User Story  
  
* Sign in with the application to start using.
* Set up a profile about you and a general location and your neighborhood name.
* Find a list of different businesses in your neighborhood.
* Find Contact Information for the health department and Police authorities near your neighborhood.
* Create Posts that will be visible to everyone in your neighborhood.
* Change your neighborhood when I decide to move out.
* Only view details of a single neighborhood.
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/Michael-Otieno/nieghborhood_search.git```
##### Navigate into the folder and install requirements  
 ```bash 
cd neighbourhood 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv .venv - source .venv/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations hood
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 2.2.6](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [m.otieno205@gmail.com]  
  
## License 

* Copyright (c) 2019 **Michael-Otieno**
