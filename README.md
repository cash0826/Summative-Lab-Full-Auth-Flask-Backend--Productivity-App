# Summative-Lab-Flask-SQLAlchemy-Workout-Application-Backend
This lab will follow a one-to-many relationship type, since users can be associated to many journal entries

## Installation

Run `pipenv install` to create your virtual environment and install dependencies. 
Run `pipenv shell` to enter the virtual environment.
run `npm install --prefix client-with-sessions` to install node dependencies for the frontend.

```bash
pipenv install && pipenv shell
npm install --prefix client-with-sessions
```

Change to the Server directory and configure the the Flask App environment variables:
```bash
cd server
export FLASK_APP=app.py
export FLASK_RUN_PORT=5555
```
Use set instead of export if on Window OS

To get create the database from the initial migration, run:

```bash
flask db upgrade
python seed.py
```
To open and view the backend, make sure that you are in the server directory and run:
```bash
python app.py
```

Run React in another terminal from the project root directory with:

```bash
npm start --prefix client-with-sessions
```

# API Endpoints

Authentication:
* GET /check_session
* POST /signup
* POST /login
* DELETE /logout
* DELETE /clear_session

Protected sources:
* GET /<resource>
* POST /<resource>
* PATCH /<resource>/<id>
* DELETE /<resource>/<id>
