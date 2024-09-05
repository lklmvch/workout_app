from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import UserRegistrationView


app_name = 'users'
urlpatterns = [
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('user-register/', UserRegistrationView.as_view(), name='user-registration'),
]
