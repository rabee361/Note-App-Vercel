from django.shortcuts import render , redirect
from .models import *
from .forms import NoteForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import *

# def home(request):
#     notes = Note.objects.all()
#     form = NoteForm()
#     if request.method== 'POST':
#         form = addNote(request)
#         return redirect('home')
#     context = {
#         'form' : form,  
#         'notes' : notes,
#     }
#     return render(request , 'notes.html' , context)


# def addNote(request):
#     name = request.POST.get('name')
#     if Note.objects.filter(name__exact =name).exists():
#         return redirect('home')
#     else:
#         form = NoteForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return form



# def deleteNote(request , pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return redirect('home')


# def updateNote(request, pk):
#     note = Note.objects.get(id=pk)
#     form = NoteForm(instance=note)
#     if request.method == 'POST':
#         note.name = request.POST.get('name')
#         note.save()
#         return redirect('home')
#     context = {
#         'form':form
#     }
#     return render(request,'notes.html' , context = context)


# def checkNote(request , pk):
#     note = Note.objects.get(id=pk)
#     if note.done == False:
#         note.done = True
#     else:
#         note.done = False
#     note.save()
#     return redirect('home')

@api_view(['POST'])
def addNote(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


class getNote(APIView):
    def get(self,request,pk):
        try:        
            note = Note.objects.get(id=pk)
        except:
            return Response('no query with this id!!')
        serializer = NoteSerializer(note,many=False)
        data=serializer.data
        return Response(data)

    def delete(self,request,pk):
        note = Note.objects.get(id=pk)
        note.delete()
        return Response('done')

    def post(self,request,pk):
        note = Note.objects.get(id=pk)
        note.name = request.data['name']
        note.done = request.data['done']
        note.save()
        serializer = NoteSerializer(note,many=False)
        data=serializer.data
        return Response(data)


class allNotes(APIView):
    def get(self,request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes , many=True)
        data = serializer.data
        return Response(data)

    def post(self,request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return redirect('all-notes')

