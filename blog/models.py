from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    # TODO: add created and updated timestamps
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class PostLike(models.Model):
    # TODO: add updated timestamp
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        unique_together = ('author', 'post')
