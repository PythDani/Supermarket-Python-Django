from django.urls import path
from . import views   

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path("",  views.home, name="home"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("products/", views.products, name="products"),
    path("products/crear", views.crear, name="crear"),
    path("products/editar/<int:id>", views.editar, name="editar"),
    path("products/eliminar/<int:id>", views.eliminar, name="eliminar"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
