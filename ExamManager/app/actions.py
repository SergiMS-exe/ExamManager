# pylint: disable=no-member
from app import db, models
from .models import *
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
import re, random
from app import db, app


def register(name, surname, email, password, radioT):
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

        return '/teacherpage/'+str(last_id+1)+"/-1", None
    elif radioT == "student":
        last_id = Student.query.all()[-1].student_id
        my_student = Student(student_id=last_id+1, student_name=name,
                             student_surname=surname, student_email=email, student_password=password)
        db.session.add(my_student)
        db.session.commit()

        return '/studentpage/'+str(last_id+1)+"/-1", None
    else:
        error = 'Invalid data. Please try again.'
        return 'reg.html', error

def login(email, password):
    student = Student.query.filter_by(student_email=email).first()
    examiner = Examiner.query.filter_by(examiner_email=email).first()
    if student != None:
        if student.student_password == password:
            try:
                group_id = StudentExamGroup.query.filter_by(
                    student_id=student.student_id).first().group_id
            except:
                group_id = -1
            return '/studentpage/'+str(student.student_id)+"/"+str(group_id), None
    elif examiner != None:
        if examiner.examiner_password == password:
            try:
                group_id = getGroupsExaminer(examiner.examiner_id)[0].group_id
            except:
                group_id = -1
            return '/teacherpage/'+str(examiner.examiner_id)+"/"+str(group_id), None

    error = 'Invalid Credentials. Please try again.'
    return 'index.html', error


def addExam(group_id, name, date, time):
    date_time = date+' '+time
    date_time_obj = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M')
    last_id = ExamGroup.query.all()[-1].group_id
    exam = models.Exam(
        exam_id=last_id+1,
        exam_name=name,
        exam_date=date_time_obj.date(),
        exam_time=date_time_obj.time(),
        group_id=group_id
        )
    db.session.add(exam)
    db.session.commit()


def addQuestion(exam_id, text, answers):
    my_question_id = ExamQuestion.query.all()[-1].question_id+1
    question = models.ExamQuestion(
        question_id=my_question_id,
        question_text=text,
        exam_id=exam_id
    )
    db.session.add(question)
    last_answer_id = ExamAnswer.query.all()[-1].answer_id

    for key, value in answers.items():
        last_answer_id += 1

        answer = models.ExamAnswer(
            answer_id=last_answer_id+1,
            answer_text=key,
            question_id=my_question_id,
            correct=value
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
        # exam_id=0   # Dummy variable for exam id, should be replaced at some point
    )
    db.session.add(temp)
    db.session.commit()

def getGroupsExaminer(examiner_id):
    # Function that returns a list of exam group objects which has the provided examiner_id
    listGroups = []
    query = db.session.query(models.ExamGroup).filter(
        models.ExamGroup.examiner_id == examiner_id)
    for groups in query:
        temp = models.ExamGroup(
            group_id=groups.group_id,
            group_name=groups.group_name,
            examiner_id=groups.examiner_id,
            # exam_id=groups.exam_id
        )
        listGroups.append(temp)
        db.session.close()
    return listGroups


def getGroupsStudent(student_id):  # added to do more cohesive code
    group = []
    group_ids = StudentExamGroup.query.filter_by(student_id=student_id).all()
    for group_id in group_ids:
        group.append(ExamGroup.query.filter_by(
            group_id=group_id.group_id).first())
    return group


def getGroupById(group_id):  # added to do more cohesive code
    return ExamGroup.query.filter_by(group_id=group_id).first()

def getGroupsStudent(student_id):       #added to do more cohesive code
    group=[]
    group_ids=StudentExamGroup.query.filter_by(student_id=student_id).all()
    for group_id in group_ids:
        group.append(ExamGroup.query.filter_by(group_id=group_id.group_id).first())
    return group
    
def getGroupById(group_id):     #added to do more cohesive code
    return ExamGroup.query.filter_by(group_id=group_id).first()

def getParticipants(my_group_id):
    # Function that returns a list of student objects which is participants of the given exam group
    listParticipants = []
    listIds = []
    groups = StudentExamGroup.query.filter_by(group_id=my_group_id).all()
    for group in groups:
        listIds.append(group.student_id)
    for id in listIds:
        try:
            s = Student.query.filter_by(student_id=id).all()[0]
        except:
            return listParticipants
        temp = models.Student(student_id=s.student_id,
                              student_name=s.student_name,
                              student_surname=s.student_surname,
                              student_email=s.student_email,
                              student_password=s.student_password
                              )
        listParticipants.append(temp)
    return listParticipants

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
    query = ExamAnswer.query.filter_by(question_id=question_id)
    for answer in query:
        temp = models.ExamAnswer(answer_id=answer.answer_id, answer_text=answer.answer_text,
                                 question_id=answer.question_id, correct=answer.correct)
        listAnswers.append(temp)
        db.session.close()
    return listAnswers

