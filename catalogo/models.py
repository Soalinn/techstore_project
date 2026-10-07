from django.db import models

# Create your models here.

class Producto(models.Model):
    CATEGORIAS = [
        ('consolas', 'Consolas'),
        ('notebooks', 'Notebooks'),
        ('componentes', 'Componentes'),
        ('perifericos', 'Periféricos'),
    ]

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices= CATEGORIAS)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    descripcion = models.TextField()
    disponible = models.BooleanField(default=True) 


    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"


