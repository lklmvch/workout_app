from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView, DetailView
from rest_framework import generics, viewsets, status, serializers
from rest_framework.decorators import action

from .forms import UserContactsForm, ImageForm, CourseRegistrationForm
from .models import Image, Course, Registration
from .serializers import ImageSerializer, CourseSerializer, RegistrationSerializer

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


class CourseRegistrationFormView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseRegistrationForm
    template_name = 'course_registration.html'

    def form_valid(self, form):
        # Add the current user to the course (many-to-many relationship)
        course = form.save()
        course.users.add(self.request.user)  # Add the logged-in user to the course

        return redirect(reverse('schedule'))
    # def get(self, request, course_id):
    #     # Render the HTML form template
    #     form = CourseRegistrationForm()
    #     course = get_object_or_404(Course, id=course_id)
    #     return render(request, 'course_registration.html', {'form': form, 'course_name': course.name, 'course_id': course_id})
    #
    # def post(self, request, course_id):
    #     form = CourseRegistrationForm(request.POST)
    #     if form.is_valid():
    #         # Process the registration form and save the registration
    #         form.save()  # Assuming your form's save() handles course assignment
    #         return JsonResponse({"message": "Registration successful!"})
    #     return JsonResponse(form.errors, status=400)


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


class CourseMembersView(DetailView):
    model = Course
    template_name = 'main/course_members.html'
    context_object_name = 'members'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Use self.get_object() or self.object to access the course instance
        # context['members'] = Registration.objects.filter(course=self.object())
        context['members'] = self.object.registrations.all()
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['members'] = Registration.objects.filter(course=self.object)  # Assuming 'user' is the related name of the ForeignKey/ManyToManyField
    #     return context

    # def get_queryset(self):
    #     course_id = self.kwargs['course_id']
    #     course = get_object_or_404(Course, id=course_id)
    #     return course.user.all()




