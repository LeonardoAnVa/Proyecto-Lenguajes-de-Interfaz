from django.urls import path
from . import views
from .views import Home, ReporteroView, ReporteroAlta, ReporteroBaja, ReporteroEditar, noticiaAlta, \
    noticiaEditar, noticiaEliminar, NoticiasView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('reporteros', ReporteroView.as_view(), name='reporteros'),
    path('reportero_alta', ReporteroAlta.as_view(), name='reportero_alta'),
    path('reportero_baja/<id>', ReporteroBaja.as_view(), name='reportero_baja'),
    path('reportero_editar/<id>', ReporteroEditar.as_view(), name='reportero_editar'),
    path('vistaNoticias', NoticiasView.as_view(), name='vistaNoticias'),
    path('noticia_alta', noticiaAlta.as_view(), name='noticia_alta'),
    path('noticia_editar/<int:id>', noticiaEditar.as_view(), name='noticia_editar'),
    path('noticia_eliminar/<int:id>', noticiaEliminar.as_view(), name='noticia_eliminar'),
    ]