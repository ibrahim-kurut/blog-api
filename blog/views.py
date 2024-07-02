from django.shortcuts import render

from .serializers import CategorySerializer, PostSerializer

from .models import Category, Post

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAdminOrReadOnly



class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # only admin can be add a category
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


    # for return created successfully message
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        message = {
            "message": "Category created successfully",
        }
        return Response(message, status=status.HTTP_201_CREATED, headers=headers)


    # for return update successfully message
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        msg = {
            "message": "Category updated successfully",
        }

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(msg)


    # for return delete successfully message
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        message = {
            "message": "Category deleted successfully",
            }
        return Response(message,status=status.HTTP_204_NO_CONTENT)



# =============== Post Views ===============

class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
   

    # for return created successfully message
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        message = {
            "message": "post created successfully",
            }
        return Response(message, status=status.HTTP_201_CREATED, headers=headers)

      # for return update successfully message
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        msg = {
            "message": "post updated successfully",
        }

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(msg)


    # for return delete successfully message
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        message = {
            "message": "post deleted successfully",
            }
        return Response(message,status=status.HTTP_204_NO_CONTENT)

