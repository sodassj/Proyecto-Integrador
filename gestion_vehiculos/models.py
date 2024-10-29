from django.db import models

# Create your models here.

class Automovil(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    anio = models.IntegerField()
    foto = models.ImageField(upload_to='automoviles/')
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo}"
