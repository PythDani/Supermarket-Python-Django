from django.urls import path
from . import views   


urlpatterns = [
    path("",  views.home, name="home"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("products/", views.products, name="products"),
    path("products/crear", views.crear, name="crear"),
    
]
