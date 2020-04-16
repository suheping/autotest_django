from rest_framework import viewsets
from rest_framework import mixins
from backend.models import ApiGroup, Apis
from backend.serializers import ApiGroupSerializer, APiSerializer
from rest_framework.response import Response


class apiGroupViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = ApiGroup.objects.all()
    serializer_class = ApiGroupSerializer
    # 按照项目id筛选
    lookup_field = 'projId'


class apiViewSet(mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 viewsets.GenericViewSet):
    queryset = Apis.objects.all()
    serializer_class = APiSerializer
