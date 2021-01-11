# pylint: disable=no-member
from flask import Flask, render_template, request, redirect, url_for, flash
from .models import Examiner,Student
import re
from app import db, app




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

@app.route('/editexam')
def editexam():
    return render_template('editexam.html')

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
    email = request.form['email']

    #check if at least one radio button is selected
    try: 
        radioT = request.form['radioT']
    except:
        error = 'You have to choose if you want to register as a student or as an examiner'
        return render_template('reg.html', error=error)


    # create user and add db logic to save data to db
    print(name, Surname, email, password, repeatPassword, dob, radioT)

    #check if that e a
    student = Student.query.filter_by(student_email=request.form['email']).all()
    examiner = Examiner.query.filter_by(examiner_email=request.form['email']).all()
    if len(student)>0 or len(examiner)>0:
        error = 'This email is already registered'
        return render_template('reg.html', error=error)

    if (password != repeatPassword):
        error = 'Passwords mismatch . Please try again.'
        return render_template('reg.html', error=error)
    
    # radioT decides whether user data goes to examiner or student please send data respectively and a assign
    # unique id , please give that id into a variable so that students can know their ids and we can later work
    # with groups
    if radioT == "examiner":
        last_id = Examiner.query.all()[-1].examiner_id
        my_examiner = Examiner(last_id+1,name,Surname,email,password)
        db.session.add(my_examiner)
        db.session.commit()

        return redirect('/teacherpage')
    elif radioT == "student":
        last_id = Student.query.all()[-1].student_id
        my_student = Student(last_id+1,name,Surname,email,password)
        db.session.add(my_student)
        db.session.commit()

        return redirect('/studentpage')
    else:
        error = 'Invalid data. Please try again.'
        return render_template('reg.html', error=error)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
# add whatever parameters you want
def login():
    error = None
    if request.method == 'POST':
        # check if email/in examiner  table or student table and change redirect
        # request.form['email']  in student then  return redirect('/studentpage')
        # else
        student = Student.query.filter_by(student_email=request.form['email']).all()
        examiner = Examiner.query.filter_by(examiner_email=request.form['email']).all()
        if len(student)>0:
            return redirect('/studentpage')
        elif len(examiner)>0:
            return redirect('/teacherpage')
        else:
            error = 'Invalid Credentials. Please try again.'
                    
    return render_template('index.html', error=error)
