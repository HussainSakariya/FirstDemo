from django.db import models

# Create your models here.

class student(models.Model):
    no=models.IntegerField(primary_key=True)
    name=models.TextField(max_length=20)
    age=models.IntegerField(null=False)