from django.urls import path

from . import views

urlpatterns = [
    path("criar_garcom", views.criar_garcom, name="criar_garcom")
]
