from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
import os 

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app=app)

from app import views,models
if os.path.exists('./Exammanager/app.db'):
        os.remove('./Exammanager/app.db')
        print("Old Database removed.")
from app import db_create
from app import default
from app import actions