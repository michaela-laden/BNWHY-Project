from django.shortcuts import render
from django.views.generic import ListView
from bnwhy.api.models import Post

def index(request):
    return render(request, 'index.html',{})

def alteryx(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'Alteryx.html',context)