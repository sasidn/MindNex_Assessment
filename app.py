import os
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from the .env file
load_dotenv()

# Get the database connection URL from the environment variables
db_url = os.getenv("DATABASE_URL")

# Create the SQLAlchemy engine
engine = create_engine(db_url,connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}
})
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('questionaire.html')


if __name__ == '__main__':
    app.run(debug=True)