from django.shortcuts import render
from rest_framework import viewsets
from .import serializers
from .import models
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
# services view set here
class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer