from django import forms

from .models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.SelectMultiple()
    )

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class' : 'form-control'})
    )

    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'class' : 'form-control'})
    )

    #activo = forms.???

    precio = forms.DecimalField(
        widget=forms.TextInput(attrs={'class' : 'form-control'})
    )

    class Meta:
        model = Producto
        fields = ["nombre", "categorias", "precio", "descripcion", "activo"]


class CForm(forms.ModelForm):

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class' : 'form-control'})
    )

    class Meta:
        model = Categoria
        fields = ["nombre"]

class VerForm(forms.ModelForm):

    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.SelectMultiple(attrs={'disabled' : 'disabled'})
    )

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'disabled' : 'disabled', 'class' : 'form-control'})
    )

    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'disabled' : 'disabled', 'class' : 'form-control'})
    )

    activo = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'disabled' : 'disabled'})
    )

    precio = forms.DecimalField(
        widget=forms.TextInput(attrs={'disabled' : 'disabled', 'class' : 'form-control'})
    )

    class Meta:
        model = Producto
        fields = ["nombre", "categorias", "precio", "descripcion", "activo"]