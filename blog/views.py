from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView, CreateView

from .models import Articles
from .forms import ArticlesForm


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

