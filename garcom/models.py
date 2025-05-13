from django.db import models

class Garcom(models.Model):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField(max_length=15)
    sexo = models.CharField(max_length=15)
    foto = models.CharField(max_length=254)