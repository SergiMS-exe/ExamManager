from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app=app)

from app import views,models,default