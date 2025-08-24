from django.urls import path
from django import *
from home import views

urlpatterns = [
    path('',views.home),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
]
