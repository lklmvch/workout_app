from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, TextInput, Form, PasswordInput, EmailField


class LoginUserForm(Form):
    username = CharField(label='Login',
                                   widget=TextInput(attrs={'class': 'form-input'})
                                   )
    password = CharField(label='Password',
                                   widget=PasswordInput(attrs={'class': 'form-input'})
                                   )

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = CharField(label='First Name', widget=TextInput(attrs={
        'class': "col-lg-9",
        'placeholder': "First Name"}))
    last_name = CharField(label='Last Name', widget=TextInput(attrs={
        'class': "col-lg-9",
        'placeholder': "Last Name"}))

    email = forms.EmailField(required=True)

    username = CharField(label='Username', widget=TextInput(attrs={
        'class': "col-lg-9",
        'placeholder': "Username"}))

    password1 = CharField(label='Password', widget=PasswordInput(attrs={
        'class': "col-lg-9",
        'placeholder': "Password"}))

    password2 = CharField(label='Password', widget=PasswordInput(attrs={
        'class': "col-lg-9",
        'placeholder': "Repeat password"}))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        widgets = {
            'first_name': TextInput(attrs={
                'class': "col-lg-9",
                'placeholder': "First Name"}),
            'last_name': TextInput(attrs={
                'class': "col-lg-9",
                'placeholder': "Last Name"}),
            'username': TextInput(attrs={
                'class': "col-lg-9",
                'placeholder': "Username"}),
            'password1': PasswordInput(attrs={
                'class': "col-lg-9",
                'placeholder': "Password"
            }),
            'password2': PasswordInput(attrs={
                'class': "col-lg-9",
                'placeholder': "Repeat password"

            }),
        }

        # def clean_password2(self):
        #     cd = self.cleaned_data
        #     if cd['password1'] != cd['password2']:
        #         raise ValidationError('Passwords don\'t match.')
        #     return cd['password2']

        # def clean_username(self):
        #     username = self.cleaned_data['username']
        #     if get_user_model().objects.filter(username=username).exists():
        #         raise ValidationError('The username already exists')
        #     return username
