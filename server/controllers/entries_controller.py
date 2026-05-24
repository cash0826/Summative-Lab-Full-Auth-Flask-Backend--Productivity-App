from sqlite3 import IntegrityError
from config import db
from flask_restful import Resource
from flask import request, session
from models.entries import Entry, EntrySchema

# global variable to help with memory
entry_schema = EntrySchema()

# Entries GET / POST / PATCH / DELETE
class Entries_Controller(Resource):
  
  # GET /entries
  def get(self):
    # Adding Pagination
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    entries = Entry.query.filter_by(user_id=session['user_id']).paginate(page=page, per_page=per_page, error_out=False)
    return {
      "pages": entries.pages,
      "per_page": entries.per_page,
      "total": entries.total,
      "total_pages": entries.pages,
      "items": [entry_schema.dump(entry) for entry in entries.items]
    }
  
  # POST /entries
  def post(self):
    request_json = request.get_json()
    
    try:
      entry = Entry(
        date=request_json.get('date'),
        first_line=request_json.get('first_line'),
        mood=request_json.get('mood'),
        text=request_json.get('text')
      )
      
      entry.user_id = session['user_id']
      
      db.session.add(entry)
      db.session.commit()
      
      return entry_schema.dump(entry), 201
    except IntegrityError:
      return {'error': '422 Unprocessable Entity'}, 422
    
  # PATCH /entries/<id>
  def patch(self, id):
    request_json = request.get_json()
    
    entry = Entry.query.filter_by(id=id, user_id=session['user_id']).first()
    
    if entry:
      for key in request_json:
        setattr(entry, key, request_json[key])
      
      db.session.commit()
      
      return entry_schema.dump(entry), 200
    else:
      return {'error': '404 Not Found'}, 404
  
  # DELETE /entries/<id>
  def delete(self, id):
    entry = Entry.query.filter_by(id=id, user_id=session['user_id']).first()
    
    if entry:
      db.session.delete(entry)
      db.session.commit()
      
      return {}, 204
    else:
      return {'error': '404 Not Found'}, 404
  