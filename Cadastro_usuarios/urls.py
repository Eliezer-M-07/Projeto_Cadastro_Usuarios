from django.contrib import admin
from django.urls import path
from app_cadastro_usuarios import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('atualizar/<int:id>', views.atualizar, name='atualizar'),
    path('salvar/', views.salvar, name='salvar'),
]