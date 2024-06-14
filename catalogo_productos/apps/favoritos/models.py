from django.db import models

# Create your models here.

from apps.usuarios.models import Usuario
from apps.productos.models import Producto

class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'producto')