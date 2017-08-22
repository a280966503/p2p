from django.db import models

class LoginInfo(models.Model):
    username=models.CharField(max_length=50,default=None)
    password=models.CharField(max_length=200,default=None)
    state=models.IntegerField(default=0)
    usertype=models.IntegerField(default=1)

