# pylint: disable=no-member
from app import db, models
import datetime

<<<<<<< HEAD

=======
>>>>>>> origin/Sergio
def saveExam(exam_id,exam_name,exam_date,exam_time,duration,group_id,questions,answers):
    myExam = models.Exam(exam_id=exam_id,exam_name = exam_name, exam_date=datetime.datetime.combine(exam_date,exam_time),duration = duration, group_id=group_id)
    # if db.session.query(Exam).filter(
    db.session.add(myExam)
    for question in questions:
        try:
            db.session.add(question)
        except Exception as e:
            print(e)
    for answer in answers:
        try:
            db.session.add(answer)
        except Exception as e:
            print(e)
    db.session.commit()
    # ok = db.session.query(models.Exam).filter(models.Exam.exam_id== exam_id)
    # for u in ok:
    #    print(u.exam_id, u.exam_date)
    
def modifyExam():
    pass





def test():
    questions=[models.ExamQuestion(question_text="who is the president of USA?", exam_id=1202100001),
        models.ExamQuestion(
        question_id=15, question_text="who is Chloe Malujlo Jr?", exam_id=1202100001)]
    answers=[models.ExamAnswer(answer_text="Donald Trump", question_id=13, correct=True),
                   models.ExamAnswer( answer_text="Andrzej Dupa", question_id=13),
                   models.ExamAnswer(answer_text="Marvin Gerald", question_id=13),
                   models.ExamAnswer(answer_text="Andrzej Duda ", question_id=13),
                   models.ExamAnswer(answer_text="CEO of IBM", question_id=15),
                   models.ExamAnswer(answer_text="Great PM in Project Software Eng.", question_id=15., correct=True),
                   models.ExamAnswer(answer_text="Teacher at PWR", question_id=15),
                   models.ExamAnswer(answer_text="Great PM in Project Software Eng.", question_id=15),
                   models.ExamAnswer(
                       answer_id=100, answer_text="Cleaning Lady in mercure Hotel", question_id=2)]
    group_id =12
    saveExam(exam_id=1202100009,exam_name="Math Test",exam_date= datetime.date(year=2022,month= 8,day= 14,),exam_time=datetime.time(hour=14,minute=25,second=0) , duration= datetime.time(1, 30, 0), group_id=group_id,questions=questions,answers=answers)
    





test()