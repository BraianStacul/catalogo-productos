import django_filters
from django import forms
from .models import Producto

class ProductoFilter(django_filters.FilterSet):

    buscador = django_filters.CharFilter(
        field_name='nombre',
        lookup_expr='icontains',
        label='Nombre',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre de la materia para buscar'
        })
    )

    class Meta:
        model = Producto
        fields = ['buscador']
