from rest_framework import serializers
from backend.models import ApiGroup, Apis


class ApiGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiGroup
        fields = ('id', 'projId', 'apiGroupJson',)


class APiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apis
        fields = "__all__"
