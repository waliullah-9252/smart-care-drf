from rest_framework import serializers
from .import models
from django.contrib.auth.models import User

# patient serializer here
class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)
    class Meta:
        model = models.Pateint
        fields = '__all__'

# patient registration from or serializer class implementation
class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']

        if password != password2:
            raise serializers.ValidationError({
                'errors': 'Password does not match'
            })
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({
                'errors': 'This Email already exists, please another valid email address !'
            })
        account = User(username = username, email = email, first_name = first_name, last_name = last_name)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account
    
# Login serializer creation
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
