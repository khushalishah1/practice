from django.db import models
from django.forms import ModelForm


# Create your models here.
class login(models.Model):
    username=models.CharField(db_column="login_id",max_length=15)
    password=models.CharField(db_column="password",max_length=20)

    def __str__(self):
        return self.username

class signup(models.Model):
    username=models.CharField(db_column="login_id",max_length=15)
    password1=models.CharField(db_column="password",max_length=20,default=None)

    def __str__(self):
        return self.username
