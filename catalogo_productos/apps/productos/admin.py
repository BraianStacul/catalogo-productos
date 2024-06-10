from django.contrib import admin

# Register your models here.

from .models import Categoria, Producto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]

admin.site.register(Categoria, CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]

admin.site.register(Producto, ProductoAdmin)