from django.urls import path

from usuarios.views import LogoutSesion, GrupoListar, GrupoAlta

urlpatterns = [
    path('logout', LogoutSesion.as_view(), name='logout'),
    path('grupo_listar', GrupoListar.as_view(), name='grupo_listar'),
    path('grupo_alta', GrupoAlta.as_view(), name='grupo_alta'),
    ]