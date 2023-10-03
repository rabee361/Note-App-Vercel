from .serilaizers import *
from noteapp.models import *
from rest_framework.response import Response
from django.shortcuts import redirect , render
from rest_framework.decorators import api_view
from rest_framework.views import APIView

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

