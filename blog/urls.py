from django.urls import path

from .views import PostLikePerPostListView, PostListView

urlpatterns = [
    path(r'posts/', PostListView.as_view()),
    path(r'posts/<int:post_id>/likes/', PostLikePerPostListView.as_view()),
]
