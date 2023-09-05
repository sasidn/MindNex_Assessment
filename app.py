from flask import Flask, render_template, jsonify, request
from database import load_users_from_db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('questionaire.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)