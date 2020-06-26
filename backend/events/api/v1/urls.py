from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import EventsViewSet

router = DefaultRouter()
router.register("events", EventsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
