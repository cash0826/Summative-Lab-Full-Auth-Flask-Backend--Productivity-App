from flask import request, session
from flask_restful import Resource
from config import app, api
from controllers.auth import Signup, CheckSession, Login, Logout
from controllers.entries import Entries

@app.before_request
def check_if_logged_in():
  open_access = ['signup', 'check_session', 'login']
  if (request.endpoint) not in open_access and (not session.get('user_id')):
    return {'error': '401 Unauthorized'}, 401

# Resources / Controllers
api.add_resource(Signup, '/signup')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(Entries, '/entries')

if __name__ == "__main__":
  app.run(debug=True, port=5555)