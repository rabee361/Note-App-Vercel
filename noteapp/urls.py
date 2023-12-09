from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home , name="home"),
    path('delete-note/<str:pk>' , deleteNote , name="delete-note"),
    path('check-note/<str:pk>' , checkNote , name="check-note"),
    path('login/' , loginUser , name="login"),
    path('register/' , registerUser , name="register"),
    path('logout/' , logoutUser , name='logout')

]
