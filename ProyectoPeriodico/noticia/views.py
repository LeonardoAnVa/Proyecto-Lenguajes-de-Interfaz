from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View

from noticia.forms import ReporteroForm, NoticiaForm
from noticia.models import Reportero, Noticia


class Home(View):
    def get(self, request):
        cdx = {
            'titulo': 'Inicio',
            'noticias': Noticia.objects.all(),
            'encabezado': "Noticias Pal Barrio",
            'hay_agregar': False
        }
        return render(request, 'home/index.html', cdx)

class ReporteroView(View):
    def get(self, request):
        cdx = {
            'titulo': 'Reporteros',
            'reporteros': Reportero.objects.all(),
            'encabezado': "Reporteros",
            'hay_agregar': True,
            'link_agregar': "/reportero_alta",
            'filtro': "nombre"

        }
        return render(request, 'reportero/listar.html', cdx)

    def post(self, request):
        if 'filtro_checkbox' not in request.POST:
            nombre = request.POST['filtro']
            reporteros = Reportero.objects.filter(nombre__icontains=nombre).all()
        else:
            reporteros = Reportero.objects.all()
        cdx = {
            'titulo': 'Reporteros',
            'reporteros': reporteros,
            'encabezado': "Reporteros",
            'hay_agregar': True,
            'link_agregar': "/reportero_alta",
            'filtro': "nombre"
        }
        return render(request, 'reportero/listar.html', cdx)

class ReporteroAlta(View):
    def get(self, request):
        form = ReporteroForm()
        cdx = {
            'titulo': 'Alta Reporteros',
            'form': form,
            'btn_submit_texto': "Guardar",
            'encabezado': "Alta Reporteros",
            'color_fondo': 'w3-green'
        }
        return render(request, 'reportero/abc.html', cdx)

    def post(self, request):
        form = ReporteroForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            form.save()
            #user = authenticate(username=username, password=password)
            user = Reportero.objects.filter(username=username).first()
            user.set_password(password)
            user.save()
            return redirect('reporteros')
        cdx = {
            'titulo': 'Error en Alta Reporteros',
            'form': form,
            'encabezado': "Alta Reporteros",
            'btn_submit_texto': "Guardar",
            'color_fondo': 'w3-green'
        }
        return render(request, 'reportero/abc.html', cdx)

class ReporteroBaja(View):
    def get(self, request, id):
        #Reportero.objects.filter(id=id).delete()
        reportero = Reportero.objects.filter(id=id).first()
        form = ReporteroForm(instance=reportero)
        cdx = {
            'titulo': 'Eliminar Reportero',
            'form': form,
            'btn_submit_texto': "Eliminar",
            'encabezado': "Baja Reporteros",
            'color_fondo': 'w3-red'
        }
        return render(request, 'reportero/abc.html', cdx)

    def post(self, request, id):
        Reportero.objects.filter(id=id).delete()
        return redirect("reporteros")

class ReporteroEditar(View):
    def get(self, request, id):
        reportero = Reportero.objects.filter(id=id).first()
        form = ReporteroForm(instance=reportero)
        cdx = {
            'titulo': 'Editar Reportero',
            'form': form,
            'btn_submit_texto': "Guardar Cambios",
            'encabezado': "Editar Reporteros",
            'color_fondo': 'w3-yellow'
        }
        return render(request, 'reportero/abc.html', cdx)

    def post(self, request, id):
        reportero = Reportero.objects.filter(id=id).first()
        form = ReporteroForm(request.POST, request.FILES, instance=reportero)
        if form.is_valid():
            #print(form.cleaned_data)
            #print(f'password: {form.cleaned_data["password"]}')
            form.save()
            reportero.set_password(form.cleaned_data["password"])
            reportero.save()
            return redirect('reporteros')
        cdx = {
            'titulo': 'Error en Editar Reportero',
            'form': form,
            'btn_submit_texto': "Guardar Cambios",
            'encabezado': "Editar Reporteros",
            'color_fondo': 'w3-yellow'
        }
        return render(request, 'reportero/abc.html', cdx)

class NoticiasView(View):
    def get(self, request):
        cdx = {
            'titulo': 'Noticias',
            'noticias': Noticia.objects.all(),  # Obtiene todas las noticias
            'encabezado': "Últimas Noticias",
            'hay_agregar': True,
            'link_agregar': "/noticia_alta",
            #'filtro': "nombre"

        }

        return render(request, 'noticias/gestion_noticias.html', cdx)


class noticiaAlta(View):
    def get(self, request):
        form = NoticiaForm()
        cdx = {
            'titulo': 'Alta de Noticias',
            'form': form,
            'btn_submit_texto': "Guardar",
            'encabezado': "Agregar Noticia",
            'color_fondo': 'w3-green'
        }
        return render(request, 'noticias/noticia_alta.html', cdx)

    def post(self, request):
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            # Si el formulario es válido, se guarda la nueva noticia
            noticia = form.save(commit=False)  # Guarda la noticia pero no la comitea todavía
            noticia.autor = request.user  # Suponiendo que quieres asignar el usuario actual como autor
            noticia.save()
            return redirect('vistaNoticias')  # Redirige a la vista de noticias
        else:

            cdx = {
                'titulo': 'Error en Alta de Noticias',
                'form': form,
                'encabezado': "Alta de Noticias",
                'btn_submit_texto': "Guardar",
                'color_fondo': 'w3-green'
            }
            return render(request, 'noticias/noticia_alta.html', cdx)

class noticiaEditar(View):
    def get(self, request, id):
        noticia = Noticia.objects.filter(id=id).first()
        form = NoticiaForm(instance=noticia)
        cdx = {
            'titulo': 'Editar Noticia',
            'form': form,
            'btn_submit_texto': "Guardar Cambios",
            'encabezado': "Editar Noticia",
            'color_fondo': 'w3-yellow'
        }
        return render(request, 'noticias/noticia_alta.html', cdx)

    def post(self, request, id):
        noticia = Noticia.objects.filter(id=id).first()
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            #print(form.cleaned_data)
            #print(f'password: {form.cleaned_data["password"]}')
            form.save()
            #noticia.set_password(form.cleaned_data["password"])
            noticia.save()
            return redirect('vistaNoticias')
        cdx = {
            'titulo': 'Error en Editar Noticia',
            'form': form,
            'btn_submit_texto': "Guardar Cambios",
            'encabezado': "Modificar Noticia",
            'color_fondo': 'w3-yellow'
        }
        return render(request, 'noticias/noticia_alta.html', cdx)


class noticiaEliminar(View):
    def get(self, request, id):

        noticia = Noticia.objects.filter(id=id).first()
        form = NoticiaForm(instance=noticia)
        cdx = {
            'titulo': 'Eliminar Noticia',
            'form': form,
            'btn_submit_texto': "Eliminar",
            'encabezado': "Quitar Noticia",
            'color_fondo': 'w3-red'
        }
        return render(request, 'noticias/noticia_alta.html', cdx)
    def post(self, request, id):
        Noticia.objects.filter(id=id).delete()
        return redirect("vistaNoticias")