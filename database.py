from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv()

db_connection_string = os.environ['DATABASE_URL']

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_users_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from users"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs