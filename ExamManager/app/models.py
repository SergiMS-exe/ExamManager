from app import db

class Examiner(db.Model):
    examiner_id = db.Column(db.Integer, primary_key=True)
    examiner_name = db.Column(db.String(255))
    examiner_surname = db.Column(db.String(255))
    examiner_email = db.Column(db.String(255), unique=True)
    examiner_password = db.Column(db.String(255))

    def __repr__(self):
        return #add representation

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(255))
    student_surname = db.Column(db.String(255))
    student_email = db.Column(db.String(255), unique=True)
    student_password = db.Column(db.String(255))

    def __repr__(self):
        return #add representation

class Exam(db.Model):
    exam_id = db.Column(db.Integer, primary_key=True)
    exam_date = db.Column(db.Date)
    group_id = db.Column(db.Integer, db.ForeignKey(ExamGroup.group_id))

    def __repr__(self):
        return #add representation

class ExamGroup(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(255))
    examiner_id = db.Column(db.Integer, db.ForeignKey(Examiner.examiner_id))
    exam_id = db.Column(db.Integer, db.ForeignKey(Exam.exam_id))

    def __repr__(self):
        return #add representation

class ExamStudent(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey(Student.student_id), primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey(Exam.exam_id), primary_key=True)
    grade = db.Column(db.Float)

    def __repr__(self):
        return #add representation

class ExamQuestion(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String)
    exam_id = db.Column(db.Integer, db.ForeignKey(Exam.exam_id))

    def __repr__(self):
        return #add representation

class ExamAnswer(db.Model):
    answer_id = db.Column(db.Integer, primary_key=True)
    answer_text = db.Column(db.String)
    question_id = db.Column(db.Integer, db.ForeignKey(ExamQuestion.question_id))

    def __repr__(self):
        return #add representation

class StudentAnswer(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey(ExamStudent.student_id), primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey(ExamStudent.exam_id), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey(ExamQuestion.question_id), primary_key=True)
    answer_id = db.Column(db.Integer, db.ForeignKey(ExamAnswer.answer_id), primary_key=True)

    def __repr__(self):
        return #add representation

class StudentExamGroup(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey(Student.student_id), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey(ExamGroup.group_id), primary_key=True)

    def __repr__(self):
        return #add representation

