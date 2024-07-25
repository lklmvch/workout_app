from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


# def plans(request):
#     return HttpResponse('<ul><li>First plan</li><li>Second plan</li><li>Third plan</li></ul>')
