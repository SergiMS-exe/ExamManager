# pylint: disable=no-member
from flask import Flask, render_template, request, redirect, url_for, flash
from .models import Examiner,Student
import re
from app import db, app

<<<<<<< HEAD



=======
>>>>>>> origin/Sergio
radioT=""

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('reg.html')


@app.route('/teacherpage')
def teacher():
    return render_template('teacherpage.html')


@app.route('/studentpage')
def student():
    return render_template('studentpage.html')

# register data handling
# you can add more logic
@app.route('/handle_data', methods=['POST', 'GET'])
def handle_data():
    name = request.form['Name']
    Surname = request.form['Surname']
    password = request.form['Password']
    repeatPassword = request.form['repeatPassword']
    dob = request.form['dob']
<<<<<<< HEAD
    radioT = request.form['radioT']
    email = request.get["email"]

=======
    email = request.form['email']

    try:
        radioT = request.form['radioT']
    except:
        error = 'You have to choose if you want to register as a student or as a examiner'
        return render_template('reg.html', error=error)

    #regular expression that matches with an email (something@something.something)
    re_email = re.search(r'(^[\w]+)@([\w]+)'+'.com', email)
    if not re_email:
        return render_template('reg.html', error="Please enter a valid E-mail")

    #check if that email cis already registered
    student = Student.query.filter_by(student_email=email).all()
    examiner = Examiner.query.filter_by(examiner_email=email).all()
    if len(student)>0 or len(examiner)>0:
        return render_template('reg.html', error="That E-mail is already registered")
>>>>>>> origin/Sergio

    # create user and add db logic to save data to db
    print(name, Surname, email, password, repeatPassword, dob, radioT)

    if (password != repeatPassword):
        error = 'Passwords mismatch . Please try again.'
        return render_template('reg.html', error=error)
    
<<<<<<< HEAD
        # radioT decides whether user data goes to examiner or student please send data respectively and a assign
        # unique id , please give that id into a variable so that students can know their ids and we can later work
        # with groups
    if radioT == "examiner":
        last_id = Examiner.query.all().last().examiner_id
        my_examiner = Examiner(last_id+1,name,Surname,email,password)
=======
    # radioT decides whether user data goes to examiner or student please send data respectively and a assign
    # unique id , please give that id into a variable so that students can know their ids and we can later work
    # with groups
    if radioT == "examiner":
        last_id = Examiner.query.all()[-1].examiner_id
        my_examiner = Examiner(examiner_id=last_id+1,examiner_name=name,examiner_surname=Surname,
            examiner_email=email,examiner_password=password)
>>>>>>> origin/Sergio
        db.session.add(my_examiner)
        db.session.commit()

        return redirect('/teacherpage')
<<<<<<< HEAD
    elif radioT == "student":
        last_id = Student.query.all().last().student_id
        my_student = Student(last_id+1,name,Surname,email,password)
=======
        
    elif radioT == "student":
        last_id = Student.query.all()[-1].student_id
        my_student = Student(student_id=last_id+1,student_name=name,student_surname=Surname, 
            student_email=email, student_password=password)
>>>>>>> origin/Sergio
        db.session.add(my_student)
        db.session.commit()

        return redirect('/studentpage')
<<<<<<< HEAD
    else:
        error = 'Invalid data. Please try again.'
        return render_template('reg.html', error=error)
=======
>>>>>>> origin/Sergio


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
# add whatever parameters you want
def login():
    error = None
    if request.method == 'POST':
        # check if email/in examiner  table or student table and change redirect
        # request.form['email']  in student then  return redirect('/studentpage')
        # else
<<<<<<< HEAD
        student = Student.query.filter(student_email=request.form['email'])
        examiner = Examiner.query.filter(examiner_email=request.form['email'])
=======
        email = request.form['email']
        student = Student.query.filter_by(student_email=email).all()
        examiner = Examiner.query.filter_by(examiner_email=email).all()
>>>>>>> origin/Sergio
        if len(student)>0:
            return redirect('/studentpage')
        elif len(examiner)>0:
            return redirect('/teacherpage')
        else:
            error = 'Invalid Credentials. Please try again.'
                    
    return render_template('index.html', error=error)
