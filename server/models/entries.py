from config import db
from marshmallow import Schema, fields
from .users import UserSchema

class Entry(db.Model):
  __tablename__ = "entries"
  
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date, nullable=False)
  first_line = db.Column(db.String(30), 
                         db.CheckConstraint('length(first_line) <= 30'), 
                         nullable=False)
  mood = db.Column(db.String, nullable=True)
  text = db.Column(db.Text)
  
  # Foreign Key to store Journal Entry
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  
  # Relationship Mapping: One-to-Many
  user = db.relationship('User', back_populates='entries')
  
class EntrySchema(Schema):
  id = fields.Int
  date = fields.Date(format="%Y-%m-%d")
  first_line = fields.Str(load_default='Empty Entry', dump_default="Empty Entry")
  mood = fields.Str(load_default="Reflective", dump_default="Reflective")
  
  user = fields.Nest(UserSchema(exclude=("entries",)))