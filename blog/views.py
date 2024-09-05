from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import ArticlesForm
from .models import Articles
from .serializers import ArticlesSerializer

class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


# class ArticlesListView(generics.ListCreateAPIView):
#     queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializer
#
# class ArticlesUpdateView(generics.UpdateAPIView):
#     queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializer
#
#
# class ArticlesDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Articles.objects.all()
#     serializer_class = ArticlesSerializer





# class ArticlesAPIView(APIView):
#     def get(self, request):
#         w = Articles.objects.all()
#         return Response({'posts': ArticlesSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = ArticlesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'posts': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#         try:
#             instance = Articles.objects.get('pk')
#         except:
#             return Response({'error': 'Object does not exist'})
#
#         serializer = ArticlesSerializer(data = request.data, instance=instance)
#         serializer.is_valid()
#         serializer.save()
#
#         return Response({'posts': serializer.data})


def blog(request):
    news = Articles.objects.order_by('date')
    return render(request, 'main/blog.html', {'news': news})

class BlogDetailView(DetailView):
    model = Articles
    template_name = 'main/blog_single.html'
    context_object_name = 'article'


@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save()
            article.author = request.user or None
            article.save()
        else:
            error = 'Incorrect data'

    form = ArticlesForm()
    data = {
        'form': form,

    }
    return render(request, 'main/add_article.html', data)

class AddArticle(CreateView):
    model = Articles
    template_name = 'main/add_article.html'
    context_object_name = 'add_article'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)

