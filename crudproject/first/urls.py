from django.urls import path
from . import views

urlpatterns=[
    path('',views.logins,name="logins"),
    path('sign',views.signups,name="signup"),
    path('home',views.homepage,name='homepage'),
    path('logout',views.logoutpage,name='logout')
]