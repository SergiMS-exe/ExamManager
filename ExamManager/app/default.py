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
    ExamStudents = [models.ExamStudent(student_id=251567, exam_id=1202100001, grade=5),
                    models.ExamStudent(student_id=251452,
                                       exam_id=1202100002, grade=4),
                    models.ExamStudent(student_id=251234,
                                       exam_id=1202100001, grade=3),
                    models.ExamStudent(student_id=251236,
                                       exam_id=1202100003, grade=4.5),
                    models.ExamStudent(student_id=251235, exam_id=1202100005, grade=0)]
    ExamQuestions = [models.ExamQuestion(
        question_id=1, question_text="who is the president of poland?", exam_id=1202100001),
        models.ExamQuestion(
        question_id=2, question_text="who is Chloe Malujlo?", exam_id=1202100001),
        models.ExamQuestion(
        question_id=3, question_text="what is Python ?", exam_id=1202100001),
        models.ExamQuestion(
        question_id=4, question_text="what is JavaScript?", exam_id=1202100001),
        models.ExamQuestion(
        question_id=5, question_text="who is MarK Zuckerberg?", exam_id=1202100002),
        models.ExamQuestion(
        question_id=6, question_text="what is DDR in IT?", exam_id=1202100004),
        models.ExamQuestion(
        question_id=7, question_text="what is Edx?", exam_id=1202100004),
        models.ExamQuestion(
        question_id=8, question_text="Is java a Script Language?", exam_id=1202100002),
        models.ExamQuestion(
        question_id=9, question_text="Where is located Poland?", exam_id=1202100001),
        models.ExamQuestion(
        question_id=10, question_text="What is a DVD", exam_id=1202100003),
        models.ExamQuestion(
        question_id=11, question_text="What is the meaning of CD", exam_id=1202100003),
        models.ExamQuestion(question_id=12, question_text="What is A LED", exam_id=1202100003)]

    ExamAnswers = [models.ExamAnswer(answer_id=1, answer_text="Donald Trump", question_id=1),
                   models.ExamAnswer(
                       answer_id=2, answer_text="Andrzej Dupa", question_id=1),
                   models.ExamAnswer(
                       answer_id=3, answer_text="Marvin Gerald", question_id=1),
                   models.ExamAnswer(
                       answer_id=4, answer_text="Andrzej Duda ", question_id=1, correct=True),
                   models.ExamAnswer(
                       answer_id=5, answer_text="CEO of IBM", question_id=2),
                   models.ExamAnswer(
                       answer_id=6, answer_text="Police Officer", question_id=2),
                   models.ExamAnswer(
                       answer_id=7, answer_text="Teacher at PWR", question_id=2),
                   models.ExamAnswer(
                       answer_id=8, answer_text=" Great PM in Project Software Eng.", question_id=2, correct=True),
                   models.ExamAnswer(
                       answer_id=9, answer_text="Cleaning Lady in mercure Hotel", question_id=2),
                   models.ExamAnswer(
                       answer_id=10, answer_text="Programming Language", question_id=3, correct=True),
                   models.ExamAnswer(
                       answer_id=11, answer_text="type of Dog", question_id=3),
                   models.ExamAnswer(
                       answer_id=12, answer_text="Streaming Video website", question_id=3),
                   models.ExamAnswer(
                       answer_id=13, answer_text="Computer HardWare", question_id=3),
                   models.ExamAnswer(
                       answer_id=14, answer_text="Programming Language", question_id=4, correct=True),
                   models.ExamAnswer(
                       answer_id=15, answer_text="A mailBox name", question_id=4),
                   models.ExamAnswer(
                       answer_id=16, answer_text="It is a Company", question_id=4),
                   models.ExamAnswer(
                       answer_id=17, answer_text="CEO pwr", question_id=5),
                   models.ExamAnswer(
                       answer_id=18, answer_text="Facebook Inventor", question_id=5, correct=True),
                   models.ExamAnswer(
                       answer_id=19, answer_text="Car seller in Poland", question_id=5),
                   models.ExamAnswer(
                       answer_id=20, answer_text=" Great PM in Project Software Eng.", question_id=5),
                   models.ExamAnswer(
                       answer_id=21, answer_text="Polish Singer ", question_id=5),
                   models.ExamAnswer(
                       answer_id=22, answer_text="DDR (Double Data Rate) is a type of fast, expensive, volatile Random Access Memory (RAM)", question_id=6 , correct=True),
                   models.ExamAnswer(
                       answer_id=23, answer_text="Digital Directory Register", question_id=6),
                   models.ExamAnswer(
                       answer_id=24, answer_text="Doubled Digged Repository ", question_id=6),
                   models.ExamAnswer(
                       answer_id=25, answer_text="A Web Browser", question_id=6),
                   models.ExamAnswer(
                       answer_id=26, answer_text="Russian Social Network ", question_id=7),
                   models.ExamAnswer(
                       answer_id=27, answer_text="elearnmig Platform", question_id=7, correct=True),
                   models.ExamAnswer(
                       answer_id=28, answer_text="Ethernet Dx", question_id=7),
                   models.ExamAnswer(
        answer_id=29, answer_text="Electronic Component", question_id=7),
        models.ExamAnswer(
        answer_id=30, answer_text="No,But allow to write scripts", question_id=8, correct=True),
        models.ExamAnswer(answer_id=31, answer_text="yes", question_id=8),
        models.ExamAnswer(
            answer_id=32, answer_text="Programming Language", question_id=8),
        models.ExamAnswer(
            answer_id=33, answer_text="No, It a markup language", question_id=8),
        models.ExamAnswer(
            answer_id=34, answer_text="In Africa", question_id=9),
        models.ExamAnswer(
            answer_id=35, answer_text="In America", question_id=9),
        models.ExamAnswer(
            answer_id=36, answer_text="In Europe", question_id=9, correct=True),
        models.ExamAnswer(answer_id=37, answer_text="In Asia", question_id=9),
        models.ExamAnswer(
            answer_id=38, answer_text="Dangerous Vibes Direction", question_id=10),
        models.ExamAnswer(
            answer_id=39, answer_text="Digital Versatile Disc", question_id=10, correct=True),
        models.ExamAnswer(
            answer_id=40, answer_text="Dom Version D", question_id=10),
        models.ExamAnswer(
            answer_id=41, answer_text="Dealers in sector VD", question_id=10),
        models.ExamAnswer(
            answer_id=42, answer_text="Circular Diagram", question_id=11),
        models.ExamAnswer(
            answer_id=43, answer_text="China Direction", question_id=11),
        models.ExamAnswer(
            answer_id=44, answer_text="Compact Disk", question_id=11, correct=True),
        models.ExamAnswer(
            answer_id=45, answer_text="Light Ellicitation Diagram", question_id=12),
        models.ExamAnswer(
            answer_id=46, answer_text="Electoric Coponent made of Secmi-Conductors", question_id=12, correct=True),
        models.ExamAnswer(
            answer_id=47, answer_text="Windos comand", question_id=12),
        models.ExamAnswer(answer_id=48, answer_text="Java IDE", question_id=12)]

    StudentAnswers = [models.StudentAnswer(
        student_id=251567, exam_id=1202100001, question_id=1, answer_id=4),
        models.StudentAnswer(
            student_id=251567, exam_id=1202100001, question_id=2, answer_id=8),
        models.StudentAnswer(
            student_id=251567, exam_id=1202100001, question_id=3, answer_id=10),
        models.StudentAnswer(
            student_id=251567, exam_id=1202100001, question_id=4, answer_id=1),
        models.StudentAnswer(student_id=251452, exam_id=1202100001, question_id=1, answer_id=1)]

    StudentExamGroups = [models.StudentExamGroup(student_id=251567, group_id=1),
                         models.StudentExamGroup(student_id=251452, group_id=1)]
    for exam in Exams:
        db.session.add(exam)

    # db.session.commit()
    # eTest = models.Exam.query.all()
    # for u in eTest:
    #     print(u.exam_id, u.exam_date)
    # db.session.commit()
    for student in Students:
        db.session.add(student)

    for examiner in Examiners:
        db.session.add(examiner)

    for examGroup in ExamGroups:
        db.session.add(examGroup)

    for examStudent in ExamStudents:
        db.session.add(examStudent)
    for examQuestion in ExamQuestions:
        db.session.add(examQuestion)

    for examAnswer in ExamAnswers:
        db.session.add(examAnswer)
    for studentAnswer in StudentAnswers:
        db.session.add(studentAnswer)

    for studentExamGroup in StudentExamGroups:
        db.session.add(studentExamGroup)
    eTest = models.Exam.query.all()
    # for u in eTest:
    #     print(u.exam_id, u.exam_date, u.duration)
    db.session.commit()


run()
