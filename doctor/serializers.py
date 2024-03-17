from rest_framework import serializers
from .import models

# specialization serializers 
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = '__all__'

# designations serializers 
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = '__all__'

# available time serializers 
class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime
        fields = '__all__'

# doctor serializers 
class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    specilization = serializers.StringRelatedField(many=True)
    designation = serializers.StringRelatedField(many=True)
    available_time = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Doctor
        fields = '__all__'

# reviewer serializers 
class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(many=False)
    doctor = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Review
        fields = '__all__'