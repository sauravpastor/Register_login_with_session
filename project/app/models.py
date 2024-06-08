from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.CharField(max_length=12)
    Password = models.CharField(max_length=50)


class Query(models.Model):
    Email = models.EmailField(max_length=50)
    Title = models.CharField(max_length=100)
    discription = models.TextField(max_length=100)
