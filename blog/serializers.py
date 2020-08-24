from django.contrib.auth import get_user_model
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Post, PostLike


class ShortUserInfoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'first_name', 'last_name', 'email')
        read_only_fields = ('id',)


class PostLikeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = PostLike
        fields = ('id', 'author_id', 'post_id', 'created')
        read_only_fields = ('id',)


class PostSerializer(HyperlinkedModelSerializer):
    author = ShortUserInfoSerializer(read_only=True)
    likes = PostLikeSerializer(source='postlike_set', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'likes')
        read_only_fields = ('id',)
