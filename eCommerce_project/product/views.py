from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer


# class CategoryViewSet(ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing categories.
#     """
#
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#     @extend_schema(responses=CategorySerializer)
#     def list(self, request, *args, **kwargs):
#         # serializer = CategorySerializer(self.queryset, many=True)
#         # return Response(serializer.data)
#         return super().list(request, *args, **kwargs)
#
#     @extend_schema(request=CategorySerializer, responses=CategorySerializer)
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#
# class BrandViewSet(ModelViewSet):
#     """
#     A simple ViewSet for viewing brands.
#     """
#
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#
#     @extend_schema(responses=BrandSerializer)
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#         # serializer = BrandSerializer(self.queryset, many=True)
#         # return Response(serializer.data)
#
#
# class ProductViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for viewing products.
#     """
#
#     queryset = Product.objects.all()
#
#     @extend_schema(responses=ProductSerializer)
#     def list(self, request):
#         serializer = ProductSerializer(self.queryset, many=True)
#         return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing categories.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing brands.
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing products.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
