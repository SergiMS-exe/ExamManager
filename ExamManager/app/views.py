# pylint: disable=no-member
from flask import Flask, render_template, request, redirect, url_for, flash
from .models import Examiner, Student, ExamGroup, StudentExamGroup, Exam
import re
from app import db, app, actions
from .extra_classes import Template_Group


import datetime


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
# check if email/in examiner  table or student table and change redirect
def login():  # FUNTIONAL
    error = None
    if request.method == 'POST':
        next_page, error = actions.login(
            request.form['email'], request.form['password'])
        if error == None:
            return redirect(next_page)
    return render_template('index.html', error=error)


@app.route('/register', methods=['POST', 'GET'])
def register():  # FUNTIONAL
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


@app.route('/teacherpage/<examiner_id>/<group_id>', methods=['GET', 'POST'])
def teacher(examiner_id, group_id):  # FUNTIONAL
    groups = actions.getGroups(examiner_id)
    if request.method == 'POST':
        try:
            if request.form['btn-creategroup'] == 'Add New Group':
                groupName = request.form['inp-groupname']
                last_id=actions.addNewGroup(groupName, examiner_id)
                return redirect('/teacherpage/'+str(examiner_id)+"/"+str(last_id))
            for group in groups:
                if request.form['GroupButton'] == group.group_name:
                    return redirect('/teacherpage/'+str(examiner_id)+"/"+str(group.group_id))
            if request.form['buttonExam'] == 'Add New Exam':
                return redirect("/teacherpage/"+str(examiner_id)+"/"+str(group_id)+"/editexam")
            if request.form['AddParticipant'] == "Add":
                student_id = request.form['ParticipantId']
                actions.addParticipantToExam(group_id, student_id)
                return redirect('/teacherpage/'+str(examiner_id)+"/"+str(group_id))    
        except:
            pass

    user = Examiner.query.filter_by(examiner_id=examiner_id).first()
    exams = Exam.query.filter_by(group_id=group_id)
    return render_template('teacherpage.html', user=user, examGroup=groups, exams=exams, group_id=group_id)


@app.route('/teacherpage/<examiner_id>/<group_id>/editexam', methods=['GET', 'POST'])
def editexam(examiner_id, group_id):  # FUNTIONAL
    print(1)
    if request.method == 'POST':
        try:
            print(2)
            if request.form['SaveExam'] == 'SUBMIT EXAM':
                print(3)
                name = request.form['examname']
                print(4)
                date = request.form['examdate']
                print(5)
                time = request.form['examtime']
                print(6)
                actions.addExam(group_id=group_id, name=name, date=date, time=time)
                print('Im ok')
                return redirect(url_for("teacher",examiner_id=examiner_id,group_id=group_id))
        except:
            pass
    user = Examiner.query.filter_by(examiner_id=examiner_id).first()
    group = ExamGroup.query.filter_by(group_id=group_id).first()
    return render_template('editexam.html', user=user, examgroup=group)


@app.route('/teacherpage/<examiner_id>/<group_id>/<exam_id>/editexam_questions', methods=['GET', 'POST'])
def editQuestions(examiner_id, group_id, exam_id): #FUNTIONAL
    if request.method == 'POST':
        try:
            if request.form["delete"]=="x":
                return redirect('/teacherpage/'+str(examiner_id)+"/"+str(group_id))
            answer = ord(request.form['foo'])
            answer=int(answer)-97
            question = request.form['question']
            options=[]
            optionA = request.form['in-answerA']
            options.append(optionA)
            optionB = request.form['in-answerB']
            options.append(optionB)
            optionC = request.form['in-answerC']
            options.append(optionC)
            optionD = request.form['in-answerD']
            options.append(optionD)
            answers={}
            for i in range(4):
                if(i==answer):
                    answers[options[i]]=True
                else:
                    answers[options[i]]=False
            actions.addQuestion(exam_id,question,answers)
            if request.form['saveQuestion']=="Save and exit":
                return redirect('/teacherpage/'+str(examiner_id)+"/"+str(group_id))
            if request.form['saveQuestion']=="Save and next":
                return redirect('/teacherpage/'+str(examiner_id)+"/"+str(group_id)+"/"+str(exam_id)+"/editexam_questions")
        except:
            pass
    user = Examiner.query.filter_by(examiner_id=examiner_id).first()
    exam = Exam.query.filter_by(exam_id=exam_id).first()
    return render_template('editexam-question.html', user=user, exam=exam)


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
    return render_template('studentpage.html', user=user, examgroups=examgroups)
