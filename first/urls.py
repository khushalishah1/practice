from django.urls import path
from . import views

urlpatterns=[
    path('',views.logins,name="logins"),
    path('sign',views.signups,name="signup"),
    path('home',views.homepage,name='homepage'),
    path('logout',views.logoutpage,name='logout'),
    path('insertproduct',views.insertproduct_view,name='insert_product'),
    path('viewproduct',views.viewproduct_view,name='view_product'),
    path('deleteproduct/<int:id>',views.deleteproduct_view,name='delete_product'),
    path('<int:id>',views.updateproduct_view,name='update_product')
]