from django.db import models
class Contact(models.Model):
    fullname=models.CharField(max_length=50)
    fullemail1=models.CharField(max_length=50)
    fullmessage=models.TextField()
# Create your models here.