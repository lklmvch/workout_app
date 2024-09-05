from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'articles', ArticlesViewSet)

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_article', views.add_article, name='add_article'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('api/v1/', include(router.urls)),
    # path('api/v1/articles', ArticlesViewSet.as_view({'get': 'list'}), name='api_articles'),
    # path('api/v1/articles/<int:pk>', ArticlesViewSet.as_view({'put': 'update'})),
]
