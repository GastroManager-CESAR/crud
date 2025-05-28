from django.db import models

class Garcom(models.Model):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=253)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=252)
    foto = models.CharField(max_length=254)