from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    notes = Note.objects.filter(user=request.user)

    if request.method== 'POST':
        form = addNote(request)
        return redirect('home')
    context = { 
        'notes' : notes,
    }
    return render(request , 'notes.html' , context)


def addNote(request):
    name = request.POST.get('name')
    if Note.objects.filter(name__exact =name).exists():
        return redirect('home')
    else:
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
    return form


@login_required(login_url='login')
def deleteNote(request , pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return redirect('home')


@login_required(login_url='login')
def checkNote(request , pk):
    note = Note.objects.get(id=pk)
    if note.done == False:
        note.done = True
    else:
        note.done = False
    note.save()
    return redirect('home')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user :
            login(request,user)
            return redirect('home')
    context = {}
    return render(request,'login.html' , context)

def registerUser(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')

    context = {
        'form' : form
    }
    return render(request , 'register.html' , context)


def logoutUser(request):
    logout(request)
    return redirect('login')