from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_article', views.add_article, name='add_article'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog_detail')
]
