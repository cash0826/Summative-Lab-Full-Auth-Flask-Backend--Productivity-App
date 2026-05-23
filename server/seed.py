from random import randint, choice as rc
from faker import Faker
from app import app, db

from users import User
from entries import Entry

fake = Faker()

with app.app_context():
  # Delete all rows in current tables
  print("Deleting all records...")
  User.query.delete()
  Entry.query.delete()
  
  # Creating admin
  print("Creating admin and 1 user...")
  admin = User(email="admin@journalentries.com", image_url="https://preview.redd.it/i-bought-a-tie-for-our-cat-so-he-would-fit-in-better-at-our-v0-sn6p92gm6jt01.jpg?auto=webp&s=2e76ace1637e33bded98bb8535f9898e4fadfadd")
  me = User(email="melanie@journalentries.com", image_url="https://media.licdn.com/dms/image/v2/D4E03AQGt_3oMjXhXeA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1718269730908?e=1781136000&v=beta&t=1Ipz6MwBK7657VUWgE2Zx42erzsFqYXzHAtwmMo8Ku0")
  
  admin.password_hash = 'adminpassword'
  me.password_hash = 'mepassword'
  
  db.session.add(admin, me)
  db.session.commit()
  
  # Creating entries
  print("Creating journal entries...")
  entries = []
  for i in range(50):
    text = fake.paragraph(nb_sentences=8)
    
    entry = Entry(
      date=fake.date(),
      first_line=fake.sentence(),
      mood='',
      text=text
    )
    
    entry.user = rc(admin, me)
    entries.append(entry)
  
  db.session.add_all(entries)
  db.sesion.commit()
  print("Complete.")
  