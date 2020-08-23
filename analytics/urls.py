from django.urls import path
from .views import UserActivityPerUserList, AnalyticsList

urlpatterns = [
    path(r'users/<int:user_id>/activity/', UserActivityPerUserList.as_view()),  # TODO: review access
    path(r'analytics/', AnalyticsList.as_view())
]
