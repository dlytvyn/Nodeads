from rest_framework import viewsets

from elements.models import Element
from elements.permissions import Permissions
from elements.serializer import ElementSerializer


class ElementViewSet(viewsets.ModelViewSet):
    permission_classes = (Permissions,)
    queryset = Element.objects.all()
    serializer_class = ElementSerializer



