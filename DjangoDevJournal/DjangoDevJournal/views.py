from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, welcome to Home page")
    return render(request, 'websites/index.html')

def about(request):
    return render(request, 'websites/about.html')

def contact(request):
    return HttpResponse("Hello, welcome to Contact page")