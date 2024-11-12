from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import UserRegistrationView, SignUpView

app_name = 'users'
urlpatterns = [
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('sign-up', SignUpView.as_view(), name='sign-up'),
]
