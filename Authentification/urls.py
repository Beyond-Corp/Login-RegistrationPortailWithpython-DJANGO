from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homeP'),
    path('signup/', views.signup, name='signupP'),
    path('signin/', views.signin, name='signinP'),
    path('signout/', views.signout, name='signoutP'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
