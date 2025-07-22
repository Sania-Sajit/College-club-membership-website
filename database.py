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






