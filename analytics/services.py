from datetime import datetime, timedelta

from django.db.models import Count, QuerySet
from django.db.models.functions import TruncDate
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from analytics.models import UserActivity
from blog.models import PostLike


class AnalyticsService:
    USER_ACTIVITY_RESULTS_LIMIT = 30
    MAXIMUM_ANALYTICS_RANGE_DAYS = 10

    def get_analytics(self, from_date: datetime = None, to_date: datetime = None) -> list:
        if not to_date:
            to_date = timezone.now()
        if not from_date:
            from_date = to_date - timedelta(days=self.MAXIMUM_ANALYTICS_RANGE_DAYS)
        if not (0 <= (to_date - from_date).days <= self.MAXIMUM_ANALYTICS_RANGE_DAYS):
            raise ValidationError(f"The difference between to_date and from_date should be non-negative "
                                  f"and lower then {self.MAXIMUM_ANALYTICS_RANGE_DAYS}")

        return list(PostLike.objects.all()
                    .filter(created__gte=from_date, created__lte=to_date)
                    .annotate(created_date=TruncDate('created'))
                    .values("created_date")
                    .annotate(count=Count('id')))

    def get_user_activity_query_set(self, user_id: int) -> QuerySet:
        if not user_id:
            raise ValidationError("User ID parameter was skipped.")
        return UserActivity.objects.filter(user_id=user_id).order_by('-created')[:self.USER_ACTIVITY_RESULTS_LIMIT]
