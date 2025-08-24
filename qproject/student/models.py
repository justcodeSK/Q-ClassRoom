from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Place=models.CharField(max_length=50)
    Email=models.EmailField()
    Type=models.CharField(max_length=50)
    Phone=models.IntegerField()
    User=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Value=models.IntegerField(default=0)