# Create your views here.
from django.shortcuts import render

def index(request):
    context = {'message': 'Hello'}
    return render(request, 'siteapp/index.html', context)

def blog(request):
    context = {}
    return render(request, 'siteapp/blog/index.html', context)