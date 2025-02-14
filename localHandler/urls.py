from django.contrib import admin
from django.urls import path, include
from localHandler import views

urlpatterns = [
    path('register', views.RegisterLocalBaseUpdate.as_view()),
]
