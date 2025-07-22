from sqlalchemy import create_engine,text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine=create_engine(db_connection_string )

def load_clubs_from_db():
  with engine.connect() as conn:
      result = conn.execute(text("SELECT * FROM clubs"))

      clubs = []
      for row in result.all():
          clubs.append(dict(row._mapping))
      return clubs

def load_club_from_db(id):
  with engine.connect() as conn:
      result = conn.execute(text("SELECT * FROM clubs WHERE id = :val"),{"val":id})

      rows=result.all()

      if len(rows)==0:
        return None
      else:
        return dict(rows[0]._mapping)


def add_application_to_db(club_id, data):
  with engine.begin() as conn:
    query = text("""
      INSERT INTO applications(club_id, name, stud_id, phone, email, why_join) 
      VALUES (:club_id, :name, :stud_id, :phone, :email, :why_join)
    """)
    conn.execute(query, {
      "club_id": club_id,
      "name": data['name'],
      "stud_id": data['stud-id'],
      "phone": data['phone'],
      "email": data['mail'],
      "why_join": data['why-join']
    })




