from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def service1(request):
    return render(request, 'book-keeping-and-outsourcing-of-staff.html')

def service2(request):
    return render(request, 'customer-support.html')

def service3(request):
    return render(request, 'data-entry.html')