from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
import os
<<<<<<< HEAD
=======

>>>>>>> origin/Sergio
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app=app)

from app import views, models
<<<<<<< HEAD
if os.path.exists('./Exammanager/app.db'):
    os.remove('./Exammanager/app.db')
from app import db_create, default, actions
=======
#import app.views
if os.path.exists('./Exammanager/app.db'):
    os.remove('./Exammanager/app.db')
from app import db_create, default, actions
>>>>>>> origin/Sergio
