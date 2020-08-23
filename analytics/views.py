from rest_framework import generics
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from analytics.serializers import UserActivitySerializer, AnalyticsSerializer, AnalyticsFilterSerializer
from analytics.services import AnalyticsService


class UserActivityPerUserList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserActivitySerializer

    service = AnalyticsService()

    def get_queryset(self):
        return self.service.get_user_activity_query_set(user_id=self.kwargs['user_id'])


class AnalyticsList(views.APIView):
    permission_classes = (IsAuthenticated,)

    service = AnalyticsService()

    def get(self, request):
        analytics_filters = AnalyticsFilterSerializer(request.GET)
        return Response(AnalyticsSerializer(self.service.get_analytics(**analytics_filters.data), many=True).data)
