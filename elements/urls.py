from django.urls import path, include
from rest_framework import routers

from elements.views import ElementViewSet

app_name = 'elements'

elements_router = routers.DefaultRouter()
elements_router.register(r'elements', ElementViewSet)

urlpatterns = [
    path('', include(elements_router.urls))
]