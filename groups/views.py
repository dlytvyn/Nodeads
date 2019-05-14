from rest_framework import viewsets

from groups.models import Group
from groups.pagination import StandardResultsSetPagination
from groups.serializer import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = StandardResultsSetPagination
