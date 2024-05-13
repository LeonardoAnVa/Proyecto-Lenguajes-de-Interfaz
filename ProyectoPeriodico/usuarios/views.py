from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views import View

from usuarios.forms import GroupForm


# Create your views here.
class LogoutSesion(View):
    def get(self, request):
        logout(request)  # Cierra la sesión del usuario actual
        return redirect('home')  # Redirige a la página de inicio o a otra página deseada
class GrupoListar(View):
    def get(self, request):
        grupos = Group.objects.all()
        cdx={
            'grupos': grupos,
            'titulo': 'Grupos',
            'encabezado': "Grupos",
            'hay_agregar': True,
            'link_agregar': "/usuarios/grupo_alta",
        }
        return render(request, 'grupo_listar.html', cdx)
class GrupoAlta(View):
    def get(self, request):
        form = GroupForm()
        cdx={
            'form': form,
            'titulo': 'Grupo Nuevo',
            'encabezado': "Grupo Nuevo",
        }
        return render(request, 'grupo_abc.html', cdx)

    def post(self, request):
        form = GroupForm(request.POST)
        #print(f'name: {form.clean_name()}')
        if form.is_valid():
            form.save()
            return redirect('grupo_listar')
        cdx={
            'form': form,
            'titulo': 'Grupo Nuevo',
            'encabezado': "Grupo Nuevo",
        }
        return render(request, 'grupo_abc.html', cdx)