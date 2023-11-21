from rest_framework import serializers
from .models import User
from django.contrib.auth.admin import UserAdmin


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    extra_kwargs = {
        'ip_address': {
            'read_only': True,
        }
    }

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'email', 'address', 'address', 'city', 'state', 'country', 'date_of_birth', 'profile_picture', 'phone_number', 'ip_address', 'date_joined']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)