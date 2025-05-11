from django.db import models

class Item(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)