from django.urls import path, include
from . import views
from rest_framework import routers

from .views import MediaViewSet, CourseViewSet, CourseRegistrationFormView, CourseMembersView, RegisterForClassView



router = routers.SimpleRouter()
router.register(r'media', MediaViewSet)
router.register(r'class', CourseViewSet)


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('schedule', views.schedule, name='schedule'),
    path('schedule/<int:pk>/members/', CourseMembersView.as_view(), name='course_members'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery_upload', views.gallery_upload, name='gallery_upload'),
    path('contacts', views.contacts, name='contacts'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('api/v1/', include(router.urls)),
    path('api/v1/register/<int:course_id>/', RegisterForClassView.as_view(), name='register_for_class'), #API form view
    path('register/<int:course_id>/', CourseRegistrationFormView.as_view(), name='register_form'), # HTML form view
]


