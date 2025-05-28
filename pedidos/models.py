from django.db import models

class Pedido(models.Model):
    item = models.CharField(max_length=200)
    preco = models.FloatField(max_length=200)
    mesa = models.IntegerField()
    garcom = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)