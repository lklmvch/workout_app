from django.test import TestCase
from .models import UserContacts, Course
from rest_framework.test import APITestCase
from .serializers import CourseSerializer

class UserContactsModelTest(TestCase):
    def setUp(self):
        self.usercontact = UserContacts.objects.create(
            name="Test User",
            email="testuser@email.com",
            message="test message"
        )

    def test_UserContacts_creation(self):
        """Test that a UserContacts instance is created properly."""
        usercontact = UserContacts.objects.get(name="Test User")
        self.assertEqual(usercontact.email, "testuser@email.com")
        self.assertEqual(usercontact.message, "test message")



class CourseSerializerTest(APITestCase):
    def setUp(self):
        self.course_data = {
            'name': 'Test Course',
            'description': 'Test course description',
            'trainer': 1
        }

    def test_valid_course_serializer(self):
        """Test that the serializer works with valid data."""
        serializer = CourseSerializer(data=self.course_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], 'Test Course')
        self.assertEqual(serializer.validated_data['trainer'], 1)

    def test_invalid_course_serializer(self):
        """Test that the serializer fails with invalid data."""
        invalid_data = {'name': ''}
        serializer = CourseSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)
