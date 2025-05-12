from django.db import models

class Garcom(models.Model):
    nome_completo = models.CharField()
    cpf = models.CharField()
    data_nascimento = models.DateField()
    sexo = models.CharField()
    foto = models.CharField()