def getQuiz(exam_id):
    questions=getQuestions(exam_id)
    quiz={}
    for question in questions:
        answers=getAnswers(question.question_id)
        quiz[question]=answers
    return quiz

def getQuiz(exam_id):
    questions = getQuestions(exam_id)
    quiz = {}
    for question in questions:
        answers = getAnswers(question.question_id)
        quiz[question] = answers
        shuffled=shuffleQuestions(quiz)
    return shuffled


def shuffleQuestions(q):
    keys=list(q.keys())
    random.shuffle(keys)
    return dict([(key, q[key]) for key in keys])


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
    db.session.commit()
    db.session.close()


def studentUpcomingExams(student_id):
    upcoming = []

    query1 = db.session.query(ExamStudent.exam_id).filter_by(
        student_id=student_id).subquery()
    query2 = Exam.query.filter(Exam.exam_date >= datetime.datetime.now()).filter(
        Exam.exam_id.in_(query1)).all()
    for exam in query2:
        upcoming.append(exam)

    return upcoming


def teacherUpcomingExams(examiner_id):
    upcoming = []

    query1 = db.session.query(ExamGroup.group_id).filter_by(
        examiner_id=examiner_id).subquery()
    query2 = Exam.query.filter(Exam.exam_date >= datetime.datetime.now()).filter(
        Exam.group_id.in_(query1)).all()
    for exam in query2:
        upcoming.append(exam)
    return upcoming


def getUserExaminer(examiner_id):  # added to do more cohesive code
    return Examiner.query.filter_by(examiner_id=examiner_id).first()


def getExamParticipants(exam_id):
    return ExamStudent.query.filter_by(exam_id=exam_id).all()


def getUserStudent(student_id):  # added to do more cohesive code
    return Student.query.filter_by(student_id=student_id).first()


def getExams(group_id):  # added to do more cohesive code
    exams = Exam.query.filter_by(group_id=group_id)
    upcoming = []
    done = []
    for exam in exams:
        if exam.exam_date >= datetime.date.today():
            upcoming.append(exam)
        else:
            done.append(exam)
    return done, upcoming


def getExamById(exam_id):  # added to do more cohesive code
    return Exam.query.filter_by(exam_id=exam_id).first()


def getPoints(exam_id, student_id):
    exam_student = ExamStudent.query.filter_by(
        exam_id=exam_id, student_id=student_id).first()
    try:
        return exam_student.grade
    except:
        return -1


def deleteParticipantFromExam(group_id, student_id):
    participant = StudentExamGroup.query.filter_by(
        group_id=group_id, student_id=student_id).first()
    db.session.delete(participant)
    db.session.commit()
    db.session.close()


def deleteExam(group_id, exam_id):
    exam = Exam.query.filter_by(group_id=group_id, exam_id=exam_id).first()
    db.session.delete(exam)
    db.session.commit()
    db.session.close()


def deleteGroup(group_id):

    group = ExamGroup.query.filter_by(group_id=group_id).first()

    exams = Exam.query.filter_by(group_id=group_id).all()
    participants = getParticipants(group_id)

    for exam in exams:
        db.session.delete(exam)

    for participant in participants:
        db.session.delete(participant)

    db.session.delete(group)
    db.session.commit()
    db.session.close()


def saveAnswersFromStudents(exam_id, quiz, student_id):
    for question, answers in quiz.items():
        for answer in answers:
            studentAns = models.StudentAnswer(
                exam_id=exam_id, student_id=student_id, answer_id=answer, question_id=question)
            db.session.add(studentAns)

    db.session.commit()
    db.session.close()


def calculateGrade(student_id, exam_id):
    correct = 0
    quiz=getQuiz(exam_id)
    for question, answers in quiz:
        answerSwtudent = StudentAnswer.query.filter_by(question_id=question.question_id).first()
        for answer in answers:
            if answer.correct and answer.answer_id==answerSwtudent.answer_id:
                correct+=1
    grade = "{}/ {}".format(correct, len(quiz))

    gradeFloat = correct/len(quiz)*5
    print(gradeFloat)

    ExamStudent.update().where(student_id=student_id).values(grade=gradeFloat)

    return grade , gradeFloat
