from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post, PostLike, UserActivity


class ShortUserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')
        read_only_fields = ('id',)


class PostLikeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PostLike
        fields = ('id', 'author', 'post')
        read_only_fields = ('id',)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = ShortUserInfoSerializer()
    likes = PostLikeSerializer(source='postlike_set', many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'likes')
        read_only_fields = ('id',)


class UserActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserActivity
        fields = ('id', 'user', 'resource')
        read_only_fields = ('id',)
