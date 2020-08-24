from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from blog.models import Post


class LikesService:

    def like_post(self, post_id: int, user: User, serializer) -> None:
        try:
            get_object_or_404(Post, pk=post_id)  # Validate that post exists
            serializer.save(post_id=post_id, author=user)
        except IntegrityError:
            raise ValidationError("The object can be liked only once.")
