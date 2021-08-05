from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .serializers import (
    NoteSerializer,
    NoteDetailSerializer,
    PostSerializer,
    PostDetailSerializer,
)
from .permissions import AdminPermission

from notes.models import Note
from posts.models import Post


class PostListCreate(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AdminPermission,)
        return super(PostListCreate, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    def get_permissions(self):
        if self.request.method in ('PUT', 'PATCH'):
            self.permission_classes = (AdminPermission,)
        return super(PostRetrieveUpdateDestroy, self).get_permissions()


class NoteListCreate(ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AdminPermission,)
        return super(NoteListCreate, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NoteRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteDetailSerializer

    def get_permissions(self):
        if self.request.method in ('PUT', 'PATCH'):
            self.permission_classes = (AdminPermission,)
        return super(NoteRetrieveUpdateDestroy, self).get_permissions()
