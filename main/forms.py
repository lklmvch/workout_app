from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import UserContacts, Image, Course
from django.forms import ModelForm, Form, Textarea, PasswordInput, CharField, EmailField, TextInput


class UserContactsForm(ModelForm):
    class Meta:
        model = UserContacts
        fields = ('name', 'email', 'message')

        widgets = {
            'name': TextInput(attrs={
                'class': "col-lg-6",
                'placeholder': "Name"
            }),
            'email': TextInput(attrs={
                'class': "col-lg-6",
                'placeholder': "Email"
            }),
            'message': Textarea(attrs={
                'class': 'col-lg-12',
                'placeholder': "Message"
            })

        }


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ("name", "img")


class CourseRegistrationForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name']  # or other fields you want to display

    phone_number = CharField(max_length=13, required=True)  # e.g., +375XXXXXXXXX

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Get the user from kwargs
        super().__init__(*args, **kwargs)
    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")
        if not phone.startswith("+375") or len(phone) != 13:
            raise ValidationError("Phone number must start with +375 and contain exactly 9 digits after.")
        return phone

    # Method to add current user to the course
    def save(self, *args, **kwargs):
        course = super().save(*args, **kwargs)
        return course







