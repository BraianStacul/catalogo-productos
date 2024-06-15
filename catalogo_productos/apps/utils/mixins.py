from django.shortcuts import render, redirect

class VerificarAdmin:
    
    def dispatch(self, request, *args, **kwargs):

        if not self.request.user.es_admin:
            return redirect("error_permisos")

        return super(VerificarAdmin, self).dispatch(request, *args, **kwargs)