from rest_framework import serializers
from backend.models import ApiGroup


class ApiGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiGroup
        fields = ('id', 'projId', 'apiGroupJson')

    def create(self, validated_data):
        # return super().create(validated_data)
        return ApiGroup.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # return super().update(instance, validated_data)
        instance.projId = validated_data.get('projId', instance.projId)
        instance.apiGroupJson = validated_data.get(
            'apiGroupJson', instance.apiGroupJson)
        instance.save()
        return instance
