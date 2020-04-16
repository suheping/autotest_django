
from rest_framework import generics
from backend.models import ApiGroup
from backend.serializers import ApiGroupSerializer


class ApiGroupList(generics.ListCreateAPIView):
    queryset = ApiGroup.objects.all()
    serializer_class = ApiGroupSerializer


class ApiGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApiGroup.objects.all()
    serializer_class = ApiGroupSerializer
