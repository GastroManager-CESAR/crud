from django.urls import path

from . import views

urlpatterns = [
    path("atualizar_item", views.atualizar_item, name="atualizar_item"),
    path("atualizar_item/<int:id>", views.atualizar_item, name="atualizar_item"),
    path("criar_item", views.criar_item, name="criar_item"),
    path("deletar_item/<int:id>", views.deletar_item, name="deletar_item")
]
