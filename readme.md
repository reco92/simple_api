

# Python/Django Challenge

## Description
This is a simple project to implement a endpoint to convert a number into english words.

Included a Postman collection to can test


## IMPORTANT: How to run the project

* Create a virtualenv: `python -m venv virtualenv` and activate it `. virtualenv/bin/activate`.
* Install dependencies: `pip install -r requirements.txt`
* Setup DB: `cd simple_api ; ./manage.py migrate`
* Start the api service: `cd simple_api ; ./manage.py runserver 0.0.0.0:8000`
* Can use a Postman client to test, collection and enviroment provided in the folder `PostmanCollection`. Ensure to setup in the imported enviroment the variables `username` and `password` with the same values you created your superuser or any other user you have.
* In the postman collection first use the endpoint `Request Token` to get credentials.
