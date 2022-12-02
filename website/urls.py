from django.urls import path
from .views import index, blog, service1, service2, service3
urlpatterns = [
    path('', index, name='index'),
    path('blog', blog, name='blog'),
    path('book-keeping-and-outsourcing-of-staff', service1, name='book-keeping-and-outsourcing-of-staff'),
    path('customer-support', service2, name='customer-support'),
    path('data-entry', service3, name='data-entry'),
]