from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('schedule', views.schedule, name='schedule'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery_upload', views.gallery_upload, name='gallery_upload'),
    path('contacts', views.contacts, name='contacts'),
    path('blog_single', views.blog_single, name='blog_single'),

]
