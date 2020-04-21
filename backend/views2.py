from rest_framework import viewsets, filters
from autotest_django.util.customModelViewSet import CustomModelViewSet
from backend.models import ApiGroup, Apis
from backend.serializers import ApiGroupSerializer, APiSerializer
from backend.filter import apiFilter
from django_filters import rest_framework
# from rest_framework_extensions.mixins import ListUpdateModelMixin


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
    # filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_backends = (rest_framework.DjangoFilterBackend,
                       filters.OrderingFilter,)
    filter_class = apiFilter
    ordering_fields = ['apiSortNo']
    ordering = 'apiSortNo'
