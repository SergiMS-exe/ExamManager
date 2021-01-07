from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app=app)

from app import default,views,db_create,db_migrate,db_upgrade,db_downgrade

def login(username, password):
    