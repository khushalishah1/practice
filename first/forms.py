from django import forms
from .models import *


class login_form(forms.Form):
    username = forms.CharField(max_length=15)
    password=forms.CharField(max_length=20)


class signup_form(forms.Form):
    username = forms.CharField(max_length=15)
    password1 = forms.CharField(max_length=20,widget=forms.PasswordInput)
    password2=forms.CharField(max_length=20,widget=forms.PasswordInput)
    email=forms.EmailField()


class insertproduct_form(forms.ModelForm):
    class Meta:
        model=insertproduct
        fields="__all__"