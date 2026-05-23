import os

class Config:
  SECRET_KEY = os.environ.get("SECRET_KEY", "my-top-secret-key")
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///entries.db")
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  
  # IF JWT was used
  # JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-top-secret-key')
  # JWT_ACCESS_TOKEN_EXPIRES = 30