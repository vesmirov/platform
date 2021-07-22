from django.contrib.auth import get_user_model
from rest_framework import serializers

from notes.models import Note, NoteComment
from posts.models import Post, PostComment


User = get_user_model()


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    class Meta():
        model = Note
        fields = '__all__'


class NoteCommentSerializer(serializers.ModelSerializer):
    class Meta():
        model = NoteComment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta():
        model = Post
        fields = '__all__'


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta():
        model = PostComment
        fields = '__all__'


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
