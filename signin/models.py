from django.db import models

class Signin(models.Model):
    username1=models.CharField(max_length=50)
    email=models.CharField(max_length=200)
    password1=models.CharField(max_length=50)
# Create your models here.
