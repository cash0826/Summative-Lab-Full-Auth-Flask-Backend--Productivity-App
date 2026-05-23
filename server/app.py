from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_bcrypt import Bcrypt

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)
  app.json.compact = False
  
  db = SQLAlchemy()
  migrate = Migrate(app, db)
  db.init_app(app)
  
  api = Api(app)
  
  bycrypt = Bcrypt(app)
  
  # Resources / Controllers
  # Users
  # Entries
  
  with app.app_context():
    db.create_all()
  
  return app

if __name__ == "__main__":
  app = create_app()
  app.run(debug=True, port=5555)