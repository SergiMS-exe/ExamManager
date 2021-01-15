from app import db, models
from .models import ExamGroup, Exam, StudentExamGroup, Student
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from .models import Examiner, Student
import re
from app import db, app
import random
import copy

# retrieve from db
original_questions = {" 1.where is something located ": ["this is the answer ", "this is option something", "this is some toher option", 'other'],
                      " 2.where is something located ": ["this is the answer ", "this is option something", "this is some toher option", 'other'],
                      " 3.where is something located ": ["this is the answer ", "this is option something", "this is some toher option", 'other']}

questions = copy.deepcopy(original_questions)


def shuffle(q):
    """
    This function is for shuffling 
    the dictionary elements.
    """
    selected_keys = []
    i = 0
    while i < len(q):
        current_selection = random.choice(q.keys())
        if current_selection not in selected_keys:
            selected_keys.append(current_selection)
            i = i+1
    return selected_keys


@app.route('/studentpage/<student_id>')# I have to add exam_id
def quiz():
    questions_shuffled = shuffle(questions)
    for i in questions.keys():
        random.shuffle(questions[i])
    return render_template("/exam", q=questions_shuffled, o=questions)


@app.route('studentpage/<student_id>/<group_id>/<exam_id>', methods=['POST'])
def exam_answers():
    correct = 0
    for i in questions.keys():
        answered = request.form[i]
        if original_questions[i][0] == answered:
            correct = correct+1
            result = "{} / {}".format(correct, len(questions))

    return render_template("/studentpage/<student_id>", result=result)
