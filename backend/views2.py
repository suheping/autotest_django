from rest_framework import viewsets
# from rest_framework import mixins
# from backend.util.customModelViewSet import CustomModelViewSet
from autotest_django.util.customModelViewSet import CustomModelViewSet
from backend.models import ApiGroup, Apis
from backend.serializers import ApiGroupSerializer, APiSerializer
# from rest_framework.response import Response
from backend.filter import apiFilter
from django_filters import rest_framework
from rest_framework import views


class apiGroupViewSet(CustomModelViewSet,
                      viewsets.GenericViewSet):
    queryset = ApiGroup.objects.all()
    serializer_class = ApiGroupSerializer
    # 查询详情时，按照projId查询
    lookup_field = 'projId'


class apiViewSet(CustomModelViewSet,
                 viewsets.GenericViewSet):
    queryset = Apis.objects.all()
    serializer_class = APiSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = apiFilter
