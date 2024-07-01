
from rest_framework import routers

from apps.entity.views import CoordinateEntityViewSet, LabelViewSet

router = routers.DefaultRouter()
router.register(r'entities', CoordinateEntityViewSet, basename='entities')
router.register(r'labels', LabelViewSet, basename='labels')
