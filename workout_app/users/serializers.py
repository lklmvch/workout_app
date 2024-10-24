from django.contrib.auth.models import User
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'}, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    # Validate that the two passwords match
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    # Create a new user with the validated data
    def create(self, validated_data):
        # Remove password2 from the data, as we don't need it for user creation
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
