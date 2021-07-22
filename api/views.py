from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    NoteSerializer,
    NoteCommentSerializer,
    PostSerializer,
    PostCommentSerializer,
    UserSerializer,
)

from notes.models import Note, NoteComment
from posts.models import Post, PostComment


class NoteAPIView(APIView):
    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetailAPIView(APIView):
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)

