from django.shortcuts import render, redirect

def verificar_permisos():

    def deco_verificar_permisos(f):
        def check(request, *arg, **kwargs):
            if not request.user.is_authenticated:
                return redirect("error_permisos")
            return f(request, *arg, **kwargs)

        return check

    return deco_verificar_permisos

def verificar_favorito():

    def deco_verificar_permisos(f):
        def check(request, *arg, **kwargs):
            if not request.user.is_authenticated:
                return redirect("iniciar_sesion")
            return f(request, *arg, **kwargs)

        return check

    return deco_verificar_permisos