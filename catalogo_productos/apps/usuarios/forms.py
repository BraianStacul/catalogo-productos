from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.usuarios.models import Usuario

class FormularioRegistro(forms.Form):
    username = forms.CharField(label="Nombre de usuario")
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField()

class FormularioRegistroUsuario(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label="Repita contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Usuario
        fields =  ["username", "first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super(FormularioRegistroUsuario, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs["class"] = "form-control"

class EditUser(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label="Repita contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Usuario
        fields =  ["username", "first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super(EditUser, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs["class"] = "form-control"