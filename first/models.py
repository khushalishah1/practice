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
    password2=models.CharField(max_length=20,default=None)
    email=models.EmailField(db_column="email",default=None,null=True)

    def __str__(self):
        return self.username

class insertproduct(models.Model):
    pname=models.CharField(db_column='product_name',max_length=30)
    pdescription=models.CharField(db_column='product_description',max_length=200)

    def __str__(self):
        return self.pname