from django.db import models

class item(models.Model):
    id=models.IntegerField(primary_key=True)
    value=models.CharField(max_length=30)

