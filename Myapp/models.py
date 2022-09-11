from django.db import models

# Create your models here.
class Employee(models.Model):
    fname = models.CharField(max_length=20)
    empid = models.IntegerField(max_length=10)
    role = models.CharField(max_length=20)
    add = models.TextField()
    