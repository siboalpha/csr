from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.

def index(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank-you')
    context = {'form': form}
    return render(request, 'index.html', context)

def blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {'blog':blog}
    return render(request, 'single-blog.html', context)

def blogs(request):
    blogs = Blog.objects.filter(status='Published')
    context = {'blogs':blogs}
    return render(request, 'blogs.html', context)

def thankYou(request):
    return render(request, 'thank-you.html')

def service1(request):
    return render(request, 'book-keeping-and-outsourcing-of-staff.html')

def service2(request):
    return render(request, 'customer-support.html')

def service3(request):
    return render(request, 'data-entry.html')

def service4(request):
    return render (request, 'payroll-management-and-funding.html')

def service5(request):
    return render(request, 'non-deposit-taking-micorfinance.html')

def service6(request):
    return render(request, 'financial-analysis-and-calculations-related-services.html')