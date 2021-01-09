from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
import os
from app import views, models
from app import db_create, default, actions

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app=app)

if os.path.exists('./Exammanager/app.db'):
    os.remove('./Exammanager/app.db')
