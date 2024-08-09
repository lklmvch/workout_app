from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView

from .forms import UserContactsForm, ImageForm
from .models import Image


def index(request):
    return render(request, 'main/index.html')



def about(request):
    return render(request, 'main/about.html')


def schedule(request):
    return render(request, 'main/schedule.html')


def gallery(request):
    photos = Image.objects.all()[::-1]
    return render(request, 'main/gallery.html', {'photos': photos})

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'



def blog_single(request):
    return render(request, 'main/blog_single.html')



def contacts(request):
    error = ''
    if request.method == 'POST':
        form = UserContactsForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            error = 'Incorrect data'

    form = UserContactsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/contacts.html', data)

@login_required
def gallery_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, "main/home.html", {"form": form})
    else:
        form = ImageForm()
    return render(request, "main/gallery_upload.html", {"form": form})



# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             # Create a new user object but avoid saving it yet
#             user = form.save(commit=False)
#             # Set the chosen password
#             user.set_password(form.cleaned_data['password'])
#             # Save the User object
#             user.save()
#             return render(request, 'main/index.html', {'new_user': user})
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'main/register.html', {'user_form': form})





