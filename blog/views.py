from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from blog.models import Post
from blog.serializers import PostSerializer, PostLikeSerializer
from blog.services import LikesService


class PostListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostLikePerPostListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostLikeSerializer

    service = LikesService()

    def get_queryset(self):
        # Not PostLike.objects.filter(post_id=self.kwargs['post_id']).order_by('id') because we will get OK(200)
        # code even if the post is not exists
        return get_object_or_404(Post, pk=self.kwargs['post_id']).postlike_set.order_by('id')

    def perform_create(self, serializer):
        self.service.like_post(self.kwargs['post_id'], self.request.user, serializer)
