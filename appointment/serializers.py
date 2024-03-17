from rest_framework import serializers
from .import models

# appointment serializer create
class AppointmentSerializer(serializers.ModelSerializer):
    pateint = serializers.StringRelatedField(many=False)
    doctor = serializers.StringRelatedField(many=False)
    time = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Appointment
        fields = '__all__'
