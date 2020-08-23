from .models import UserActivity


class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            UserActivity(
                user=request.user,
                resource=request.META.get('PATH_INFO'),
                last_time_logged_in=request.user.last_login,
                method=request.method
            ).save()

        response = self.get_response(request)
        return response
