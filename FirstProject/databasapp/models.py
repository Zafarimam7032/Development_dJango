from django.db import models

class Student(models.Model):
  studentid=models.CharField(max_length=200,primary_key=True)
  studentName=models.CharField(max_length=300)
  collegeName=models.CharField(max_length=200)
  address=models.TextField
