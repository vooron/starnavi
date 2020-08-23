from django.contrib.auth import get_user_model
from rest_framework.serializers import HyperlinkedModelSerializer


class UserRegistrationSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')
