from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from . forms import signup_form
from .models import *

# Create your views here.
def logins(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username,password)
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            print("hello")
            return redirect('homepage')
        else:
            return HttpResponse("username and password not correct!!!")
    return render(request,'login.html')

def signups(request):
    if request.method == "POST":
        uname=request.POST.get('username')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password2')
        my_form=signup(username=uname,password1=pass1)
        my_form.save()
        if pass1!=pass2:
            return HttpResponse("your password not same")
        my_user=User.objects.create_user(uname,pass1,pass2  )
        my_user.save()
        return redirect('logins')
    return render(request,'signup.html')

@login_required(login_url='logins')
def homepage(request):
    print("in home page")
    return render(request,'home.html')

def logoutpage(request):
    logout(request)
    return redirect('logins')