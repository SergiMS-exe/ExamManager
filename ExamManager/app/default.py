# pylint: disable=no-member
from app import db, models
import datetime


def run():
    Examiners = [models.Examiner(examiner_id=2021001, examiner_name="Chloe Vann der", examiner_surname="Sar", examiner_email="chloe.vann.der.sar@gmail.com", examiner_password="jjjjj"),
                 models.Examiner(examiner_id=2021002, examiner_name="vassita ", examiner_surname="volgov ",
                                 examiner_email="vassitavolgov1@gmail.com", examiner_password="jjjjj"),
                 models.Examiner(examiner_id=2021003, examiner_name="Aleksey ", examiner_surname="Volkov",
                                 examiner_email="AlekseyVolkov@gmail.com", examiner_password="jjjjj"),
                 models.Examiner(examiner_id=2021004, examiner_name="Mounim ",
                                 examiner_surname="Mouani", examiner_email="Mounimmouani@gmail.com", examiner_password="jjjjj"),
                 models.Examiner(examiner_id=2021005, examiner_name="Monsif ", examiner_surname="Chouini",
                                 examiner_email="Monsif Chouini@gmail.com", examiner_password="jjjjj"),
                 models.Examiner(examiner_id=2021006, examiner_name="Edward",
                                 examiner_surname=" McBell", examiner_email="EdwardMcBell@gmail.com", examiner_password="jjjjj"),
                 models.Examiner(examiner_id=2021007, examiner_name="Paula ", examiner_surname="Kimberly",
                                 examiner_email="PaulaKimberly@gmail.com", examiner_password="jjjjj"),
                 models.Examiner(examiner_id=2021008, examiner_name="Bill ", examiner_surname="Kim",
                                 examiner_email="BillKim@gmail.com", examiner_password="jjjjj"),
                 models.Examiner(examiner_id=2021009, examiner_name="Wiiliam ", examiner_surname="GeorgeTown",
                                 examiner_email="WiiliamGeorgeTown@gmail.com", examiner_password="jjjjj"),
                 models.Examiner(examiner_id=2021010, examiner_name="Michael ", examiner_surname="Scofield",
                                 examiner_email="Michael Scofield@gmail.com", examiner_password="jjjjj"),
                 models.Examiner(examiner_id=20210011, examiner_name="Lincoln ", examiner_surname="Burrows",
                                 examiner_email="Lincoln Burrows@gmail.com", examiner_password="jjjjj"),
                 models.Examiner(examiner_id=20210012, examiner_name="Aleksander ", examiner_surname="Mahone",
                                 examiner_email="AleksanderMahone@gmail.com", examiner_password="jjjjj"),
                 models.Examiner(examiner_id=20210013, examiner_name="Paul ", examiner_surname="Killerman",
                                 examiner_email="PaulKillerman@gmail.com", examiner_password="jjjjj"),
                 models.Examiner(examiner_id=20210014, examiner_name="David ",
                                 examiner_surname="Ballern", examiner_email="DavidBallern@gmail.com"),
                 models.Examiner(examiner_id=20210015, examiner_name="Sergio ", examiner_surname="Suarez", examiner_email="SergioSuarez@gmail.com", examiner_password="jjjjj")]

    Students = [models.Student(student_id=251567, student_name="Edouard Makenga", student_surname="Badibake", student_email="edouardmkakenga0@gmail.com", student_password="kkkkk"),
                models.Student(student_id=251452, student_name="Maxime ", student_surname="LeBlanc",
                               student_email="MaximeLeBlanc@gmail.com", student_password="kkkkk"),
                models.Student(student_id=251230, student_name="Peter", student_surname="LeRusse",
                               student_email="PeterLeRusse0@gmail.com", student_password="kkkkk"),
                models.Student(student_id=251231, student_name="Avril ", student_surname="Lavigne",
                               student_email="AvrilLavigne0@gmail.com", student_password="kkkkk"),
                models.Student(student_id=251232, student_name="Marvin ", student_surname="Mcfadden",
                               student_email="MarvinMcfadden0@gmail.com", student_password="kkkkk"),
                models.Student(student_id=251233, student_name="Natasha ", student_surname="Kooper",
                               student_email="NatashaKooper@gmail.com", student_password="kkkkk"),
                models.Student(student_id=251234, student_name="Ed",
                               student_surname="Sheeran", student_email="EdSheeran@gmail.com", student_password="kkkkk"),
                models.Student(student_id=251235, student_name="Bob ",
                               student_surname="Marley", student_email="BobMarley@gmail.com", student_password="kkkkk"),
                models.Student(student_id=251236, student_name="Piotr ", student_surname="Fabianski",
                               student_email="PiotrFabianski@gmail.com", student_password="kkkkk"),
                models.Student(student_id=251237, student_name="Dead ",
                               student_surname="Poll", student_email="DeadPoll@gmail.com", student_password="kkkkk"),
                models.Student(student_id=251238, student_name="Luna ",
                               student_surname="Tuna", student_email="LunaTuna@gmail.com", student_password="kkkkk"),
                models.Student(student_id=251239, student_name="Carlos ",
                               student_surname="Moreli", student_email="CarlosMoreli.com", student_password="kkkkk"),
                models.Student(student_id=251455, student_name="Xing xi ", student_surname="ji ping", student_email="Xingzijiping@gmail.com", student_password="kkkkk")]

    Exams = [models.Exam(exam_id=1202100001, exam_date=datetime.date(2021, 5, 14), group_id=1),
             models.Exam(exam_id=1202100002, exam_date=datetime.date(
                 2021, 3, 14), group_id=2),
             models.Exam(exam_id=1202100003, exam_date=datetime.date(
                 2021, 1, 14), group_id=3),
             models.Exam(exam_id=1202100004, exam_date=datetime.date(
                 2021, 7, 14), group_id=5),
             models.Exam(exam_id=1202100005, exam_date=datetime.date(
                 2021, 8, 14), group_id=4),
             models.Exam(exam_id=1202100006, exam_date=datetime.date(2021, 8, 14), group_id=6)]

             
    ExamGroups = [models.ExamGroup(group_id=1, group_name="G--1", examiner_id=2021010, exam_id=1202100001),
                 models.ExamGroup(group_id=2, group_name="G--2",
                                  examiner_id=2021010, exam_id=1202100002),
                 models.ExamGroup(group_id=3, group_name="G--3",
                                  examiner_id=2021009, exam_id=1202100003),
                 models.ExamGroup(group_id=4, group_name="G--4",
                                  examiner_id=2021004, exam_id=1202100006),
                 models.ExamGroup(group_id=5, group_name="G--5",
                                  examiner_id=2021011, exam_id=1202100003),
                 models.ExamGroup(group_id=6, group_name="G--6", examiner_id=2021010, exam_id=1202100004)]
    
    # db.session.flush()
    # for exam in Exams:
    #     db.session.add(exam)

    # # # db.session.commit()
    # # # eTest = models.Exam.query.all()
    # # # for u in eTest:
    # # #     print(u.exam_id, u.exam_date)
    # # # db.session.commit()
    # for student in Students:
    #     db.session.add(student)
    # for examiner in Examiners:
    #     db.session.add(examiner)
    # for examGroup in ExamGroups:
    #     db.session.add(examGroup)
    
    eTest = models.ExamGroup.query.all()
    for u in eTest:
        print(u.group_id, u.group_name,u.examiner_id)

    db.session.commit()
run()
