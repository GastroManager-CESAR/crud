from django.urls import path

from . import views

urlpatterns = [
    path("criar_item", views.criar_item, name="criar_item")
]