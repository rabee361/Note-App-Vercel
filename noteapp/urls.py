from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('all-notes/' , allNotes.as_view() , name="all-notes"),
    path('get-note/<str:pk>' , getNote.as_view() , name = "get-note"),
    # path('update-note/<str:pk>' , updateNote , name = "update-note"),
    # path('check-note/<str:pk>' , checkNote , name="check-note"),
    # path('uncheck-note/<str:pk>' , uncheckNote , name="uncheck-note"),

]
