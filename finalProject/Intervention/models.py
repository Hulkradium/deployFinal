# Academic / Discipline Intervention System

from django.db import models

# Create your models here.
class Lecturer(models.Model):
    lect_id = models.CharField(max_length=5, primary_key = True)
    lect_name = models.TextField()
    lect_email = models.TextField()
    department = models.CharField(max_length=3)
    password = models.TextField(default='null')

class Student(models.Model):
    stud_id = models.CharField(max_length=12, primary_key = True)
    stud_name = models.TextField()
    stud_phone = models.CharField(max_length=12)
    course = models.CharField(max_length=4)
    mentor = models.ForeignKey(Lecturer, on_delete = models.CASCADE)

class Severity(models.Model):
    sev_id = models.CharField(max_length=2, primary_key=True)
    sev_level = models.TextField()
    sev_desc = models.TextField()

class Intervention(models.Model):
    int_id = models.AutoField(primary_key=True)
    int_stud_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    int_lect_id = models.ForeignKey(Lecturer, on_delete = models.CASCADE)
    date_report = models.DateField()
    description = models.TextField()
    action = models.TextField()
    category = models.TextField()
    int_sev_id = models.ForeignKey(Severity, on_delete=models.CASCADE)