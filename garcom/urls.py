from django.urls import path

from . import views

urlpatterns = [
    path("deletar_item/<int:id>",views.deletar_item, name="deletar item"),
    path('atualizar_garcom', views.atualizar_garcom, name='atualizar_garcom')
]
