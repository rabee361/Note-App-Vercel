from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm  
from django import forms

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('name',)

class MyForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'type' : 'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'type' : 'password'}))

    class Meta:
        model = User
        fields = ("username","email","password1","password2")
