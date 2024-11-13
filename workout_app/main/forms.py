from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import UserContacts, Image
from django.forms import ModelForm, TextInput, Textarea, PasswordInput, CharField


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




