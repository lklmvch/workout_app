from django.urls import path, include
from . import views
from rest_framework import routers

from .views import MediaViewSet, CourseViewSet

from .views import RegisterForClassView


router = routers.SimpleRouter()
router.register(r'media', MediaViewSet)
router.register(r'course', CourseViewSet)


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('schedule', views.schedule, name='schedule'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery_upload', views.gallery_upload, name='gallery_upload'),
    path('contacts', views.contacts, name='contacts'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('api/v1/', include(router.urls)),
    path('api/v1/register/', RegisterForClassView.as_view(), name='register-for-class'),

]

