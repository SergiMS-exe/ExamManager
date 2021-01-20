import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
import time
rewrite = False
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app=app)

from app import views, models

print("""Choose application mode:
                1) Client 
                2) Server Admin
                0) exit""")
chosen = input("Your choice: ")
print("___________________________________________________________________________________")
if chosen == "1":
    if os.path.exists('./Exammanager/app.db') == False:
        from app import db_create
        from app import default
elif chosen == "2":
    if os.path.exists('./Exammanager/app.db'):
        os.remove('./Exammanager/app.db')
    rewrite = True
    from app import db_create
    from app import test
    time.sleep(4)
    print("Unit test Done ,Please check the log file!")
    exit(0)
elif chosen == "0":
    exit(0)
else:
    print("Incorrect choice. Rerun")
    print("___________________________________________________________________________________")
from app import actions