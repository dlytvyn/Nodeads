from django.urls import path, include
from rest_framework import routers

from groups.views import GroupViewSet

app_name = 'groups'

groups_router = routers.DefaultRouter()
groups_router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(groups_router.urls))
]