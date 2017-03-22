from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20,default='')
    age=models.IntegerField(default=20)
    hobby=models.CharField(max_length=100,default='')
