from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html',{})
    

