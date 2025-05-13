from django.urls import path

from . import views

urlpatterns = [
    path("criar_garcom", views.criar_garcom, name="criar_garcom"),
    path("deletar_item/<int:id>",views.deletar_item, name="deletar item"),
    path('atualizar_garcom', views.atualizar_garcom, name='atualizar_garcom')
]
