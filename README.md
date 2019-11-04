# Neighbourhood Watch
# Description
a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

# Technologies used
- Python 3.6
- HTML
- Bootstrap 3
- Heroku
- Postgresql
- Django

# Setup and installations
## Prerequisites
Python3.6
virtualenv
Pip

# Setting up environment variables
Create a .env file and paste paste the following filling where appropriate:

- SECRET_KEY='<YOUR_SECRET_KEY_HERE>
- DEBUG=True #set to false in production
- DB_NAME=<YOUR_DATA_BASE_NAME>
- DB_USER=<YOUR_DATA_BASE_USER>
- DB_PASSWORD=<YOUR_DATA_BASE_PASSWORD>
- DB_HOST='127.0.0.1'
- MODE='dev' #set to 'prod' in production
- ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
- DISABLE_COLLECTSTATIC=1

# Install dependancies
## Install dependancies that will create an environment for the app to run

- pip install -r requirements.txt
- Run migrations
- python manage.py migrate
- Run the app
- python manage.py runserver


# Contact
If you run into any issues or have questions, ideas or concerns. Contact me or make a contribution to the code. Email :agasarojulia@gmail.com ,Github username:Julia-Agasaro.

# Built With
Python3.6 - Python is a programming language that lets you work quickly and integrate systems more effectively Django - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design postgresql - PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance. Versioning version 1.0.0
Versioning
We use SemVer for versioning. For the versions available, see the tags on this repository.

# Authors
## Julia Agasaro

# License
This project is licensed under the MIT License -

# Acknowledgments
Moringa School
