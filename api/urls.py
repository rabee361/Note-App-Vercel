from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('notes/' , handleNote.as_view(), name="notes")
]
