from app import db, bcrypt
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from marshmallow import Schema, fields
from entries import EntrySchema

class User(db.Model):
  __tablename__= "users"
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, unique=True, nullable=False)
  _password_hash = db.Column(db.String, nullable=False)
  image_url = db.Column(db.String)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)
  
  entries = db.relationship('Entry', back_populates='user')
  
  # Validate Email
  @validates('email')
  def validate_email(self, key, address):
    if not isinstance(address, str):
      raise ValueError("Email must be a string.")
    if len(address) > 35:
      raise ValueError("Email too long.")
    if '@' not in address:
      raise ValueError("Email must have a '@' in the address.")
  
  # Validate Password and Password Properties
  @hybrid_property
  def password_hash(self):
    raise AttributeError("Password hashes may not be viewed")
  
  @password_hash.setter
  def password_hash(self, password):
    password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
    self._password_hash = password_hash.decode('utf-8')
    
  def authenticate(self, password):
    # check_password is doing a lot of heavy lifting here:
    # it generates a salt, appends it and validates it
    return bcrypt.check_password(self._password_hash, password.encode('utf-8'))
  
class UserSchema(Schema):
  id = fields.Int()
  username = fields.String()
  
  entries = fields.List(fields.Nested(lambda: EntrySchema(exclude=("user",))))