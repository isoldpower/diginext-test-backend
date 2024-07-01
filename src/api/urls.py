from django.urls import include, path

from apps.entity.urls import router as entity_router

urlpatterns = [
    path(r"entities/", include(entity_router.urls)),
]
