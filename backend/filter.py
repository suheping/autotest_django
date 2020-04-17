import django_filters
from backend.models import Apis


class apiFilter(django_filters.FilterSet):

    class Meta:
        model = Apis
        fields = ['projId', 'apiGroupId']
