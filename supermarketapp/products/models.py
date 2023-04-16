from django.db import models

# Create your models here.

class Product(models.Model):
    
    id= models.AutoField(primary_key=True)
    precio = models.IntegerField(verbose_name='Precio')
    nombre_producto = models.CharField(max_length=30, verbose_name='NombreProducto')


