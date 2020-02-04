from django.shortcuts import render
from django.views.generic import View


posts = [
    {'author' : 'Michaela', 
     'title' : 'Question 1', 
     'content' : 'first post',
     'date': 'January 1, 2020'
    }
]


def index(request):
    return render(request, 'index.html',{})

def alteryx(request):
    context = {
        'posts' : posts
    }
    return render(request, 'Alteryx.html',context)

    

