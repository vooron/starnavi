from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.serializers import UserRegistrationSerializer


class RegistrationView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        serializer.save()
