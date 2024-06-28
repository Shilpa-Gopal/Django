from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to Home page")

def about(request):
    return HttpResponse("Hello, welcome to About page")

def contact(request):
    return HttpResponse("Hello, welcome to Contact page")