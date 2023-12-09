from .serilaizers import *
from base.models import *
from rest_framework.response import Response
from django.shortcuts import redirect , render
from rest_framework.views import APIView
from rest_framework.response import Response
from base.forms import *

class handleNote(APIView):
    def get(self,request):
        form = NoteForm()
        print(request.user)
        notes = Note.objects.all()
        serializer = NoteSerializer(notes ,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
        return Response(serializer.data)
