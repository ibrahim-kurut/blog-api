
from django.urls import path, include

from .views import CategoryModelViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("categories", CategoryModelViewSet)  # categories/ categories/<int:pk>/

urlpatterns = [
    path("", include(router.urls))
]