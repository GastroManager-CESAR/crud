from django.urls import path

from . import views

urlpatterns = [
    path("atualizar_garcom", views.atualizar_garcom, name="atualizar_garcom"),
    path("atualizar_garcom/<int:id>", views.atualizar_garcom, name="atualizar_garcom"),
    path("criar_garcom", views.criar_garcom, name="criar_garcom"),
    path("deletar_garcom/<int:id>", views.deletar_garcom, name="deletar_garcom"),
    path("", view=views.listar_garcom, name="listar_garcom")
]
