from django.db import models

# Create your models here.

class Examiner(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=40)
    email=models.EmailField()
    password=models.CharField()

    class Meta:
        verbose_name='examiner'
        verbose_name_plural='examiners'

class Student(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=40)
    email=models.EmailField()
    password=models.CharField()

    class Meta:
        verbose_name='student'
        verbose_name_plural='students'

class ExamGroup(models.Model):
    name=models.CharField(max_length=30)
    examinerID=models.ForeignKey(Examiner, on_delete=models.CASCADE)

    class Meta:
        verbose_name='exam group'
        verbose_name_plural='exam groups'

class Student_ExamGroup(models.Model):
    studentID=models.ForeignKey(Student, on_delete=models.CASCADE)
    groupID=models.ForeignKey(ExamGroup, on_delete=models.CASCADE)

class Exam(models.Model):
    