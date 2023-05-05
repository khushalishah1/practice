from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from .models import *
from .forms import *

# Create your views here.
def logins(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        my_loginform=login(username=username,password=password)
        my_loginform.save()
        # print(username,password)
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'successfully login')
            return redirect('homepage')
        else:
            messages.error(request,'check password')
            return redirect('logins')
    return render(request,'login.html')

def signups(request):
    if request.method == "POST":
        uname=request.POST.get('username')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password2')
        email1=request.POST.get('email')
        my_form=signup(username=uname,password1=pass1,email=email1,password2=pass2)
        my_form.save()
        if pass1!=pass2:
            return HttpResponse("your password not same")
        my_user=User.objects.create_user(uname,email1,pass1)
        my_user.save()

        subject = 'welcome to GFG world'
        message = f'Hi {my_user.username}, thank you for registering in geeksforgeeks.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [my_user.email, ]
        print("mail sent")
        send_mail(subject, message, email_from, recipient_list)

        messages.success(request, 'successfully sign up')
        return redirect('logins')
    return render(request,'signup.html')

@login_required(login_url='logins')
def homepage(request):
    return render(request,'home.html')

def logoutpage(request):
    logout(request)
    return redirect('logins')

def insertproduct_view(request):
    if request.method == 'POST':
        insertp_form=insertproduct_form(request.POST)
        if insertp_form.is_valid():
            insertp_form.save()
            return redirect('view_product')
    else:
        insertp_form = insertproduct_form()

    return render(request,'insertproduct.html',{'insertp_form':insertp_form})

def viewproduct_view(request):
    x = insertproduct.objects.all()
    # print(x)
    context={
        'data': x
    }
    return render(request,'viewproduct.html',context)

def deleteproduct_view(request,id):
    x=insertproduct.objects.get(pk=id)
    x.delete()
    return redirect('view_product')

def updateproduct_view(request,id):
    if request.method == "POST":
        x=insertproduct.objects.get(pk=id)
        updatep_form=insertproduct_form(request.POST,instance=x)
        if updatep_form.is_valid():
            updatep_form.save()
            return redirect('view_product')
    else:
        x = insertproduct.objects.get(pk=id)
        updatep_form = insertproduct_form(instance=x)
    context={
        'updatep_form': updatep_form
    }
    return render(request,'updateproduct.html',context)

