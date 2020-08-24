from rest_framework.serializers import HyperlinkedModelSerializer, Serializer, IntegerField, DateField

from analytics.models import UserActivity


class UserActivitySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserActivity
        fields = ('id', 'user_id', 'resource', 'method', 'created', 'last_time_logged_in')
        read_only_fields = ('id',)


class AnalyticsSerializer(Serializer):
    date = DateField(source='created_date')
    likes_count = IntegerField(source='count')

    def create(self, validated_data):
        return dict(**validated_data)

    def update(self, instance, validated_data):
        raise NotImplementedError("ReadOnly object")


class AnalyticsFilterSerializer(Serializer):
    from_date = DateField(default=None)
    to_date = DateField(default=None)

    def create(self, validated_data):
        return dict(**validated_data)

    def update(self, instance, validated_data):
        raise NotImplementedError("ReadOnly object")
