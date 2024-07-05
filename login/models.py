from django.db import models
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
# Create your models here.

class Signin(models.Model):
    username1=models.CharField(max_length=50)
    email=models.CharField(max_length=200)
    password1=models.CharField(max_length=50)
    
class Join(models.Model):
    Namej=models.CharField(max_length=50)
    Bdatej=models.CharField(max_length=200)
    Instaj=models.CharField(max_length=50)
    Numberj=models.CharField(max_length=200)
    Emailj=models.CharField(max_length=200)