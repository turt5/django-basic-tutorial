from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    

class Course(models.Model):
    courseCode=models.CharField(max_length=10)
    courseName=models.CharField(max_length=100)