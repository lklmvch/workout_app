from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action

from .forms import UserContactsForm, ImageForm
from .models import Image, Registration, Course, UserContacts
from .serializers import ImageSerializer, RegistrationSerializer, CourseSerializer

from rest_framework.response import Response
from .permissions import IsTrainer



class MediaViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

def index(request):
    return render(request, 'main/index.html')



def about(request):
    return render(request, 'main/about.html')


def schedule(request):
    courses = Course.objects.all()
    return render(request, 'main/schedule.html', {'courses': courses})


def gallery(request):
    photos = Image.objects.all()[::-1]
    return render(request, 'main/gallery.html', {'photos': photos})

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'



def blog_single(request):
    return render(request, 'main/blog_single.html')


# class UserContactsViewSet(viewsets.ModelViewSet):
#     queryset = UserContacts.objects.all()
#     serializer_class = CourseSerializer
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
            return render(request, "main/index.html", {"form": form})
    else:
        form = ImageForm()
    return render(request, "main/gallery_upload.html", {"form": form})



class RegisterForClassView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            registration = serializer.save()
            return Response({"message": "Registration successful!", "registration_id": registration.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('name')
    serializer_class = CourseSerializer

    # Allow ordering by name and created_at fields
    ordering_fields = ['name', 'trainer']

    @action(detail=True, methods=['get'], permission_classes=[IsTrainer])
    def members(self, request, pk=None):
        course = self.get_object()  # Get the course instance
        # Get all registrations related to this course
        registrations = Registration.objects.filter(course=course)
        serializer = RegistrationSerializer(registrations, many=True)  # Serialize the registrations
        return Response(serializer.data)  # Return serialized data







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


