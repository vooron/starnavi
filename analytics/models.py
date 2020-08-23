from django.contrib.auth.models import User
from django.db import models


class UserActivity(models.Model):
    # TODO: add updated timestamp
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.CharField(max_length=120)  # API resource URI
    method = models.CharField(max_length=8)
    last_time_logged_in = models.DateTimeField()  # allows us to determine to which session this action belongs to
    created = models.DateTimeField(auto_now_add=True)
