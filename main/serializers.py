from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import serializers
import re

from .models import Course, UserContacts, Registration
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"

# class UserContactsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserContacts
#         fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class RegistrationSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=13)  # Example: +375XXXXXXXXX (13 characters)

    # We will add custom validation for the phone_number field
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())


    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    def validate_phone_number(self, value):
        # Check if the phone number starts with +375 and has exactly 9 digits following
        if not re.match(r'^\+375\d{9}$', value):
            raise serializers.ValidationError("Phone number must start with +375 and contain exactly 9 digits.")
        return value


    def validate_course_id(self, value):
        # Validate that course exists
        try:
            course = Course.objects.get(id=value)
        except Course.DoesNotExist:
            raise serializers.ValidationError("Course does not exist.")
        return value

    def create(self, validated_data):
        # Extract the course and user info from the validated data
        registration = Registration.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            course=validated_data['course']
        )

        return registration

