from django.urls import path, include
from rest_framework import routers

from groups_elements.views import ElementViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'elements', ElementViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls))
]