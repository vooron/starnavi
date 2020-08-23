from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from blog.models import Post, PostLike, UserActivity
from blog.serializers import PostSerializer, PostLikeSerializer, UserActivitySerializer


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostLikeList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

    def get_queryset(self):
        if "post_id" in self.kwargs:
            print(f"Method PostLikeList.get_queryset was called with post_id={self.kwargs['post_id']}")
            return PostLike.objects.filter(post_id=self.kwargs['post_id'])
        else:
            return self.queryset

    def perform_create(self, serializer):
        if "post_id" in self.kwargs:
            print(f"Method PostLikeList.perform_create was called with post_id={self.kwargs['post_id']}")
            serializer.save(post_id=self.kwargs['post_id'])
        else:
            serializer.save()


class UserActivityPerUserList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserActivitySerializer

    def get_queryset(self):
        return UserActivity.objects.filter(user_id=self.kwargs['user_id'])
