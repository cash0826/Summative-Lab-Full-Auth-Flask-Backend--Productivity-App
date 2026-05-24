from random import randint, choice as rc
from faker import Faker
from config import app, db

from models import User, Entry

fake = Faker()

with app.app_context():
  # Delete all rows in current tables
  print("Deleting all records...")
  User.query.delete()
  Entry.query.delete()
  
  # Creating admin
  print("Creating admin and 1 user...")
  
  seeded_users = []
  
  admin = User(email="admin@email.com",
               image_url="https://preview.redd.it/i-bought-a-tie-for-our-cat-so-he-would-fit-in-better-at-our-v0-sn6p92gm6jt01.jpg?auto=webp&s=2e76ace1637e33bded98bb8535f9898e4fadfadd")
  me = User(email="melanie@email.com", 
            image_url="https://media.licdn.com/dms/image/v2/D4E03AQGt_3oMjXhXeA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1718269730908?e=1781136000&v=beta&t=1Ipz6MwBK7657VUWgE2Zx42erzsFqYXzHAtwmMo8Ku0")
  
  admin.password_hash = 'adminpassword'
  seeded_users.append(admin)
  me.password_hash = 'melaniepassword'
  seeded_users.append(me)
  
  db.session.add_all(seeded_users)
  db.session.commit()
  
  # Creating entries
  print("Creating journal entries...")
  entries = []
  for i in range(50):
    mood = rc(['happy', 'sad', 'angry', 'anxious', 'excited', 'content'])
    text = fake.paragraph(nb_sentences=randint(3, 10))
    
    entry = Entry(
      date=fake.date_object(),
      first_line=fake.sentence(),
      mood=mood,
      text=text
    )
    
    entry.user = rc(seeded_users)
    entries.append(entry)
  
  db.session.add_all(entries)
  db.session.commit()
  print("🌱 Database Seeded Successfully!")
  