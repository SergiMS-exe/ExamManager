# pylint: disable=no-member
from flask import Flask, render_template, request, redirect, url_for, flash
from .models import Examiner, Student, ExamGroup, StudentExamGroup
import re
from app import db, app, actions
from .extra_classes import Template_Group


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
# check if email/in examiner  table or student table and change redirect
def login():
    error = None
    if request.method == 'POST':
        next_page, error = actions.login(
            request.form['email'], request.form['password'])
        if error == None:
            return redirect(next_page)
    return render_template('index.html', error=error)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['Name']
        surname = request.form['Surname']
        password = request.form['Password']
        repeatPassword = request.form['repeatPassword']
        dob = request.form['dob']
        email = request.form['email']

        # check if at least one radio button is selected
        try:
            radioT = request.form['radioT']
        except:
            error = 'You have to choose if you want to register as a student or as an examiner'
            return render_template('reg.html', error=error)

        # create user and add db logic to save data to db
        print(name, surname, email, password, repeatPassword, dob, radioT)

        if (password != repeatPassword):
            error = 'Passwords mismatch . Please try again.'
            return render_template('reg.html', error=error)

        next_page, error = actions.register(
            name, surname, email, password, radioT)

        if error == None:
            return redirect(next_page)
        else:
            return render_template(next_page, error=error)

    else:
        return render_template('reg.html')


@app.route('/teacherpage/<examiner_id>', methods=['GET', 'POST'])
def teacher(examiner_id):
    if request.method == 'POST':
        if request.form['btn-creategroup'] == 'Add New Group':
            groupName = request.form['inp-groupname']
            actions.addNewGroup(groupName, examiner_id)
            # actions.getGroups(examiner_id)

            return redirect('/teacherpage/'+str(examiner_id))

    user = Examiner.query.filter_by(examiner_id=examiner_id).first()
    groups = ExamGroup.query.filter_by(examiner_id=examiner_id).all()
    return render_template('teacherpage.html', user=user, examGroup=groups)


@app.route('/teacherpage/<examiner_id>/<group_id>/editexam', methods=['GET', 'POST'])
def editexam(examiner_id, group_id):
    if request.method == 'POST':
        print(examiner_id, group_id)
    user = Examiner.query.filter_by(examiner_id=examiner_id).first()
    group = ExamGroup.query.filter_by(group_id=group_id).first()
    """ user= 
    group_id=
        exam_id = """
    return render_template('editexam.html', user=user)


@app.route('/studentpage/<student_id>/<group_id>/exam')
def exam():
    return render_template('exam.html')


@app.route('/studentpage/<student_id>', methods=['POST', 'GET'])
def student(student_id):
    user = Student.query.filter_by(student_id=student_id).first()
    studentExamGroups = StudentExamGroup.query.filter_by(
        student_id=student_id).all()
    examgroups = []
    for examGroup in studentExamGroups:
        examgroups.append(ExamGroup.query.filter_by(
            group_id=examGroup.group_id).first())
    groups = []
    """for i in examgroups:
        Examiner.query.filter_by
        groups.append(Template_Group(i.group_id, i.group_name, )) """
    return render_template('studentpage.html', user=user)
