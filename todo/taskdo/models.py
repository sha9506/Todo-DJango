from django.db import models


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length= 300)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    
class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=10, null=True, unique=True)
    
