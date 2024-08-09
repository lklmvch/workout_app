from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import LoginUserForm, UserRegistrationForm


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Authorisation'}

    # def get_success_url(self):
    #     return reverse_lazy('home')
# def login_user(request):
#     if request.method == 'post':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['isername'], password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
#     else:
#         form = LoginUserForm()
#     return render(request, 'users/login.html', {'form': form})


# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('users:login'))


class RegisterUser(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Registration'}
    success_url = 'users:login'

# def register(request):
#     form = UserRegistrationForm()
#     return render(request, 'users/register.html', {'form': form})