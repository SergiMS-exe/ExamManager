import os
rewrite = False
if os.path.exists('./Exammanager/app.db') and rewrite !=True:
    os.remove('./Exammanager/app.db')
    rewrite = True
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app=app)

from app import views, models
from app import db_create, default
from app import actions