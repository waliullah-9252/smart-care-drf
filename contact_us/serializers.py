from rest_framework import serializers
from . import models

# contact us serializer
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = '__all__'