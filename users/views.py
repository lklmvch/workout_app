from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from .serializers import UserRegistrationSerializer

import random
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# from workout_app.tasks import send_confirmation_email


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Authorisation'}


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # # Generate a random confirmation code
            # confirmation_code = str(random.randint(100000, 999999))
            #
            # # Send the confirmation email asynchronously
            # send_confirmation_email.delay(user.email, confirmation_code)
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



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


# class RegisterUser(CreateView):
#     form_class = UserRegistrationForm
#     template_name = 'users/register.html'
#     extra_context = {'title': 'Registration'}
#     success_url = 'users:login'

# def register(request):
#     form = UserRegistrationForm()
#     return render(request, 'users/register.html', {'form': form})

