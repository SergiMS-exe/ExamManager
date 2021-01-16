from unittest.mock import MagicMock, patch
 
from app.actions import register, addNewGroup, addExam
from app.models import Examiner, Student,ExamGroup
 
 
def test_register_fails_when_user_is_already_registered():
    name, surname, email, password, radioT = 'John', 'Doe', 'john.doe@gmail.com', '123', 'examiner'
    form = register(name, surname, email, password, radioT)
 
    expected_error = 'This email is already registered'
 
    assert form == ('reg.html', expected_error)
 
def test_register_adding_examiner_passes():
    name, surname, email, password, radioT = 'John', 'Doe', 'john.doe@gmail.com', '123', 'examiner'
    form = register(name, surname, email, password, radioT)
 
    assert form == '/teacherpage', None

def test_register_adding_student_passes():
    name, surname, email, password, radioT = 'John', 'Smith', 'john.smith@gmail.com', '123', 'student'
    form = register(name, surname, email, password, radioT)
 
    assert form == '/studentpage', None

# with pytest.raises(ExceptionError) as error:
#     assert error is ...
def test_add_new_group():
    x = len(ExamGroup.query.all())
    addNewGroup("G-1", 111)
    ...
    assert len(ExamGroup.query.all()) == x + 1
 
def test_add_exam_passes():
    currrent_exam_group_len = len(ExamGroup.query.all())
    expected_exam_name = 'CEO training'
    addExam(1, expected_exam_name, ...)
 
    x = ExamGroup.query.all()
 
    assert x[-1].exam_name == expected_exam_name
    assert len(x) == currrent_exam_group_len
 
 
 
#def __init__(self, db):
#    self.db = db
 