from rest_framework import serializers
from .import models

# services serializer here
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'