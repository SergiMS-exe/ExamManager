# pylint: disable=no-member
from app import db, models
from .models import *
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
import re
from app import db, app


def register(name, surname, email, password, radioT): #FUNCTIONAL
    # check if that the user is already registered
    student = Student.query.filter_by(
        student_email=request.form['email']).all()
    examiner = Examiner.query.filter_by(
        examiner_email=request.form['email']).all()

    if len(student) > 0 or len(examiner) > 0:
        error = 'This email is already registered'
        return 'reg.html', error

    # radioT decides whether user data goes to examiner or student please send data respectively and a assign
    # unique id , please give that id into a variable so that students can know their ids and we can later work
    # with groups

    if radioT == "examiner":
        last_id = Examiner.query.all()[-1].examiner_id
        my_examiner = Examiner(examiner_id=last_id+1, examiner_name=name,
                               examiner_surname=surname, examiner_email=email, examiner_password=password)
        db.session.add(my_examiner)
        db.session.commit()

        return '/teacherpage/'+str(last_id+1)+'/-1', None
    elif radioT == "student":
        last_id = Student.query.all()[-1].student_id
        my_student = Student(student_id=last_id+1, student_name=name,
                             student_surname=surname, student_email=email, student_password=password)
        db.session.add(my_student)
        db.session.commit()

        return '/studentpage'+str(last_id+1)+'/-1', None
    else:
        error = 'Invalid data. Please try again.'
        return 'reg.html', error


def login(email, password): # FUNCTIONAL
    student = Student.query.filter_by(student_email=email).first()
    examiner = Examiner.query.filter_by(examiner_email=email).first()
    if student != None:
        if student.student_password == password:
            return '/studentpage/'+str(student.student_id), None
    elif examiner != None:
        if examiner.examiner_password == password:
            try:
                group_id=getGroups(examiner.examiner_id)[0].group_id
            except:
                group_id=-1
            return '/teacherpage/'+str(examiner.examiner_id)+"/"+str(group_id), None

    error = 'Invalid Credentials. Please try again.'
    return 'index.html', error

def addExam(group_id, name, date, time): #I think we won't need exam duration, so complicated
    last_id = ExamGroup.query.all()[-1].group_id
    exam = models.Exam(
        exam_id=last_id+1, 
        exam_name = name,
        exam_date=date,
        exam_time = time,
        group_id=group_id
        )
    db.session.add(exam)
    db.session.commit()

def addQuestion(exam_id, text, answers):
    my_question_id = ExamQuestion.query.all()[-1].question_id+1
    question = models.ExamQuestion(
        question_id = my_question_id,
        question_text = text,
        exam_id = exam_id
    )
    db.session.add(question)
    last_answer_id = ExamAnswer.query.all()[-1].answer_id

    for key, value in answers.items():
        last_answer_id+=1
        
        answer = models.ExamAnswer(
            answer_id = last_answer_id+1,
            answer_text = key,
            question_id = my_question_id,
            correct = value
        )    
        db.session.add(answer)
    
    db.session.commit()


def addNewGroup(group_name, examiner_id):
    # Function to add a new examgroup object to the db
    last_id = ExamGroup.query.all()[-1].group_id
    temp = models.ExamGroup(
        group_id=last_id+1,
        group_name=group_name,
        examiner_id=examiner_id,
        #exam_id=0   # Dummy variable for exam id, should be replaced at some point
    )
    db.session.add(temp)
    db.session.commit()
    return last_id+1


def getGroups(examiner_id):
    # Function that returns a list of exam group objects which has the provided examiner_id
    listGroups = []
    query = db.session.query(models.ExamGroup).filter(
        models.ExamGroup.examiner_id == examiner_id)
    for groups in query:
        temp = models.ExamGroup(
            group_id=groups.group_id,
            group_name=groups.group_name,
            examiner_id=groups.examiner_id,
            #exam_id=groups.exam_id
        )
        listGroups.append(temp)
        db.session.close()
    return listGroups
# getGroups(2021010)

# add new group linking


# @app.route('/newGroup', methods=['GET', 'POST'])
def newGroup():
    groupName = request.form["inp-groupname"]
    print(groupName)
    examinerID = ""
    # please get the right examiner id of the current user
    # uncomment the bottom lines
    #addNewGroup(groupName , examinerID)
    #examGroup = getGroups(examinerID)

    # there is for loop inside the html file that will show groupinstance divs
    # return redirect('teacherpage', examGroup)
    # divs as soon as they are passed in here , check their attribues please


def getParticipants(my_group_id):
    # Function that returns a list of student objects which is participants of the given exam group
    listParticipants = []
    listIds = []
    groups = StudentExamGroup.query.filter_by(group_id=my_group_id).all()
    for group in groups:
        listIds.append(group.student_id)
    for id in listIds:
        s = Student.query.filter_by(student_id=id).all()[0]
        temp = models.Student(student_id=s.student_id,
                              student_name=s.student_name,
                              student_surname=s.student_surname,
                              student_email=s.student_email,
                              student_password=s.student_password
                              )
        listParticipants.append(temp)
    return listParticipants
# getParticipants(1)


def getQuestions(exam_id):
    listQuestions = []
    query = db.session.query(models.ExamQuestion).filter(
        models.ExamQuestion.exam_id == exam_id)
    for question in query:
        temp = models.ExamQuestion(question_id=question.question_id, question_text=question.question_text,
                                   exam_id=question.exam_id, question_point=question.question_point)
        listQuestions.append(temp)
        db.session.close()
    return listQuestions


def getAnswers(question_id):
    listAnswers = []
    query = db.session.query(models.ExamAnswer).filter(
        models.ExamAnswer.question_id == question_id)
    for answer in query:
        temp = models.ExamAnswer(answer_id=answer.answer_id, answer_text=answer.answer_text,
                                 question_id=answer.question_id, correct=answer.correct)
        listAnswers.append(temp)
        db.session.close()
    return listAnswers


def saveExam(exam_name, exam_date, exam_time, duration, group_id, questions, answers, exam_id=None):
    myExam = None
    if exam_id == None:
        myExam = models.Exam(exam_name=exam_name, exam_date=datetime.datetime.combine(
            exam_date, exam_time), duration=duration, group_id=group_id)
    else:
        myExam = models.Exam(exam_id=exam_id, exam_name=exam_name, exam_date=datetime.datetime.combine(
            exam_date, exam_time), duration=duration, group_id=group_id)
    db.session.merge(myExam)
    for question in questions:
        try:
            db.session.merge(question)
        except Exception as e:
            print(e)
    for answer in answers:
        try:
            db.session.merge(answer)
        except Exception as e:
            print(e)
    db.session.commit()



def editExam(exam_id):
    query = db.session.query(models.Exam).filter(
        models.Exam.exam_id == exam_id)
    exam = None
    for e in query:
        val = models.Exam(exam_id=e.exam_id, exam_name=e.exam_name,
                          exam_date=e.exam_date, duration=e.duration, group_id=e.group_id)
        exam = val
    db.session.close()
    listQuestions = getQuestions(exam_id)
    listAnswers = []
    for question in listQuestions:
        answers = getAnswers(question.question_id)
        for ans in answers:
            listAnswers.append(ans)

    return [exam, listQuestions, listAnswers]


def addParticipantToExam(group_id, student_id):
    # Function to add a new student to the StudentExamGroup
    temp = models.StudentExamGroup(group_id=group_id, student_id=student_id)
    db.session.add(temp)
    """query = db.session.query(models.StudentExamGroup).filter(
        models.StudentExamGroup.group_id == group_id)
    for groups in query:
        print(groups.student_id)"""
    db.session.close()
# addParticipantToExam(student_id=251566, group_id=1)


"""def test():
    questions = [models.ExamQuestion(question_text="who is the president of USA?", exam_id=1202100009),
                 models.ExamQuestion(
        question_id=15, question_text="who is Chloe Malujlo Jr?", exam_id=1202100009)]
    answers = [models.ExamAnswer(answer_text="Donald Trump", question_id=13, correct=True),
               models.ExamAnswer(answer_text="Andrzej Dupa", question_id=13),
               models.ExamAnswer(answer_text="Marvin Gerald", question_id=13),
               models.ExamAnswer(answer_text="Andrzej Duda ", question_id=13),
               models.ExamAnswer(answer_text="CEO of IBM", question_id=15),
               models.ExamAnswer(
        answer_text="Great PM in Project Software Eng.", question_id=15., correct=True),
        models.ExamAnswer(answer_text="Teacher at PWR", question_id=15),
        models.ExamAnswer(
        answer_text="Great PM in Project Software Eng.", question_id=15),
        models.ExamAnswer(
        answer_id=100, answer_text="Cleaning Lady in mercure Hotel", question_id=2)]
    group_id = 12
    saveExam(exam_id=1202100009, exam_name="Math Test", exam_date=datetime.date(year=2022, month=8, day=14,), exam_time=datetime.time(
        hour=14, minute=25, second=0), duration=datetime.time(1, 30, 0), group_id=group_id, questions=questions, answers=answers)

    values = editExam(1202100001)
    exam = values[0]
    saveExam(exam_id=exam.exam_id, exam_name=exam.exam_name, exam_date=exam.exam_date, exam_time=exam.exam_date.time(
    ), duration=exam.duration, group_id=exam.group_id, questions=values[1], answers=values[2])
    saveExam(exam_id=exam.exam_id, exam_name=exam.exam_name, exam_date=exam.exam_date, exam_time=exam.exam_date.time(
    ), duration=exam.duration, group_id=exam.group_id, questions=values[1], answers=values[2])


test()
"""
