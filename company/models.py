from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver

class Company(models.Model):
    name = models.CharField(max_length=50,unique=True)

class Department(models.Model):
    name = models.CharField(max_length=255),
    company = models.ForeignKey(Company,related_name='department',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Employee(models.Model):
    name = models.CharField(max_length=255),
    address= models.CharField(max_length=255),
    department = models.ForeignKey(Department,related_name='employee',on_delete=models.CASCADE)

    def __str__(self):
        return self.name.address
# Create your models here.

class User(models.Model):
    id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    repassword = models.CharField(max_length=30)

