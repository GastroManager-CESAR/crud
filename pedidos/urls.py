from django.urls import path

from . import views

urlpatterns = [
    path("atualizar_pedido/<int:id>", views.atualizar_pedido, name="atualizar_pedido"),
    path("criar_pedido", views.criar_pedido, name="criar_pedido"),
    path("deletar_pedido/<int:id>", views.deletar_pedido, name="deletar_pedido"),
    path("", view=views.listar_pedidos, name="listar_pedido")
]