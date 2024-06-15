from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    categorias = models.ManyToManyField(Categoria)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="productos_img/")