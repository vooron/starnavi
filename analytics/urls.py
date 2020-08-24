from django.urls import path

from .views import UserActivityPerUserListView, AnalyticsListView

urlpatterns = [
    path(r'users/<int:user_id>/activity/', UserActivityPerUserListView.as_view()),  # TODO: review access
    path(r'analytics/', AnalyticsListView.as_view())
]
