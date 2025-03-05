from django.urls import re_path, include
from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()

router.register(
    r'pet',
    viewsets.PetViewSet,
)

urlpatterns = [
    re_path(r'', include(router.urls))
]