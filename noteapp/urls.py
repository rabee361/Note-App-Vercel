from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home , name="home"),
    path('delete-note/<str:pk>' , deleteNote , name="delete-note"),
    path('check-note/<str:pk>' , checkNote , name="check-note"),

]
