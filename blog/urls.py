from django.urls import path

from .views import PostLikePerPostList, PostList

urlpatterns = [
    path(r'posts/', PostList.as_view()),
    path(r'posts/<int:post_id>/likes/', PostLikePerPostList.as_view()),
]
