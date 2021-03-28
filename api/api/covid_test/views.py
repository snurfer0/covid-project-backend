from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from .models import Test, User
from django.http import Http404
from .serializers import TestSerializer, UserSerializer
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'admin': '/api/admin/',
        'users': '/api/users/',
        'user': '/api/users/<int:pk>/',
        'tests': '/api/tests/',
        'test': '/api/tests/<int:pk>/',
    }
    return Response(api_urls)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TestList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
