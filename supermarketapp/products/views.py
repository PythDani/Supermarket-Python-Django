from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import ProductForm
from .models import Product

# Create your views here.

def home(request):
    return render(request, './products/home.html')

def nosotros(request):
    return render(request, './products/nosotros.html')

def products(request):
    products_list= Product.objects.all()
    return render(request, './products/all.html', {'products_list': products_list})

def crear(request):
    formulario = ProductForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('products')

    return render(request, './products/crear.html', {'formulario':formulario})

def editar(request, id):
     
     producto=Product.objects.get(id=id)
     formulario = ProductForm(request.POST or None, request.FILES or None, instance=producto)
     if formulario.is_valid():
        formulario.save()
        return redirect('products')
     
     return render(request, './products/editar.html', 
        {
      
         'formulario': formulario        
         
         })

def eliminar(request, id):
    producto=Product.objects.get(id=id)
    producto.delete()
    return redirect('products')
