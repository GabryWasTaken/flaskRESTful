![Flaskrestful](https://cdn.discordapp.com/attachments/733391066136313879/1160249107680604271/FLASK_restful.png?ex=6533f92f&is=6521842f&hm=ecb6362d4e2e3e668e8f11dad557de972965e63a46d97258445737388dde9d17&)

![Logo](https://img.shields.io/badge/Created%20by-GabryWasTaken-red)
## DESCRIPTION
**This RESTful API allows you to:**
* Register a new user by sending name, email and password via the POST /create_user method
* Get user details through the GET /user/<user_id> method
* Get all users with the GET /users method

Representational State Transfer (REST) is an architectural approach for creating web APIs based on the HTTP protocol, it is used for building web services. \
A Restful application is an API that is based on REST. A REST API is used to manipulate a subset of resources by selecting requests from the client to the server that can be of the GET, POST, PUT, and DELETE types.

## PREREQUISITES

![Python3.10](https://img.shields.io/badge/Install-Python%203.10%20or%20greater-blue?link=https%3A%2F%2Fwww.python.org%2Fdownloads%2F) ![sqlite3](https://img.shields.io/badge/install-SQLite3-orange)

Install the external dependencies, they are located in
```bash
requirements.txt
```
## HOW TO RUN PROGRAM

* Install all of the prerequisites in your virtual environment or your machine with the following command:
```bash
pip install -r requirements.txt
```
* Write this command to run the API:
```bash
python3 ./app.py
``` 
* Or : 
```bash
flask run
``` 
if you wanna start the program with flask run you need to set the environment variable with the command:
```bash
set FLASK_APP=app.py
``` 
In another terminal start the request.py to send the various request to the API, with the following command:
```bash
python3 ./request.py
``` 




