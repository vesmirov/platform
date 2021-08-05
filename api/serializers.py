from django.contrib.auth import get_user_model
from rest_framework import serializers

from notes.models import Note, NoteComment
from posts.models import Post, PostComment


User = get_user_model()


class NoteCommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta():
        model = NoteComment
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta():
        model = Note
        fields = '__all__'


class NoteDetailSerializer(NoteSerializer):
    comment = NoteCommentSerializer(read_only=True, many=True)


class PostCommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta():
        model = PostComment
        fields = ('id', 'author', 'published', 'text')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta():
        model = Post
        fields = '__all__'


class PostDetailSerializer(PostSerializer):
    comments = PostCommentSerializer(read_only=True, many=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = (
            'pk',
            'username',
            'email',
            'first_name',
            'last_name',
            'role',
        )
