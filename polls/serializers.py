from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'name', 'paradigm')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post', 'text', 'author')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'title', 'content', 'draft', 'updated', 'created')