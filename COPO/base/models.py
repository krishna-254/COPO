from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
import os

def get_path(instance, filename):
    return os.path.join('Excel',str(instance.subject),filename)

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length = 20, primary_key = True)

class Subject(models.Model):
    name = models.CharField(max_length = 20)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    semester = models.IntegerField()

class Attainment(models.Model):
    name = models.CharField(max_length = 20, default = timezone.now, primary_key = True)
    IA_1 = models.IntegerField()
    IA_2 = models.IntegerField()
    Assignment = models.IntegerField()
    ESE = models.IntegerField()
    
class CourseOutcome(models.Model):
    name = models.CharField(max_length = 20, default = timezone.now, primary_key = True)
    per1 = models.IntegerField()
    per2 = models.IntegerField()
    per3 = models.IntegerField()
    per4 = models.IntegerField()
    
choise=(
    ('Throry','Throry'),
    ('Practical','Practical'),
)

class CalculateExcel(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE, default = 1)
    subject = models.CharField(max_length = 20)
    type = models.CharField(max_length = 40,choices = choise)
    semester = models.IntegerField()
    attainment = models.ForeignKey(Attainment, on_delete = models.CASCADE)
    courseOutCome = models.ForeignKey(CourseOutcome, on_delete = models.CASCADE)
    file = models.FileField(upload_to=get_path)