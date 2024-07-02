
from django.urls import path, include

from .views import CategoryModelViewSet, PostModelViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
'''
url = /blog/api/categories/
url = /blog/api/posts/
'''
router.register("categories", CategoryModelViewSet)  # categories/ categories/<int:pk>/
router.register("posts", PostModelViewSet)  # categories/ categories/<int:pk>/

urlpatterns = [
    path("", include(router.urls))
]