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
    groups = actions.getGroupsExaminer(examiner_id)
    exams= actions.getExams(group_id)
    group_name=""
    user = actions.getUserExaminer(examiner_id) 
    if group_id!="-1" :
        group_name= actions.getGroupById(group_id).group_name
    participants=actions.getParticipants(group_id)
    if request.method == 'POST':
        try:
            if request.form['btn-creategroup'] == 'Add New Group':
                groupName = request.form['inp-groupname']
                actions.addNewGroup(groupName, examiner_id)
                return redirect('/teacherpage/'+str(examiner_id)+"/"+str(group_id))
        except:
            pass
        for group in groups:
            try:
                if request.form['deleteGroup']==group.group_name:
                    actions.deleteGroup(group.group_id)
                    group=actions.getGroupsExaminer(examiner_id)[0].group_id
                    return redirect('/teacherpage/'+str(examiner_id)+"/-1")
            except:
                pass
            try:
                if request.form['GroupButton'] == group.group_name:
                    return redirect('/teacherpage/'+str(examiner_id)+"/"+str(group.group_id))
            except:
                pass
        try:
            if request.form['buttonExam'] == 'Add New Exam':
                return redirect("/teacherpage/"+str(examiner_id)+"/"+str(group_id)+"/editexam")
        except:
            pass
        try:
            if request.form['AddParticipant'] == "Add":
                student_id = request.form['ParticipantId']
                actions.addParticipantToExam(group_id, student_id)
                return render_template('teacherpage.html', user=user, examGroup=groups,participants=participants, group_id=group_id, group_name=group_name)
        except:
            pass
        for exam in exams:
            try:
                if request.form['delete']==exam.exam_name:
                    actions.deleteExam(exam.exam_id)
                    return redirect('/teacherpage/'+str(examiner_id)+"/"+str(group_id))
            except:
                pass
        try:
            if request.form['filter']=="Upcoming Exams":
                return render_template('teacherpage.html', user=user, examGroup=groups,exams=exams, group_id=group_id, group_name=group_name)
            if request.form['filter']=="Participants":
                return render_template('teacherpage.html', user=user, examGroup=groups,participants=participants, group_id=group_id, group_name=group_name)
            if request.form['filter']=="Results":
                return render_template('teacherpage.html', user=user, examGroup=groups,exams=exams, group_id=group_id, group_name=group_name)
        except:
            pass
   
    return render_template('teacherpage.html', user=user, examGroup=groups, exams=exams, group_id=group_id, group_name=group_name)

@app.route('/teacherpage/<examiner_id>/<group_id>/editexam', methods=['GET', 'POST'])
def editexam(examiner_id, group_id):  # FUNTIONAL
    if request.method == 'POST':
        try:
            if request.form['SaveExam'] == 'SUBMIT EXAM':
                name = request.form['examname']
                date = request.form['examdate']
                time = request.form['examtime']
                actions.addExam(group_id=group_id, name=name, date=date, time=time)
                return redirect("/teacherpage/"+str(examiner_id)+"/"+str(group_id))
        except:
            pass
    user = actions.getUserExaminer(examiner_id)
    group = actions.getGroupById(group_id)
    return render_template('editexam.html', user=user, examgroup=group)

@app.route('/teacherpage/<examiner_id>/<group_id>/<exam_id>/editexam_questions', methods=['GET', 'POST'])
def editQuestions(examiner_id, group_id, exam_id): #FUNTIONAL
    if request.method == 'POST':
        try:
            if request.form["questionAction"]=="x":
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
            if request.form['questionAction']=="Save and exit":                
                return redirect('/teacherpage/'+str(examiner_id)+"/"+str(group_id))
            if request.form['questionAction']=="Save and next":        
                return redirect('/teacherpage/'+str(examiner_id)+"/"+str(group_id)+"/"+str(exam_id)+"/editexam_questions")
        except:
            pass
    user = actions.getUserExaminer(examiner_id)
    exam = actions.getExamById(exam_id)
    return render_template('editexam-question.html', user=user, exam=exam)

@app.route('/exam/<exam_id>/<student_id>', methods=['POST', 'GET'])
def exam(exam_id,student_id):
    user=actions.getUserStudent(student_id)
    return render_template('exam.html', user=user)

@app.route('/studentpage/<student_id>/<group_id>', methods=['POST', 'GET'])
def student(student_id,group_id): #FUNTIONAL
    examgroups = []
    exams=[]
    results=[]
    groups=actions.getGroupsStudent(student_id)
    user = actions.getUserStudent(student_id)
    studentExamGroups = StudentExamGroup.query.filter_by(student_id=student_id).all() #complete
    for examGroup in studentExamGroups:
        examgroups.append(ExamGroup.query.filter_by(group_id=examGroup.group_id).first()) #complete
        if str(examGroup.group_id)==str(group_id):
            results,exams=actions.getExams(group_id)
    if request.method == 'POST':
        try:
            if request.form['btn-futureexams'] == 'Upcoming Exams':
                option='Upcoming'
                return render_template('studentpage.html', user=user, examgroups=examgroups,exams=exams, group_id=group_id, option=option)
            if request.form['btn-futureexams'] == 'Results':
                option='Results'
                return render_template('studentpage.html', user=user, examgroups=examgroups,results=results, group_id=group_id, option=option)
        except:
            print("error")
        for group in groups:
            try:
                if request.form['GroupButton'] == group.group_name:
                    return redirect('/studentpage/'+str(student_id)+"/"+str(group.group_id)+"/"+str(option))
            except:
                pass
        for exam in exams:    
            try:
                if request.form['btn-takeexam']==exam.exam_name:
                    return redirect("/exam/"+str(exam.exam_id)+"/"+str(student_id))
            except:
                pass    
    return render_template('studentpage.html', user=user, examgroups=examgroups,exams=exams, group_id=group_id)
