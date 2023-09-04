import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from the .env file
load_dotenv()

# Get the database connection URL from the environment variables
db_url = os.getenv("DATABASE_URL")

# Create the SQLAlchemy engine
engine = create_engine(db_url, echo=True)
