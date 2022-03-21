from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePrincipal, name='homePrincipal'),
    path('empresa/<int:id>', views.empresaView, name="empresa-view"),
    path('editar-empresa/<int:id>', views.editarEmpresa, name="editar-empresa"),
    path('remover-empresa/<int:id>', views.removerEmpresa, name="remover-empresa"),
    path('adicionar-empresa/', views.novaEmpresa, name="adicionar-empresa"),
]
