from rest_framework import viewsets

from groups_elements.models import Element, Group
from groups_elements.pagination import StandardResultsSetPagination
from groups_elements.permissions import Permissions
from groups_elements.serializers import GroupSerializer, ElementSerializer


class ElementViewSet(viewsets.ModelViewSet):
    permission_classes = (Permissions,)
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

    queryset = Element.objects.get_queryset(full_query=False)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = StandardResultsSetPagination
