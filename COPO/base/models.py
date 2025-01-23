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

# class Subject(models.Model):
#     name = models.CharField(max_length = 20)
#     course = models.ForeignKey(Course, on_delete = models.CASCADE)
#     semester = models.IntegerField()

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
    
choice=(
    ('Theory','Theory'),
    ('Practical','Practical'),
)

class CalculateExcel(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE, default = 1)
    subject = models.CharField(max_length = 20)
    type = models.CharField(max_length = 40,choices = choice)
    semester = models.IntegerField()
    attainment = models.ForeignKey(Attainment, on_delete = models.CASCADE)
    courseOutCome = models.ForeignKey(CourseOutcome, on_delete = models.CASCADE)
    file = models.FileField(upload_to=get_path)
    
    
from django.db import models
class Teacher(models.Model):
    USER_TYPE_CHOICES = [
        ('HOD', 'Head of Department'),
        ('Teaching Professor', 'Teaching Professor'),
        ('Admin', 'Admin'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    teacher_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.user_type})"


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hod = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        related_name='departments_as_hod',
        limit_choices_to={'user_type': 'HOD'},
    )

    def __str__(self):
        return self.name




class Class(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='classes'
    )
    batch = models.CharField(max_length=10)  # Example: '2023-2027'
    division = models.CharField(max_length=1, default='A')

    def __str__(self):
        return f"{self.department.name} - {self.batch} - {self.division}"


class Subject(models.Model):
    class_assigned = models.ForeignKey(
        Class, on_delete=models.CASCADE, related_name='subjects'
    )
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, related_name='subjects'
    )

    def __str__(self):
        return f"{self.name} ({self.class_assigned})"


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    enrollment_id = models.CharField(max_length=20, unique=True)
    student_class = models.ForeignKey(
        Class, on_delete=models.CASCADE, related_name='students'
    )

    def __str__(self):
        return f"{self.name} ({self.enrollment_id})"
