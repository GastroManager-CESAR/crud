from django.urls import path

from . import views

urlpatterns = [
    path('atualizar_garcom', views.atualizar_garcom, name='atualizar_garcom')
]
