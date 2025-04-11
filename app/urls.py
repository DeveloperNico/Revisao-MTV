from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_personagens, name='listar_personagens'),
    path('criar/', views.criar_bruxo, name='criar_bruxo'),
    path('atualizar/<int:pk>/', views.atualizar_bruxo, name='atualizar_bruxo'),
    path('deletar/<int:pk>/', views.deletar_bruxo, name='deletar_bruxo')
]