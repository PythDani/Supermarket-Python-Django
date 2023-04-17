from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def home(request):
    return render(request, './products/home.html')

def nosotros(request):
    return render(request, './products/nosotros.html')

def products(request):
    products_list= Product.objects.all()
    return render(request, './products/all.html', {'products_list': products_list})

