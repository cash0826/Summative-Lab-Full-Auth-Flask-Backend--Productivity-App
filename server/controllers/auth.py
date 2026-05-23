from sqlite3 import IntegrityError
from config import db
from flask_restful import Resource
from flask import request, session
from models.users import User, UserSchema

# /signup POST
class Signup(Resource):
  def post(self):
    request_json = request.get_json()
    
    email = request_json.get('email')
    password = request_json.get('password')
    image_url = request_json.get('image_url')
    
    user = User(email=email, image_url=image_url)
    user.password_hash = password
    
    try:
      db.session.add(user)
      db.session.commit()
      session['user_id'] = user.id
      return UserSchema().dump(user), 201
    except IntegrityError:
      return {'error': '422 Unprocessable Entity'}, 422

# /check_session GET
class CheckSession(Resource):
  def get(self):
    if session.get('user_id'):
      user = User.query.filter_by(id=session['user_id']).first()
      return UserSchema().dump(user), 200
    else:
      return {'error': '401 Unauthorized'}, 401

# /login POST
class Login(Resource):
  def post(self):
    request_json = request.get_json()
    email = request_json.get('email')
    password = request_json.get('password')
    
    user = User.query.filter_by(email=email).first()
    
    if user and user.authenticate(password):
      session['user_id'] = user.id
      return UserSchema().dump(user), 200
    else:
      return {'error': '401 Unauthorized'}, 401

# /logout DELETE
class Logout(Resource):
  def delete(self):
    if session.get('user_id'):
      session['user_id'] = None
      return {}, 204
    else:
      return {'error': '401 Unauthorized'}, 401